from langchain_community.document_loaders import PyPDFLoader
Loader = PyPDFLoader("books/dl-curriculum.pdf")

data = Loader.load()
print(data[1].page_content)