PRESIDENCY UNIVERSITY - AI COLLEGE ENQUIRY PORTAL

PROJECT CONTENTS
- app.py                         Flask application and simple chatbot responses
- templates/index.html           Website structure and chat interaction
- static/style.css                Website design and responsive styling
- static/presidency-campus.png    Campus photograph supplied for this project
- static/presidency-logo.png      Presidency logo supplied for this project

HOW TO RUN IN VS CODE (WINDOWS)
1. Extract the ZIP file into a new folder.
2. Open Visual Studio Code.
3. Choose File > Open Folder and select Presidency-University-AI-Enquiry-Portal.
4. Open Terminal > New Terminal.
5. Run:  pip install flask
6. Run:  python app.py
7. Open this address in your browser: http://127.0.0.1:5000
8. To stop the server, click the terminal and press Ctrl + C.

IMPORTANT
- This is a student project demo using a simple keyword-based chatbot, not a trained generative AI model.
- The university image and logo are included as supplied by the user.
- Chatbot answers are general demo guidance. Verify and replace course, fee, admission,
  contact and other details with current official university information before presenting.
- Internet is only needed to load the Google Fonts. The website itself and chatbot run locally.

OPTIONAL INSTALL METHOD
You can also install the project dependency with:
    pip install -r requirements.txt


RENDER DEPLOYMENT SETTINGS
- Build command: pip install -r requirements.txt
- Start command: gunicorn app:app
- Runtime: Python 3
- Root directory: leave blank (the app.py file is in the repository root after uploading the folder contents).

This project is a demo. Verify all university information with official sources before public use.
