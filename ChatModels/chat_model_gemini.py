from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

Model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temprature = 2.0,max_completion_tokens=100)

Result =Model.invoke("writea 5 line poem on cricket")

print(Result.text)