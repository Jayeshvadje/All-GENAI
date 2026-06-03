from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional ,Literal

from openai.types.responses.response_reasoning_item import Summary

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")
# class review(TypedDict):
#     name : Annotated[Optional[str],"Write the name of the person who is giving this review only if the name is provided"]
#     age : Annotated[Optional[int],"Write the age of the person who is giving this review only if the age is provided"]
#     Key_themes : Annotated[list[str],"Write the all the thing written in the review "]
#     pro : Annotated[Optional[list[str]],"Write down all the pros inside the list if pros are mentioned other wise do not put it"]
#     cons: Annotated[
#         Optional[list[str]], "Write down all the cons inside the list if pros are mentioned other wise do not put it"]
#     Summary : Annotated[str, "Write a short summary of the review"]
#
# structured_model = model.with_structured_output(review)

# result = structured_model.invoke("Title:Finally, the base iPhone feels completely Pro.""I’ve been using my iPhone 17 (256GB, Mist Blue) for a few months now, and I can confidently say this is the base-model iPhone Apple should have made years ago. The addition of the 120Hz ProMotion display is a game-changer—scrolling is buttery smooth, and the screen is absolutely gorgeous, especially when compared to older 60Hz models.The new A19 chip runs everything flawlessly, from heavy games to everyday multitasking, without breaking a sweat. I also appreciate that Apple made 256GB the base storage—it takes a lot of the pressure off when shooting 4K video. Speaking of cameras, the 48MP Ultra Wide and the upgraded 18MP front selfie sensor are fantastic; the photos are incredibly crisp, and the added flexibility is super noticeable during social events.Battery life has been solid as well. It comfortably gets me through a full day of typical use with about \(20\%\) to \(30\%\) to spare by midnight. If you’re upgrading from an iPhone 16 or older, this phone doesn't feel like a compromise at all. Highly recommend!")

# print(result)
# print(result["Summary"])
# print(result["name"])
# print(result["cons"])
# print(result["Key_themes"])

# above code is for type dict and below is for pydentic

from pydantic import BaseModel,Field

class Review2(BaseModel):
    name: Optional[str]= Field( description="Write the name of the person who is giving this review only if the name is provided")
    age: Optional[int]= Field(description= "Write the age of the person who is giving this review only if the age is provided")
    Key_themes:list[str]= Field(description= "Write the all the thing written in the review ")
    Summary: str= Field(description="Write a short summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of this review either neutral , negative or positive")


structured_model = model.with_structured_output(Review2)
result = structured_model.invoke("Title:Finally, the base iPhone feels completely Pro.""I’ve been using my iPhone 17 (256GB, Mist Blue) for a few months now, and I can confidently say this is the base-model iPhone Apple should have made years ago. The addition of the 120Hz ProMotion display is a game-changer—scrolling is buttery smooth, and the screen is absolutely gorgeous, especially when compared to older 60Hz models.The new A19 chip runs everything flawlessly, from heavy games to everyday multitasking, without breaking a sweat. I also appreciate that Apple made 256GB the base storage—it takes a lot of the pressure off when shooting 4K video. Speaking of cameras, the 48MP Ultra Wide and the upgraded 18MP front selfie sensor are fantastic; the photos are incredibly crisp, and the added flexibility is super noticeable during social events.Battery life has been solid as well. It comfortably gets me through a full day of typical use with about \(20\%\) to \(30\%\) to spare by midnight. If you’re upgrading from an iPhone 16 or older, this phone doesn't feel like a compromise at all. Highly recommend!")

print(result.Summary)
print(result)