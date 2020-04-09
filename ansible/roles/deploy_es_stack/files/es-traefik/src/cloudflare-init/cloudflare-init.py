import os
import requests
import json

cf_domain = os.getenv("CF_DOMAIN")
cf_dynamic = os.getenv("CF_DYNAMIC")
cf_zone_id = os.getenv("CF_ZONE_ID")
cf_email = os.getenv("CF_API_EMAIL")
cf_api = os.getenv("CF_API_KEY")
cf_acme = os.getenv("CF_ACME")
web_url = os.getenv("WEBSERVER_HOST")
traefik_url = os.getenv("TRAEFIK_HOST")
kibana_url = os.getenv("KIBANA_HOST")
elasticsearch_url = os.getenv("ELASTICSEARCH_HOST")
elasticsearch_external = os.getenv("ELASTICSEARCH_EXTERNAL")
apm_url = os.getenv("APM_HOST")
apm_external = os.getenv("APM_EXTERNAL")
grafana_url = os.getenv("GRAFANA_HOST")
grafana_external = os.getenv("GRAFANA_EXTERNAL")


data = [web_url, kibana_url, traefik_url]


if elasticsearch_external == "true":
    data.append(elasticsearch_url)
if apm_external == "true":
    data.append(apm_url)
if grafana_external == "true":
    data.append(grafana_url)


if cf_acme == "true":
    url = "https://api.cloudflare.com/client/v4/zones/" + cf_zone_id + "/dns_records"
    headers = {
    'X-Auth-Email': cf_email,
    'X-Auth-Key': cf_api,
    'Content-Type': 'application/json'
    }

    for subdomain in data:
        record = {
            "type" : "CNAME",
            "name" : subdomain + "." + cf_domain,
            "content" : cf_dynamic + "." + cf_domain,
            "proxied": True
        }

        payload = json.dumps(record)
        print(payload + "\n")

        response = requests.request("POST", url, headers=headers, data = payload)
        print(response.text)
else:
    print("Cloudflare disabled")
