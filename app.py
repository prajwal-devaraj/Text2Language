from flask import Flask, render_template, request
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import pycountry

app = Flask(__name__)

DetectorFactory.seed = 0  # To make detection consistent

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
    language = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form["text_input"]
        try:
            lang_code = detect(input_text)
            language = get_language_name(lang_code)
        except LangDetectException:
            language = "Could not detect language (input too short or ambiguous)."

    return render_template("index.html", language=language, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
