import streamlit as st
import boto3

from boto3 import Session

# Insert CLI profile name here
boto_sess = Session(profile_name='boto3user')

s3_resource = boto_sess.resource('s3')
for bucket in s3_resource.buckets.all():
    st.write(bucket.name)

st.header('Welcome to  Audio Converter streamlit app!')


st.header("Audio to text")
audio = st.file_uploader("Choose a file")

if st.button("Run"):
    generated_text = "Got it"
    st.write(generated_text)
