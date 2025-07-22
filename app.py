import streamlit as st
from src import Conversation

st.markdown("""
<style>
    .chat-message {
        padding: 0.75rem 1rem;
        margin: 0.5rem;
        border-radius: 1rem;
        max-width: 70%;
        word-wrap: break-word;
        display: inline-block;
    }

    .chat-user {
        margin-left: auto;
        text-align: right;
    }

    .chat-assistant {
        margin-right: auto;
        text-align: left;
    }

    .chat-container {
        display: flex;
        flex-direction: column;
    }
            
    /* Light Theme */
    @media (prefers-color-scheme: light) {
    .chat-user {
        background-color: #DCF8C6;
        color: black;
        }

    .chat-assistant {
        background-color: #F1F0F0;
        color: black;
        }
    }

    /* Dark Theme */
    @media (prefers-color-scheme: dark) {
    .chat-user {
        background-color: #2e8b57;
        color: white;
        }

    .chat-assistant {
        background-color: #444654;
        color: white;
        }
    }
""", unsafe_allow_html=True)

model = st.text_input("Enter a model")
if model:
    convo = Conversation(model)
else:
    convo = Conversation()

st.title("My RAGBot")
# Initialize message state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    content = msg["content"]
    css_class = "chat-user" if msg["role"] == "user" else "chat-assistant"
    st.markdown(f"""
    <div class="chat-container">
        <div class="chat-message {css_class}">{content}</div>
    </div>
    """, unsafe_allow_html=True)

# Chat input box (at the bottom)
input_text = st.chat_input("Start speaking")

if input_text:
    # Send input to the LLM
    reply = convo.speak(input_text)  # This should also internally update convo.messages
    
    # Store user and assistant messages
    st.session_state.messages += convo.messages
    st.rerun()
 # Add prompt and response to state messages
    # st.experimental_rerun()
# print(st.session_state.messages)