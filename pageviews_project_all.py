import argparse
import os
import pandas as pd


def aggregate_pagecounts(input_path, lang):
    data = []
    for file_name in os.listdir(input_path):
        date = file_name.split('-')[1]
        time = file_name.split('-')[2]

        ts = pd.Timestamp(date + 'T' + time)

        # second column is pageviews
        # no prefix for wikipedia
        # source: https://dumps.wikimedia.org/other/pagecounts-ez/projectcounts/readme.txt
        hourly_views = 0
        with open(input_path + file_name, 'r') as f:
            for line in f.readlines():

                # check if correct language, but avoid suffixed projects
                words = line.split(' ')
                if lang == words[0]:
                    hourly_views = int(words[2])

        data.append({'Timestamp': ts, 'Page views': hourly_views})

    # sort by timestamp
    data = pd.DataFrame(data).sort_values(by='Timestamp')
    return data


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get the overall hourly pageviews for a given wikipedia language project.')

    parser.add_argument('--lang', help='which language project to produce aggregates for')
    parser.add_argument('--input', help='path containing extracted pagecounts-ez dump')
    parser.add_argument('--output', help='path to place resulting csv file')
    args = parser.parse_args()

    df = aggregate_pagecounts(args.input, args.lang)

    df.to_csv(args.output)
