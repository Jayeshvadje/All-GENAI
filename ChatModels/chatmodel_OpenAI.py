from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-5-nano",temperature=1.5,max_completion_tokens=100)

Result = model.invoke("who is indian cricket team captain")

print(Result.content)