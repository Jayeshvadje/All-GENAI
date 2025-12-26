from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

messages = [SystemMessage("you are a helpfull assistance"),
           HumanMessage("tell me about langchain")]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)