import os
import argparse
import markdown2
import hashlib


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='specify the path of markdown file')
    args = parser.parse_args()
    return args

def getMD5(path):
    content = open(path, 'rb').read()
    h = hashlib.md5()
    h.update(content)
    return h.hexdigest()

if __name__ == '__main__':
    args = getArgs()
    path = args.path
    if(path == None or not os.path.exists(path)):
        print('Bad path specified. Exiting.')
        exit()

    hash_before = getMD5(path)
    while(True):
        hash_test = getMD5(path)
        if hash_before != hash_test:
            print('file modified')
        hash_before = hash_test

