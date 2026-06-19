from dotenv import load_dotenv


load_dotenv()


from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

print("Chatbot is ready! Start chatting with the bot (type 'exit' to quit).")
chat_history = []

while True:
    prompt=input("YOU: ")
    chat_history.append(prompt) #append user prompt to chat history 
    if(prompt=="exit"):
        print("Exiting the chat. Goodbye!")
        break
    response=model.invoke(chat_history)
    chat_history.append(response.content) #append LLM response to chat history
    print("BOT: ",response.content)