# Retrieve Konfigurations of all Loadbalancer, Pools, HealthCheck and WAF
TENANT=domain
NAMESPACE=default
API_TOKEN=xxxxxxxxxxxxxxxxxxx

# XC Based Variables
PATH_HTTP_LB=/api/config/namespaces/$NAMESPACE/http_loadbalancers
PATH_POOL=/api/config/namespaces/$NAMESPACE/origin_pools
PATH_HEALTH=/api/config/namespaces/$NAMESPACE/healthchecks
PATH_WAF=/api/waf/namespaces/$NAMESPACE/app_firewalls
# Get Objects

        
get_objects () {
    case "$1" in
    "http_loadbalancers")
      path=$PATH_HTTP_LB
      ;;
    "origin_pools")
      path=$PATH_POOL
      ;;
    "healthchecks")
      path=$PATH_HEALTH
      ;;
    "waf")
      path=$PATH_WAF
      ;; 
    esac

    curl -sX GET https://$TENANT.console.ves.volterra.io/$path -H "Authorization: APIToken $API_TOKEN"
}        
        

get_all_LBs () {
    get_objects "http_loadbalancers"
    
}