#!/bin/bash
# --- 设置脚本的工作目录 (关键步骤) ---
# 无论脚本如何被启动，都先切换到脚本文件所在的目录。
cd "$(dirname "$0")"

# --- 配置输出目录 ---
OUTPUT_DIR="callmd2word"

# 作用:
# 1. 自动扫描当前目录，查找两种格式的 Markdown 文件。
# 2. 根据文件名中的日期对文件进行分组。
# 3. 对于每个日期，将所有相关的 .md 文件合并成一个 .md 文件。
# 4. 将所有生成的 .md 和 .docx 文件存放到名为 "$OUTPUT_DIR" 的子目录中。
# 5. 脚本会自动创建该子目录。

# --- 检查核心依赖 ---
if ! command -v pandoc &> /dev/null; then
    echo "错误：未安装 pandoc。请先安装 pandoc。"
    exit 1
fi

# --- 确保输出目录存在 ---
echo "信息：确保输出目录 '$OUTPUT_DIR' 存在..."
mkdir -p "$OUTPUT_DIR"

# --- 准备 Pandoc 转换选项 ---
declare -a PANDOC_OPTS
if [ -f "$(pwd)/template.dotx" ]; then
    echo "信息：找到模板文件 'template.dotx'，将使用该模板进行转换。"
    PANDOC_OPTS=("--reference-doc=$(pwd)/template.dotx")
else
    echo "警告：未找到 'template.dotx' 模板文件，将使用默认样式。"
    PANDOC_OPTS=()
fi
echo "========================================"

# --- 主逻辑：查找唯一日期，并直接在循环中处理 ---
find . -maxdepth 1 -type f \( -name "????-??-??_*.md" -o -name "ReadItLater ????-??-?? *.md" \) -exec basename {} \; | \
sed -n -e 's/^\(....-..-..\)_.*/\1/p' -e 's/^ReadItLater \(....-..-..\) .*/\1/p' | \
sort -u | \
while IFS= read -r date; do
    if [ -z "$date" ]; then
        continue
    fi

    echo ""
    echo "--- 开始处理日期: $date ---"

    # 【关键修改】将输出文件名指向子目录
    MERGED_MD="${OUTPUT_DIR}/${date}.md"
    OUTPUT_DOCX="${OUTPUT_DIR}/${date}.docx"

    > "$MERGED_MD"
    echo "信息：已创建/清空合并文件 '$MERGED_MD'"

    is_first_file=true

    find . -maxdepth 1 -type f \( -name "${date}_*.md" -o -name "ReadItLater ${date} *.md" \) -print0 | sort -z | \
    while IFS= read -r -d $'\0' md_file; do
        clean_filename=$(basename "$md_file")
        echo "  -> 正在合并: $clean_filename"

        title=""
        case "$clean_filename" in
            "????-??-??_"*)
                title=$(echo "$clean_filename" | cut -d'_' -f3- | sed 's/\.md$//')
                ;;
            "ReadItLater "*)
                title=$(echo "$clean_filename" | sed 's/\.md$//' | cut -d' ' -f1,3)
                ;;
            *)
                title=$(basename "$clean_filename" .md)
                ;;
        esac

        if [ "$is_first_file" = false ]; then
            echo -e "\n\n---\n\n" >> "$MERGED_MD"
        fi
        is_first_file=false

        echo "# $title" >> "$MERGED_MD"
        echo "" >> "$MERGED_MD"
        cat "$md_file" >> "$MERGED_MD"
    done

    echo "信息：日期 '$date' 的所有文件已合并到 '$MERGED_MD'"

    echo "信息：正在将 '$MERGED_MD' 转换为 '$OUTPUT_DOCX'..."
    pandoc \
        "${PANDOC_OPTS[@]}" \
        --from=gfm \
        --to=docx \
        --output="$OUTPUT_DOCX" \
        "$MERGED_MD"

    if [ $? -eq 0 ]; then
        echo "成功：已生成 Word 文档 '$OUTPUT_DOCX'"
    else
        echo "错误：文件 '$MERGED_MD' 转换为 Word 文档失败！"
    fi
done

echo ""
echo "========================================"
echo "所有任务已完成。文件已生成在 '$OUTPUT_DIR' 目录中。"
# 增加一个暂停，以便在双击运行时能看到输出结果
echo "按 Enter 键退出..."
read