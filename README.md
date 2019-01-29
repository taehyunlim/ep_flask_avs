# EP-Flask
This repo serves as a boilerplate for the [Flask web server](http://flask.pocoo.org/) with [EasyPost Python client library](https://github.com/EasyPost/easypost-python) pre-installed to be import-ready.


Installation
---------------
Install virtualenv in the root directory of this repo (`ep-flask`) and upgrade `pip` before installing dependencies:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```


Setup env
------------
`cd` into `ep_flask` and concatenate strings into env variables:
```
$ cd ep_flask
$ touch .flaskenv .env
$ echo "FLASK_APP=app.py" >> .flaskenv
$ echo "FLASK_ENV=development" >> .flaskenv
$ echo "FLASK_DEBUG=1" >> .flaskenv
$ echo “EP_API_KEY=your_ep_api_key” >> .env
```
Check if there are any typos:
```
$ cat .env .flaskenv 
```


Run 
------
```
$ flask run
$ open http://localhost:5000/address
```
