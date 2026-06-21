from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#chat template

chat_template = ChatPromptTemplate([
    ('system','you are helpful customer support agent'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
])


#load chat history : load from database in chat_history variable
chat_history=[]

#create prompt

prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query':"where is my refund"
})

