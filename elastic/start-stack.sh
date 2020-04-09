#!/bin/bash
# Sets ENV vars for docker-compose

# Elasticsearch
export ES_NODE="elastic"
export ES_CLUSTER="es-traefik"
export ES_VERSION="7.6.1"
export KIBANA_DARK_MODE="true"

# frontend urls ex: traefik.CF_DOMAIN
export TRAEFIK_HOST="traefik"
export KIBANA_HOST="kibana"
export ELASTICSEARCH_HOST="elastic"
export ELASTICSEARCH_EXTERNAL="false"
export APM_HOST="apm"
export APM_EXTERNAL="false"

# htaccess - traefik + kibana frontend
export htaccess_user="<user>"
export htaccess_password="<password>"

# Webserver
export WEBSERVER_HOST="web"
export APM_SERVER="http://apm-server:8200"
export APM_SERVICE="webserver"

# Grafana
export GRAFANA_HOST="grafana"
export GRAFANA_EXTERNAL="true"

# Cloudflare
## TEST - NO CF Local 
export CF_DOMAIN="docker.local"
export CF_ACME="false"

## PROD - CF
#export CF_DOMAIN="<cloudflare domain>"
#export CF_ACME="true"
export CF_API_EMAIL="<cloudflare-email>"
export CF_API_KEY="<cloudflare-global-api-key>"
export CF_DYNAMIC="dynamic-traefik"
export CF_ZONE_ID="<cloudflare-domain-zone-id>"

# https://github.com/oznu/docker-cloudflare-ddns#creating-a-cloudflare-api-token
export CF_API_KEY_SCOPED="<cloudflare-scoped-api-key>"

# htpasswd generation
mkdir ./htaccess
htpasswd -b -c ./htaccess/.htpasswd ${htaccess_user} ${htaccess_password}

# RUN SECTION
sysctl -w vm.max_map_count=262144
echo "Visit https://${TRAEFIK_HOST}.${CF_DOMAIN} to watch startup as added"

## TEST - NO CF
docker-compose up --build --scale cf_dynamic_ip=0 --scale cf_init=0 -d

## PROD - CF
#docker-compose up --build -d
