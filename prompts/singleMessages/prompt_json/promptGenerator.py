from langchain_core.prompts import PromptTemplate


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

template.save("prompt.json")