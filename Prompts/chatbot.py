from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate ,ChatPromptTemplate ,MessagesPlaceholder
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

prompt_template = ChatPromptTemplate([("system","you are a helfull chatbot assistance"),
                                      MessagesPlaceholder(variable_name ="chat_history"),
                                      ("human","{query}")
                                      ])

import os

# Get the directory where chatbot.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "chat_history.txt")
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

result = prompt_template.invoke({"chat_history" : chat_history , "query" : "where is my refund "})
print(result)
