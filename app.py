from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    msg = message.lower()

    # Greeting
    if any(word in msg for word in ["hi", "hello", "vanakkam", "வணக்கம்"]):
        return "Hello! / வணக்கம்! How can I help you today?"

    # Services
    elif any(word in msg for word in ["service", "services", "சேவை", "சேவைகள்"]):
        return "We provide AI solutions and customer support services. / நாங்கள் AI மற்றும் customer support சேவைகள் வழங்குகிறோம்."

    # Price
    elif any(word in msg for word in ["price", "cost", "pricing", "விலை", "கட்டணம்"]):
        return "Our pricing starts from ₹999. / எங்கள் சேவை விலை ₹999 முதல் தொடங்குகிறது."

    # Payment issues
    elif any(word in msg for word in ["payment", "paid", "pay", "பணம்", "கட்டணம்", "payment issue"]):
        return "Please check your payment details or contact support. / தயவுசெய்து payment விவரங்களை சரிபார்க்கவும் அல்லது support-ஐ தொடர்பு கொள்ளவும்."

    # Contact support
    elif any(word in msg for word in ["contact", "support", "help", "தொடர்பு", "உதவி"]):
        return "You can contact customer support at support@example.com. / support@example.com-ல் எங்களை தொடர்பு கொள்ளலாம்."

    # Thanks
    elif any(word in msg for word in ["thank", "thanks", "நன்றி"]):
        return "You're welcome! 😊 / மகிழ்ச்சி!"

    # Bye
    elif any(word in msg for word in ["bye", "goodbye", "பை", "பிரியாவிடை"]):
        return "Goodbye! Have a great day 👋 / நல்ல நாளாக இருக்கட்டும்!"

    # Default
    else:
        return "Sorry, I didn’t understand that. Can you please rephrase? / மன்னிக்கவும், புரியவில்லை. தயவுசெய்து மீண்டும் கூறவும்."

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