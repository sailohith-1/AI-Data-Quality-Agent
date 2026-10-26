import os

from dotenv import load_dotenv
from google import genai

from search import retrieve_rule


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Create Gemini client
client = genai.Client(api_key=api_key)


# User question
question = "Can a purchase amount be negative?"


# Retrieve relevant rule
result = retrieve_rule(question)


if result is None:

    print("No relevant rule was found.")

else:

    rule = result["text"]

    print("\nRetrieved rule:")
    print(rule)


    # Create prompt for Gemini
    prompt = f"""
You are a data quality assistant.

Answer the user's question using the provided company data-quality rule.

Do not invent rules.
Do not use outside assumptions.
If the rule does not provide enough information, say so.

Company Rule:
{rule}

User Question:
{question}

Give a clear and concise answer.
"""


    # Ask Gemini
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )


    print("\nGemini Answer:")
    print(interaction.output_text)