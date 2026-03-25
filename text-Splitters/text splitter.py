from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loaders= PyPDFLoader("dl-curriculum.pdf")

docs = loaders.load()


splitter = CharacterTextSplitter(chunk_size=10,
                                 chunk_overlap=0,
                                 separator ="")

result = splitter.split_documents(docs)
print(result[5].page_content)