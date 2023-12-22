## Basics
    https://docs.cloud.f5.com/docs/api
    
### Show all Loadbalancers
    curl -sX GET https://<<tenant>>.console.ves.volterra.io/api/config/namespaces/default/http_loadbalancers -H "Authorization: APIToken <<api_token>>"

### Show specific Loadbalancer
    curl -sX GET https://<<tenant>>.console.ves.volterra.io/api/config/namespaces/default/http_loadbalancers/<<lb_name>> -H "Authorization: APIToken <<api_token>>"

### create object
    List all objects:   curl -sX GET https://<<tenant>>.console.ves.volterra.io/<<path>> -H "Authorization: APIToken <<api_token>>"
    Create new objects: curl -X POST https://<<tenant>>.console.ves.volterra.io/<<path>> -H "Authorization: APIToken <<api_token>>" -H "Content-type:application/json" -d @<<jsonfile.json>>
    Override objects:   curl -X PUT  https://<<tenant>>.console.ves.volterra.io/<<path>>/<<name>> -H "Authorization: APIToken <<api_token>>" -H "Content-type:application/json" -d @<<jsonfile.json>>
    
    Paths:
        /api/config/namespaces/<<namespace>>/http_loadbalancers
        /api/waf/namespaces/<<namespace>>/app_firewalls
        /api/config/namespaces/<<namespace>>/origin_pools
        /api/config/namespaces/<<namespace>>/healthchecks

    BODY: {metadata:, spec:}

