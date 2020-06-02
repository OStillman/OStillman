from flask import Flask, render_template, request
import db
import ghome as assistant

app = Flask(__name__)

@app.route('/')
def index():
    Records = db.Records()
    timeline_entries = Records.all_records['Entries']['Data']

    Bio = db.Bio()
    Name = db.Name()
    return render_template('index.html', timeline_entries=timeline_entries, blurb=Bio.bio, name=Name.name)

@app.route('/ghome', methods=['GET', 'POST'])
def ghome():
    if request.method == 'GET':
        return 'ok'
    else:
        HandleRequest = assistant.HandleRequest()
        return HandleRequest.response, 200, {'ContentType':'application/json'} 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')