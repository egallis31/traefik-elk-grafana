# Cloud Based Host/Application Monitoring Stack

* Comprised of ELK stack that auto discovers new docker containers
* Filebeat will read all stdout from containers
* Metricbeat will gather metrics from containers and host

## Ansible

* Setup for host to install stack
* Check `ansible/README.md` for deployment instructions

## Elastic

* Check `elastic/README.md` for deployment instructions
* Run `start-stack.sh` after editing variables

## Stack

* Elasticsearch
  * Metrics + Logs Datasource
* Kibana
  * Elasticsearch management + dashboards
* Kibana-init
  * Kibana init container - who doesn't love dark mode
* Filebeat
  * gathers container logs through autodiscovery docker hints ships to elastic
* Metricbeat
  * gathers container and service metrics through autodiscovery docker hints ships to elastic
* Traefik
  * Auto discovery load balancer for docker, ships access logs and metrics to elastic
* APM-Server
  * gathers application metrics and ships to elastic
* Sample Webserver - with apm integration
  * simple flask webserver to gather APM metrics
* Cloudflare-init
  * creates CNAME records for all services defined and maps to A record for dynamic
* Cloudflare dynamic ddns
  * uses gloabl ip address to create A record for DNS entries
* Grafana - for extra datasources + alerting
  * auto provisioning for datasources + dashboards

## Elasticsearch

* If planning to collect data from other local hosts, include port 9200 in the compose file.
* If planning to have externally accessible, please follow Elastic's guide to enable Security

## Kibana

* Access and search dashboards for `Traefik`
* View logs/metrics real time under menu bars on left

## Grafana

* Easily customizable dashboard system that support numerous datasources
* Handles alerting and allows for more customizable dashboards

## Traefik

* frontends are currently protected with basic-auth
* TODO: implementing `authelia/authelia` with local users/LDAP (few weeks after sem.)

## Sample Webserver

* Visit the frontend address in traefik for APM data to be populated

## Cloudflare

* This stack works with Cloudflare TLS settings for Full (strict)
* Requests are all sent over TLS 1.3
* All DNS records point to Cloudflare, meaning origin IP is not exposed
* Check `elastic/README.md` for all Cloudflare API values needed
