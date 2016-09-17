"""
Script which makes calls to Grammarly, using websocket, and return the mistakes analysis
http://grammarly.com/
"""
import argparse
import json
import ssl
import sys
import time
import traceback
from datetime import datetime

import websocket


connection = None

COOKIE = "optimizelyEndUserId=oeu1459928410487r0.9973470086697489; intellimizeEUID=b1cc1e5a1c.1473594831; grauth=AABCnwG0eVNAm5eqZ08c7eETkEVOw7aB68scg459gsAr4Sx-WDneHzxrcUpilnDPMIdV7w; optimizely_current=; optimizely_reported=; redirect_location=eyJ0b2tlbiI6IkFBQkNud0cwZVZOQW01ZXFaMDhjN2VFVGtFVk93N2FCNjhzY2c0NTlnc0FyNFN4LVdEbmVIenhyY1VwaWxuRFBNSWRWN3ciLCJsb2NhdGlvbiI6Imh0dHBzOi8vYXBwLmdyYW1tYXJseS5jb20vIn0=; funnelType=free; browser_info=CHROME:48:COMPUTER:SUPPORTED:FREEMIUM; _ga=GA1.2.2091691156.1459928435; optimizelySegments=%7B%22299712489%22%3A%22gc%22%2C%22300064087%22%3A%22false%22%2C%22300337320%22%3A%22referral%22%2C%22753030770%22%3A%22brand_f1%22%2C%224659346861%22%3A%22true%22%2C%224734220892%22%3A%22true%22%2C%224666431804%22%3A%22true%22%2C%224724020596%22%3A%22true%22%2C%225810602057%22%3A%22true%22%7D; optimizelyReferrer=; optimizelyBuckets=%7B%225369272632%22%3A%225399830512%22%7D; isGrammarlyUser=true; _free=true; gnar_containerId=DmIkk3XbUl0K; mp_c10dd64c87f70ef5563a63c368797e8c_mixpanel=%7B%22distinct_id%22%3A%20440873981%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.uk%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.uk%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpap%22%3A%20%5B%5D%2C%22utm_source%22%3A%20%22google%22%2C%22utm_medium%22%3A%20%22cpc%22%2C%22utm_campaign%22%3A%20%22brand_f1%22%2C%22utm_content%22%3A%20%2276996511046%22%2C%22utm_term%22%3A%20%22grammarly%22%7D; mp_mixpanel__c=0; __fngrprnt__=4BIClOcibJ4r; experiment_groups=referral_icon_gift_text"
HOST = "capi.grammarly.com"
ORIGIN = "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen"
SEC_WEBSOCKET_KEY = "FeMpG84JjbpSHCJpRe0rcw=="

websocket._handshake._create_sec_websocket_key = lambda: SEC_WEBSOCKET_KEY


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
    Wait message from websocket, return the message in the format of a dict.
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
    print("trying to establish the websocket connection...")
    global connection
    try:
        connection = websocket.create_connection(
            "wss://capi.grammarly.com/freews",
            cookie=COOKIE,
            host=HOST,
            origin=ORIGIN)
    except TimeoutError:
        print("connection time out: retrying in 3s...")
        time.sleep(3)
        return connect()
    else:
        connection.send(json.dumps(HELLO_MSG))
        msg = wait_message()
        if msg["action"] != "start":
            print("connection with problems: retrying in 1s...")
            time.sleep(1)
            return connect()
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
    print(TEXT_MSG)
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
            if replacement and original_word.lower() == replacement:
                analysis["symbol"] = "C"
            elif "spelling" in original_symbol:
                analysis["symbol"] = "SP"
            elif "AVsAn".lower() in original_symbol:
                analysis["symbol"] = "AR"
            if analysis not in analysis_list:
                analysis_list.append(analysis)
    return analysis_list


def check(text):
    global connection
    while not connection:
        try:
            connection = connect()
        except ssl.SSLError as e:
            print(e)
            time.sleep(2)

    try:
        changes = evaluate_text(text)
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        print("EXCEPTION!!!! ", i)
        print(e)

    
    return sorted(changes, key=lambda i: i["start"])


def main(input_filename, output_filename):
    global connection
    connection = connect()
    with open(input_filename) as in_fp:
        with open(output_filename, "w") as out_fp:
            min_i = 0
            i = 0
            for line in in_fp:
                if i >= min_i:
                    print("<<<<<<<<<<<<<<<<<<", i, ">>>>>>>>>>>>>>>>")
                    print(datetime.now().isoformat())
                    data = json.loads(line)
                    try:
                        data["changes"] = evaluate_text(data["text"])
                    except Exception as e:
                        traceback.print_exc(file=sys.stdout)
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


connection = connect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run grammarly in a dataset input file')
    parser.add_argument('--input', '-i', help='Dataset input file (read-only)', required=True)
    parser.add_argument('--output', '-o', help='Dataset output file (write)', required=True)
    args = parser.parse_args()
    main(args.input, args.output)
