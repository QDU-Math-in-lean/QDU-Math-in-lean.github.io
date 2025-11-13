#!/bin/bash

echo "QDU Math in Lean"
echo "================================"
echo ""
echo "请选择操作："
echo "1) 更新文件列表"
echo "2) 启动本地服务器"
echo "3) 两者都执行"
echo "4) 退出"
echo ""
read -p "请输入选项 (1-4): " choice

case $choice in
    1)
        echo ""
        echo "正在扫描并更新文件列表..."
        python3 generate_filelist.py
        echo ""
        echo "完成！"
        ;;
    2)
        echo ""
        echo "启动本地服务器..."
        echo "访问: http://localhost:8000/project.html"
        echo "按 Ctrl+C 停止服务器"
        echo ""
        python3 -m http.server 8000
        ;;
    3)
        echo ""
        echo "正在扫描并更新文件列表..."
        python3 generate_filelist.py
        echo ""
        echo "文件列表更新完成！"
        echo ""
        echo "启动本地服务器..."
        echo "访问: http://localhost:8000/project.html"
        echo "按 Ctrl+C 停止服务器"
        echo ""
        python3 -m http.server 8000
        ;;
    4)
        echo "再见！"
        exit 0
        ;;
    *)
        echo "无效选项"
        exit 1
        ;;
esac
