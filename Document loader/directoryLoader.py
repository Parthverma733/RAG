#Helps to load multiple files at same time


from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)


#load everything at once
docs = loader.load() 

#load when needed
docs = loader.lazy_load()

