from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st


st.header("Reasearch Tool ")

user_input=st.text_input("Enter your search term")

if st.button("Search"):
    st.text("Enter your search term")
