import streamlit as st
from src import Conversation

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Goodbye World")
convo = Conversation()
user_input = st.text_input("Start speaking")
for message in convo.messages:
    st.text(message["content"])
if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Here call convo.speak and get assistant reply:
    reply = convo.speak(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})

print(st.session_state.messages)
for msg in st.session_state.messages:
    st.write(f"**{msg['role'].capitalize()}:** {msg["content"]}")