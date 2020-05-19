# markdown-to-html 

auto regenerates html from markdown file if modification is detected

> most of github markdown syntax works

> check [example.md](example.md)

## setup and run

* install requirements

```
$ pip install -r requirements.txt
```

* run app.py

```
$ python app.py -p PATH-TO-MARKDOWN
```

## working

watches specified markdown file for modifications, if the file was modified, html is generated

## usage

`app.py [-h] -p PATH [-r REFRESH]`

arguments:

* `-h` - displays a help message
* `-p / --path PATH` - specify the path of markdown file 
* `-r / --refresh REFRESH` - specify time interval in seconds to watch for file changes 


