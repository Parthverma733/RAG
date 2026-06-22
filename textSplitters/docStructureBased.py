#recursive char text splitter:


from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

#load pdf:
# from langchain_community.document_loaders import PyPDFLoader,PDFPlumberLoader

# loader = PyPDFLoader('parth verma resume.pdf')

# docs = loader.load()

# text = docs[0].page_content

text = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create object
s1 = Student("Parth", 20)

# Call method
s1.display()"""

# split:

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=0
)
res = splitter.split_text(text)

print(res)

# or directly use split document function


# res = splitter.split_documents(docs)

# print(res)