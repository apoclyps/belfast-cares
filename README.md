# belfast-cares getting-setup-guide

A Django app utilizing postgres & bootstrap, which can easily be deployed to Heroku.

This application was initially created using the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Local Setup

### Setup Python IDE
Download the pycharm ide - community edition from
```sh 
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC
```

### Ensure you have python and pip installed
```sh
wget https://bootstrap.pypa.io/get-pip.py
pip install -upgrade pip
pip install virtualenv
```

### Checkout source code using Git
```sh
git clone https://github.com/apoclyps/belfast-cares.git
```

### Mac Setup - Installing services
```sh
brew install heroku
brew install postgresql
brew services start postgresql
```

### Linux Distros - Installing Services
```sh
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
sudo apt-get install sudo apt-get install python-dev libpq-dev python-dev
```

### Create Virtual Enviroment & Install Deps
```sh
virtualenv hackathon-env
source hackathon-env/bin/activate

pip install -r requirements.txt
```

### Create local database
```sh
createdb belfastcares
psql belfastcares
CREATE USER user WITH PASSWORD 'password';
```

### Add to ~/.bash_profile
```sh
export DATABASE_URL='postgres:/user:password@localhost:5431/belfastcares'
```

### Run local server
```sh
python manage.py createsuperuser
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
