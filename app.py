#!/usr/bin/env python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import argparse
import hashlib
import markdown
from jinja2 import Template
mess="""
<script type="text/javascript">
window.onload = function() {
    if(!window.location.hash) {
        window.location = window.location + '#loaded';
        window.location.reload();
    }
}
</script>
"""

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
    html_path = file + '.html'
    content2 = open(html_path, 'w')
    content2.write(html)
    content2.close()
    # refresh=open(html_path,'a')
    # refresh.write(mess)
    # refresh.close()
    print(f'generated HTML at {html_path}')

if __name__ == '__main__':
    args = loadArgs()
    path = args.path
    print(f'watching file {path}')
    refresh = args.refresh
    hash_before = getMD5(path)
    html = generateHTML(path)
    driver = webdriver.Safari()
    driver.get('file:///Users/ridhambhagat/Documents/markdown-to-html/testing.html')
    while(True):
        hash_test = getMD5(path)
        if hash_before != hash_test:
            print('file modified')
            html = generateHTML(path)
            driver.refresh()
            


        hash_before = hash_test
        time.sleep(refresh)
    driver.quit()
        

