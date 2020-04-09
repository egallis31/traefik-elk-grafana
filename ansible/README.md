# Ansible - Setup ELK Traefik + Docker Monitoring

* ONLY ABLE TO DEPLOY WITH CLOUDFLARE ENABLED
* NEED LATEST ANSIBLE - `sudo apt-add-repository --yes --update ppa:ansible/ansible && sudo apt-get install ansible`

## Deploy

* Edit the inventory file and replace all variables with `<>`
* All other values are defaults that can be edited
* Run `ansible-playbook -i ./inventory ./deploy-stack.yml`

## Stop

* Run `ansible-playbook -i ./inventory ./stop-stack.yml`

## Roles

### apt_upgrade_all

* ensures all packages are up to date

### install_docker

* installs docker and logs into private repo if enabled

#### Env Vars

* Edit values in `inventory`

| Name  | Description | Values |
|:-----:|:-----------:|:------:|
| DOCKER_PRIVATE_REPO | enables or disables private repo login | True, False |
| DOCKER_REPO | HTTPS URL for docker repo | `https://<docker repo address>` |
| DOCKER_REPO_USER | docker repo username | `<repo username>` |
| DOCKER_REPO_PASS | docker repo password | `<repo password>` |

### deploy_es_stack

* uses docker-compose to start stack

#### ENV Var Configuration

* Edit values in `inventory`

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

### stop_es_stack

* stops stack

## CF Zone API - DDNS

* Create Scoped API Key: <https://github.com/oznu/docker-cloudflare-ddns>
