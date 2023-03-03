from flask import Flask, request, jsonify,render_template
import openai

app = Flask(__name__)

openai.api_key = "INSERT_YOUR_OPENAI_API_KEY_HERE"

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/prompt', methods=["POST"])
def prompt():
    string = request.json['string']
    response = openai.Completion.create(
        engine="davinci",
        prompt=string,
        max_tokens=100,
        temperature=0.7,
        top_p=1,
        n=1,
    )
    return jsonify(response.choices[0].text)

if __name__ == '__main__':
    app.run()