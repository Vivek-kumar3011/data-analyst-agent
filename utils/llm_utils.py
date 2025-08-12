"""
llm_utils.py
Utility functions for interacting with an LLM (e.g., OpenAI GPT models).
"""

import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str, model: str = "gpt-4o-mini", temperature: float = 0.0) -> str:
    """
    Send a prompt to the LLM and return its response.

    Args:
        prompt (str): The prompt/question to send to the model.
        model (str): The LLM model name.
        temperature (float): Controls creativity (0.0 = deterministic).

    Returns:
        str: Model's text response.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Error communicating with LLM: {e}")

def analyze_with_llm(instructions: str, data_preview: str) -> str:
    """
    Combine instructions and a data preview into a prompt for analysis.

    Args:
        instructions (str): Task description/questions for analysis.
        data_preview (str): A short preview of the dataset or content.

    Returns:
        str: LLM's analysis.
    """
    prompt = (
        f"Here are your instructions:\n{instructions}\n\n"
        f"Here is a preview of the data:\n{data_preview}\n\n"
        "Please analyze accordingly."
    )
    return ask_llm(prompt)
