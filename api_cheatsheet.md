## Basics
    https://docs.cloud.f5.com/docs/api

### Show all Loadbalancers
    curl -sX GET https://<<tenant>>.console.ves.volterra.io/api/config/namespaces/default/http_loadbalancers -H "Authorization: APIToken <<api_token>>"

### Show specific Loadbalancer
    curl -sX GET https://<<tenant>>.console.ves.volterra.io/api/config/namespaces/default/http_loadbalancers/<<lb_name>> -H "Authorization: APIToken <<api_token>>"

### create object
    curl  https://<<tenant>>.console.ves.volterra.io/<<path>> -H "Content-type:application/json" -X POST -d @<<jsonfile.json>>
    Paths:
        /api/waf/namespaces/{namespace}/app_firewalls
        /api/config/namespaces/<<namespace>>/origin_pools
        /api/config/namespaces/<<namespace>>/healthchecks

    BODY: {metadata:, spec:}

