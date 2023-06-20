# Application Endpoint Group (EPG)

## Filter by leaf policy group

```
# iserver get aci epg --apic apic21 --contract k8s_esx71_PolGrp --view member

Apic: apic21 (mode:online, cache:off)
```

Developer

```
# iserver get aci epg --apic apic21 --contract k8s_esx71_PolGrp --view member

{
    "duration": 1129,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 651,
        "total_time": 1044
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

True	393	-	connect apic21o.emea-sp.cisco.com:443
True	375	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	276	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationEpg.md)