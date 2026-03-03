from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import dotenv
dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
prompt_template1 = PromptTemplate(input_variables=["email"],
                                 template= "Classify the {email} type whether its complaint,inquiry,feedback")

if  prompt_template1 == "complaint":
    model.invoke("Generate apology-style response")
elif prompt_template1 == "inquiry":
     model.invoke("Generate informative response")
elif prompt_template1 == "feedback":
    model.invoke("Generate appreciation response")
else:
    model.invoke("Generate thankyou response")

parser=StrOutputParser()

chain = prompt_template1 | model | parser
result = chain.invoke({"email" : "I am very disappointed. My order arrived damaged and nobody is responding."})
print(result)
