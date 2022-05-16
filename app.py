import time
from flask import flask, request
import os
import base64
from jinja2 import Template

app = Flask(__name__)

TESTS_DIRECTORY = "tests"
CRONJOBS_DIRECTORY = "cronjobs"

SPLUNK_URL = oc.getenv('SPLUNK_URL')
SPLUNK_TOKEN = oc.getenv('SPLUNK_TOKEN')

@app.get('/tests')
def download_tests():
    tests = {}
    for filename in os.listdir(TESTS_DIRECTORY):
        file = os.path.join(TESTS_DIRECTORY, filename)
        file_content = open(file).read()
        templated_content = Template(file_content.render(SPLUNK_TOKEN=SPLUNK_TOKEN, SPLUNK_URL=SPLUNK_URL)
        tests[filename] = base64.b64encode(templated_content.encoded()).decode()
    return json.dumps(tests)

@app.get('/cronjobs')
def download_cronjobs():
    cronjobs = {}
    for filename in os.listdir(CRONJOBS_DIRECTORY):
        file = os.path.join(CRONJOBS_DIRECTORY, filename)
        cronjobs[filename] = base64.b64encode(open(file).read().encoded()).decode()
    return json.dumps(cronjobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
