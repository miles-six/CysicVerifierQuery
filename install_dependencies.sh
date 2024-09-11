#!/bin/bash

# 检查是否安装了 pip
if ! command -v pip &> /dev/null
then
    echo "pip 未安装。请先安装 Python 和 pip。"
    exit 1
fi

# 安装依赖
pip install -r requirements.txt

# 检查是否安装成功
if [ $? -eq 0 ]; then
    echo "依赖安装成功！"
else
    echo "依赖安装失败，请检查错误信息。"
fi