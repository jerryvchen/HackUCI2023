from flask import Flask, redirect
import datetime

x = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/data')

@app.route('/data')
def get_time():
    return {
        'Name': "jerry", 
        "age": "2000", 
        "Date": x, 
        "programming": "death"
    }


if __name__ == '__main__':
    app.run(debug=True)