import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.title("Datasweeper Sterling Integrator by Moiz Qureshi")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization, creating the Project for Quarter 3!")

# Sidebar Menu with two buttons
sidebar_option = st.sidebar.radio("Select Option", ["XLSX and CSV", "Mindset"])

if sidebar_option == "XLSX and CSV":
    # File Uploader
    uploaded_files = st.file_uploader("Upload your files (accepts CSV and Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue

            # file details
            st.write("Preview the head of the dataframe")
            st.dataframe(df.head())

            # Data Cleaning Options
            st.subheader("Data Cleaning Options")
            if st.checkbox(f"Clean data for {file.name}"):
                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"Remove Duplicates from the file: {file.name}"):
                        df.drop_duplicates(inplace=True)
                        st.write("Duplicates removed successfully!")

                with col2:
                    if st.button(f"Fill missing values for {file.name}"):
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("Missing values have been filled!")

            # Select columns to Keep
            st.subheader("Select columns to Keep")
            columns = st.multiselect(f"Choose columns for: {file.name}", df.columns, default=df.columns)
            df = df[columns]

            # Data Visualization
            st.subheader("Data Visualization")
            if st.checkbox(f"Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

            # Conversion Options
            st.subheader("Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    buffer.seek(0)

                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

        st.success("All files processed successfully!")

elif sidebar_option == "Mindset":
    # Mindset functionality
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
