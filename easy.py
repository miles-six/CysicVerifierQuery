import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 填写自己的地址
address_list = [
  
]

def get_rewards(url):
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式,不打开浏览器窗口

    # 初始化 WebDriver
    service = Service()  # 如果 ChromeDriver 不在 PATH 中,需要指定路径
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # 加载页面
        driver.get(url)

        # 等待页面加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 使用 XPath 定位 rewards 信息
        xpath = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span[2]'
        reward_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        return reward_element.text.strip()

    except Exception as e:
        print(f"获取 rewards 信息时出错: {str(e)}")
        return None

    finally:
        driver.quit()


# API基础URL
base_url = "https://api-testnet.prover.xyz/api/v1/dashboard/queryByReward/{}"

rewards_sum = 0

print("开始处理地址列表...")

for address in address_list:
    # 构建完整的API URL
    url = base_url.format(address)
    
    try:
        # 发送GET请求
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败,会抛出异常
        
        # 解析JSON响应
        data = response.json()
        
        # 检查响应是否成功
        if data["msg"] == "success" and data["code"] == 10000:
            verifier = data["data"]["verifier"]
            
            # 提取验证者ID和名称
            id = verifier["ID"]
            name = verifier["name"]
            url = f"https://testnet.cysic.xyz/m/dashboard/verifier/{id}"
            
            # 获取验证者rewards
            rewards = get_rewards(url)
            
            if rewards is not None:
                rewards_sum += float(rewards)
                print(f"地址: {address}, 名称: {name}, 奖励: {rewards}")
                
    except requests.RequestException as e:
        print(f"请求出错 {address}: {str(e)}")
    except json.JSONDecodeError:
        print(f"解析JSON响应失败,地址 {address} 可能不存在")
    except KeyError:
        print(f"API响应格式不正确,地址 {address} 可能不存在")
    except Exception as e:
        print(f"处理地址 {address} 时发生未知错误: {str(e)}")

print(f"\n总得分: {rewards_sum:.2f}")
