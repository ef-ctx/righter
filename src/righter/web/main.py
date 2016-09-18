"""
How to run from root:
PYTHONPATH=`pwd`/src:$PYTHONPATH python -m righter.web.main
"""
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


ESSAY_C178718 = {
    "id": "C178718",
    "text": "\n            Dear James, How are you?  Some serious problems have been brought to my attention relating to your working styly and habits. This is a formal letter of warning to ask you to improve your work. let me outline the areas in which you need to improve your communicate with colleagues.You often doesn't think about teamwork and never update the databse. You must be more carful with time mannagement. You has been late for appointments before.You must be more tidy because this is your workplace. You must be more professional. I am looking forward that you will become better, otherwise you will out of here. Yours sincerely, Paul\n            ",
     "nationality": "cn",
     "changes": [
        {
            "selection": "James",
            "start": 18,
            "symbol": "C"
        },
        {
            "selection": "How",
            "start": 25,
            "symbol": "C"
        },
        {
            "selection": "let",
            "start": 206,
            "symbol": "C"
        },
        {
            "selection": "Paul",
            "start": 635,
            "symbol": "C"
        },
        {
            "selection": "styly",
            "start": 120,
            "symbol": "SP"
        },
        {
            "selection": "doesn",
            "start": 303,
            "symbol": "SP"
        },
        {
            "selection": "databse",
            "start": 353,
            "symbol": "SP"
        },
        {
            "selection": "carful",
            "start": 379,
            "symbol": "SP"
        },
        {
            "selection": "mannagement",
            "start": 396,
            "symbol": "SP"
        }
    ],
    "level": "7"
}


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
        body = dict(ESSAY_C178718)
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
    if essay_id != "C178718":
        response = jsonify({u"error": "Inexistent essay"})
        response.status_code = 400
    else:
        body = dict(ESSAY_C178718)
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
    if (request_body["id"] == "C178718") and (request_body["text"] == ESSAY_C178718["text"]):
        annotated = {item["start"] for item in ESSAY_C178718["changes"] if item.get("symbol") in types}
        predicted = {item["start"] for item in body["changes"]}
        body["analysis"] = {
            "precision": precision(annotated, predicted),
            "recall": recall(annotated, predicted)
        }
    response = jsonify(body)
    return response


if __name__ == "__main__":
    app.run()
