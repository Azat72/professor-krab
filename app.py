import streamlit as st
from utils import ask_professor_krab

st.set_page_config(page_title="Профессор КРАБ", layout="wide")
st.title("👨‍⚖️ Профессор КРАБ — юридический помощник")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("Ваш вопрос:")

if st.button("Задать вопрос"):
    if question.strip():
        answer = ask_professor_krab(question, st.session_state.chat_history)
        st.session_state.chat_history.append({"user": question, "bot": answer})

for chat in st.session_state.chat_history[::-1]:
    st.markdown(f"**Вы:** {chat['user']}")
    st.markdown(f"**Профессор КРАБ:** {chat['bot']}")
