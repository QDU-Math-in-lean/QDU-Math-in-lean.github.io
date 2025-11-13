#!/usr/bin/env python3
"""
自动生成文件列表的脚本
运行方式: python3 generate_filelist.py
会自动更新 project.html 中的文件列表
"""

import os
from pathlib import Path

def scan_markdown_files(directory='sources'):
    """扫描指定目录下的所有 Markdown 文件"""
    files = []
    sources_dir = Path(directory)
    
    if sources_dir.exists():
        for md_file in sorted(sources_dir.rglob('*.md')):
            # 转换为相对路径，使用正斜杠
            file_path = str(md_file).replace('\\', '/')
            files.append(file_path)
    
    return files

def generate_filelist_js(files):
    """生成 JavaScript 文件列表代码"""
    js_code = "        const fileList = [\n"
    for file in files:
        js_code += f"            '{file}',\n"
    js_code += "        ];"
    return js_code

def update_html_file(html_file='project.html'):
    """更新 HTML 文件中的文件列表"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 扫描文件
    files = scan_markdown_files()
    new_filelist = generate_filelist_js(files)
    
    # 查找并替换文件列表部分
    start_marker = "        const fileList = ["
    end_marker = "        ];"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("错误：找不到文件列表配置")
        return False
    
    # 找到结束位置
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print("错误：找不到文件列表结束标记")
        return False
    
    end_idx += len(end_marker)
    
    # 替换内容
    new_content = content[:start_idx] + new_filelist + content[end_idx:]
    
    # 写回文件
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"成功更新文件列表，共 {len(files)} 个文件：")
    for file in files:
        print(f"   - {file}")
    
    return True

if __name__ == '__main__':
    update_html_file()
