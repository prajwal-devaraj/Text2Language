# Text2Language 🌍  
**Instant Language Detection Web App**

---

## About

Text2Language is a lightweight Flask web application that detects the language of any text you input.  
It supports 100+ languages and displays the full language name using AI-powered detection.

---

## Features

- Detects text language from 100+ languages  
- Shows full language names (e.g., French, Spanish)  
- Simple, elegant web interface  
- Fast and runs locally without internet

---

## How to Run

1. Make sure you have Python 3.8+ installed.  
2. Install required packages:

```bash
pip install flask langdetect pycountry


📂 Project Structure
Text2Language/
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── style.css         # CSS styling
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

⚙️ Installation
1️⃣ Clone the Repository

git clone https://github.com/yourusername/Text2Language.git
cd Text2Language

2️⃣ Install Requirements
pip install -r requirements.txt

3️⃣ Run the App
python app.py

🌍 Usage
Open http://127.0.0.1:5000/ in your browser

Enter text in any language

Click Detect Language

See the detected language in full form

📦 Requirements
Python 3.8+

Flask

langdetect

pycountry

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome!
For major changes, please open an issue first to discuss.
