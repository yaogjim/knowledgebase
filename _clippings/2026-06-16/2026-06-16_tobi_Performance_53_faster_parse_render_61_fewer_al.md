---
title: "2026-06-16_github_com_Performance_53_faster_parse_render_61_fewer_alloca"
source: "https://github.com/Shopify/liquid/pull/2056"
author:
  - "[[@tobi]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#start"
  - "#byteindex"
  - "github"
  - "@tobi"
---

# Performance: 53% faster parse+render, 61% fewer allocations by tobi · Pull Request #2056 · Shopify/liquid

[Skip to content](#start-of-content)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/Shopify/liquid/pull/2056?resume=1)

## Conversation

[![@tobi](https://avatars.githubusercontent.com/u/347?s=80&v=4)](/tobi)

Member

## Summary

**53% faster combined parse+render time, 61% fewer object allocations** on the ThemeRunner benchmark (real Shopify theme templates with production-like data). Zero test regressions — all 974 unit tests pass.

| Metric | Main | This PR | Change |
| --- | --- | --- | --- |
| Combined (parse+render) | 7,469µs | 3,534µs | **\-53%** |
| Parse time | 6,031µs | 2,353µs | **\-61%** |
| Render time | 1,438µs | 1,146µs | **\-20%** |
| Object allocations | 62,620 | 24,530 | **\-61%** |

Measured with YJIT enabled on Ruby 3.4, using `performance/bench_quick.rb` (best of 3 runs, 10 iterations each with GC disabled, after 20-iteration warmup).

## Methodology

This PR was developed through **~120 automated experiments** using an autoresearch loop: edit → commit → run tests → benchmark → keep/discard. Each change was validated against the full unit test suite before benchmarking. Changes that regressed either correctness or the primary metric were reverted immediately.

The approach was allocation-driven: profile where objects are created, eliminate the ones that aren't needed, and defer the ones that are. With GC consuming 74% of total CPU time, every avoided allocation has outsized impact on wall-clock performance.

## Architecture changes

### 1\. Cursor class (lib/liquid/cursor.rb)

A `StringScanner` wrapper with higher-level methods tuned for Liquid's grammar. One Cursor per `ParseContext`, reused across all tag/variable/expression parsing:

```
cursor = parse_context.cursor
cursor.reset(markup)
cursor.skip_ws
tag_name = cursor.scan_tag_name # C-level regex via StringScanner
cursor.expect_id("in") # zero-alloc: regex skip + byte compare
cursor.skip_fragment # zero-alloc: regex skip
```

Key insight from [tenderlove's article on fast tokenizers](https://tenderlovemaking.com/2023/09/02/fast-tokenizers-with-stringscanner/): C-level `StringScanner.scan` / `skip` with compiled regexes is 2-3x faster than Ruby-level `peek_byte` / `scan_byte` loops. Methods that previously had 20+ lines of manual byte scanning are now 1-3 line regex delegations.

### 2\. String#byteindex tokenizer

Replaced `StringScanner` -based tokenizer with `String#byteindex` for finding `{%` and `{{` delimiters. The tokenizer accounts for ~30% of parse time, and `byteindex('{', pos)` is ~40% faster than `StringScanner#skip_until(/\{[\{\%]/)` for single-byte searching. Variable token scanning uses manual byte inspection matching the original tokenizer's exact edge-case handling (unclosed tags, `{{` → `{%` nesting).

### 3\. Zero-Lexer variable parsing

100% of variables in the benchmark (1,197) now parse through `Variable#try_fast_parse` — a byte-level scanner that extracts the name expression and filter chain without touching the Lexer or Parser. **Zero Lexer/Parser fallbacks.** Even multi-argument filters like `pluralize: 'item', 'items'` are scanned directly with comma-separated arg handling. Only keyword arguments (`key: value`) would fall through (none appear in the benchmark).

## What changed (by impact)

### Parse optimizations (~61% faster, ~38K fewer allocs)

**Replaced StringScanner tokenizer with `String#byteindex`.** Single-byte `byteindex` searching is ~40% faster than regex-based `skip_until`. This alone reduced parse time by ~12%.

**Pure-byte `parse_tag_token`.** Eliminated the costly `StringScanner#string=` reset that was called for every `{% %}` token (878 times). Manual byte scanning for tag name + markup extraction is faster than resetting and re-scanning via StringScanner.

**Replaced regex with Cursor scanning in hot paths.**`FullToken` regex → Cursor, `VariableParser` regex → manual byte scanner, `For#Syntax` regex → Cursor, `If#SIMPLE_CONDITION` regex → Cursor, `INTEGER_REGEX` / `FLOAT_REGEX` → Cursor `scan_number`, `WhitespaceOrNothing` regex → `match?`.

**Fast-path Variable initialization.** All variables parse through `try_fast_parse` which extracts name + filters via byte-level scanning. Cached no-arg filter tuples (`NO_ARG_FILTER_CACHE`) avoid repeated `[name, EMPTY_ARRAY]` creation.

**Fast-path VariableLookup.**`simple_lookup?` uses `match?` regex (8x faster than byte scan). Simple identifier chains skip `scan_variable` entirely.

**Avoid unnecessary string allocations.**`Expression.parse` skips `strip` when no whitespace. Variable fast-path reuses markup string directly when possible. `block_delimiter` strings cached per tag name.

### Render optimizations (~20% faster, ~3K fewer allocs)

**Splat-free filter invocation.**`invoke_single` / `invoke_two` avoid `*args` array allocation for 90% of filter calls.

**Primitive type fast paths.**`find_variable` returns immediately for String/Integer/Float/Array/Hash/nil — skipping `to_liquid` and `respond_to?(:context=)`. Same in `VariableLookup#evaluate`. Hash fast-path via `instance_of?(Hash)` before `respond_to?` chain.

**Cached small integer `to_s`.** Pre-computed frozen strings for 0-999 avoid 267 `Integer#to_s` allocations per render.

**`Condition#evaluate` fast path.** Skip `loop do...end` block when no `child_relation` — avoids closure allocation for all benchmark conditions.

**While loop for `If#@blocks.each`.** Avoids Proc creation for 1-2 element arrays (YJIT optimizes `each` better for long arrays, but `while` wins for short ones).

**Lazy initialization.** Context defers StringScanner and `@interrupts`. Registers defers `@changes` hash. `static_environments` uses `EMPTY_ARRAY` when empty.

### Code simplified

The Cursor consolidation replaced ~150 scattered `getbyte` / `byteslice` calls with a shared vocabulary. Example:

```
# Before: 15 lines of manual byte scanning
def scan_id
  start = @ss.pos
  b = @ss.peek_byte
  return unless b && ((b >= 97 && b <= 122) || (b >= 65 && b <= 90) || b == USCORE)
  @ss.scan_byte
  while (b = @ss.peek_byte)
 break unless (b >= 97 && b <= 122) || ...
 @ss.scan_byte
  end
  @source.byteslice(start, @ss.pos - start)
end

# After: C-level regex is 2-3x faster
ID_REGEX = /[a-zA-Z_][\w-]*\??/
def scan_id = @ss.scan(ID_REGEX)
```

## What did NOT work

- **Split-based tokenizer** — `String#split` with regex is 2.5x faster but can't handle `{{` followed by `%}` (variable-becomes-tag nesting that Liquid supports)
- **Tag name interning** via byte-based perfect hash — collision issues, and verification loop overhead kills the speed gain
- **`String#match` for name extraction** — MatchData creates +5K allocs, far worse than manual scanning
- **`while` loops replacing `each` in hot render paths** — YJIT optimizes `each` better for many-iteration loops; only wins for short 1-2 element arrays
- **Shared expression cache across templates** — leaks state between parses, grows unboundedly
- **`TruthyCondition` subclass** — YJIT polymorphism at evaluate call site hurts more than 115 saved allocs

## Benchmark reproduction

```
cd performance
bundle exec ruby bench_quick.rb # single run
# or
./auto/autoresearch.sh # tests + 3-run best-of
```

## Files changed

- **`lib/liquid/cursor.rb`** — new Cursor class (StringScanner wrapper with regex-based methods)
- **`lib/liquid/tokenizer.rb`** — `String#byteindex` -based tokenizer replacing StringScanner
- **`lib/liquid/block_body.rb`** — Cursor-based tag/variable parsing, regex `blank_string?`
- **`lib/liquid/variable.rb`** — `try_fast_parse` with multi-arg filter support, `NO_ARG_FILTER_CACHE`, `invoke_single` / `invoke_two` render dispatch
- **`lib/liquid/variable_lookup.rb`** — `simple_lookup?` regex, `parse_simple` fast path, primitive type fast paths in `evaluate`
- **`lib/liquid/expression.rb`** — byte-level `parse_number`, conditional `strip`
- **`lib/liquid/context.rb`** — `invoke_single` / `invoke_two`, primitive fast paths in `find_variable`, lazy init
- **`lib/liquid/condition.rb`** — `evaluate` fast path skipping loop block for simple conditions
- **`lib/liquid/strainer_template.rb`** — `invoke_single` / `invoke_two` dispatch
- **`lib/liquid/tags/if.rb`** — Cursor conditions, while-loop render, inlined `to_liquid_value`
- **`lib/liquid/tags/for.rb`** — Cursor-based `lax_parse`
- **`lib/liquid/block.rb`** — cached `block_delimiter` strings
- **`lib/liquid/registers.rb`** — lazy `@changes` hash
- **`lib/liquid/utils.rb`** — cached small integer `to_s`, lazy `seen` hash, `slice_collection` Array fast path
- **`lib/liquid/parse_context.rb`** — Cursor instance
- **`lib/liquid/resource_limits.rb`** — expose `last_capture_length` for render loop optimization

added 30 commits

`[add quick benchmark script for autoresearch](/Shopify/liquid/pull/2056/commits/4ea835ae044cbcc7922f458a84682093f6c2aa15 "add quick benchmark script for autoresearch")`

`[4ea835a](/Shopify/liquid/pull/2056/commits/4ea835ae044cbcc7922f458a84682093f6c2aa15)`

`[replace FullToken regex with manual byte parsing in parse_for_document](/Shopify/liquid/pull/2056/commits/3329b09dd4d1434bb746c82c5c380407e9c4a696 "replace FullToken regex with manual byte parsing in parse_for_document")`

`[3329b09](/Shopify/liquid/pull/2056/commits/3329b09dd4d1434bb746c82c5c380407e9c4a696)`

`[replace VariableParser regex scan with manual byte parser in Variable…](/Shopify/liquid/pull/2056/commits/97e6893c1a31dc00a31228d9f61099b83a3c5171 "replace VariableParser regex scan with manual byte parser in VariableLookup")`

`[97e6893](/Shopify/liquid/pull/2056/commits/97e6893c1a31dc00a31228d9f61099b83a3c5171)`

```
…Lookup
```

`[add auto/bench.sh: unit tests + liquid-spec + perf benchmark](/Shopify/liquid/pull/2056/commits/7aded8e61fe570b69f23b8d8b2102c55271f3fe2 "add auto/bench.sh: unit tests + liquid-spec + perf benchmark")`

`[7aded8e](/Shopify/liquid/pull/2056/commits/7aded8e61fe570b69f23b8d8b2102c55271f3fe2)`

`[use getbyte instead of string indexing in whitespace_handler and crea…](/Shopify/liquid/pull/2056/commits/2b78e4bf729d917e63123b5475e14ef9c1c5e32c "use getbyte instead of string indexing in whitespace_handler and create_variable")`

`[2b78e4b](/Shopify/liquid/pull/2056/commits/2b78e4bf729d917e63123b5475e14ef9c1c5e32c)`

```
…te_variable
```

`[use equal? for frozen array comparison in Lexer, skip whitespace with…](/Shopify/liquid/pull/2056/commits/d291e63006191ad76f3f73b6d4bcf1234c456b25 "use equal? for frozen array comparison in Lexer, skip whitespace with \s+")`

`[d291e63](/Shopify/liquid/pull/2056/commits/d291e63006191ad76f3f73b6d4bcf1234c456b25)`

```
… \s+
```

`[avoid unnecessary strip allocation in Expression.parse, use byteslice…](/Shopify/liquid/pull/2056/commits/d79b9fa2549c2a97a654d5156f2d58f0da5a8f42 "avoid unnecessary strip allocation in Expression.parse, use byteslice for string literals")`

`[d79b9fa](/Shopify/liquid/pull/2056/commits/d79b9fa2549c2a97a654d5156f2d58f0da5a8f42)`

```
… for string literals
```

`[short-circuit parse_number with first-byte check before regex](/Shopify/liquid/pull/2056/commits/fa412245f70e1a10d780b62f4c94641a5d55baa9 "short-circuit parse_number with first-byte check before regex")`

`[fa41224](/Shopify/liquid/pull/2056/commits/fa412245f70e1a10d780b62f4c94641a5d55baa9)`

`[fast-path String in render_obj_to_output, avoid Utils.to_s dispatch f…](/Shopify/liquid/pull/2056/commits/c1113ad2f806412a5a444c8e461c781e21883384 "fast-path String in render_obj_to_output, avoid Utils.to_s dispatch for common case")`

`[c1113ad](/Shopify/liquid/pull/2056/commits/c1113ad2f806412a5a444c8e461c781e21883384)`

```
…or common case
```

`[fast-path variable_lookups: skip mutable string alloc when no dot/bra…](/Shopify/liquid/pull/2056/commits/1a79cf62661efb00038208b4049fad2cd40ad15a "fast-path variable_lookups: skip mutable string alloc when no dot/bracket follows")`

`[1a79cf6](/Shopify/liquid/pull/2056/commits/1a79cf62661efb00038208b4049fad2cd40ad15a)`

```
…cket follows
```

`[use frozen EMPTY_ARRAY for Variable filters when no filters present](/Shopify/liquid/pull/2056/commits/5da223275a538611fcdc1cc988e0d887c1c456ac "use frozen EMPTY_ARRAY for Variable filters when no filters present")`

`[5da2232](/Shopify/liquid/pull/2056/commits/5da223275a538611fcdc1cc988e0d887c1c456ac)`

`[fast-path simple variable parsing: skip Lexer/Parser for plain dot-se…](/Shopify/liquid/pull/2056/commits/25f9224c856444746c1ffe961e24cc91697da0c6 "fast-path simple variable parsing: skip Lexer/Parser for plain dot-separated lookups")`

`[25f9224](/Shopify/liquid/pull/2056/commits/25f9224c856444746c1ffe961e24cc91697da0c6)`

```
…parated lookups
```

`[replace SIMPLE_VARIABLE regex with byte-level scanner to avoid MatchData](/Shopify/liquid/pull/2056/commits/3939d7453106a40ece2de431f3d204406dff73a8 "replace SIMPLE_VARIABLE regex with byte-level scanner to avoid MatchData")`

`[3939d74](/Shopify/liquid/pull/2056/commits/3939d7453106a40ece2de431f3d204406dff73a8)`

`[fast-path simple if conditions: skip ExpressionsAndOperators scan for…](/Shopify/liquid/pull/2056/commits/fe7a2f5aa8e951ea10e0eeacccbd7bfcdf0d755b "fast-path simple if conditions: skip ExpressionsAndOperators scan for single conditions")`

`[fe7a2f5](/Shopify/liquid/pull/2056/commits/fe7a2f5aa8e951ea10e0eeacccbd7bfcdf0d755b)`

```
… single conditions
```

`[skip TagAttributes scan in for tag when no colon present](/Shopify/liquid/pull/2056/commits/6bcc2936a2819367cca6c0719df8e2c1d2f46146 "skip TagAttributes scan in for tag when no colon present")`

`[6bcc293](/Shopify/liquid/pull/2056/commits/6bcc2936a2819367cca6c0719df8e2c1d2f46146)`

`[fast-path render for filter-less variables: skip render method overhead](/Shopify/liquid/pull/2056/commits/f8b015646aa96246b0df4dbdb4d1c53b21ee6351 "fast-path render for filter-less variables: skip render method overhead")`

`[f8b0156](/Shopify/liquid/pull/2056/commits/f8b015646aa96246b0df4dbdb4d1c53b21ee6351)`

`[unified fast-path Variable parsing: handle both plain lookups and fil…](/Shopify/liquid/pull/2056/commits/8a92a4e45185aad1c03ba5d3911c06cc2b93fa85 "unified fast-path Variable parsing: handle both plain lookups and filter chains without full Lexer pass for name")`

`[8a92a4e](/Shopify/liquid/pull/2056/commits/8a92a4e45185aad1c03ba5d3911c06cc2b93fa85)`

```
…ter chains without full Lexer pass for name
```

`[expose expression_cache/string_scanner via attr_reader, skip regex in…](/Shopify/liquid/pull/2056/commits/2d3b856b36859faab53eb68ecbe428433ac2a0f7 "expose expression_cache/string_scanner via attr_reader, skip regex in filter args without colon")`

`[2d3b856](/Shopify/liquid/pull/2056/commits/2d3b856b36859faab53eb68ecbe428433ac2a0f7)`

```
… filter args without colon
```

`[replace For tag Syntax regex with manual byte-level parser](/Shopify/liquid/pull/2056/commits/cfa0dfe3cad4c8f332abc7f33f0c274523826d92 "replace For tag Syntax regex with manual byte-level parser")`

`[cfa0dfe](/Shopify/liquid/pull/2056/commits/cfa0dfe3cad4c8f332abc7f33f0c274523826d92)`

`[avoid empty array allocation in evaluate_filter_expressions for no-ar…](/Shopify/liquid/pull/2056/commits/544d8f1c17c41006f0a87778325203135ec79578 "avoid empty array allocation in evaluate_filter_expressions for no-arg filters")`

`[544d8f1](/Shopify/liquid/pull/2056/commits/544d8f1c17c41006f0a87778325203135ec79578)`

```
…g filters
```

`[use getbyte dispatch instead of start_with? in parse_for_document](/Shopify/liquid/pull/2056/commits/82407092cc1a5f63f91fb236c55c25576e1956a2 "use getbyte dispatch instead of start_with? in parse_for_document")`

`[8240709](/Shopify/liquid/pull/2056/commits/82407092cc1a5f63f91fb236c55c25576e1956a2)`

`[return [tag_name, markup, newlines] from parse_tag_token: avoid 2 whi…](/Shopify/liquid/pull/2056/commits/58d251452170935e08009f4f1de26cbd71d373e0 "return [tag_name, markup, newlines] from parse_tag_token: avoid 2 whitespace string allocs")`

`[58d2514](/Shopify/liquid/pull/2056/commits/58d251452170935e08009f4f1de26cbd71d373e0)`

```
…tespace string allocs
```

`[use frozen EMPTY_ARRAY for disabled_tags in Variable](/Shopify/liquid/pull/2056/commits/b86143eb0e862fe9f266afb702040966fbaa03ac "use frozen EMPTY_ARRAY for disabled_tags in Variable")`

`[b86143e](/Shopify/liquid/pull/2056/commits/b86143eb0e862fe9f266afb702040966fbaa03ac)`

`[hoist write score check out of render loop: skip increment_write_scor…](/Shopify/liquid/pull/2056/commits/db434923d0392dab0f6c05a24dd75478432d52e4 "hoist write score check out of render loop: skip increment_write_score when no limits active")`

`[db43492](/Shopify/liquid/pull/2056/commits/db434923d0392dab0f6c05a24dd75478432d52e4)`

```
…e when no limits active
```

`[extend fast-path to handle quoted string literal variables (262 more …](/Shopify/liquid/pull/2056/commits/17daac92da2a94cea60bab95a3123cbb25583d46 "extend fast-path to handle quoted string literal variables (262 more fast-pathed)")`

`[17daac9](/Shopify/liquid/pull/2056/commits/17daac92da2a94cea60bab95a3123cbb25583d46)`

```
…fast-pathed)
```

`[autoresearch: add autoresearch.md/sh, increase benchmark warmup to 20…](/Shopify/liquid/pull/2056/commits/2543fdc1a101f555db208fb0deeb2e3bf1ae9e36 "autoresearch: add autoresearch.md/sh, increase benchmark warmup to 20 iterations")`

`[2543fdc](/Shopify/liquid/pull/2056/commits/2543fdc1a101f555db208fb0deeb2e3bf1ae9e36)`

```
… iterations
```

`[split filter parsing: scan no-arg filters directly, only invoke Lexer…](/Shopify/liquid/pull/2056/commits/9fd7cec564c0e77621cafb3d3d9d864547c4120a "split filter parsing: scan no-arg filters directly, only invoke Lexer when args present")`

`[9fd7cec](/Shopify/liquid/pull/2056/commits/9fd7cec564c0e77621cafb3d3d9d864547c4120a)`

```
… when args present
```

`[add security constraint to autoresearch.md, fix strict mode gate](/Shopify/liquid/pull/2056/commits/ad98d1f32925b221d3a8ba87f9d9a9528bcfcb0f "add security constraint to autoresearch.md, fix strict mode gate")`

`[ad98d1f](/Shopify/liquid/pull/2056/commits/ad98d1f32925b221d3a8ba87f9d9a9528bcfcb0f)`

`[autoresearch.md: add strategic direction toward single-pass scanner a…](/Shopify/liquid/pull/2056/commits/83037f978ba73c248186817ce836aa822c8d05ee "autoresearch.md: add strategic direction toward single-pass scanner architecture")`

`[83037f9](/Shopify/liquid/pull/2056/commits/83037f978ba73c248186817ce836aa822c8d05ee)`

```
…rchitecture
```

added 10 commits

`[Replace manual scan_comparison_op with regex — cleaner and avoids byt…](/Shopify/liquid/pull/2056/commits/11c22eb75d4e18b10d6a99a271626a19fbbe8019 "Replace manual scan_comparison_op with regex — cleaner and avoids byteslice allocation for op strings\n\nResult: {"status":"keep","combined_µs":4007,"parse_µs":2808,"render_µs":1199,"allocations":25535}")`

`[11c22eb](/Shopify/liquid/pull/2056/commits/11c22eb75d4e18b10d6a99a271626a19fbbe8019)`

```
…eslice allocation for op strings\n\nResult: {"status":"keep","combined_µs":4007,"parse_µs":2808,"render_µs":1199,"allocations":25535}
```

`[Replace manual rest_blank? with regex skip + eos? check\n\nResult: {"…](/Shopify/liquid/pull/2056/commits/e15b163f1a9bbad88a80525e9b86b15757023371 "Replace manual rest_blank? with regex skip + eos? check\n\nResult: {"status":"keep","combined_µs":4047,"parse_µs":2795,"render_µs":1252,"allocations":25535}")`

`[e15b163](/Shopify/liquid/pull/2056/commits/e15b163f1a9bbad88a80525e9b86b15757023371)`

```
…status":"keep","combined_µs":4047,"parse_µs":2795,"render_µs":1252,"allocations":25535}
```

`[Replace manual scan_quoted_string with regex capture groups\n\nResult…](/Shopify/liquid/pull/2056/commits/fd4a7af2904bb918acc1062e126d9939aea16f5e "Replace manual scan_quoted_string with regex capture groups\n\nResult: {"status":"keep","combined_µs":4102,"parse_µs":2849,"render_µs":1253,"allocations":25535}")`

`[fd4a7af](/Shopify/liquid/pull/2056/commits/fd4a7af2904bb918acc1062e126d9939aea16f5e)`

```
…: {"status":"keep","combined_µs":4102,"parse_µs":2849,"render_µs":1253,"allocations":25535}
```

`[Replace manual scan_dotted_id with regex\n\nResult: {"status":"keep",…](/Shopify/liquid/pull/2056/commits/71e22e6a8422ac0d2368817a300f54595af20735 "Replace manual scan_dotted_id with regex\n\nResult: {"status":"keep","combined_µs":4121,"parse_µs":2812,"render_µs":1309,"allocations":25535}")`

`[71e22e6](/Shopify/liquid/pull/2056/commits/71e22e6a8422ac0d2368817a300f54595af20735)`

```
…"combined_µs":4121,"parse_µs":2812,"render_µs":1309,"allocations":25535}
```

`[Minor cleanup: optimize expect_id with while loop and early return\n\…](/Shopify/liquid/pull/2056/commits/1a019151eb277b133b10d4d44c7a35d5f3a050cc "Minor cleanup: optimize expect_id with while loop and early return\n\nResult: {"status":"keep","combined_µs":4184,"parse_µs":2921,"render_µs":1263,"allocations":25535}")`

`[1a01915](/Shopify/liquid/pull/2056/commits/1a019151eb277b133b10d4d44c7a35d5f3a050cc)`

```
…nResult: {"status":"keep","combined_µs":4184,"parse_µs":2921,"render_µs":1263,"allocations":25535}
```

`[Skip to_liquid_value for String/Integer keys in VariableLookup — avoi…](/Shopify/liquid/pull/2056/commits/22b5ff15879cd56e57e2f83c6c004c7b5147f83e "Skip to_liquid_value for String/Integer keys in VariableLookup — avoids respond_to? dispatch\n\nResult: {"status":"keep","combined_µs":4131,"parse_µs":2893,"render_µs":1238,"allocations":25535}")`

`[22b5ff1](/Shopify/liquid/pull/2056/commits/22b5ff15879cd56e57e2f83c6c004c7b5147f83e)`

```
…ds respond_to? dispatch\n\nResult: {"status":"keep","combined_µs":4131,"parse_µs":2893,"render_µs":1238,"allocations":25535}
```

`[Replace manual blank_string? with regex match — cleaner code\n\nResul…](/Shopify/liquid/pull/2056/commits/76afdf154f44f9b81f573e7702f2926a50e2c141 "Replace manual blank_string? with regex match — cleaner code\n\nResult: {"status":"keep","combined_µs":4196,"parse_µs":3042,"render_µs":1154,"allocations":25535}")`

`[76afdf1](/Shopify/liquid/pull/2056/commits/76afdf154f44f9b81f573e7702f2926a50e2c141)`

```
…t: {"status":"keep","combined_µs":4196,"parse_µs":3042,"render_µs":1154,"allocations":25535}
```

`[Cache no-arg filter tuples [name, EMPTY_ARRAY] — reuse frozen tuples …](/Shopify/liquid/pull/2056/commits/228ecdb6a21beff67c94b142bdf310bf14aab2bf "Cache no-arg filter tuples [name, EMPTY_ARRAY] — reuse frozen tuples across templates\n\nResult: {"status":"keep","combined_µs":4147,"parse_µs":2992,"render_µs":1155,"allocations":24881}")`

`[228ecdb](/Shopify/liquid/pull/2056/commits/228ecdb6a21beff67c94b142bdf310bf14aab2bf)`

```
…across templates\n\nResult: {"status":"keep","combined_µs":4147,"parse_µs":2992,"render_µs":1155,"allocations":24881}
```

`[update autoresearch.md with current progress](/Shopify/liquid/pull/2056/commits/38d8055c3bd036a32716816b394d970c04aa8d6d "update autoresearch.md with current progress")`

`[38d8055](/Shopify/liquid/pull/2056/commits/38d8055c3bd036a32716816b394d970c04aa8d6d)`

`[Skip context.evaluate for String lookup keys in VariableLookup — avoi…](/Shopify/liquid/pull/2056/commits/8f2f0ee0354b9d211197c970b14f58dd28ab82de "Skip context.evaluate for String lookup keys in VariableLookup — avoids respond_to? dispatch\n\nResult: {"status":"keep","combined_µs":4103,"parse_µs":2881,"render_µs":1222,"allocations":24881}")`

`[8f2f0ee](/Shopify/liquid/pull/2056/commits/8f2f0ee0354b9d211197c970b14f58dd28ab82de)`

```
…ds respond_to? dispatch\n\nResult: {"status":"keep","combined_µs":4103,"parse_µs":2881,"render_µs":1222,"allocations":24881}
```

changed the title ~Performance: 35% faster parse+render, 53% fewer allocations~ Performance: 47% faster parse+render, 60% fewer allocations

requested a review from [ianks](/ianks)

added 4 commits

`[Baseline: 3,818µs combined, 24,881 allocs\n\nResult: {"status":"keep"…](/Shopify/liquid/pull/2056/commits/c09e722f9b0dd807962a09acc7d431456e9300fa "Baseline: 3,818µs combined, 24,881 allocs\n\nResult: {"status":"keep","combined_µs":3818,"parse_µs":2722,"render_µs":1096,"allocations":24881}")`

`[c09e722](/Shopify/liquid/pull/2056/commits/c09e722f9b0dd807962a09acc7d431456e9300fa)`

```
…,"combined_µs":3818,"parse_µs":2722,"render_µs":1096,"allocations":24881}
```

`[Replace StringScanner tokenizer with String#byteindex — 12% faster pa…](/Shopify/liquid/pull/2056/commits/b7ae55f7a985e6798e153d402d0d15fa4632be78 "Replace StringScanner tokenizer with String#byteindex — 12% faster parse, no regex overhead for delimiter finding\n\nResult: {"status":"keep","combined_µs":3556,"parse_µs":2388,"render_µs":1168,"allocations":24882}")`

`[b7ae55f](/Shopify/liquid/pull/2056/commits/b7ae55f7a985e6798e153d402d0d15fa4632be78)`

```
…rse, no regex overhead for delimiter finding\n\nResult: {"status":"keep","combined_µs":3556,"parse_µs":2388,"render_µs":1168,"allocations":24882}
```

`[Confirmation run: byteindex tokenizer consistently 3,400-3,600µs\n\nR…](/Shopify/liquid/pull/2056/commits/e25f2f1d52391b5386f79fec84df5305121cf2da "Confirmation run: byteindex tokenizer consistently 3,400-3,600µs\n\nResult: {"status":"keep","combined_µs":3464,"parse_µs":2335,"render_µs":1129,"allocations":24882}")`

`[e25f2f1](/Shopify/liquid/pull/2056/commits/e25f2f1d52391b5386f79fec84df5305121cf2da)`

```
…esult: {"status":"keep","combined_µs":3464,"parse_µs":2335,"render_µs":1129,"allocations":24882}
```

`[Clean up tokenizer: remove unused StringScanner setup and regex const…](/Shopify/liquid/pull/2056/commits/b37fa98c9121d84c9d68f4b000a269de6c71f339 "Clean up tokenizer: remove unused StringScanner setup and regex constants\n\nResult: {"status":"keep","combined_µs":3490,"parse_µs":2331,"render_µs":1159,"allocations":24882}")`

`[b37fa98](/Shopify/liquid/pull/2056/commits/b37fa98c9121d84c9d68f4b000a269de6c71f339)`

```
…ants\n\nResult: {"status":"keep","combined_µs":3490,"parse_µs":2331,"render_µs":1159,"allocations":24882}
```

changed the title ~Performance: 47% faster parse+render, 60% fewer allocations~ Performance: 52% faster parse+render, 60% fewer allocations

added 3 commits

`[parse_tag_token without StringScanner: pure byte ops avoid reset(toke…](/Shopify/liquid/pull/2056/commits/f6baeaed1e7a907497735fc5a62e477cb46155ef "parse_tag_token without StringScanner: pure byte ops avoid reset(token) overhead, -12% combined\n\nResult: {"status":"keep","combined_µs":3350,"parse_µs":2212,"render_µs":1138,"allocations":24882}")`

`[f6baeae](/Shopify/liquid/pull/2056/commits/f6baeaed1e7a907497735fc5a62e477cb46155ef)`

```
…n) overhead, -12% combined\n\nResult: {"status":"keep","combined_µs":3350,"parse_µs":2212,"render_µs":1138,"allocations":24882}
```

`[update autoresearch docs with current progress](/Shopify/liquid/pull/2056/commits/46927b9e901d9542b8ddef75167217ad3b122e5f "update autoresearch docs with current progress")`

`[46927b9](/Shopify/liquid/pull/2056/commits/46927b9e901d9542b8ddef75167217ad3b122e5f)`

`[Clean confirmation run: 3,314µs (-55% from main), stable\n\nResult: {…](/Shopify/liquid/pull/2056/commits/ae9a2e26b0a635497902914ee19fc00279e6184e "Clean confirmation run: 3,314µs (-55% from main), stable\n\nResult: {"status":"keep","combined_µs":3314,"parse_µs":2203,"render_µs":1111,"allocations":24882}")`

`[ae9a2e2](/Shopify/liquid/pull/2056/commits/ae9a2e26b0a635497902914ee19fc00279e6184e)`

```
…"status":"keep","combined_µs":3314,"parse_µs":2203,"render_µs":1111,"allocations":24882}
```

changed the title ~Performance: 52% faster parse+render, 60% fewer allocations~ Performance: 55% faster parse+render, 60% fewer allocations

added 4 commits

`[Condition#evaluate: skip loop block for simple conditions (no child_r…](/Shopify/liquid/pull/2056/commits/ca327b01b19ee062a3ed93677dfba1952269c599 "Condition#evaluate: skip loop block for simple conditions (no child_relation) — saves 235 allocs\n\nResult: {"status":"keep","combined_µs":3445,"parse_µs":2284,"render_µs":1161,"allocations":24647}")`

`[ca327b0](/Shopify/liquid/pull/2056/commits/ca327b01b19ee062a3ed93677dfba1952269c599)`

```
…elation) — saves 235 allocs\n\nResult: {"status":"keep","combined_µs":3445,"parse_µs":2284,"render_µs":1161,"allocations":24647}
```

`[Replace simple_lookup? byte scan with match? regex — 8x faster per ca…](/Shopify/liquid/pull/2056/commits/99454a9be2626f5e5642399c353d0129e104b029 "Replace simple_lookup? byte scan with match? regex — 8x faster per call, cleaner code\n\nResult: {"status":"keep","combined_µs":3489,"parse_µs":2353,"render_µs":1136,"allocations":24647}")`

`[99454a9](/Shopify/liquid/pull/2056/commits/99454a9be2626f5e5642399c353d0129e104b029)`

```
…ll, cleaner code\n\nResult: {"status":"keep","combined_µs":3489,"parse_µs":2353,"render_µs":1136,"allocations":24647}
```

`[Inline to_liquid_value in If render — avoids one method dispatch per …](/Shopify/liquid/pull/2056/commits/db348e0dac565e3f1ccb4ab82cb6abfacc40410e "Inline to_liquid_value in If render — avoids one method dispatch per condition evaluation\n\nResult: {"status":"keep","combined_µs":3459,"parse_µs":2318,"render_µs":1141,"allocations":24647}")`

`[db348e0](/Shopify/liquid/pull/2056/commits/db348e0dac565e3f1ccb4ab82cb6abfacc40410e)`

```
…condition evaluation\n\nResult: {"status":"keep","combined_µs":3459,"parse_µs":2318,"render_µs":1141,"allocations":24647}
```

`[Replace @blocks.each with while loop in If render — avoids block proc…](/Shopify/liquid/pull/2056/commits/b195d092128cd9e428ce79eaeccac5c76eccfb47 "Replace @blocks.each with while loop in If render — avoids block proc allocation per render\n\nResult: {"status":"keep","combined_µs":3496,"parse_µs":2356,"render_µs":1140,"allocations":24530}")`

`[b195d09](/Shopify/liquid/pull/2056/commits/b195d092128cd9e428ce79eaeccac5c76eccfb47)`

```
… allocation per render\n\nResult: {"status":"keep","combined_µs":3496,"parse_µs":2356,"render_µs":1140,"allocations":24530}
```

changed the title ~Performance: 55% faster parse+render, 60% fewer allocations~ Performance: 52% faster parse+render, 61% fewer allocations

`[update autoresearch experiment log](/Shopify/liquid/pull/2056/commits/3182b7c1b3758b0f5fe2d0fcc71a48bbcb11c946 "update autoresearch experiment log")`

`[3182b7c](/Shopify/liquid/pull/2056/commits/3182b7c1b3758b0f5fe2d0fcc71a48bbcb11c946)`

changed the title ~Performance: 52% faster parse+render, 61% fewer allocations~ Performance: 53% faster parse+render, 61% fewer allocations

[![basicBrogrammer](https://avatars.githubusercontent.com/u/6913826?s=60&v=4)](/basicBrogrammer)

reviewed

[View reviewed changes](/Shopify/liquid/pull/2056/files/3182b7c1b3758b0f5fe2d0fcc71a48bbcb11c946)

[auto/autoresearch.md](/Shopify/liquid/pull/2056/files/3182b7c1b3758b0f5fe2d0fcc71a48bbcb11c946#diff-a3e52792857295c8eb1843ceb89f762ab3baa46864e6f23329fd6dd1a56d9a76)

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

Was this and auto/bench.sh your only input file? I've only tested autoresearch with a skill for setup. I didn't give it a benchmark script instead i instructed the agent to use the time from the minitest output.

Member Author

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

initially, before building autoresearch

mentioned this pull request

[Performance plugin TiddlyWiki/TiddlyWiki5#9728](/TiddlyWiki/TiddlyWiki5/pull/9728)

Draft

## Merge info

![@yaogjim](https://avatars.githubusercontent.com/u/3283576?s=80&v=4)

Remember, contributions to this repository should follow its [contributing guidelines](/Shopify/liquid/blob/5fa36267aa1f97ab1f87971ef948bc6730c42e58/CONTRIBUTING.md), [security policy](/Shopify/.github/blob/5eea7e85db75d40827cb229aa4c7bd9ac8ee05a0/SECURITY.md), and [code of conduct](/Shopify/.github/blob/5eea7e85db75d40827cb229aa4c7bd9ac8ee05a0/CODE_OF_CONDUCT.md).

**ProTip!** Add [.patch](/Shopify/liquid/pull/2056.patch) or [.diff](/Shopify/liquid/pull/2056.diff) to the end of URLs for Git’s plaintext views.

### Labels

None yet