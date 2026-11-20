from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Demo responses: update these details with the university's latest official information.
def chatbot_response(question):
    question = question.lower().strip()

    if any(word in question for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 Welcome to the Presidency University enquiry assistant. What would you like to know today?"
    elif any(word in question for word in ["course", "courses", "program", "degree"]):
        return "We offer BCA, BBA, B.Com ,B.Sc Computer Science and B.tech"
    elif any(word in question for word in ["fee", "fees", "payment", "cost", "scholarship"]):
        return "Our annual fees are: BCA - Rs. 45,000, BBA - Rs. 40,000, B.Com - Rs. 30,000 ,B.Sc - Rs. 50,000.and B.Tech-Rs 400000"
    elif any(word in question for word in ["admission", "apply", "application", "join", "eligibility"]):
        return "Visit our college office, collect the application form, submit your documents and complete the admission process."
    elif any(word in question for word in ["time", "timing", "hours", "open"]):
        return "University timings are Monday to Saturday, 8:50 AM to 4:15 PM."
    elif any(word in question for word in ["facility", "facilities", "library", "lab", "canteen", "sports", "hostel", "campus"]):
        return "For current information about campus facilities, library, laboratories, sports and accommodation"
    elif any(word in question for word in ["where", "location", "address", "reach", "directions"]):
        return "Presidency University Located in Rajankunte,Banglore,Karnataka India"
    elif any(word in question for word in ["contact", "phone", "email", "number"]):
        return "Contact us at 9876543210 or info@abccollege.example."
    elif any(word in question for word in ["thank", "thanks"]):
        return "You're welcome! 😊 Happy to Help you"
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
    app.run(debug=True)
