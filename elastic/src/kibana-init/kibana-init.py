import os
import json
import requests

dark_mode = os.getenv("KIBANA_DARK_MODE", "false")

def change_dark_mode(dark_mode):
    print("Kibana Dark Mode: " + dark_mode)
    url = "http://kibana:5601/api/kibana/settings/theme:darkMode"

    data = {"value": dark_mode}
    payload = json.dumps(data)
    headers = {
    'kbn-xsrf': 'true',
    'Content-Type': 'application/json'
    }

    requests.request("POST", url, headers=headers, data = payload)
    return

change_dark_mode(dark_mode)
