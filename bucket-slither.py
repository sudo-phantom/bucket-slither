from pkgutil import get_data
import requests
import json
import argparse
import os
import sys


parser = argparse.ArgumentParser(description='Public Bucket Discovery tool.', fromfile_prefix_chars='@')
parser._optionals.title = "OPTIONS"
parser.add_argument('-d', '--domain', type=str, help='Specify Target Domain to get bucket names')
parser.add_argument('-f', '--file', help='option to use file containing bucketnames', type=argparse.FileType())
parser.add_argument('-o','--output', default='output', help='optional ouput name to prepend to scan outputs.')
args = parser.parse_args()


if args.domain is not None:
    hosts = args.domain
elif  args.file is not None:
    hosts = args.file.read()
else:
    print('Bucket name argument not set')
    os.error

output = args.output

class slither():
    '''class to query s3 buckets'''
    def __init__(self, data):
        self.data = data

    def get_data():
        url = f"https://{hosts}.s3.amazonaws.com/"
        url2 = f"http://s3.amazonaws.com/{hosts}"
        urls = [url, url2]
        for x in urls:
            r = requests.get(x)
            data = r.status_code
        data_stats = urls
        return data,  data_stats

print(f"{slither.get_data()}")

if __name__ == '__main__':
    slither.get_data()
