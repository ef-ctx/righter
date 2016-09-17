import json
import argparse

import righter
from righter.competitor import ginger
from righter.competitor import language_tool
from righter.competitor import pyenchant
from righter.competitor import whitesmoke
from righter.log import logger


algorithms = {
    "ginger": ginger.check,
    "language-tool": language_tool.check,
    "righter": righter.check,
    "pyenchant": pyenchant.check_hunspell,
    "pyenchant-hunspell": pyenchant.check_hunspell,
    "pyenchant-aspell": pyenchant.check_aspell,
    "whitesmoke": whitesmoke.check,
    None: righter.check
}


class AlgorithmNotFound(Exception):
    pass


def apply_algorithm(algorithm, text):
    """
    Predict English mistakes using the algorithm of choice.
    """
    check = algorithms.get(algorithm)
    if not check:
        raise AlgorithmNotFound()
    return check(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', help='File with one json per line containing the key text', required=True)
    parser.add_argument('-o', '--file-output', help='Save analysis to output file', required=True)
    parser.add_argument('-a', '--algorithm', help='Name of the algorithm to use')
    args = parser.parse_args()

    check = algorithms.get(args.algorithm)
    if not check:
        raise AlgorithmNotFound()

    with open(args.input_file, 'r') as input_fp:
        with open(args.file_output, 'w') as output_fp:
            for line in input_fp:
                writing = json.loads(line.strip())
                try:
                    writing['changes'] = check(writing['text'])
                except ginger.SentenceTooBigError:
                    logger.error("Unable to process <%s> on ginger (Sentence too big)", writing['id'])
                else:
                    print(json.dumps(writing), file=output_fp)
