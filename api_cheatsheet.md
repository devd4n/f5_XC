## Basics
    https://docs.cloud.f5.com/docs/api

### Show all Loadbalancers
    curl -sX GET https://sodexo.console.ves.volterra.io/api/config/namespaces/default/http_loadbalancers -H "Authorization: APIToken <<api_token>>"

### Show specific Loadbalancer
    curl -sX GET https://sodexo.console.ves.volterra.io/api/config/namespaces/default/http_loadbalancers/<<lb_name>> -H "Authorization: APIToken <<api_token>>"

    
