from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

Loader = DirectoryLoader(
    path = "books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
data=Loader.lazy_load()
print(data[45].page_content)