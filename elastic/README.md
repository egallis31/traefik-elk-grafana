# Traefik + Docker Monitoring Stack

* Comprised of ELK stack that auto discovers new docker containers
* Filebeat will read all stdout from containers
* Metricbeat will gather metrics from containers and host
* APM Server gathers transactions, spans, errors from web hosts

## Important

* MAKE SURE DOMAIN IS REGISTERED IN CLOUDFLARE IF USING `PROD`
* Use `TEST` if you would like to run locally
* Check `start-stack.sh` and comment the correct run commands

## ENV Var Configuration

* Edit values in `start-stack.sh`

| Name  | Description | Values |
|:-----:|:-----------:|:------:|
| TRAEFIK_HOST | traefik sub domain | traefik.CF_DOMAIN|
|htaccess_user | frontend auth for traefik + kibana + grafana | username |
|htaccess_password| frontend auth for traefik + kibana + grafana | password |
| CF_ACME | enables or disables CF acme | true, false |
| CF_DOMAIN | traefik frontend domain + cloudflare domain acme | example.com |
| CF_API_EMAIL | CF account email | cloudflare admin email |
| CF_API_KEY| CF master api key | CF api key |
| CF_DYNAMIC| CF dynamic address for cname records | subdomain |
| CF_ZONE_ID| CF Domain id  | string found in overview tab |
| CF_API_KEY_SCOPED | cf dynamic ddns update key | <https://dash.cloudflare.com/profile/api-tokens> |
| ELASTICSEARCH_HOST | elasticsearch sub domain  | es.CF_DOMAIN |
| ELASTICSEARCH_EXTERNAL | sets elasticsearch to also route through traefik | true, false |
| ES_NODE | elasticsearch node name | name |
| ES_CLUSTER | elasticsearch cluster name | cluster name |
| ES_VERSION | elasticsearch cluster version | 7.6.1 |
| KIBANA_HOST | kibana sub domain | kibana.CF_DOMAIN|
| KIBANA_DARK_MODE | kibana enable dark mode | true or false |
| GRAFANA_HOST| grafana sub domain | grafana.CF_DOMAIN |
| GRAFANA_EXTERNAL | grafana route through traefik | true, false |
| APM_HOST | apm server sub domain | apm.CF_DOMAIN |
| APM_EXTERNAL | apm route through traefik | true, false |
| APM_SERVER | default apm server address |`http://apm-server:8200`|
| APM_SERVICE| apm service name for website | `webserver` |
| WEBSERVER_HOST | webserver sub domain | web.CF_DOMAIN |

## Health Checks

* neccessary to ensure elastic beats set up and index properly upon first up
* same to ensure traefik will request the proper certificates

## CF Zone API - DDNS (PROD ONLY)

* Create Scoped API Key: <https://github.com/oznu/docker-cloudflare-ddns>
