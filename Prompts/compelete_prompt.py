from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, load_prompt
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")
template = load_prompt("template.json")

chain = template | model

result = chain.invoke({"story_name":"a father of a son" , "genre" : "horror"})


story_text = result.content

with open("story_content.txt","w", encoding="utf-8") as f:
    f.write(story_text)
    f.close()
print("\n[Success] Story saved successfully to story.txt!")

prompt_template = ChatPromptTemplate([("system","you are a helpfull chatbot assistance"),
                                      MessagesPlaceholder(variable_name ="story_content"),
                                      ("human","{quetion}")
                                      ])


with open("story_content.txt","r",encoding="utf-8") as f:
    story_context = f.read()
    f.close()


prompt_template = ChatPromptTemplate([
    ("system",
        "You are a helpful chatbot assistant. Answer the user's questions based "
        "strictly on the following story context:\n\n{story_context}"),
    ("human","{question}")
     ])
qa_chain=prompt_template | model
result1 = qa_chain.invoke({
    "story_context": story_context,
    "question": "what is the name of the son"
})


print("\nBot Answer:")
result1=result1.content
print(result1)