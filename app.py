#!/usr/bin/env python
from selenium import webdriver

import os
import time
import argparse
import hashlib
import markdown
from jinja2 import Template
def loadArgs():
    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-p', '--path', required=True,
                        help='specify the path of markdown file')
    optional.add_argument('-r', '--refresh', type=int, default=1,
                        help='specify time interval in seconds to watch for file changes')
    parser._action_groups.append(optional)
    args = parser.parse_args()
    if not os.path.exists(args.path):
        print('Bad path specified. Exiting.')
        exit()
    return args

def getMD5(path):
    content = open(path, 'rb').read()
    h = hashlib.md5()
    h.update(content)
    return h.hexdigest()

def generateHTML(path):
    md_content = open(path, 'r').read()
    extensions=['extra', 'smarty', 'sane_lists', 'toc', 'pymdownx.tilde'
                ,'codehilite']
    html_content = markdown.markdown(md_content, extensions=extensions,
                                    output_format='html5')
    html_template = Template(open('index.html', 'r').read()) 
    html = html_template.render(path=path, content=html_content)
    filename = os.path.basename(path)
    (file, ext) = os.path.splitext(filename)
    html_path =  file + '.html'
    content2 = open(html_path, 'w')
    content2.write(html)
    content2.close()
    print(f'generated HTML at {html_path}')
   

if __name__ == '__main__':
    enpath=os.environ['PATH']
    loc=os.getcwd()
    if('geckodriver' not in enpath):
    	print('ha')
    	os.system('export PATH=$PATH:'+loc+'geckodriver')
    args = loadArgs()
    path = args.path
    print(f'watching file {path}')
    refresh = args.refresh
    hash_before = getMD5(path)
    html = generateHTML(path)
    driver = webdriver.Firefox()
    loc=os.getcwd()
    driver.get('file://'+loc+'/testing.html')


    while(True):
        hash_test = getMD5(path)
        if hash_before != hash_test:
            print('file modified')
            html = generateHTML(path)
            driver.refresh()
        hash_before = hash_test    



    time.sleep(refresh)
    driver.quit()


