from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction=(
        "You are a customer service support chatbot. "
        "Only answer customer-related queries like services, pricing, payments, refunds, support. "
        "Respond politely and professionally. Support English and Tamil."
    )
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    try:
        response = model.generate_content(
            f"You are a professional customer support chatbot. Answer clearly and politely.\nUser: {user_message}"
        )
        reply = response.text
    except Exception as e:
        reply = "Sorry, I am facing a technical issue. Please try again later."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)