# Application Profile

## Event view

```
# iserver get aci ap --apic apic21 --name *k8s* --when 7d --view event

Apic: apic21 (mode:online, cache:off)

Application Profile - Event Logs last 7d [#1]
---------------------------------------------

+---------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| Application Profile | Sev  | Code     | Cause      | Created Time                  | Description                                                          |
+---------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4209236 | transition | 2023-07-26T08:03:41.872+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+---------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s* --when 7d --view event

{
    "duration": 8349,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 538,
        "disconnect_time": 0,
        "mo_time": 5282,
        "total_time": 5820
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	538	-	connect apic21o.emea-sp.cisco.com:443
True	545	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	505	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	366	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	3866	4027	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ApplicationProfile.md)