# Application Endpoint Group (EPG)

## Audit view

```
# iserver get aci epg --apic apic21 --when 60d --name vk8s_1 --view audit

Apic: apic21 (mode:online, cache:off)

EPG - Audit Logs last 60d [#0]
------------------------------
None
```

Developer

```
# iserver get aci epg --apic apic21 --when 60d --name vk8s_1 --view audit

{
    "duration": 4012,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 477,
        "disconnect_time": 0,
        "mo_time": 2656,
        "total_time": 3133
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

True	477	-	connect apic21o.emea-sp.cisco.com:443
True	503	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	350	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1803	1873	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ApplicationEpg.md)