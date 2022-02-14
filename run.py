from flask import Flask
app = Flask(__name__)

from datetime import datetime
import pytz


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    ##now  = datetime.now()
    ##return now.strftime("%H:%M:%S")
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    return datetime_NY.strftime("%H:%M:%S")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
