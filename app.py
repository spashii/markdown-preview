import os
import argparse
import markdown2
import filecmp


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='specify the path of markdown file')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = getArgs()
    path = args.path
    if(path == None or not os.path.exists(path)):
        print('Bad path specified. Exiting.')
        exit()

    file_watch = open(path, 'r')
    while(True):
        print(f'watching {path}')
        file_watch_new = open(path, 'r')
        if(filecmp.cmp(file_watch, file_watch_new)):
            print('file has changed')
