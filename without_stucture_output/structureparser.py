from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model= ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

template1 =PromptTemplate(template = 'write a deatiled summary on {topic}',
                          input_variable = ["topic"])

template2= PromptTemplate(template = 'Write a 5 line summary on {text}',
                          input_variable = ["text"])



parser =StrOutputParser()

Chain = template1 | model | parser | template2 | model | parser

result = Chain.invoke({"topic" : "black hole"})
print(result)