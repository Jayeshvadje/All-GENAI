from dataclasses import Field

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, Annotated,Optional,Literal
from pydantic import BaseModel,Field

model= ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

#schema

class Review(BaseModel):
    Key_themes :list[str] =  Field(description="write down all the things discussed in the review in the list.")
    pros : Optional[list[str]]= Field(default=None,description="Write down all the pros inside the list if pros are mentioned other wise do not put it")
    cons: Optional[list[str]] =Field(default =None, description= "Write down all the cons inside the list if cons are mentioned other wise do not put it")
    summary:str = Field(description ="A brief summary of this review")
    sentiment:Literal["pos","neg"]=Field(description="Return sentiment of this review either neutral , negative or positive")

Structured_model = model.with_structured_output(Review)

result = Structured_model.invoke("I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—do I really need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.Pros:Insanely powerful processor (great for gaming and productivity)Stunning 200MP camera with incredible zoom capabilities Long battery life with fast charging S-Pen support is unique and useful Cons: Bulky and heavy – not great for one-handed use Bloatware still exists in One UI Expensive compared to competitors")

print(result)
