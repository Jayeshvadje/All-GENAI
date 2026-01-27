from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



Template = PromptTemplate( template= "give me the summary of \n{topic}",
                           input_variables= ["topic"])

model = ChatGoogleGenerativeAI( model = "gemini-2.5-flash")


parser = StrOutputParser()


chain = Template | model | parser

result = chain.invoke({"topic" : "gentelman"})
print(result)




