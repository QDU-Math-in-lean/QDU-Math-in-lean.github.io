#!/usr/bin/env python3
"""
简单的HTTP服务器，支持自动扫描Markdown文件
运行方式: python3 server.py
然后访问: http://localhost:8000/project.html
"""

import http.server
import socketserver
import json
import os
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 如果请求的是文件列表API
        if self.path == '/api/files':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # 扫描sources目录下的所有.md文件
            files = []
            sources_dir = Path('sources')
            if sources_dir.exists():
                for md_file in sources_dir.rglob('*.md'):
                    # 转换为相对路径，使用正斜杠
                    file_path = str(md_file).replace('\\', '/')
                    files.append(file_path)
            
            # 排序文件列表
            files.sort()
            
            # 返回JSON数据
            response = json.dumps(files, ensure_ascii=False)
            self.wfile.write(response.encode('utf-8'))
        else:
            # 其他请求使用默认处理
            super().do_GET()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"服务器运行在 http://localhost:{PORT}/")
        print(f"请访问: http://localhost:{PORT}/project.html")
        print("按 Ctrl+C 停止服务器")
        httpd.serve_forever()
