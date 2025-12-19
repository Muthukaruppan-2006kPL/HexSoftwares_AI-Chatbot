from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    msg = message.lower()

    # Greeting
    if any(word in msg for word in ["hi", "hello", "hey", "vanakkam", "வணக்கம்"]):
        return "Hello! 👋 How can I help you today? / வணக்கம்! நான் எப்படி உதவலாம்?"

    # Services
    elif any(word in msg for word in ["service", "services", "offer"]):
        return "We provide online shopping services including fast delivery, secure payments, and easy returns."

    # Pricing
    elif any(word in msg for word in ["price", "cost", "pricing"]):
        return "Our products are competitively priced with regular offers and discounts."

    # Order tracking
    elif any(word in msg for word in ["order", "track", "delivery", "status"]):
        return "You can track your order in the 'My Orders' section. Delivery usually takes 3–5 business days."

    # Payment issues
    elif any(word in msg for word in ["payment", "paid", "failed", "refund", "return"]):
        return "For payment or refund issues, please wait 3–5 business days or contact customer support."

    # Trust / why choose us
    elif any(word in msg for word in ["why", "choose", "trust", "secure"]):
        return "Our platform offers secure payments, fast delivery, easy returns, and 24/7 customer support."

    # Contact support
    elif any(word in msg for word in ["contact", "support", "help"]):
        return "You can contact our customer support at support@onlineshop.com or call 1800-123-456."

    # Thanks
    elif any(word in msg for word in ["thank", "thanks", "நன்றி"]):
        return "You're welcome 😊 Happy shopping!"

    # Bye
    elif any(word in msg for word in ["bye", "goodbye"]):
        return "Goodbye 👋 Have a great day!"

    # Default
    else:
        return (
            "I'm here to help with orders, payments, delivery, and support queries. "
            "Please ask a customer-related question."
        )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)