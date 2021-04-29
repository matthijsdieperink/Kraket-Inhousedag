from flask import Flask, request, redirect, render_template
import pandas as pd

# Setting up the Flask application
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
app = Flask(__name__)


# Read data using Pandas
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
cardata = pd.read_excel('./data/data.xlsx')
cardata = cardata.iloc[0:10, :]  # Get first 10 rows only for now
# Maybe highlight what the use for to_dict is here?
cardata = cardata.to_dict(orient='records')
_id = len(cardata)


# Homepage
@app.route('/')
def _():
    return render_template('home.html')


# Data page
@app.route('/data')
def _data():
    # Not sure what the extra inputs are doing, but also not sure whether we should go into so much detail
    return render_template('data.html', data=cardata, _id=_id)


# Detail page for one data object (a car), after clicking the id on the data page
# Maybe mention that the click functionality is defined in the html file, not here?
@ app.route('/data/<id>')
def _data_id(id):
    car = [c for c in cardata if c['ID'] == int(id)][0]
    return f"This is car #{car['ID']}. Be creative :-)"


# POST request to add new data
# To read more about POST requests: https://en.wikipedia.org/wiki/POST_(HTTP)
@ app.route('/add_new_data', methods=["POST"])
def _add_new_data():
    global _id
    _id += 1
    form = request.form.to_dict()  # The data from the page enters here
    form['ID'] = _id
    cardata.append(form)
    return redirect('/data')  # Refreshes the page?


# More Flask stuff, this runs the server on http://localhost:5000
# Maybe highlight that the debug=True allows you to makes and save changes that you will see right away
app.run(host='localhost', port=5000, debug=True)
