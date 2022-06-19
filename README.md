## Reference
https://www.youtube.com/watch?v=WFzRy8KVcrM&list=PLeGc_lalTbVH2ooMArbPwDi36SIO-U6Vi&index=1&t=1030s

## Dependencies

### Pip Freeze & Pip Install

* pip freeze
```sh
pip3 freeze > requirements.txt
```

* install from `requirements.txt`
```sh
pip3 install -r requirements.txt
```


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

* install [python-dotenv](https://pypi.org/project/python-dotenv/) to utilize `.flaskenv`
```sh
pip3 install python-dotenv
```

* install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#installation) to setup database
```sh
pip3 install Flask-SQLAlchemy
```

### Other Dependencies

* install (validators)[https://validators.readthedocs.io/en/latest/] to validate email
```sh
pip3 install validators
```

## Config File

### `.flaskenv` file
* contain configuration of flask environment, flask app, & DB URI
* the idea is to bundle flask config, so everytime run flask in different terminal, do need to specify the config 1 by 1
* this `.flaskenv` is safe to push to version control

### `.env` file
* contain sensitive config
* better keep it in local, use .gitignore for this

## Generate `database.db`

* enter flask shell by type this in terminal:
```sh
flask shell
```

* import db
```sh
from src.database import db
```

* create db
```sh
db.create_all()
```