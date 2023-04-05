## Pre-requirements
Python 3.10 

## Follow below steps to verify the restful endpoint
1. Get the source code of the project
```shell
# Option1: Unzip the compressed file
tar -zxf srental-0.0.1.tar.gz -C srental

# Option2: Git clone from repo
git clone https://github.com/everydots/srental.git
```
2. Go into project and create a virtual environment and activate it by using python 3.10:

```shell
cd srental-0.0.1
python3 -m venv venv
source venv/bin/activate
```

2. Run below command to install the project dependencies:

```shell
pip3 install -r requirements.txt
```

3. Run below command in your local to start a flask application (in production, can use `Gunicorn` or `Waitress`)
   1. By default, this app will listen port `8080`. If port already been used, Can add parameter `--port 9090` to specify another port
   2. By default, this app using development mode. If you want to change, Can modify `FLASK_DEBUG` to `false` in file: `.flaskenv`
```shell
flask run
```

4. Run below command to call restful endpoint of `/spaceship/optimize` after your app run successfully
```shell
curl -s -H "Content-Type: application/json" -X POST  \
-d '[
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]' \
"http://localhost:8080/spaceship/optimize"
```

