from langchain_community.document_loaders import TextLoader
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()




model =init_chat_model(model="mistral-small-2506", temperature=0.9)


prompt = PromptTemplate(
    template='write a summary for the the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('file.txt',encoding='utf-8')


docs = loader.load()



chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))



# print(type(docs))

# print(len(docs))

# print(docs[0])

# print(docs[0].page_content)

# print(docs[0].metadata)

