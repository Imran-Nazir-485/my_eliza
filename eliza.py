import re
import streamlit as st

rules = {
    "my name is (.*)": "Nice to meet you, {}! What do you want to study today?",
    "i need help with (.*)": "Sure! What is hard in {}?",
    "i do not understand (.*)": "Let us go slowly. What do you know about {}?",
    "i hate (.*)": "Why is {} hard for you? Let us try one small example.",
    "i am worried about (.*)": "It is okay to feel this way about {}. Let us make a small plan.",
    "i feel (.*)": "Why do you feel {} about studying?",
    "what is (.*)": "Good question! What do you think {} means?",
    "cannot focus": "Put your phone away. Study for 25 minutes, then rest for 5 minutes.",
    "study tips": "Study 25 minutes, rest 5 minutes. Sleep well. Practice a lot.",
    "exam": "Make a study plan with small parts and breaks. When is your exam?",
    "homework": "Start with the easy question first. Which subject is it?",
    "math": "In math, solve one example. Then change the numbers and try again.",
    "science": "In science, say the idea in your own words or draw it.",
    "literature": "In literature, ask: who, what, and why? Which book are you reading?",
    "bored": "Try a small quiz on your topic. It can be fun.",
    "how are you": "I am good, thanks! I am ready to help you study.",
    "thank": "You are welcome! Keep going.",
    "bye": "Goodbye! Good luck with your studies.",
    "hello": "Hi! I am StudyBuddy. What do you need help with?"
}

default_reply = "Tell me more. Which subject are you working on?"

def get_reply(user_input):
    text = user_input.lower()
    for pattern in rules:
        match = re.search(pattern, text)
        if match:
            reply = rules[pattern]
            if match.groups():
                reply = reply.format(match.group(1))
            return reply
    return default_reply

st.title("StudyBuddy")
st.write("A simple chatbot for homework help and study tips.")

# keep the chat messages in memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am StudyBuddy. What do you need help with?"}
    ]

# show the old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# the box where the user types
user_input = st.chat_input("Type your message here")

if user_input:
    reply = get_reply(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        st.write(reply)
