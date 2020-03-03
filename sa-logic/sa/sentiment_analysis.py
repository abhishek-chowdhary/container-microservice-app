from textblob import TextBlob
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity
    returnObject='{"sentence":"'+str(sentence)+'","polarity":"'+str(polarity)+'"}'
    return Response(returnObject, headers={'content-type': 'application/json'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
