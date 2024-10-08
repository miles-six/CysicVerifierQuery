# Cysic Rewards Checker

这个项目用于检查 Cysic 网络上验证者的奖励信息。

## 功能

- 从预定义的地址列表中获取验证者信息
- 查询每个验证者的奖励
- 计算总奖励金额

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/miles-six/CysicVerifierQuery.git
   cd cysic_rewards
   ```

2. 运行安装脚本：
   ```
   chmod +x install_dependencies.sh
   ./install_dependencies.sh
   ```

   这将安装所有必要的 Python 依赖。

3. 确保您已安装 Chrome 浏览器和相应版本的 ChromeDriver。

## 使用方法

1. 编辑 `easy.py` 文件，在 `address_list` 中添加您想要查询的地址。

2. 运行脚本：
   ```
   python easy.py
   ```

3. 脚本将输出每个地址的验证者信息和奖励，以及总奖励金额。
4. 效果如下
<img width="617" alt="image" src="https://github.com/user-attachments/assets/65f4e8f5-0d42-4253-bab1-678cb6c1abb5">


## 注意事项

- 请确保遵守 API 的使用政策。
- 该脚本依赖于网页结构，如果网页发生变化，可能需要更新 XPath。
欢迎提交 Pull Requests 来改进这个项目。

