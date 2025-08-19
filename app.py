import streamlit as st
import datetime
from groq import Groq

# Sidebar for API Key input
st.sidebar.title("🔑 Enter Groq API Key")
api_key = st.sidebar.text_input("Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)

    st.title("🔮 AI Astrologer (Groq Powered)")
    st.write("Enter your birth details and ask any astrology question!")

    # User Inputs
    name = st.text_input("Your Name")

    # Fix DOB issue → allow 1900 till today
    dob = st.date_input(
        "Date of Birth",
        value=datetime.date(2000, 1, 1),
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today()
    )

    tob = st.time_input("Time of Birth", value=datetime.time(12, 0))
    pob = st.text_input("Place of Birth")
    question = st.text_area("Ask any question (e.g., career, love, health)")

    if st.button("🔮 Get Astrology Reading"):
        user_prompt = f"""
        Name: {name}
        Date of Birth: {dob}
        Time of Birth: {tob}
        Place of Birth: {pob}
        Question: {question}

        You are a Vedic astrologer. Give a personalized astrology-based answer.
        """

        with st.spinner("Calculating your stars ✨..."):
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a wise Indian Vedic astrologer."},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

        st.subheader("🌟 Your Astrology Reading")
        st.write(response.choices[0].message.content)
else:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar to continue.")
