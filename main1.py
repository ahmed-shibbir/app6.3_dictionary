from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")  # it is a static file and is better kept
                                    # here instead of placing inside the function

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api/v1/<word>')
def dictionary(word):
    definition = df[df['word'] == word]['definition'].squeeze()
    results = {'definition': definition, 'word': word}
    return results


# @app.route('/api/v1/<word>')
# def dictionary(word):
#     definition = word.upper()
#     results = {'definition': definition, 'word': word}
#     return results


if __name__ == '__main__':
    app.run(debug=True, port=5001)
