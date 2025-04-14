import requests
import os

API_KEY = os.getenv("API_KEY")  # получаем ключ из настроек Streamlit
API_URL = "https://api.deepseek.com/chat/completions"

def ask_professor_krab(question, chat_history):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {
            "role": "system",
            "content": "Ты — Профессор КРАБ (КРБ-Аналитика), эксперт в области права. Отвечай чётко, профессионально и с лёгким юмором. Представляйся в начале."
        }
    ]

    # добавляем историю чата
    for msg in chat_history:
        messages.append({"role": "user", "content": msg["user"]})
        messages.append({"role": "assistant", "content": msg["bot"]})

    # добавляем новый вопрос
    messages.append({"role": "user", "content": question})

    data = {
        "model": "deepseek-chat",
        "messages": messages,
        "stream": False
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Ошибка: {response.status_code} - {response.text}"
