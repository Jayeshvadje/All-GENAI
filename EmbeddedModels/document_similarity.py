from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")

documents = ["sachin Tendulkar: I have seen God, he bats at number 4 for India.",
"Virat Kohli: Self-belief and hard work will always earn you success.",
"MS Dhoni: You don't win or lose the games because of the 11 you select. You win or lose with what those 11 do on the field.",
"Rohit Sharma: Nothing is easy in cricket. Maybe when you watch it on TV, it looks easy. But it is not. You have to use your brain and time the ball.",
"Sir Donald Bradman: I saw him on television and was struck by his technique, so I asked my wife to come in. I feel that this player is playing the same as I used to play."]


query = "tell me about dhoni"

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)


scores= cosine_similarity([query_embeddings],doc_embeddings) [0]
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("score = ",score)

