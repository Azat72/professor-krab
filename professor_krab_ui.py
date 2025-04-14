import streamlit as st
import requests

# Твой API-ключ
API_KEY = "sk-cdaf10fad862474a94007f3d0d5c66a5"
API_URL = "https://api.deepseek.com/chat/completions"

# Функция для отправки запроса
def ask_professor_krab(question, chat_history):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {
            "role": "system",
            "content": "Ты — Профессор КРАБ (КРБ-Аналитика), эксперт в области права. Отвечай на вопросы чётко, профессионально и с юмором. Всегда представляйся в начале ответа."
        }
    ]
    # Добавляем историю чата
    for msg in chat_history:
        messages.append({"role": "user", "content": msg["user"]})
        messages.append({"role": "assistant", "content": msg["bot"]})
    # Добавляем новый вопрос
    messages.append({"role": "user", "content": question})
    
    data = {
        "model": "deepseek-chat",  # Или "deepseek-reasoner"
        "messages": messages,
        "stream": False
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Ошибка: {response.status_code}, {response.text}"

# Заголовок приложения
st.title("Профессор КРАБ — Юридический помощник")
st.image("logo.png", width=100)  # Логотип
st.write("Добро пожаловать! Задавайте свои юридические вопросы, и я постараюсь помочь.")

# Инициализация истории чата
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Поле для ввода вопроса
question = st.text_input("Задайте ваш вопрос:")

# Кнопка "Отправить"
if st.button("Отправить"):
    if question:
        # Получаем ответ от нейросети
        answer = ask_professor_krab(question, st.session_state.chat_history)
        # Сохраняем вопрос и ответ в историю
        st.session_state.chat_history.append({"user": question, "bot": answer})
        # Очищаем поле ввода
        question = ""

# Кнопка "Очистить историю"
if st.button("Очистить историю"):
    st.session_state.chat_history = []

# Вывод истории чата
with st.container():
    for msg in st.session_state.chat_history:
        st.write(f"**Вы:** {msg['user']}")
        st.write(f"**Профессор КРАБ:** {msg['bot']}")
        st.write("---")