from pathlib import Path
import ollama

PROMPT_PATH = Path("app/prompts/qa_prompt.txt")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    TEMPLATE = f.read()


def generate_answer(question: str, context: str):

    prompt = TEMPLATE.format(
        context=context,
        question=question
    )

    response = ollama.chat(
        model="llama3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]