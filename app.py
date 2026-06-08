import streamlit as st
from chatbot import generate_response

st.set_page_config(
    page_title="Career Advisor Chatbot",
    page_icon="🎯"
)

st.title("🎯 Career Advisor Chatbot")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask your career question...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(user_input)
            st.markdown(response)

    # Store assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })