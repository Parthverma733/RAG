#recursive char text splitter:


from langchain_text_splitters import RecursiveCharacterTextSplitter

#load pdf:
# from langchain_community.document_loaders import PyPDFLoader,PDFPlumberLoader

# loader = PyPDFLoader('parth verma resume.pdf')

# docs = loader.load()

# text = docs[0].page_content

text = """Poetry is in my blood.

Like plasma, or white cells, it exists in my veins.

Bred of English professors and nurses,

It's clear which gene is dominant.

 

I picked up a pen, and set it to paper,

the words flowing like tears into tissues.

I find poetry in everything,

Even the way a person walks down the street."""

# split:

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)
res = splitter.split_text(text)

print(res)

# or directly use split document function


# res = splitter.split_documents(docs)

# print(res)