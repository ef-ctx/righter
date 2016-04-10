import json
import websocket


cookie = "optimizelyEndUserId=oeu1459928410487r0.9973470086697489; _mhbkts=gdn; _gat=1; grauth=AABCAbFtEQyApg22JHd-rVzeQehX0nOd5Awy46c96sRt9UCm2BxttgZT4NZ7-7l548g9Ig; redirect_location=eyJ0b2tlbiI6IkFBQkNBYkZ0RVF5QXBnMjJKSGQtclZ6ZVFlaFgwbk9kNUF3eTQ2Yzk2c1J0OVVDbTJCeHR0Z1pUNE5aNy03bDU0OGc5SWciLCJsb2NhdGlvbiI6Imh0dHA6Ly93d3cuZ3JhbW1hcmx5LmNvbS9leHRlbnNpb24tc3VjY2VzcyJ9; funnelType=free; browser_info=CHROME:48:COMPUTER:SUPPORTED:FREEMIUM; optimizelySegments=%7B%22299712489%22%3A%22gc%22%2C%22300064087%22%3A%22false%22%2C%22300337320%22%3A%22search%22%2C%22753030770%22%3A%22none%22%2C%224659346861%22%3A%22true%22%2C%224734220892%22%3A%22true%22%2C%224666431804%22%3A%22true%22%2C%224724020596%22%3A%22true%22%7D; optimizelyReferrer=; experiment_groups=001_post_reg_control2|002_post_reg_show; optimizelyBuckets=%7B%225369272632%22%3A%225399830512%22%7D; _ga=GA1.2.2091691156.1459928435; gnar_containerId=DmIkk3XbUl0K; mp_mixpanel__c=2; __fngrprnt__=uUpUxuQHv7KV; mp_c10dd64c87f70ef5563a63c368797e8c_mixpanel=%7B%22distinct_id%22%3A%20%22153ea840982d0-0d8ba8847-3d700057-240000-153ea840983677%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.uk%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.uk%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Linux%22%2C%22%24browser%22%3A%20%22Chrome%22%2C%22%24browser_version%22%3A%2048%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.uk%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.uk%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpap%22%3A%20%5B%5D%7D"

headers = [
    "Host: capi.grammarly.com",
    "Origin: chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen",
    #"Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits",
    #"Sec-WebSocket-Key: s2PXpLhNq/0wOXCP3QK2hA==",
    #"Sec-WebSocket-Version:13",
    #"User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"
]


HELLO_MSG = {
    "token": None,
    "docid": "ce925f29-d809-15a7-4a63-ba8396c50b91",
    "client": "extension",
    "protocolVersion": "1.0",
    "clientVersion": "6.580.393",
    "extDomain": "outlook.office365.com",
    "action": "start","id":0
}

TEXT = "the book is on an tabel. and it came too europe last monday.\nJulia has lots of friend, she is happy yesterday."
TEXT_DECORATED = "+0:0:the book is on an tabel. and it came too europe last monday.\nJulia has lots of friend, she is happy yesterday.:0"
TEXT_MSG = {
    "ch": [
        TEXT_DECORATED
    ],
    "rev": 0,
    "action": "submit_ot",
    "id": 1
}


def process_message(original_msg):
    #print("RECEIVED:", original_msg)
    return json.loads(original_msg)

def connect():
    """
    Establish a websocket connection, return channel object.
    """
    connection = websocket.create_connection(
        "wss://capi.grammarly.com/freews",
        cookie=cookie,
        header=headers)
        #subprotocols=["wamp.2.json"],
        #timeout=settings.TIMEOUT)
    connection.send(json.dumps(HELLO_MSG))
    msg = connection.recv()
    msg = process_message(msg)
    assert msg["action"] == "start"
    return connection

def evaluate_text(text=TEXT):
    formatted_text = "+0:0:{}:0".format(text)
    TEXT_MSG["ch"] = [formatted_text]
    connection.send(json.dumps(TEXT_MSG))
    msg = connection.recv()
    msg = process_message(msg)
    assert msg["action"] == "submit_ot"
    text_id = msg["id"]
    analysis_list = []
    while not msg["action"] == "finished":
        msg = connection.recv()
        msg = process_message(msg)
        if msg["action"] == "alert":
            analysis = {
                "start": msg["begin"],
                "selection": msg["text"],
                "suggestions": msg["replacements"],
                "explanation": msg.get("explanation"),
                "originalSymbol": "{}.{}.{}".format(msg["group"], msg["category"], msg.get("point", ""))
            }
            original_symbol = analysis["originalSymbol"].lower()
            original_word = text[msg["begin"]:msg["end"]]
            replacement = ""
            if msg["replacements"]:
                replacement = msg["replacements"][0].lower()
            if replacement and original_word == replacement:
                analysis["symbol"] = "C"
            elif "spelling" in original_symbol:
                analysis["symbol"] = "SP"
            elif "AVsAn".lower() in original_symbol:
                analysis["symbol"] = "A"
            if analysis not in analysis_list:
                analysis_list.append(analysis)
    return analysis_list

