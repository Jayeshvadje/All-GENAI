from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "Your long document text goes here...with all my help"

# Split text into chunks of 500 characters with 50 characters overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=2,
    length_function=len
)

chunks = text_splitter.create_documents([text])
print(chunks[1].page_content)