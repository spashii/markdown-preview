import argparse
import markdown2


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='specify the path of markdown file')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = getArgs()
    if(args.path == None):
        print('No path specified. Exiting.')
        exit()
    print(args.path)
