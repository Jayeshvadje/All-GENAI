from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import dotenv
dotenv.load_dotenv()
model=ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
prompt= PromptTemplate(template = "Make a summary from the poem - \n {poem}",input_variables = ["poem"])

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")
chain = prompt | model | parser

data = loader.load()
result = chain.invoke({"poem" : data[0].page_content})
print(result)
