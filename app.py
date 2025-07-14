from flask import Flask, render_template, request
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import pycountry

app = Flask(__name__)

# For consistent detection results
DetectorFactory.seed = 0

def get_language_name(lang_code):
    try:
        language = pycountry.languages.get(alpha_2=lang_code)
        if language:
            return language.name
        else:
            return "Unknown Language"
    except:
        return "Unknown Language"

@app.route("/", methods=["GET", "POST"])
def index():
    detected_language = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form["text_input"]
        if input_text.strip() == "":
            detected_language = "Please enter some text to detect the language."
        else:
            try:
                lang_code = detect(input_text)
                detected_language = get_language_name(lang_code)
            except LangDetectException:
                detected_language = "Could not detect language. Try a longer text."

    return render_template("index.html", language=detected_language, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
