"""
Script which makes calls to Grammarly, using websocket, and return the mistakes analysis
http://grammarly.com/
"""
import json
import ssl
import time
from datetime import datetime

import websocket

connection = None

cookie = "optimizelyEndUserId=oeu1459928410487r0.9973470086697489; _mhbkts=gdn; _gat=1; grauth=AABCAbFtEQyApg22JHd-rVzeQehX0nOd5Awy46c96sRt9UCm2BxttgZT4NZ7-7l548g9Ig; redirect_location=eyJ0b2tlbiI6IkFBQkNBYkZ0RVF5QXBnMjJKSGQtclZ6ZVFlaFgwbk9kNUF3eTQ2Yzk2c1J0OVVDbTJCeHR0Z1pUNE5aNy03bDU0OGc5SWciLCJsb2NhdGlvbiI6Imh0dHA6Ly93d3cuZ3JhbW1hcmx5LmNvbS9leHRlbnNpb24tc3VjY2VzcyJ9; funnelType=free; browser_info=CHROME:48:COMPUTER:SUPPORTED:FREEMIUM; optimizelySegments=%7B%22299712489%22%3A%22gc%22%2C%22300064087%22%3A%22false%22%2C%22300337320%22%3A%22search%22%2C%22753030770%22%3A%22none%22%2C%224659346861%22%3A%22true%22%2C%224734220892%22%3A%22true%22%2C%224666431804%22%3A%22true%22%2C%224724020596%22%3A%22true%22%7D; optimizelyReferrer=; experiment_groups=001_post_reg_control2|002_post_reg_show; optimizelyBuckets=%7B%225369272632%22%3A%225399830512%22%7D; _ga=GA1.2.2091691156.1459928435; gnar_containerId=DmIkk3XbUl0K; mp_mixpanel__c=2; __fngrprnt__=uUpUxuQHv7KV; mp_c10dd64c87f70ef5563a63c368797e8c_mixpanel=%7B%22distinct_id%22%3A%20%22153ea840982d0-0d8ba8847-3d700057-240000-153ea840983677%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.uk%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.uk%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Linux%22%2C%22%24browser%22%3A%20%22Chrome%22%2C%22%24browser_version%22%3A%2048%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.uk%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.uk%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpap%22%3A%20%5B%5D%7D"
#cookie = "optimizelyEndUserId=oeu1459928410487r0.9973470086697489; gProduct=Chrome-Freemium; _mhbkts=gdn; grauth=AABCBdiDM1QKQgeU-enVbnOQAopyeHsI5OCc_GZTToDnHhLr66ZvgKMro9TKqCUMSUjVhw; isGrammarlyUser=true; _free=true; optimizelySegments=%7B%22299712489%22%3A%22gc%22%2C%22300064087%22%3A%22false%22%2C%22300337320%22%3A%22search%22%2C%22753030770%22%3A%22brand_f1%22%2C%224659346861%22%3A%22true%22%2C%224734220892%22%3A%22true%22%2C%224666431804%22%3A%22true%22%2C%224724020596%22%3A%22true%22%7D; optimizelyReferrer=; optimizelyBuckets=%7B%225369272632%22%3A%225399830512%22%7D; _ga=GA1.2.2091691156.1459928435; gnar_containerId=DmIkk3XbUl0K; mp_c10dd64c87f70ef5563a63c368797e8c_mixpanel=%7B%22distinct_id%22%3A%20440873981%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.uk%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.uk%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpap%22%3A%20%5B%5D%2C%22utm_source%22%3A%20%22google%22%2C%22utm_medium%22%3A%20%22cpc%22%2C%22utm_campaign%22%3A%20%22brand_f1%22%2C%22utm_content%22%3A%20%2276996511046%22%2C%22utm_term%22%3A%20%22grammarly%22%7D; __fngrprnt__=4BIClOcibJ4r; f=004_referral_control"
headers = [
    "Host: capi.grammarly.com",
    "Origin: chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen",
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


def wait_message():
    """
    """
    try:
        msg = connection.recv()
    except websocket._exceptions.WebSocketConnectionClosedException as e:
        print(e)
        global connection
        connection = connect()
        msg = connection.recv()
    else:
        print(msg)
        return json.loads(msg)

def connect():
    """
    Establish a websocket connection, return channel object.
    """
    global connection
    connection = websocket.create_connection(
        "wss://capi.grammarly.com/freews",
        cookie=cookie,
        header=headers)
        #subprotocols=["wamp.2.json"],
        #timeout=settings.TIMEOUT)
    connection.send(json.dumps(HELLO_MSG))
    msg = wait_message()
    assert msg["action"] == "start"
    return connection

def evaluate_text(text=TEXT):
    """
    Given a text, return its analysis object.
    The analysis object contains a list of:
        {
            "start"  # initial position
            "selection"  # string of the word or expression with issue
            "suggestions"  # may be an empty list
            "explanation"  # optional
            "originalSymbol"  # how the mistake was categorized by Grammarly
            "symbol"  # (optional) EFCAM symbol representation of originalSymbol
        }
    """
    formatted_text = "+0:0:{}:0".format(text)
    TEXT_MSG["ch"] = [formatted_text]
    connection.send(json.dumps(TEXT_MSG))
    msg = wait_message()
    assert msg["action"] == "submit_ot"
    text_id = msg["id"]
    analysis_list = []
    while not msg["action"] == "finished":
        msg = wait_message()
        if msg["action"] == "alert":
            analysis = {
                "start": msg["begin"],
                "selection": msg["text"],
                "suggestions": msg["replacements"],
                "originalSymbol": "{}.{}.{}".format(msg["group"], msg["category"], msg.get("point", ""))
            }
            explanation = msg.get("explanation")
            if explanation:
                analysis["explanation"] = explanation
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



if __name__ == "__main__":
    #text = TEXT
    #print(text)
    #evaluation = evaluate_text(text)
    #print(evaluation)
    #print(len(evaluation))
    global connection
    connection = connect()

    with open("../../../data/299.txt") as in_fp:
        with open("../../../data/299-grammarly-p10.txt", "w") as out_fp:
            # 310: some problem
            # 605: another problem
            # 712: another problem
            # 3172: after it there was an
            # ssl.SSLError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:645)
            # 7692
            #min_i = 8127
            #min_i = 8130
            min_i = 8649
            i = 0
            for line in in_fp:
                if i >= min_i:
                    print("<<<<<<<<<<<<<<<<<<", i, ">>>>>>>>>>>>>>>>")
                    print(datetime.now().isoformat())
                    data = json.loads(line)
                    try:
                        data["changes"] = evaluate_text(data["text"])
                    except Exception as e:
                        print("EXCEPTION!!!! ", i)
                        print(e)
                    else:
                        out_fp.write("{}\n".format(json.dumps(data)))
                    try:
                        connection.close()
                    except websocket._exceptions.WebSocketConnectionClosedException:
                        pass
                    connection = False
                    while not connection:
                        try:
                            connection = connect()
                        except ssl.SSLError as e:
                            print(e)
                            time.sleep(2)
                i += 1
