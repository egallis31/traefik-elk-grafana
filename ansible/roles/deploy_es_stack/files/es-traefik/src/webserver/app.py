#!/usr/bin/python3
import os
from flask import Flask, render_template, request, jsonify, redirect
from elasticapm.contrib.flask import ElasticAPM


# ENV VARS
apm_server_url = os.getenv("APM_SERVER")
apm_service_name = os.getenv("APM_SERVICE")
name = os.getenv("ES_CLUSTER")

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    # Set required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    'SERVICE_NAME': apm_service_name,

    # Use if APM Server requires a token
    'SECRET_TOKEN': '',

    # Set custom APM Server URL (default: http://localhost:8200)
    'SERVER_URL': apm_server_url,
}
apm = ElasticAPM(app)

@app.route("/")
def index_page():
    return render_template("index.html", name=name)

@app.route("/login", methods=["POST", "GET"])
def fake_login():
    return redirect("/")

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', threaded=True, debug=False, port=80)