from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-pro",
    system_instruction="""
You are an AI-powered customer support chatbot for an online shopping platform.
You can answer:
- Orders, payments, refunds, delivery
- Account & data security questions
- General questions politely
Answer in simple English.
If user writes in Tamil, reply in Tamil.
"""
)

# Rule-based replies
def predefined_answers(msg):
    msg = msg.lower()

    if any(w in msg for w in ["hi", "hello", "vanakkam", "வணக்கம்"]):
        return "Hello! / வணக்கம்! How can I help you today?"

    if "refund" in msg:
        return "Refunds are processed within 5–7 working days."

    if "payment" in msg:
        return "Please check your payment method or contact support."

    if "contact" in msg:
        return "You can contact support at support@example.com"

    if "bye" in msg:
        return "Thank you for visiting! 👋"

    return None  # Let AI handle

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    # First try rule-based
    reply = predefined_answers(user_message)

    # If no rule match → AI response
    if reply is None:
        try:
            response = model.generate_content(user_message)
            reply = response.text
        except:
            reply = "Sorry, I am facing a technical issue."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)