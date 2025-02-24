import streamlit as st

# Set page config at the very beginning
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟")

st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to your growth journey!")
st.write("Embrace Challenge, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

st.header("🔧 What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Conditions
if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goals!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflecting
st.header("Reflect on your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements
st.header("🏆 Celebrate your win!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("Big and small, every achievement counts! Share one now 🙂")

# Footer
st.write("_ _ _")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**©️ Created by Moiz Qureshi**")
