from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.route('/')
def index():
    Records = db.Records()
    timeline_entries = Records.all_records['Entries']['Data']

    Bio = db.Bio()
    return render_template('index.html', timeline_entries=timeline_entries, blurb=Bio.bio)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')