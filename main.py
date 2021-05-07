from flask import Flask, request, redirect, render_template
import pandas as pd

# Setting up the Flask application
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
app = Flask(__name__)


# Read data using Pandas, get the first 10 rows and convert the imported
# dataframe object to a python dictionary
# Pandas: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
# Dictionary: https://www.w3schools.com/python/python_dictionaries.asp
cardata = pd.read_excel('./data/data.xlsx')
cardata = cardata.iloc[0:10, :]
cardata = cardata.to_dict(orient='records')
_id = len(cardata)


# Homepage
# App.route defines the url in the browser. This route will become http://localhost:5000
@app.route('/')
def _():
    # The render template function is used to render a html page in the
    # browser for the specific route. In this case the file home.html is rendered
    # https://pythonbasics.org/flask-tutorial-templates/
    return render_template('home.html')


# Data page
@app.route('/data')
def _data():
    return render_template('data.html', data=cardata, _id=_id)


# Detail page for one data object (a car), after clicking the id
# on the data page. The click functionality of the page is defined in
# the data.html file
@ app.route('/data/<id>')
def _data_id(id):
    car = [c for c in cardata if c['ID'] == int(id)][0]
    return f"This is car #{car['ID']}. Be creative :-)"


# HTTP POST request to add new data item
# To read more about POST requests: https://en.wikipedia.org/wiki/POST_(HTTP)
@ app.route('/add_new_data', methods=["POST"])
def _add_new_data():
    global _id
    _id += 1
    # The data from the page enters the python code here
    form = request.form.to_dict()
    form['ID'] = _id
    cardata.append(form)
    # Redirect to the main data page
    return redirect('/data')


# More Flask stuff, this runs the server on http://localhost:5000.
# Debug=True allows you to see your changes immediately in the browser.
app.run(host='localhost', port=5000, debug=True)
