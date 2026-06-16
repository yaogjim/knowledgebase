---
title: "2026-06-16_percepta_ai_Can_LLMs_Be_Computers_Percepta"
source: "https://www.percepta.ai/blog/can-llms-be-computers"
author:
  - "[[@percepta.ai]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#but"
  - "#more"
  - "percepta"
  - "@percepta.ai"
---

# Can LLMs Be Computers? | Percepta

## TL;DR

Language models can solve tough math problems at research grade but struggle on simple computational tasks that involve reasoning over many steps and long context. Even multiplying two numbers or solving small Sudokus is nearly impossible unless they rely on external tools.

> But what does it take for an LLM itself to be as reliable and efficient as a computer?

We answer this by literally building a computer inside a transformer. We turn arbitrary C code into tokens that the model itself can execute reliably for millions of steps in seconds.

Here is how it works when solving an optimization problem that proceeds in many steps, namely min-cost perfect matching 1 via the Hungarian algorithm.

User

61 58 35 86 32 39 41 27 21 42

59 77 97 99 78 21 89 72 35 63

88 85 37 57 59 97 37 29 69 94

32 82 53 20 77 96 21 70 50 61

15 44 81 10 64 36 56 78 20 69

76 35 87 69 16 55 26 37 30 66

86 32 74 94 32 14 24 12 31 70

97 63 20 64 90 21 28 49 89 10

58 52 27 76 61 35 17 91 37 66

42 79 61 26 55 98 70 17 26 86

**32,537** tok/s **281,157** tokens **7,073** lines/s

Assistant

solving 10x10 assignment problem using the Hungarian algorithm..

assigning row 1.

running Dijkstra on reduced costs....

explored 1 column, found free col 9.

updating dual variables....

augmenting along path:

assign row 1 -> col 9.

cost: 0 + 21 = 21 (new row adds 21 to total)

assigning row 2.

running Dijkstra on reduced costs....

explored 1 column, found free col 6.

updating dual variables....

augmenting along path:

assign row 2 -> col 6.

cost: 21 + 21 = 42 (new row adds 21 to total)

assigning row 3.

running Dijkstra on reduced costs....

explored 1 column, found free col 8.

updating dual variables....

augmenting along path:

assign row 3 -> col 8.

cost: 42 + 29 = 71 (new row adds 29 to total)

assigning row 4.

running Dijkstra on reduced costs....

explored 1 column, found free col 4.

updating dual variables....

augmenting along path:

assign row 4 -> col 4.

cost: 71 + 20 = 91 (new row adds 20 to total)

assigning row 5.

running Dijkstra on reduced costs....

explored 2 columns, found augmenting path to free col 7.

updating dual variables....

augmenting along path:

move row 4 from col 4 to col 7.

assign row 5 -> col 4.

cost: 91 + 11 = 102 (new row adds 11 to total)

assigning row 6.

running Dijkstra on reduced costs....

explored 1 column, found free col 5.

updating dual variables....

augmenting along path:

assign row 6 -> col 5.

cost: 102 + 16 = 118 (new row adds 16 to total)

assigning row 7.

running Dijkstra on reduced costs....

21 21 29 21 10 16 1 2 3 4 5 6 7 8 9 10

The model does not call an external tool. Instead, it executes the program directly via its transformer weights, producing an execution trace token by token and streaming results at more than 30k tokens/sec on a CPU.

The key technical idea is a new decoding path for execution traces that turns the model's attention lookups from linear scans into queries that take logarithmic time, enabling millions of correct execution steps inside a single transformer run.

* * *

## Motivation: LLMs cannot compute

State-of-the-art language models can solve impressively hard mathematics, with systems able to reach gold-medal standard on the International Mathematical Olympiad 2 or even tackle open Math and Science problems 3.

At the same time, a stubborn gap remains: even state-of-the-art models still stumble on tasks that should be purely computational. They make mistakes even on basic addition, and they fail to solve even simple Sudoku puzzles without outside help. Benchmarks such as Sudoku-Bench make this failure mode especially visible, reporting low unaided solve rates.4

In practice, we bridge this gap using two families of workarounds:

