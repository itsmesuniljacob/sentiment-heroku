from flask import abort, Flask, jsonify, request
from flair.models import TextClassifier
from flair.data import Sentence
import csv

app = Flask(__name__)

classifier = TextClassifier.load('en-sentiment')

output =[]

@app.route('/api/v1/health')
def live():
    return 'I am alive'

@app.route('/api/v1/analyzeSentiment', methods=['POST'])
def analyzeSentiment():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    sentence = Sentence(message)
    classifier.predict(sentence)
    print('Sentence sentiment: ', sentence.labels)
    label = sentence.labels[0]
    response = {'result': label.value, 'polarity':label.score}
    return jsonify(response), 200

@app.route('/api/v1/sentiment', methods=['GET'])
def sentiment():
    with open('records.csv','r') as f:
        reader = csv.DictReader(f)
        for records in reader:
            sentence = Sentence(records['description'])
            classifier.predict(sentence)

    with open('records_with_sentiment.json','w')as outfile:
        json.dump(output,outfile,sort_keys=True, indent=4)

    # message = request.json['message']
    # sentence = Sentence(message)
    # classifier.predict(sentence)
    # print('Sentence sentiment: ', sentence.labels)
    # label = sentence.labels[0]
    # response = {'result': label.value, 'polarity':label.score}
    # return jsonify(response), 200

if __name__ == "__main__":
    app.run()
