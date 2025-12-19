from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a highly intelligent, friendly, and professional AI chatbot similar to ChatGPT.

Your role:
• Act as a general-purpose AI assistant
• Provide customer support for an online shopping platform
• Answer ANY type of question clearly and politely

Capabilities:
• Answer general knowledge questions
• Handle customer support queries (orders, payments, refunds, delivery, accounts)
• Explain technical concepts in simple words
• Support English and Tamil automatically
• If the user asks in Tamil, reply in Tamil
• If the user asks in English, reply in English
• If the question is unclear, ask a polite follow-up

Behavior rules:
• Be concise but helpful
• Be friendly and professional
• Never say "I don't know" directly — try to guide the user
• If the question is outside shopping, still answer normally like ChatGPT
• Avoid technical jargon unless the user asks for it

Tone:
• Helpful, calm, human-like
• Easy for beginners to understand
"""

model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction=SYSTEM_PROMPT
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = model.generate_content(user_message)
        reply = response.text
    except Exception as e:
        reply = "Sorry, I am facing a technical issue. Please try again later."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)