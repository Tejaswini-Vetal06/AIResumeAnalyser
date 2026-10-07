import streamlit as st
from resume_analyzer import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Resume Analyzer")

st.write(
    "Upload your resume and get an AI-powered analysis."
)


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing your resume..."):

            result = analyze_resume(uploaded_file)

        st.subheader("📊 Resume Analysis")

        st.write(result)