- **Tool use:** the model writes code; an external interpreter executes it; the model reports the result. Tool-integrated approaches measurably improve math reasoning.5
- **Agentic orchestration:** an outer loop stores intermediate state, decomposes tasks, and repeatedly calls the model on short contexts, effectively bolting a state machine onto the outside.

These approaches are extremely useful but they highlight an important limitation: LLMs do not reliably perform long, exact computations on their own, so in practice we often delegate the execution to external tools or orchestration systems.

An analogy makes the distinction clear. Humans cannot fly. Building airplanes does not change that; it only means we built a machine that flies for us.

Today's language models are in the same situation. When a task requires exact computation, we attach external systems (interpreters, code runners, agent loops) and let those systems do the computing.

But that means the capability still lives outside the model. The model itself is fundamentally handicapped: it cannot carry out the computation it is reasoning about, so it must repeatedly hand the task off to another system.

As a result, the model can describe algorithms, reason about them, or orchestrate tools that run them, but it cannot execute the steps itself. A system that cannot compute cannot truly internalize what computation is.

So the real question is not whether a model can talk about computation, or even access it through tools. The real question is whether it can execute computation internally: reliably, efficiently, and over very long horizons. If it could, it would stop being merely a coordinator of computation and become a computer itself.

* * *

## How we turned LLMs to computers

On the surface, nothing is broken. The transformer architecture that powers LLMs is incredibly capable. Multiple works have shown that different variants of transformers can carry out complex computations because they can simulate Turing machines and hence any effective computer 6. Recent work shows that they can even achieve these computational capabilities via training 7.

But theoretical universality is not the same as practical execution. A model can be expressive enough to simulate a computer and still be a terrible computer in practice. Classical universality results often rely on constructions where simple operations in a real machine correspond to long sequences of steps in the simulated model. In other words, representational capability alone does not guarantee practical execution efficiency.

> We tackle this by implementing a modern RAM computer inside the transformer rather than a purely theoretical model of computation. In our construction, each instruction maps to only a handful of tokens (at most 5).

But even that is not enough. The deeper problem is the decoding process itself.

Transformers have a structural handicap as executors: standard autoregressive decoding makes each step interact with the full accumulated history. A real computer updates a compact state with roughly constant work per instruction. A transformer instead generates one token at a time while continually interacting with a prefix that keeps growing. KV caching avoids recomputing past key/value projections, but decoding still requires attending over the cached prefix, so work per step remains coupled to sequence length.8

> We remove this handicap by showing that the same transformer architecture admits an efficient decoding scheme for execution-style traces. The key technical unlock is to restrict lookup heads to head dimension 2, which enables a decoding path where the dominant retrieval/update operations can be computed in log time in the sequence length (for this structured executor regime), rather than by a full prefix-sized attention sweep.

This is powerful enough to let us execute arbitrary programs inside a transformer for millions of steps.

The rest of this post walks through how this works. Feel free to skip ahead:

