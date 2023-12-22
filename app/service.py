from typing import Literal

from transformers import pipeline


def get_text_generation(message: str, model: str = "gpt2") -> str:
    """generating text responses based on user messages using the gpt model"""

    text_generation = pipeline("text-generation", model=model)
    generated_text = text_generation(message, max_length=100)[0]
    gpt_answer = generated_text["generated_text"]

    return gpt_answer
