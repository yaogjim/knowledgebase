import os
import re

def get_analysis_files():
    """获取所有分析文档文件"""
    analysis_files = []
    for root, _, files in os.walk("analysis"):
        for file in files:
            if file.endswith(".md"):
                analysis_files.append(os.path.join(root, file))
    return analysis_files

def extract_project_info(file_path):
    """从分析文档中提取项目信息"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 假设每个文档的开头都有项目名称和描述
    title_match = re.search(r'# (.*?)\n', content)
    desc_match = re.search(r'\n> (.*?)\n', content)
    
    title = title_match.group(1) if title_match else os.path.basename(file_path)
    description = desc_match.group(1) if desc_match else ""
    
    return {
        'title': title,
        'description': description,
        'path': file_path
    }

def generate_project_list():
    """生成项目列表的 Markdown 内容"""
    files = get_analysis_files()
    projects = [extract_project_info(f) for f in files]
    
    md_content = []
    for p in projects:
        md_content.append(f"### [{p['title']}]({p['path']})")
        if p['description']:
            md_content.append(f"{p['description']}\n")
    
    return "\n".join(md_content)

def update_readme():
    """更新 README.md 文件"""
    with open('README.template.md', 'r', encoding='utf-8') as f:
        template = f.read()
    
    project_list = generate_project_list()
    
    # 替换项目列表
    new_content = re.sub(
        r'<!-- PROJECT_LIST_START -->.*<!-- PROJECT_LIST_END -->',
        f'<!-- PROJECT_LIST_START -->\n{project_list}\n<!-- PROJECT_LIST_END -->',
        template,
        flags=re.DOTALL
    )
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_readme() 