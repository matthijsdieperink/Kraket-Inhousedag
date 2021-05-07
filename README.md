# Getting started

## Prerequisites
* Have Python version > 3.7.x installed (we have built this project while using Python 3.9.1, however everything > 3.7.x should most likely work);
* Have Visual Studio Code or any other Integraded Developer Environment (IDE) installed;

## Setting up a virtual environment
It's useful to work in a virtual environment due to how Python handles dependencies for projects. This will encapsulate your packages within this virual environment and will not mess up other projects.

We explain two ways for you to set up your virtual environment; using either PIP or Anaconda as a package manager. Using a configuration file the package manager will automatically install the required packages for this project and make sure they can play nicely together (taking care of any version constraints).

For this all to work you first have to create a local copy of this repository, for instance by using the `git clone` command, or by simply downloading a zip-file from github and unzipping it somewhere.

Now there are two options, from which you only need to choose one: either PIP+virtualenv or Anaconda.

### PIP + virtualenv
This option uses PIP as a package manager and the virtualenv package as an environment manager.

1. For this option to work you need the `PIP` package, which is used to install Python packages. Please make sure the `pip` command is available in your terminal.
2. Open a terminal and navigate to the repo folder by using the following command `$ cd path/to/repo` (omit `$` from your actual command).
3. Type in your terminal the following command(s) (note, the `$` shouldn't be in the command, it's just indicating a new line/command):
```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```
Note: If `pip install XYZ` does not work for Python 3, use `pip3 install XYZ`.

These commands will install the `virtualenv` package, create a new virtual environment with the right packages and activate it. 

To deactivate the virtual environment, type in your terminal:
```
$ deactivate
```

### Anaconda
This option uses Anaconda as a package and environment manager. The steps are as follows:

1. Install the Anaconda package manager onto your system, such that the `conda` command is available in your terminal.
2. Open a terminal and navigate to the repo folder by using the following command `$ cd path/to/repo` (again, omit `$` from your actual command).
3. From within the repo do `$ conda env create -f environment.yml`, which will create an Anaconda environment called `kraket_inhousedag` with the required packages.
4. Activate the environment by calling `$ conda activate kraket_inhousedag`.

You now are in a virtual environment that should contain all the packages necessary to run the application.

If you want to deactivate the environment, type in your terminal:
```
$ conda deactivate
```

## Installing more packages

***Your virtual environment should be activated when installing more packages!***

We have included the following packages for you: `Flask`, `numpy`, `pandas`, `matplotlib` and `sklearn`. If any other packages are needed, you can install them yourself. Please make sure that you are inside the virtual environment when installing new packages though!

## Run the applicaion
Type in your terminal the following command(s) (note, the `$` shouldn't be in the command, it's just indicating a new line/command):
```
$ python main.py
```
This should start up a Python server with everything ready to go. You can access the application in your browser via http://localhost:5000.

# Development
Good luck :-).