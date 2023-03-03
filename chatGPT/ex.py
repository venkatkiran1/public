import openai
from flask import Flask, request, render_template

# Set up the OpenAI API credentials
openai.api_key = "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"

# Create a Flask app instance
app = Flask(__name__)

# Create the "/prompt" route with POST method
@app.route("/prompt", methods=["POST"])
def get_prompt_response():
    # Get the input string from the form data
    input_text = request.form["input_text"]

    # Set up the OpenAI parameters
    prompt = input_text
    model = "text-davinci-002"
    max_tokens = 1024
    temperature = 0.5

    # Call the OpenAI API to generate the response
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )

    # Get the generated response from the API response
    generated_text = response.choices[0].text

    # Render the index.html template with the generated response
    return render_template("index.html", response=generated_text)

# Create the index route with GET method
@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
