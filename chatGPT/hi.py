import requests

input_string = "Tell me about your self?"
response = requests.post("http://localhost:5000/prompt",
                         data={"input": input_string})
print(response.json())
