from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, ChatMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

chat_history = [
SystemMessage(content ="you are a helpful AI Assistance")]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit" :
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print(chat_history)