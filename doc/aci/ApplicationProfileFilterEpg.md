# Application Profile (AP)

## Filter by application profiles's epg name

```
# iserver get aci ap --apic apic21 --epg vEPC/*

Apic: apic21 (mode:online, cache:off)

Application Profile [#1]
------------------------

+--------+---------+---------------------+------------------+-------------+
| Health | Faults  | Application Profile | Application EPGs | Priority    |
+--------+---------+---------------------+------------------+-------------+
| 59     | 0 0 0 0 | vEPC/vSFO_ANP       | vEPC/WWW         | unspecified | 
+--------+---------+---------------------+------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --epg vEPC/*

{
    "duration": 2053,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 478,
        "disconnect_time": 0,
        "mo_time": 1265,
        "total_time": 1743
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

True	478	-	connect apic21o.emea-sp.cisco.com:443
True	423	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	507	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	335	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationProfile.md)