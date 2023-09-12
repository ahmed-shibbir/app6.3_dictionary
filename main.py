from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

text_file = pd.read_csv("dictionary.csv")
# stations = stations[["STAID","STANAME                                 "]]
# stations = stations.to_html()


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api/v1/<word>')
def dictionary(word):
    definition = word.upper()
    results = {'definition': definition, 'word': word}
    return results


if __name__ == '__main__':
    app.run(debug=True, port=5000)
