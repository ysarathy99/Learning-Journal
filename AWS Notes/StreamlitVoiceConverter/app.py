
Streamlit App: Voice Converter
  
import streamlit as st
import boto3

from boto3 import Session

# Insert CLI profile name here
boto_sess = Session(profile_name='user with permissions to runtime')

st.header('Welcome to  Audio Converter streamlit app!')

sagemaker_runtime = boto_sess.client('sagemaker-runtime',region_name='choose-region')
# prior to this step, you should have deployed your model in Sagenaker, noted the endpoint 
endpoint_name='your_end_point' #e.g. will be a hugging-face-whisper--xxx series, depending on your runtime GPU choices

def generate_text(audio):
    payload=audio
    response = sagemaker_runtime.invoke_endpoint(EndpointName=endpoint_name,ContentType='audio/wav',Body=payload)
    result=response['Body'].read()
    text=result
    return text

st.header("Audio to text")
audio = st.file_uploader("Choose a file")

if st.button("Run"):
    generated_text = generate_text(audio)
    st.write(generated_text)
