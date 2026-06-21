from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

chat_template = ChatPromptTemplate([
    ('system','you are a helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':"Dusra"})

print(prompt)

