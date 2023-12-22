import requests

# Retrieve Konfigurations of all Loadbalancer, Pools, HealthCheck and WAF
TENANT = domain
NAMESPACE = default
API_TOKEN = xxxxxxxxxxxxxxxxxxx

# XC Based Variables
PATH_HTTP_LB = "/api/config/namespaces/" + NAMESPACE + "/http_loadbalancers"
PATH_POOL = "/api/config/namespaces/" + NAMESPACE + "/origin_pools"
PATH_HEALTH = "/api/config/namespaces/" + NAMESPACE + "/healthchecks"
PATH_WAF = "/api/waf/namespaces/" + NAMESPACE + "/app_firewalls"



# Get Objects        
def get_objects(object_type):
  match object_type:
    case "http_loadbalancers":
      path=PATH_HTTP_LB
    case "origin_pools":
      path=PATH_POOL
    case "healthchecks":
      path=PATH_HEALTH
    case "waf":
      path=PATH_WAF


  url = "https://TENANT.console.ves.volterra.io/$path"
  headers = {'Authorization':"APIToken " + API_TOKEN, 'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
  r = requests.get(url, headers=headers)
  return r.json()
  
        
def get_all_LBs():
  lb_json = get_objects("http_loadbalancers")
  