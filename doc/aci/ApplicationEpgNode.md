# Application Endpoint Group (EPG)

## Filter by deployed node name

```
# iserver get aci epg --apic apic21 --node *2207* --view node --pivot

Apic: apic21 (mode:online, cache:off)
```

Developer

```
# iserver get aci epg --apic apic21 --node *2207* --view node --pivot

{
    "duration": 1729,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 1069,
        "total_time": 1466
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

True	397	-	connect apic21o.emea-sp.cisco.com:443
True	419	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	307	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	343	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./ApplicationEpg.md)