import getAbstractFromWeb as abstract
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        URL = request.form["url"]
        print(URL)
        if request.form.get('url') is not None:
            fetching_html_text = abstract.myrequests(URL)

            text = abstract.html2text(fetching_html_text)

            abstract_content = abstract.abstract_content(text)
            return render_template("index.html", abstract=abstract_content)
        else: return render_template("index.html", abstract="Input FAILed")
    return render_template("index.html", abstract="NO INPUT")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)