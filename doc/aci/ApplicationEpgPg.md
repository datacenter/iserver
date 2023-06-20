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
    "duration": 1372,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 708,
        "total_time": 1130
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

True	422	-	connect apic21o.emea-sp.cisco.com:443
True	394	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	314	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationEpg.md)