from flask import Flask, request
from flask_cors import CORS, cross_origin
from feature_ext import get_features

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    if request.method == 'GET':
        return 'Server is running!'
    features = request.json
    more_features = get_features(features['url'])
    all_features = {}
    for key in features:
        all_features[key] = features[key]
    for key in more_features:
        all_features[key] = more_features[key]
    print(all_features)
    
 
if __name__ == '__main__':
    app.run()