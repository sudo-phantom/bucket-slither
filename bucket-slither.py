from pkgutil import get_data
import requests
import json
import argparse
import os
import sys


parser = argparse.ArgumentParser(description='Public Bucket Discovery tool.', fromfile_prefix_chars='@')
parser._optionals.title = "OPTIONS"
parser.add_argument('-d', '--domain', type=str, help='Specify Target Domain to get bucket names')
parser.add_argument('-f', '--file', help='option to use file containing bucketnames')
parser.add_argument('-o','--output', default='output', help='optional ouput name to prepend to scan outputs.')
args = parser.parse_args()



class slither():
    '''class to query s3 buckets'''
    def __init__(self, data, file):
        self.data = data
        self.file = file


    def get_data():
        #check how we are getting bucket names
        if args.domain is not None:
            hosts = args.domain
            url1 = f"http://{hosts}.s3.amazonaws.com/"
            url2 = f"http://s3.amazonaws.com/{hosts}"
            r = requests.get(url1)
            r2= requests.get(url2)
            data = r.status_code
            r.close()
            data2 = r2.status_code
            r2.close()
            return f"{url1}: {data}\n {url2}: {data2}"
        elif  args.file is not None:
            host = args.file
            datas = []
            with open(f"{host}", "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip('\n')
                    print(line)
                    url1 = f"http://{line}.s3.amazonaws.com"
                    url2 = f"http://s3.amazonaws.com/{line}"
                    r = requests.get(url1)
                    r2 = requests.get(url2)
                    data = r.status_code
                    data2 = r2.status_code

                    results = {url1: data, url2: data2}

                    print(results)

        elif args.output is not None:
            slither.logging()
        else:
            print('Bucket name argument not set')
            os.error
            

        def logging():
            output = args.output
            file = output
            file.write(slither.get_data(), "w")
            #logging not working, creating issue

        

print(f"{slither.get_data()}")

if __name__ == '__main__':
    slither.get_data()
