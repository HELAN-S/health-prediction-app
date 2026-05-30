from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_health_remark(
        glucose,
        haemoglobin,
        cholesterol):

    prompt = f"""
    You are a healthcare assistant.

    Analyze:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Give:
    1. Possible health risk
    2. Short explanation

    Keep response under 50 words.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content