import os
import requests

# 從 GitHub Secrets 取得資料
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "🎉 恭喜！GitHub Actions 已成功執行！"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

print(response.text)
