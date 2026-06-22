from langchain_text_splitters import CharacterTextSplitter

#load pdf:
from langchain_community.document_loaders import PyPDFLoader,PDFPlumberLoader

loader = PyPDFLoader('parth verma resume.pdf')

docs = loader.load()

text = docs[0].page_content

# split:

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
res = splitter.split_text(text)

print(res)

# or directly use split document function


res = splitter.split_documents(docs)

print(res)