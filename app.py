from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Demo responses: update these details with the university's latest official information.
def chatbot_response(question):
    question = question.lower().strip()

    if any(word in question for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 Welcome to the Presidency University enquiry assistant. What would you like to know today?"
    elif any(word in question for word in ["course", "courses", "program", "degree"]):
        return "You can ask the university admissions team about available undergraduate and postgraduate programmes. Course names and eligibility can change, so please confirm the latest details through the official university website."
    elif any(word in question for word in ["fee", "fees", "payment", "cost", "scholarship"]):
        return "Fees depend on the programme and academic year. Please contact the university admissions office for the current fee structure, payment schedule and scholarship information."
    elif any(word in question for word in ["admission", "apply", "application", "join", "eligibility"]):
        return "For admission, check the programme eligibility, application dates and required documents on the official Presidency University admissions page. The admissions team can confirm the current process."
    elif any(word in question for word in ["time", "timing", "hours", "open"]):
        return "University office timings may vary during holidays and events. Please confirm the current timings with the university office before visiting."
    elif any(word in question for word in ["facility", "facilities", "library", "lab", "canteen", "sports", "hostel", "campus"]):
        return "For current information about campus facilities, library, laboratories, sports and accommodation, please contact the university or refer to its official website."
    elif any(word in question for word in ["where", "location", "address", "reach", "directions"]):
        return "Presidency University is located in Bengaluru, Karnataka, India. Please use the university's official website for the latest directions and visitor information."
    elif any(word in question for word in ["contact", "phone", "email", "number"]):
        return "For verified phone numbers and email addresses, please visit the Contact section of the official Presidency University website."
    elif any(word in question for word in ["thank", "thanks"]):
        return "You're welcome! 😊 Feel free to ask another question."
    elif any(word in question for word in ["bye", "goodbye"]):
        return "Goodbye! Wishing you success in your academic journey. 👋"
    else:
        return "I can help with general questions about courses, admissions, fees, campus facilities, location and contact information. For the latest official details, please check with the university."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({"reply": "Please type a question first."})
    return jsonify({"reply": chatbot_response(user_message)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
