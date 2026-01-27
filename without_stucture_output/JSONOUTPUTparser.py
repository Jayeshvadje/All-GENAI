from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

model= ChatGoogleGenerativeAI( model = "gemini-2.5-flash-lite")
parser = JsonOutputParser()

template=PromptTemplate(template= "give me the n5 fact about {topic} \n {format_instruction}",
                         input_variables=["topic"],
                         partial_variables={"format_instruction":parser.get_format_instructions()}
                         )
chain = template | model |parser
result = chain.invoke({"topic" :"black hole"})
print(result)