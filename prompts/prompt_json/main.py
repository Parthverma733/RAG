from dotenv import load_dotenv

load_dotenv()



from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

paper_input = input("Enter your paper name: ")

#model:

model =init_chat_model(model="mistral-small-2506", temperature=0.9)

#prompt template:

template = PromptTemplate(
    template="""
You are a research assistant.

Analyze the following research paper and provide:

1. Title
2. Research Problem
3. Methodology
4. Dataset Used
5. Key Findings
6. Limitations
7. Future Work
8. Simple Explanation for Beginners

Research Paper:
{paper_input}

Response:""",
    input_variables=['paper_input']
)

prompt = template.invoke({
    'paper_input':paper_input
})

#response:

responce = model.invoke(prompt)
print(responce.content)
