from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


template = PromptTemplate(template="give me the summary of the {topic}",input_variables=["topic"])

template1 = PromptTemplate(template="give me 5 points from the summary of following\n{ text}",input_variables=["text"])

model=ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

parser = StrOutputParser()

chain = template | model | parser |template1 | model | parser

result = chain.invoke({"topic" : "gentelman"})
print(result)

chain.get_graph().print_ascii()