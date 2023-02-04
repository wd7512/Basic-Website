from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello'

@app.route("/timetable")
def mytimetable():
    return '<iframe src="https://calendar.google.com/calendar/embed?src=kcl7cbivblgokbsuo57i8e6k809882bp%40import.calendar.google.com&ctz=Europe%2FLondon" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
