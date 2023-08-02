# Application Profile (AP)

## Filter by application profile's tenant name

```
# iserver get aci ap --apic apic21 --tenant common

Apic: apic21 (mode:online, cache:off)

Application Profile [#3]
------------------------

+--------+---------+---------------------+--------------------+-------------+
| Health | Faults  | Application Profile | Application EPGs   | Priority    |
+--------+---------+---------------------+--------------------+-------------+
| 100    | 0 0 0 0 | common/default      |                    | unspecified | 
+--------+---------+---------------------+--------------------+-------------+
| 100    | 0 0 0 0 | common/privIP_TEST  | common/privIP_TEST | unspecified | 
+--------+---------+---------------------+--------------------+-------------+
| 100    | 0 0 0 0 | common/Test_ANP     | common/Test_EPG    | unspecified | 
+--------+---------+---------------------+--------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --tenant common

{
    "duration": 2397,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 571,
        "disconnect_time": 0,
        "mo_time": 1207,
        "total_time": 1778
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

True	571	-	connect apic21o.emea-sp.cisco.com:443
True	425	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	460	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	322	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationProfile.md)