from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel



model1 = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
model2 = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")


template1 = PromptTemplate(template = "give me the notes from following text file {text}",input_variables = ["text"])

template2 = PromptTemplate(template="make a 20 quetion quiz from the following text file {text}",input_variables=["text"])

template3 = PromptTemplate(template="merge the provided notes and quiz into same document {notes} and {quiz}",input_variables=["notes","quiz"])

parser = StrOutputParser()


parallel_chains = RunnableParallel({"notes": template1 | model1 |parser,
                                    "quiz": template2 | model2 | parser})

merge_chain = template3 | model2 | parser

chain = parallel_chains | merge_chain
with open("ML_word.txt","r") as file:
    content = file.read()

result = chain.invoke({"text":content})
print(result)

chain.get_graph().print_ascii()