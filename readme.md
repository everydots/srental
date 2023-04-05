Follow steps below to build the project

1. Create a virtual environment and activate it by using python 3.10:

```shell
python3 -m venv venv
source venv/bin/activate
```

2. Run below command to install the project dependencies:

```shell
pip3 install -r requirements.txt
```

3. Run below command in your local to start a flask application (in production, can use `Gunicorn` or `Waitress`)
   1. By default, The app will use port `8080`. If port already been used, Can add parameter `--port 8081` to specify another port
   2. By default, it's under development mode, if you want to change, do modify `FLASK_DEBUG` to `false` inside of `.flaskenv`
```shell
flask run
```

4. Run below command to call restful endpoint of `/spaceship/optimize` if your app run successfully
```shell
curl -s -H "Content-Type: application/json" -X POST  
-d '[
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]'
"http://localhost:8080/spaceship/optimize"
```

