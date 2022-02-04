
from pkgutil import get_data
import requests
import time
import json
import argparse
import os
import sys


parser = argparse.ArgumentParser(description='Public Bucket Discovery tool.', fromfile_prefix_chars='@')
parser._optionals.title = "OPTIONS"
parser.add_argument('-b', '--bucket', type=str, help='Specify a single Target bucketname.')
parser.add_argument('-d', '--directory', help ='list of directories to check for inside the Bucket')
parser.add_argument('-f', '--file', help='option to use file containing a list of bucketnames')
parser.add_argument('-o','--output', default='output', help='optional ouput name to prepend to scan outputs.')
args = parser.parse_args()



class slither():
    '''class to query s3 buckets'''
    def __init__(self, data, file, data2, url1, url2):
        self.data = data
        self.file = file
        self.data2 = data2
        self.url1 = url1
        self.url2 = url2


    def get_data():
        '''check how we are getting bucket names'''
        if args.bucket is not None: 
            hosts = args.bucket
            url1 = f"http://{hosts}.s3.amazonaws.com"
            url2 = f"http://s3.amazonaws.com/{hosts}"
            r = requests.get(url1)
            r2= requests.get(url2)
            data = r.status_code
            r.close()
            data2 = r2.status_code
            r2.close()
            datas = (url1, data, url2, data2)
            #print(datas)
            if args.directory is not None:
                slither.directory(url1, url2)
            return  url1, data,  url2, data2
        '''check file contents'''
        if args.file is not None:
            host = args.file
            datas = []
            with open(f"{host}", "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip('\n')
                    url1 = f"http://{line}.s3.amazonaws.com"
                    url2 = f"http://s3.amazonaws.com/{line}"
                    r = requests.get(url1)
                    time.sleep(1)
                    r2 = requests.get(url2)
                    data = r.status_code
                    data2 = r2.status_code
                    datas.append(f"{url1}: {data}, {url2}: {data2},")
                    #print(datas)
                if args.directory is not None:
                    slither.directory(url1, url2)
                r.close()
                r2.close()
                print(f"{url1} \t: {data},\n {url2} \t: {data2}\n")
        
                         
        
        
    def directory(url1, url2):       
        dir_list = args.directory
        dir_data = []
        with open(f"{dir_list}",'r') as d:
            d_lines = d.readlines()
            for d_line in d_lines:
                d_line.strip()
                print(d_line)
                url_1 = f"{url1}/{d_line}"
                url_2 = f"{url2}/{d_line}"
                d_r = requests.get(url_1)
                time.sleep(1)
                d_r2 = requests.get(url_2)
                d_data = d_r.status_code
                d_data2 = d_r2.status_code
                print(f"{url_1} \t: {d_data},\n {url_2} \t: {d_data2}\n")

            dir_data.append(f"{url_1}: {d_data} ,")
            dir_data.append(f"{url_2}: {d_data2},")

            d_r.close()
            d_r2.close()
            return(dir_data)

        '''elif args.output is not None:
            #slither.logging()
            print("output not availible in this verisn yet")
        else:
            print('Bucket name argument not set')
            os.error
            

        def logging():
            output = args.output
            file = output
            file.write(slither.get_data(), "w")
            #logging not working, creating issue
'''
        
#print(f"{slither.get_data()}")

if __name__ == '__main__':
    slither.get_data()

    
