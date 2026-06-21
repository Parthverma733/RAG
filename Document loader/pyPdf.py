from langchain_community.document_loaders import PyPDFLoader,PDFPlumberLoader

loader = PyPDFLoader('parth verma resume.pdf')

docs = loader.load()


print(docs[0].page_content)

print("\n table:\n")

tableLoader = PDFPlumberLoader('parth verma resume.pdf')
docs = tableLoader.load()
print(docs[0].page_content)
