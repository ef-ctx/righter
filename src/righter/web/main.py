"""
How to run from root:
PYTHONPATH=`pwd`/src:$PYTHONPATH python -m righter.web.main
"""
import json
import random

from flask import Flask, jsonify, request, send_from_directory

from righter.analyse import precision, recall
from righter.predict import apply_algorithm


app = Flask(__name__)
app.debug = True


SUPPORTED_ALGORITHMS = [
    "pyenchant",
    "grammarly",
    "ginger",
    "languagetool",
    "righter",
    "whitesmoke"
]


with open("data/dataset-2-1000-lines.json") as fp:
    writings = json.load(fp)
    writings_ids = list(writings.keys())


@app.route('/')
def retrieve_index():
    """
    Return index.html
    """
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/healthcheck")
def healthcheck():
    """
    Return "Atchoo!" if service is running.
    """
    return "Atchoo!"


@app.route("/essays")
def essays_collection():
    """
    Given the query string: `random=1`, return a random essay, using the format:
    {
        "text": <string>
        "id": <string>
    }
    """
    is_random = int(request.args.get('random'))
    if not is_random:
        response = jsonify({u"error": "Requires query string random=1"})
        response.status_code = 500
    else:
        random_id = random.choice(writings_ids)
        body = dict(writings[random_id])
        body.pop("changes")
        body.pop("level")
        body.pop("nationality")
        response = jsonify(body)
    return response


@app.route("/essays/<essay_id>")
def essay_instance(essay_id):
    """
    Given an id of an essay, return the essay body, if it exists
    {
        "id": <string>,
        "text": <string>
    }
    """
    if essay_id not in writings_ids:
        response = jsonify({u"error": "Inexistent essay"})
        response.status_code = 400
    else:
        body = dict(writings[essay_id])
        body.pop("changes")
        body.pop("level")
        body.pop("nationality")
        response = jsonify(body)
    return response


@app.route('/predict', methods=['POST'])
def predict():
    """
    Given a dictionary containing:
    {
        "id": <string>
        "text": <string>,
        "algorithm": <string> one of the items in SUPPORTED_ALGORITHMS,
        "types": [] # list of strings containing types to be analysed. Default: 
    }
    Apply the algorithm to identify English mistakes and return:
    {
        "changes": [] # list with the changes
        "analysis" { # optional, only if it was previously manually anotated  
            "precision": <float>
            "recall": <float>
       }
    }
    """
    request_body = request.get_json()
    ignore_type = request_body.get("ignoreType", False)
    types = request_body.get("types") or ["AR", "C", "SP"]
    changes = apply_algorithm(request_body["algorithm"], request_body["text"])
    body = {
        "changes": [i for i in changes if ignore_type or i.get("symbol") in types]
    }
    desired_id = request_body["id"]
    if (desired_id in writings_ids) and (request_body["text"] == writings[desired_id]["text"]):
        annotated = {item["start"] for item in writings[desired_id]["changes"] if item.get("symbol") in types}
        predicted = {item["start"] for item in body["changes"]}
        body["analysis"] = {
            "precision": precision(annotated, predicted),
            "recall": recall(annotated, predicted)
        }
    response = jsonify(body)
    return response


if __name__ == "__main__":
    app.run()
