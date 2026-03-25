from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """RecursiveCharacterTextSplitter is highly recommended for generic text. 
It splits text recursively based on a list of separators.
It tries to keep paragraphs together, then sentences, then words.
This ensures semantic coherence.

Example:
It uses ["\n\n", "\n", " ", ""] by default.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=10,
                                          chunk_overlap=0)

result = splitter.split_text(text)

print(result)