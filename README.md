## Reference
https://www.youtube.com/watch?v=WFzRy8KVcrM&list=PLeGc_lalTbVH2ooMArbPwDi36SIO-U6Vi&index=1&t=1030s

## Dependencies

### Virtual Env

* install virtual env
```sh
pip3 install virtualenv
```

* create virtual env
```sh
python3 -m venv vir-env
```

* activate virtual env
```sh
source vir-env/bin/activate
```

### Flask

* install flask
```sh
pip3 install flask
```

* set running environment
```sh
export FLASK_ENV=development
```

* define flask app path
```sh
export FLASK_APP=src
```

* run flask application
```sh
flask run
```

* install **python-dotenv** to utilize `.flaskenv`
```sh
pip3 install python-dotenv
```