
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
            datas = (f"url1:{url1} respone:{data}, url2:{url2} Response:{data2}")
            if args.output is not None:
                slither.logging(datas, hosts)
            
            if args.directory is not None:
                slither.directory(url1, url2)
            print(datas)
            return  datas
        '''check file contents'''
        if args.file is not None:
            host = args.file
            datas = []
            with open(f"{host}", "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    url1 = f"http://{line}.s3.amazonaws.com"
                    url2 = f"http://s3.amazonaws.com/{line}"
                    r = requests.get(url1)
                    time.sleep(1)
                    r2 = requests.get(url2)
                    data = r.status_code
                    data2 = r2.status_code
                    r.close()
                    r2.close()
                    datas.append(f"url1{url1}: {data} url2:{url2}: response:{data2}")
      
                    if args.output is not None:
                        slither.logging(datas, line)
                    if args.directory is not None:
                        slither.directory(url1, url2)
                        
                        datas.append(f"{url1} : {data}, {url2} : {data2}")
        print (datas)
        return datas
                        
                
                         
        
        
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
                print(f"{url_1}: {d_data},\n {url_2}: {d_data2}\n")

                dir_data.append(f"url1:{url_1}: response:{d_data} ,")
                dir_data.append(f"url2:{url_2}: response:{d_data2},")
                if args.output is not None:
                    slither.logging(dir_data, d_line)

                d_r.close()
                d_r2.close()
                print(f"Directory DATA----\n{dir_data}\n----\n")

    def logging(logs, filename):
        if args.output is not None:
            output = args.output
            file = f"{output}.log"
            with open(file, 'a')as f:
                f.writelines(f" {str(filename)}, {str(logs)} \n")
                f.close
      
            
        #logging not working, creating issue

if __name__ == '__main__':
    slither.get_data()

    
