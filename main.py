import pickle
from flask import Flask, request, jsonify
from helper import clean_text

# load the model
with open('Models/mnb_model.pkl', 'rb')as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict/', methods=['POST', 'GET'])
def predict() -> str:

    try:
        response = request.get_json()
        if isinstance(response, list):
            return jsonify({text: model.predict([clean_text(text)])[0] for text in response})
        else:
            return jsonify("Make sure you're sending a sequence (list/tuple) of strings")
    except:
        return "Make sure you're sending the request with the Content-type: application/json header."

app.run(debug=True, port=8080) #run app on port 8080 in debug mode
