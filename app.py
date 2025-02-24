import streamlit as st

st.set_page_config ( page_title = "Growth Mindset Project", project_icon = "🌟" )
st.title ("Growth Mindset Challenge: Web App with Streamlit")

st.header ("🚀 Welcome to your growyh journey!")
st.write ("Embrace Challenge, learn from mistakes, and unlock your full potentail. This AI Powered app help you build a growth mindset with reflaction, Challenge and achievements! 🌟")

# Quote Section
st.header ("💡 Today's Growth Mindset Quote")
st.write ("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

st.header ("🔧 What's your Challenge Today?")
user_input = st.text_input ("Describe a challenge you're fucing:")


# Conditions
if user_input:
    st.success (f"💪 You're fucing: {user_input}. Keep pushing forwards your goals!🚀")
else:
    st.warning ("Tell as about your challenge to get started!")

# reflexing
st.header ("Reflact on your Learning")
reflaction = st.text_area ("Write your reflaction here:")

if reflaction:
    st.success (f"✨Great Insight! your reflaction: {reflaction}")
else:
    st.info ("Reflacting on past experience help you grow! Share your difficulties")


# Acheivements
st.header("🏆 Celebrate your win!")
acheivment = st.text_input("Share something you've recently accomplished:")

if acheivment:
    st.success(f"🌟 Amazing! you acheived: {acheivment}")
else:
    st.info("Big and Small, every acheivement count! Share one now 🙂")


# Footer
st.write("_ _ _")
st.write("🚀 Keep Believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("** ©️ Create by Moiz Qureshi **")
