# Application Profile (AP)

## Filter by application profile's tenant name

```
# iserver get aci ap --apic apic21 --tenant common

Apic: apic21 (mode:online, cache:off)

+---------------------+--------------------+-------------+
| Application Profile | Application EPGs   | Priority    |
+---------------------+--------------------+-------------+
| common/default      |                    | unspecified | 
+---------------------+--------------------+-------------+
| common/privIP_TEST  | common/privIP_TEST | unspecified | 
+---------------------+--------------------+-------------+
| common/Test_ANP     | common/Test_EPG    | unspecified | 
+---------------------+--------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --tenant common

{
    "duration": 1295,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 698,
        "total_time": 1106
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

True	408	-	connect apic21o.emea-sp.cisco.com
True	329	12	apic21o.emea-sp.cisco.com class fvAp
True	369	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

[[Back]](./ApplicationProfile.md)