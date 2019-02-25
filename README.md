# interview-auth
Authentication API

## Setup
1. `python3 -m venv venv-interview-auth`
1. `source venv-interview-auth/bin/activate`
1. `pip install --upgrade pip; pip install -r requirements.txt -r test_requirements.txt`
1. `FLASK_APP=server.py flask run`


## Sample requests
1. Create account: `curl localhost:5000/v3/accounts -X POST --header 'Content-type: application/json' --data '{"email": "gsinkin@earnup.com", "password": "Password1!"}'`
1. Login: `curl localhost:5000/v3/accounts/login -X POST --header 'Content-type: application/json' --data '{"email": "gsinkin@earnup.com", "password": "Password1!"}'`
2. Logout: `curl localhost:5000/v3/accounts/logout --header 'Content-type: application/json' --header 'X-API-Key: a19f0000-28cc-4288-949b-1024dde58629'`
