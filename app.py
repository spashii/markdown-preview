import os
import time
import argparse
import hashlib
from markdown2 import Markdown 


def loadArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        help='specify the path of markdown file')
    parser.add_argument('-r', '--refresh', type=int,
                        help='specify time interval in seconds to watch for file changes')
    args = parser.parse_args()
    if args.path == None or not os.path.exists(args.path):
        print('Bad path specified. Exiting.')
        exit()
    if args.refresh == None or args.refresh < 0:
        args.refresh = 1
        pass
    return args

def getMD5(path):
    content = open(path, 'rb').read()
    h = hashlib.md5()
    h.update(content)
    return h.hexdigest()

def generateHTML(path):
    content = open(path, 'r').read()
    # html = '<html><body>'+
    # html = markdown2.markdown(content) 
    markdowner = Markdown()
    html = markdowner.convert(content)
    content2 = open(f'{path}.html', 'w')
    content2.write(html)

if __name__ == '__main__':
    args = loadArgs()
    path = args.path
    refresh = args.refresh
    hash_before = getMD5(path)
    html = generateHTML(path)
    while(True):
        hash_test = getMD5(path)
        if hash_before != hash_test:
            print('file modified')
        hash_before = hash_test
        time.sleep(refresh)
        print('now')