connection = connect()
evaluation = evaluate_text()
print(evaluation)
print(len(evaluation))



# 1. LOCAL -> SERVER: HELLO_MSG
# 2. LOCAL -> SERVER: TEXT_MSG
# 3. SERVER -> LOCAL: START {"sid":16933119,"action":"start","id":0}
# 4. SERVER -> LOCAL: SUBMIT OT {"rev":0,"action":"submit_ot","id":1}
# 5. SERVER -> LOCAL:

{
    "point": "General",
    "transforms": [
        "\u003cspan class\u003d\u0027gr_grammar_del\u0027\u003etatiana\u003c/span\u003e\u003cspan class\u003d\u0027gr_grammar_ins\u0027\u003eTatiana\u003c/span\u003e",
        "\u003cspan class\u003d\u0027gr_grammar_del\u0027\u003etatiana\u003c/span\u003e\u003cspan class\u003d\u0027gr_grammar_ins\u0027\u003eTatyana\u003c/span\u003e",
        "\u003cspan class\u003d\u0027gr_grammar_del\u0027\u003etatiana\u003c/span\u003e\u003cspan class\u003d\u0027gr_grammar_ins\u0027\u003eTiana\u003c/span\u003e"
    ],
    "title": "Misspelled word: \u003ci\u003etatiana\u003c/i\u003e",
    "details": "",
    "explanation": "\u003cp\u003eThe word \u003cb\u003etatiana\u003c/b\u003e\u0026nbsp;is not in\u0026nbsp;our dictionary. You can add it\u0026nbsp;to\u0026nbsp;your personal dictionary to\u0026nbsp;prevent future alerts.\n",
    "examples": "\u003cp\u003echange spelling\n",
    "todo": "",
    "handbookLink": "",
    "sentence_no": 0,
    "free": True,
    "cardLayout": {
        "category": "Correctness",
        "group": "Spelling",
        "groupDescription": "Review the following words for misspellings"
    },
    "category": "Misspelled",
    "pid": 455929,
    "rid": 455929,
    "begin": 201,
    "end": 208,
    "text": "tatiana",
    "group": "Spelling",
    "rev": 0,
    "highlightBegin": 201,
    "highlightEnd": 208,
    "highlightText": "tatiana",
    "replacements": ["Tatiana","Tatyana","Tiana"],
    "extra_properties" : {
        "priority": "1"
    },
    "action":"alert",
    "id":17
}

{
    "point": "General",
    "transforms": [
        "\u003cspan class\u003d\u0027gr_grammar_del\u0027\u003eChueyr\u003c/span\u003e\u003cspan class\u003d\u0027gr_grammar_ins\u0027\u003eChuey\u003c/span\u003e",
        "\u003cspan class\u003d\u0027gr_grammar_del\u0027\u003eChueyr\u003c/span\u003e\u003cspan class\u003d\u0027gr_grammar_ins\u0027\u003eChur\u003c/span\u003e"
    ],
    "title": "Misspelled word: \u003ci\u003eChueyr\u003c/i\u003e",
    "details": "",
    "explanation": "\u003cp\u003eThe word \u003cb\u003eChueyr\u003c/b\u003e\u0026nbsp;is not in\u0026nbsp;our dictionary. You can add it\u0026nbsp;to\u0026nbsp;your personal dictionary to\u0026nbsp;prevent future alerts.\n","examples":"\u003cp\u003echange spelling\n",
    "todo": "",
    "handbookLink": "",
    "sentence_no": 0,
    "free": True,
    "cardLayout": {
        "category": "Correctness",
        "group": "Spelling",
        "groupDescription": "Review the following words for misspellings"
    },
    "category":"Misspelled",
    "pid": 893584,
    "rid": 455929,
    "begin": 13,
    "end":19,
    "text": "Chueyr",
    "group": "Spelling",
    "rev": 0,
    "highlightBegin": 13,
    "highlightEnd": 19,
    "highlightText": "Chueyr",
    "replacements": ["Chuey","Chur"],
    "extra_properties": {
        "priority": "1"
    },
    "action": "alert",
    "id": 18
}

{
    "rev": 0,
    "scores": {
        "Vocabulary": 87.87878787878788,
        "PassiveIndex": 100.0,
        "Conciseness": 100.0,
        "Correctness": 20.0,
        "Clarity": 55.4
    },
    "score": 20,
    "removed": [],
    "errors": 0,
    "interrupts": 0,
    "skipped": 0,
    "rejected": 0,
    "blocked": 0,
    "dialect": "undefined",
    "action": "finished"
}
