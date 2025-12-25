from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=2)

st.header("Reasearch Tool ")

paper_input = st.selectbox("")

user_input=st.text_input("Enter your search term")

if st.button("Search"):
    result = model.invoke(user_input)
    st.text(result.content)