- [What does computation mean?](#but-what-does-computation-mean) — How in-model execution differs from tool use: the transformer runs the program itself, step by step.
- [More demos: Sudoku](#more-demos-sudoku) — Executing a compiled solver inside the transformer to solve the Arto Inkala Sudoku, regarded as the hardest Sudoku in the world.
- [How can computation be encoded?](#how-can-computation-be-encoded) — Execution as a trace that only appends, and how a transformer reconstructs state by looking back at prior steps.
- [Exponentially Fast Attention](#the-key-unlock-exponentially-fast-attention) — The core unlock: 2D heads turn attention into a convex-hull query, enabling log-time decoding over million-step traces.
- [What is next?](#so-what-is-next) — Richer attention, training at scale, compiling programs into weights, and growing AI systems like software.

* * *

## What does computation mean?

These days, when a model needs to compute something, it writes code. For example, to add 3 + 5, a model might output:

```bash
python -c "print(3+5)"
```

Generation then pauses. An external tool-use mechanism intercepts the code block, sends it to a sandboxed interpreter, and injects the result (`8`) back into the token stream. The model resumes, now knowing the answer.

This works, but the actual execution happened outside the model. The model specified the computation, then waited for an external system to carry it out.

Our transformer also emits a program, but instead of pausing for an external tool, it executes that program itself, step by step, within the same transformer.

To achieve this, we implemented a WebAssembly interpreter inside the transformer weights.9 WebAssembly is a low-level instruction set designed for fast, deterministic execution and a universal target that languages such as C and C++ can compile to. To compute 3 + 5, the model would write:

```bash
{
i32.const 03 00 00 00
i32.const 05 00 00 00
i32.add 00 00 00 00
output 00 00 00 00
}
```

The model then switches to fast decoding mode and executes the program itself, step by step within the same transformer, producing an execution trace of tokens:

```bash
03 00 00 00  commit(+1,sts=1,bt=0)
05 00 00 00  commit(+1,sts=1,bt=0)
08 00 00 00  commit(-1,sts=1,bt=0)
out(08)
halt
```

Each line contains tokens the model generates. The stack grows, the `add` fires, the result is output, and the machine halts, all within the model's own output stream, with no external round-trip.

code external round-trip wasm program execution trace

Tool use external

Let me compute that.\`\`\`python python -c "print(3+5)" \`\`\`

sending code

External interpreter

$ python -c "print(3+5)"

running..

returning result

In-model execution ours

Let me compute that.{ i32.const 03 00 00 00 i32.const 05 00 00 00 i32.add 00 00 00 00 output 00 00 00 00 } 03 00 00 00 commit(+1,sts=1,bt=0) 05 00 00 00 commit(+1,sts=1,bt=0) 08 00 00 00 commit(-1,sts=1,bt=0) out(08) halt The answer is \*\*8\*\*.

The key difference is that tool use is opaque: the model hands off control and receives a black-box answer. In-model execution is transparent: every intermediate step appears in the trace, and the model never leaves its own decoding loop.

* * *

Sudoku is another useful stress test for exact long-horizon computation. Learned neural approaches can achieve strong performance on easy or random Sudokus but completely stumble on the hard ones.10 A common explanation is that autoregressive models are fundamentally ill-suited for constraint-satisfaction problems because they commit to answers token-by-token and cannot revise early mistakes.11 But our fully autoregressive system achieves 100% accuracy on these benchmarks, suggesting that the real bottleneck is not the autoregressive paradigm itself — it is that solving hard Sudokus requires very long execution traces, and standard attention makes long-context generation prohibitively expensive. This is exactly the problem our fast attention path addresses.

Our system executes a fully correct compiled Sudoku solver inside the transformer itself. There is no learned heuristic standing in for the algorithm and no gap between "the model suggested a solution" and "an external system verified it". The transformer executes the solver step by step.

The guarantee is universal rather than benchmark-specific: if the compiled solver is correct, the transformer's execution is correct as well. In practice, this lets the model solve even famously hard instances such as Arto Inkala's Sudoku, reaching the correct solution in under 3 minutes.

User

8........

.. 3 6.....

. 7.. 9. 2..

. 5... 7...

.... 4 5 7..

... 1... 3.

.. 1.... 6 8

.. 8 5... 1.

. 9.... 4..

**33,313** tok/s **2,713,917** tokens **7,338** lines/s

Assistant

Puzzle loaded — 21 clues given.

Propagated constraints — 21 of 81 cells resolved so far.

Need to search. Starting depth-first exploration...

Trying 3 at row 8, col 7.

No immediate violations.

Trying 9 at row 7, col 7.

Looks consistent.

Trying 2 at row 8, col 9.

Still consistent.

Trying 1 at row 1, col 7.

No violations so far.

Trying 2 at row 1, col 2.

Contradiction — that doesn't work.

Undoing row 1 col 7. Going back up.

Undoing row 8 col 9. Trying another path.

Trying 2 at row 8, col 5.

Contradiction again.

Trying 2 at row 6, col 5.

That works.

Trying 1 at row 3, col 1.

Contradiction.

Undoing row 6 col 5. Dead end, going back.

Undoing row 7 col 7. Trying a different value.

Trying 6 at row 9, col 3.

Looks good.

Trying 4 at row 3, col 3.

Contradiction.

Trying 4 at row 3, col 8 instead.

Also a contradiction.

Trying 2 at row 1, col 4.

8

2

3

6

7

9

2

5

7

4

5

7

1

3

1

6

8

8

5

3

1

9

6

4

* * *

## How can computation be encoded?

A useful way to picture an autoregressive transformer is as a machine that lives inside its own history. A traditional computer has editable memory that it updates as a result of operations. But in a transformer there is no such thing.

There is a fixed prompt (the input or the program). Then there is a trace that only grows (the tokens the model generates). At each step, the model can only "look back" through a small number of queries (attention heads), and must then append one more token. Through this process we need to find a way to encode a working machine.

To build intuition about this model and how the encoding works, it is helpful to think about the following.

* * *

### Computation as a trace that only appends

To understand how a transformer can execute a program internally, it helps to think of computation in a slightly unusual way.

Imagine a notebook where every step of a computation is written on the next line. Once written, earlier lines cannot be changed; the notebook only grows.

- The first few lines contain the input (the prompt).
- Each new line records the next step of the computation.
- At every step you are allowed to look back at earlier lines, but you cannot edit them.

This is surprisingly close to how an autoregressive transformer operates: the prompt is the input, the generated tokens form a trace that keeps growing, and each new token is produced after looking back at a small number of positions via attention.

Here is a toy example. Given a sentence, count whether the number of verbs is odd or even. Each trace token attends to exactly two positions: the corresponding input word (to check if it is a verb) and the previous trace token (to read the running parity).

Word 8 /11 attend

Prompt

the

cat

runs V

and

the

dog

jumps V

over

fences

quickly

Execution trace

E 0

E 0

O 1

O 1

O 1

O 1

E 2

…

?

?

?

Notice that each step only needs two lookbacks (one into the prompt and one into the trace), regardless of how long the sentence is. This is the key insight: many algorithms can be expressed as a trace that only appends, where each step reads a small, fixed number of earlier positions.

> Can a computation be represented as a trace that only appends, where each step only needs to look back a small number of times?

The answer is yes. In our system the model generates such a trace explicitly. The tokens it produces represent the evolving state of a virtual machine: instruction pointer, memory and stack operations, arithmetic, control flow, and outputs. The model reconstructs the current state simply by looking back to the relevant earlier steps.

In a transformer, the look-back operations are more expressive than simply inspecting past tokens. Each step can also read intermediate states computed while deciding which token to produce — these correspond to the values stored in different attention layers. Think of it this way: each attention head acts like a shared one-dimensional array. When processing a token, the head first writes a single value at some index, then may read a single value at a (potentially different) index — one write followed by at most one read, in that order. Each token reads values published by earlier tokens and publishes values to inform future decisions.

In addition to this read/write primitive, attention can also compute *cumulative sums*. This lets us track quantities like the instruction pointer, operand-stack depth, and call-stack depth as running sums of delta increments. Together, index lookup and summing are enough to run complex computation.

The rest of this post focuses on the efficiency challenge: even if a transformer can represent such an execution trace, standard decoding still pays a growing cost as the trace becomes longer. Our fast decoding path removes that handicap, and the 2D head restriction is the key unlock that makes the fast path possible.

## The key unlock: Exponentially Fast Attention

A real computer runs long programs by updating a compact state (registers, stack, memory) with near-constant work per instruction.

A standard transformer "advances state" by generating tokens, and each next token is computed by attention over a prefix that grows forever. KV caching reuses previously computed keys/values, but it does not remove the basic scaling: at each step the query still has to interact with a cache whose size grows with the number of generated tokens. This is why decoding research often becomes an IO problem: the bottleneck becomes "make the KV cache fast enough and score against it." 12

But no matter how fast one makes KV caching, the fundamental scaling remains: the t t -th decoding step still interacts with a prefix of length t t. This means work per step grows linearly with the trace length, and the total cost of generating t t tokens grows quadratically. This is a well-known bottleneck of transformers and it is an active area of research how to design faster alternatives.13

As we'll explain below, our approach addresses the quadratic blow-up and yields exponentially faster attention lookups. Instead of spending Θ (t) \\Theta(t) time per step, our method requires O (log ⁡ t) O(\\log t) time. Here is how it looks in practice, when using our HullKVCache compared to a standard KVCache:

Elapsed: **41.6s**

HullKVCache

**41,709** tok **31,037** tok/s (**6,747** lines/s)

0 {

126 input\_base 10 04 01 00

252 i32.const 00 00 00 00

378 local.set 09 00 00 00

504 i32.const 00 00 00 00

630 local.set 08 00 00 00

756...

882 i32.const 00 04 00 00

1007 i32.const 25 00 00 00

1133 i32.store 00 00 00 00

1259...

1385 return d4 fe ff ff

1511 }

1637 1 5 0 00 commit(+0,sts=0,bt=0)

1763 00 00 00 00 commit(+1,sts=1,bt=0)

1889 00 00 00 00 commit(-1,sts=0,bt=0)

2015 00 00 00 00 commit(+1,sts=1,bt=0)

2141 03 00 00 00 commit(+0,sts=1,bt=0)

2267 ee fe ff ff commit(-1,sts=0,bt=1)

2393 01 00 00 00 commit(+1,sts=1,bt=0)

2519 00 00 00 00 commit(+1,sts=1,bt=0)

2645 branch\_taken

2771 00 00 00 00 commit(-1,sts=0,bt=0)

2896 01 00 00 00 commit(+1,sts=1,bt=0)

3022 00 00 00 00 commit(-2,sts=0,bt=0)

3148 05 00 00 00 commit(-1,sts=0,bt=0)

3274 30 00 00 00 commit(+1,sts=1,bt=0)

3400 00 00 00 00 commit(-1,sts=1,bt=0)

3526 0a 00 00 00 commit(-1,sts=1,bt=0)

3652 00 00 00 00 commit(+1,sts=1,bt=0)

3778 08 00 00 00 commit(+1,sts=1,bt=0)

3904 08 00 00 00 commit(+1,sts=1,bt=0)

4030 00 00 00 00 commit(+1,sts=1,bt=0)

4156 00 00 00 0a commit(+0,sts=1,bt=0)

4282 08 00 00 00 commit(+1,sts=1,bt=0)

4408 branch\_taken

4534 01 00 00 00 commit(-1,sts=1,bt=0)

4660 06 00 00 00 commit(+1,sts=1,bt=0)

4785 03 00 00 00 commit(+1,sts=1,bt=0)

4911 59 00 00 00 commit(+1,sts=1,bt=0)

5037 0e 00 00 00 commit(-1,sts=1,bt=0)

5163 ff ff ff ff commit(+1,sts=1,bt=0)

5289 02 04 00 00 commit(+0,sts=0,bt=0)

5415 04 00 00 00 commit(-1,sts=0,bt=0)

5541 f3 ff ff ff commit(+0,sts=0,bt=1)

5667 3f 00 00 00 commit(+0,sts=0,bt=0)

5793 19 00 00 00 commit(-1,sts=0,bt=1)

5919 10 00 00 00 commit(-1,sts=1,bt=0)

6045 44 00 00 00 commit(+1,sts=1,bt=0)

6171 01 00 00 00 commit(+1,sts=1,bt=0)

6297 01 00 00 00 commit(-1,sts=0,bt=0)

6423 commit(-1,sts=0,bt=0)

6549 00 00 00 00 commit(-1,sts=1,bt=0)

6674 branch\_taken

6800 00 00 00 00 commit(-2,sts=0,bt=0)

6926 07 00 00 00 commit(-1,sts=1,bt=0)

7052 c7 fe ff ff return\_commit

7178 branch\_taken

7304 0a 00 00 00 commit(-1,sts=0,bt=0)

7430 01 00 00 00 commit(+1,sts=1,bt=0)

7556 out(31='1')

7682 1e 00 00 00 commit(-1,sts=1,bt=0)

7808 16 00 00 00 commit(-1,sts=1,bt=0)

7934 01 00 00 00 commit(+1,sts=1,bt=0)

8060 09 00 00 00 commit(+1,sts=1,bt=0)

8186 25 00 00 00 commit(+1,sts=1,bt=0)

8312 00 00 00 00 commit(+1,sts=1,bt=0)

8438 ee fe ff ff commit(-1,sts=0,bt=1)

8563 8d 00 00 00 commit(+0,sts=0,bt=0)

8689 64 00 00 00 commit(+1,sts=1,bt=0)

8815 02 00 00 00 commit(-1,sts=1,bt=0)

8941 halt

Line **9,067** / 9,580 Done in 1.3s

KVCache

**14,982** tok **362** tok/s (**79** lines/s)

0 {

126 input\_base 10 04 01 00

252 i32.const 00 00 00 00

378 local.set 09 00 00 00

504 i32.const 00 00 00 00

630 local.set 08 00 00 00

756...

882 i32.const 00 04 00 00

1007 i32.const 25 00 00 00

1133 i32.store 00 00 00 00

1259...

1385 return d4 fe ff ff

1511 }

1637 1 5 0 00 commit(+0,sts=0,bt=0)

1763 00 00 00 00 commit(+1,sts=1,bt=0)

1889 00 00 00 00 commit(-1,sts=0,bt=0)

2015 00 00 00 00 commit(+1,sts=1,bt=0)

2141 03 00 00 00 commit(+0,sts=1,bt=0)

2267 ee fe ff ff commit(-1,sts=0,bt=1)

2393 01 00 00 00 commit(+1,sts=1,bt=0)

2519 00 00 00 00 commit(+1,sts=1,bt=0)

2645 branch\_taken

2771 00 00 00 00 commit(-1,sts=0,bt=0)

2896 01 00 00 00 commit(+1,sts=1,bt=0)

3022 00 00 00 00 commit(-2,sts=0,bt=0)

3148 05 00 00 00 commit(-1,sts=0,bt=0)

Line **3,257** / 9,580 258.9s total

HullKVCache KVCache

0s 10s 20s 30s 40s 50s 60s 0 10k 20k 30k 40k 1.3s tokens generated time (s)

In the workloads we care about (long execution traces where the model repeatedly performs a small number of structured lookups per step), the difference in scaling per step compounds.

A linear scan decoder pays a cost that keeps growing as the trace grows. A hull-based decoder keeps the cost per step essentially tied to a retrieval primitive that runs in logarithmic time. Over long horizons, that changes what is feasible: computations that would be impractically slow under standard decoding become runnable for millions of steps.

This is also why the payoff shows up most clearly on "boring" deterministic spans: exact copying, state-machine stepping, or long mechanical traces. These are precisely the steps where we do not want to spend full attention budget.

### The fast path: 2D attention

We obtain this speed-up by reframing the question. We are not attempting to speed up transformers in full generality, nor do we want to introduce yet another architecture.

Instead, we focus on vanilla transformers but under a tractable parameterization. We specifically target the case where the dimension of the heads is small: 2D.

This does not mean that the whole transformer is small. You can still have an arbitrarily large number of layers, arbitrarily many heads and arbitrarily large embeddings. It just means that the embeddings used across layers of a transformer are broken into smaller chunks resulting in more heads n heads \= d model / 2 n\_\\text{heads} = d\_\\text{model} / 2.

Of course, this restriction can come at a cost for certain tasks and is not the magic answer to everything. While we are still exploring how limiting this is in practice for training, say, large models, we find that it is still flexible enough to train efficiently and can capture very complicated logic.

In fact, for Turing completeness, 2D attention is all you need! And it is still flexible enough to represent a whole RAM computer as we show in this blog. It is a crucial enabler of building a fast-path in transformers. While abstract reasoning and planning remain part of the original path, heavy computational tasks can go through the fast path.

The model itself is a completely standard PyTorch transformer, nothing exotic:

```python
class VanillaTransformer(nn.Module):
 def __init__(self, vocab, d_model=36, n_heads=18, n_layers=7, d_ffn=36):
 super().__init__()
 self.tok = nn.Embedding(vocab, d_model)
 self.attn = nn.ModuleList([
 nn.MultiheadAttention(d_model, n_heads, batch_first=True, bias=False)
 for _ in range(n_layers)
 ])
 self.ff_in  = nn.ModuleList([nn.Linear(d_model, 2*d_ffn, bias=False) for _ in range(n_layers)])
 self.ff_out = nn.ModuleList([nn.Linear(d_ffn, d_model, bias=False) for _ in range(n_layers)])
 self.head = nn.Linear(d_model, vocab, bias=False)

 def forward(self, idx):
 T = idx.shape[1]
 x = self.tok(idx) + pos_emb(T)
 causal = torch.triu(torch.ones(T, T, device=idx.device, dtype=torch.bool), diagonal=1)
 for attn, ff_in, ff_out in zip(self.attn, self.ff_in, self.ff_out):
 y, _ = attn(x, x, x, attn_mask=causal, need_weights=False)
 x = x + y
 gate, val = ff_in(x).chunk(2, dim=-1)
 x = x + ff_out(F.relu(gate) * val)
 return self.head(x)
```

Notice: `d_model = 36` with `n_heads = 18` gives exactly 2D per head. The architecture uses 7 layers, standard `nn.MultiheadAttention`, and a gated feed-forward network. No custom attention kernels, no sparse masks; just vanilla PyTorch. The only thing that makes it special is the weights.

Let's look at how 2D attention gets us these impressive speed-ups.

### The geometric view of 2D attention

Step 5 /15 query

q 5 k 1 v 1 \= 7 k 2 v 2 \= 3 k 3 v 3 \= 9 k 4 v 4 \= 2 k 5 v 5 \= 5 low q·k high q·k

Query q 5

#### Winner

k 2

value **3** · score **3.337**

#### Top scores

1 k 2 3.337

2 k 4 3.214

3 k 5 \-2.048

4 k 1 \-2.126

5 k 3 \-4.656

The attention mechanism works as follows:

- each past token contributes a key vector k j k\_j and a value v j v\_j,
- the current step forms a query vector q q,
- relevance scores are computed for every key q ⋅ k j q \\cdot k\_j, and
- the head returns the sum of values of all keys reweighted by the softmax of their scores.

In the special case that matters for our fast path:

- each key is 2D, k j ∈ R 2 k\_j \\in \\mathbb{R}^2,
- the query q ∈ R 2 q \\in \\mathbb{R}^2 can be thought of as a direction in the plane,
- and we want the value of the point that maximizes the dot product in that direction (hard-max attention). In case of ties, we compute the average.

Despite the maximization queries being global over the whole history, there exist efficient data-structures that can answer such 2D attention queries in logarithmic time in the number of points. That is exactly the classic "supporting point" query in computational geometry: given a direction q q, find the point on the convex hull furthest in that direction. We speed up decoding by maintaining such a data-structure as tokens get generated which lets us efficiently search over the whole set of past points.

Restricting the head dimension to 2 is what enables the fast path: during inference we can replace a brute force scan ("score against every key") with a structure where the maximum can be found by looking only at a tiny subset of points in the hull.

To implement memory and stack operations, we need each attention head to answer the query "give me the value most recently stored at index i i." This index lookup is what requires 2D keys.

Store every index j j as the 2D key k j \= (2 j,− j 2) k\_j = (2j, -j^2). Looking up index i i then amounts to querying in direction q \= (i,1) q = (i, 1), since

arg ⁡ max ⁡ j { (2 j,− j 2) ⋅ (i,1) } \= i \\arg\\max\_{j} \\{ (2j, -j^2) \\cdot (i,1) \\} = i

The quadratic term − j 2 \-j^2 acts as a penalty that grows for any j ≠ i j \\neq i, ensuring only the exact match wins the argmax.

Attention can also compute cumulative sums, which we use to track quantities like the instruction pointer and stack depth. If all keys are set to the same value, attention averages all values uniformly, and multiplying by the current token position t t recovers the actual sum. This only requires 1D (or even 0D) keys — it is index lookup that forces us to 2D.

* * *

## So what is next?

We showed that a transformer can become a computer, and that opens a new interface between software and neural networks. Once programs can run efficiently inside the model's own inference loop, a much larger design space opens up.

### Richer attention mechanisms

For simplicity, our construction uses hard-max attention. But that is not a fundamental restriction. While we do not yet know whether exact softmax attention can be maintained with the same efficiency, it is easy to approximate it with k-sparse softmax attention: retrieve the top- k k keys and perform the softmax only over those. By storing points across nested convex hulls, this yields a decoding cost of O (k + log ⁡ n) O(k + \\log n).

This means the geometric fast path is not limited to our executor construction. In principle, it can accelerate any transformer with 2D heads at decoding time, replacing full linear scans with efficient geometric retrieval. The same machinery also extends naturally to 3D heads via 3D convex hulls, although higher dimensions quickly become less efficient. The key question is whether 2D already captures most of the speedup, or whether slightly larger heads unlock substantially more capability.

q outer hull · inner hull · top-k points

**k-sparse softmax** retrieves the top‑ *k* keys from **nested convex hulls** and applies softmax only over those — cost **O(k + log n)**.

The same geometric machinery extends to **3D heads** via 3D convex hulls.

### Training large models with 2D heads

The 2D-head parameterization used here is not inherently small. The total parameter count can remain comparable to standard transformers because the model can simply use more heads and layers. The real question is how capable such models become when trained at scale.

That question matters even beyond pure capability. These models could be useful in several modes: as a dedicated fast path paired with a slower, more general model; as part of a fast/slow hybrid architecture inside a single system; or as a speculative execution model that proposes tokens quickly while a regular-attention model verifies and accepts them. Regardless of their eventual capability ceiling, they already suggest a powerful systems primitive for speeding up larger models.

Standard transformer

4 heads × d\_h = 64

d\_model = 256

2D-head transformer

128 heads × d\_h = **2**

d\_model = 256 (same budget)

Deployment modes

Fast path

Fast / slow hybrid

Speculative decoding

The system presented here is a standalone transformer designed as an executor. A natural next step is to combine it with a large language model and train the model to invoke this execution pathway when exact computation is required. In such a hybrid system the language model would plan and reason, while the execution component would run algorithms.

Because the execution trace is part of the forward pass, the whole process remains differentiable: we can even propagate gradients through the computation itself. That makes this fundamentally different from an external tool. It becomes a trainable computational substrate that can be integrated directly into a larger model.

### Programs into weights & training beyond gradient descent

In our current prototype the model learns an interpreter whose behavior is encoded in its weights. But the compilation machinery we built for generating those weights can go further. In principle, arbitrary programs can be compiled directly into the transformer weights, bypassing the need to represent them as token sequences at all.

That would make weights themselves a deployment target for software. Instead of merely learning software-like behavior, models could literally contain compiled program logic as part of their internal circuitry.

C source

int fib (int n) {

int a \= 0, b \= 1;

for (int i \= 0;

i < n; i ++) {

int t \= a + b;

a \= b; b \= t;

}

return a;

}

compile

Weights become a deployment target: instead of learning software-like behavior, models **contain** compiled program logic.

If logic can be compiled into weights, then gradient descent is no longer the only way to modify a model. Weight compilation provides another route for inserting structure, algorithms, and guarantees directly into a network.

Taken seriously, this suggests a different picture of training altogether: not just optimizing weights with data, but also writing parts of the model directly. Push that idea far enough and you get systems that do not merely learn from experience, but also modify or extend their own weights, effectively rewriting parts of their internal machinery.

### Growing AI systems like software

Finally, if software becomes part of the neural architecture, then AI systems need a way to grow over time much like software libraries do today. Modern software ecosystems evolve by accumulating modules, abstractions, and reusable components. A similar process may eventually occur inside AI systems, where new computational abilities are added incrementally to the model's internal execution engine.

core math sorting graph crypto DSP new

Just as software ecosystems grow by accumulating **modules**, AI systems can add computational abilities incrementally — each one compiled into the model's internal execution engine.

New capabilities connect to the existing circuit without retraining the whole system.

Our work shows that transformers can execute programs efficiently inside their own inference loop. The broader vision is that future AI systems will not just use software; they will contain it, integrating learned representations with compiled algorithms inside a single computational substrate. In that world, software itself becomes part of the model.

## Closing thoughts

We showed that transformers can execute programs efficiently inside their own inference loop, not as an external tool, but as part of the model itself. This opens a path toward AI systems that integrate learned representations with compiled algorithms inside a single computational substrate.

We think this matters because the hardest problems we care about, sequential decision-making under uncertainty in healthcare, supply chains, and financial institutions, will require systems that can both reason flexibly and compute reliably.

We are building these systems now, and we are hiring. If you want to work on problems at the intersection of language models, reinforcement learning, and real-world decision systems, [join us](https://jobs.ashbyhq.com/percepta).