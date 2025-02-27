from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = machinetranslation.translate_english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = machinetranslation.translate_french_to_english(textToTranslate)
    return translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
