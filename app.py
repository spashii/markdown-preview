import os
import time
import argparse
import hashlib
import markdown
from jinja2 import Template


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
    html_content = markdown.markdown(content, extensions=['extra', 'smarty'], output_format='html5')
    html_template = Template(open('index.html', 'r').read()) 
    html = html_template.render(path=path, content=html_content)
    filename = os.path.basename(path)
    (file, ext) = os.path.splitext(filename)
    html_path = file + '.html'
    content2 = open(html_path, 'w')
    content2.write(html)
    print(f'generated HTML at {html_path}')

if __name__ == '__main__':
    args = loadArgs()
    path = args.path
    print(f'watching file {path}')
    refresh = args.refresh
    hash_before = getMD5(path)
    html = generateHTML(path)
    while(True):
        hash_test = getMD5(path)
        if hash_before != hash_test:
            print('file modified')
            html = generateHTML(path)
        hash_before = hash_test
        time.sleep(refresh)
        

