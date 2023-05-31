# Application Profile (AP)

## Filter by application profiles's epg name

```
# iserver get aci ap --apic apic21 --epg vEPC/*

Apic: apic21

+---------------------+------------------+-------------+
| Application Profile | Application EPGs | Priority    |
+---------------------+------------------+-------------+
| vEPC/vSFO_ANP       | vEPC/WWW         | unspecified | 
+---------------------+------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --epg vEPC/*

{
    "duration": 1090,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 637,
        "total_time": 1034
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
    }
}

Log: apic
----------

True	397	-	connect apic21o.emea-sp.cisco.com
True	289	12	apic21o.emea-sp.cisco.com class fvAp
True	348	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

[[Back]](./ApplicationProfile.md)