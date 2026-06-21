from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

messages=[
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content="Tell me about Langchain")
]
 
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print (messages)


