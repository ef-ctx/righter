import argparse
import json
import matplotlib.pyplot as plt
import numpy as np
import collections


def get_number_mistakes(writing, mistake_type):
    return len([c for c in writing["changes"] if c["symbol"] == mistake_type])


def get_number_words(writing):
    return len(writing['text'].split())


def read_writings(file_name):
    writings = []
    with open(file_name, 'r') as fp:
        for line in fp:
            writings.append(json.loads(line.strip()))
    return writings


def get_words_per_level(writings):
    words = collections.defaultdict(lambda: 0)
    for writing in writings:
        words[int(writing['level'])] += get_number_words(writing)
    return words


def get_mistakes_per_level(writings, mistake_type):
    mistakes = collections.defaultdict(lambda: 0)
    for writing in writings:
        mistakes[int(writing['level'])] += get_number_mistakes(writing, mistake_type)
    return mistakes


def plot(mistakes, words, mistake_type):
    xs = []
    for i in range(max(mistakes.keys())):
        xs.append(mistakes.get(i, 0) / float(words.get(i, 1)))
    plt.plot(xs, label=mistake_type, marker='.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', help='Parsed input file', required=True)
    parser.add_argument('-t', '--top', default=10, type=int)
    args = parser.parse_args()

    writings = read_writings(args.input_file)
    mistakes = {
        'AR': 0,
        'C': 0,
        'SP': 0,
        #'x>>y': 0,
        #'AG': 0,
        #'CO': 0,
        #'D': 0,
        #'EX': 0,
        #'HL': 0,
        #'I(x)': 0,
        #'MW': 0,
        #'NS': 0,
        #'NWS': 0,
        #'PH': 0,
        #'PL': 0,
        #'PO': 0,
        #'PR': 0,
        #'PS': 0,
        #'PU': 0,
        #'SI': 0,
        #'VT': 0,
        #'WC': 0,
        #'WO': 0,
    }
    words = get_words_per_level(writings)
    for mistake in mistakes:
        mistakes_per_level = get_mistakes_per_level(writings, mistake)
        mistakes[mistake] = sum(mistakes_per_level.values())
    mistakes = list(mistakes.items())
    mistakes.sort(key=lambda x: x[1], reverse=True)
    for mistake, _ in mistakes[:args.top]:
        mistakes_per_level = get_mistakes_per_level(writings, mistake)
        plot(mistakes_per_level, words, mistake)

    plt.ylabel("Mistakes / words")
    plt.xlabel("Level")
    plt.title("Level X Mistakes / words")
    plt.xticks(range(1, 16))
    plt.axis(xmin=1, xmax=15)
    plt.legend()
    plt.savefig('mistakes-level.png', dpi=200)
