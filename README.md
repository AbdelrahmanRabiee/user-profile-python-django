# User Profile App
 .. a class based view and formset ..

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need to install "virtualenv" so you can create a virtual environment for the project and "pip" so you can install python libraries

### Installing

open your terminal ..

```
$ mkdir wuzzuf-venv 
$ virtualenv -p python3 wuzzuf-venv 
$ source wuzzuf-venv/bin/activate
$ cd path/to/project/directory
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py makemigrations
$ python3 manage.py migrate


```
#### Dont forget to create superuser so you can log onto Django admin page 

## Project Description
This is a user profile app i used formset that help me to create a form with 3 models in one page and django better-forms "third party" i have implemented the user profile via two different ways 
1- django better-forms
2- formset 
first you will be redirect to sign up then to sign in then to profile update 

its all class based view 






