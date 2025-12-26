from click import prompt
from langchain_core.prompts import ChatPromptTemplate
chat_template = ChatPromptTemplate([("system","you are a helpful {domain} expert"),
                                    ("human","Explain in the simple terms ,what is {topic}")])

prompt= chat_template.invoke({"domain":"Cricket","topic":"Dusra"})
print(prompt)