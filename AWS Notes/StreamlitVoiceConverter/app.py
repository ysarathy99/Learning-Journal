import steamlit as st
import boto3

st.header("Audio to text")
audio = st.file_uploader("Choose a file")

if st.button("Run"):
    generated_text = "Got it"
    st.write(generated_text)
