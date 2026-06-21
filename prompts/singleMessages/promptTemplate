from dotenv import load_dotenv

load_dotenv()



from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate , load_prompt

paper_input = input("Enter your paper name: ")

#model:

model =init_chat_model(model="mistral-small-2506", temperature=0.9)

#prompt template from json:

template = load_prompt("prompt.json")

prompt = template.invoke({
    'paper_input':paper_input
})

#response:

responce = model.invoke(prompt)
print(responce.content)
