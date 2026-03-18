from groq import Groq
import streamlit as st
from PyPDF2 import PdfReader

client = Groq(api_key="your_free_api_key")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    if st.button("Analyze"):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{
                "role": "user",
                "content": f"Analyze resume and give ATS score, skills, missing skills, suggestions:\n{resume_text}"
            }]
        )

        st.write(response.choices[0].message.content)