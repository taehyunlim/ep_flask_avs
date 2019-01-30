# ep_flask
This repo serves as a boilerplate for the [Flask web server](http://flask.pocoo.org/) with [EasyPost Python client library](https://github.com/EasyPost/easypost-python) pre-installed to be import-ready.


Installation
---------------
Install virtualenv in the root directory of this repo (`ep_flask`) and upgrade `pip` before installing dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


Setup env
------------
From the root, concatenate strings into env variables:
```
touch .flaskenv .env
echo FLASK_APP=ep_flask >> .flaskenv
echo FLASK_ENV=development >> .flaskenv
echo FLASK_DEBUG=1 >> .flaskenv
echo EP_API_KEY=your_easypost_api_key >> .env
```
Check if there are any typos:
```
cat .env .flaskenv 
```


Run 
------
```
flask run
```
Open in browser: http://localhost:5000/address