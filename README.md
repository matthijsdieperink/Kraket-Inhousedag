# Getting started

## Prerequisites
* Have Python version > 3.7.x installed (we have built this project while using Python 3.9.1, however everything > 3.7.x should most likely work);
* Have Visual Studio Code or any other Integraded Developer Environment (IDE) installed;

## Setting up a virtual environment
Type in your terminal the following command(s) (note, the $ shouldn't be in the command, it's just indicating a new line/command):
```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

This will activate your virtual environment. It's useful to work in a virtual environment due to how Python handles dependencies for projects. This will encapsulate your dependencies within this virual environment and will not mess up other projects with dependencies.

To deactivate the virtual environment, type in your terminal:
```
$ deactivate
```

## Install dependencies
Type in your terminal the following command(s) (note, the $ shouldn't be in the command, it's just indicating a new line/command):
```
$ pip install -r requirements.txt
```
***Your virtual environment should be activated when installing these dependencies!***

We have included the following dependencies for you: `Flask`, `numpy`, `pandas`, `matplotlib` and `sklearn`. If any other dependencies are needed, you can install them.

## Run the applicaion
Type in your terminal the following command(s) (note, the $ shouldn't be in the command, it's just indicating a new line/command):
```
$ python main.py
```
This should start up a Python server with everything ready to go. You can access the application in your browser via http://localhost:5000.

# Development
Good luck :-).