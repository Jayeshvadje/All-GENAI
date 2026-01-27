from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from typing import Literal
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch ,RunnableLambda
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()
class feedback(BaseModel):
    sentiment : Literal["POSITIVE","NEGATIVE"] = Field(description="Sentiment of the feedback")

parser2= PydanticOutputParser(pydantic_object = feedback)

template1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback as either positive or negative.
Feedback:
{feedback}
{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    }
)

classifer_chain = template1 | model|parser2

template2 = PromptTemplate(template="Write an appropriate  response to this positive feedback\n{feedback}",
                           input_variables=["feedback"] )
template3 = PromptTemplate(template="Write an appropriate  response to this negative feedback\n{feedback}",
                           input_variables=["feedback"] )
branch_chain = RunnableBranch(
    (lambda x:x.sentiment =="positive",template2 | model | parser),
    (lambda x:x.sentiment =="positive",template3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifer_chain | branch_chain

result = chain.invoke({"feedback" : "this is a wonderful phone "})

print(result)