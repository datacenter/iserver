# VLAN Pool

## Filter by domain

```
# iserver get aci pool vlan --apic apic21 --domain *vmw*

Apic: apic21 (mode:online, cache:off)

Pool VLAN [#0]
--------------
None
```

Developer

```
# iserver get aci pool vlan --apic apic21 --domain *vmw*

{
    "duration": 777,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 361,
        "disconnect_time": 0,
        "mo_time": 337,
        "total_time": 698
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

True	361	-	connect apic21o.emea-sp.cisco.com:443
True	337	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./PoolVlan.md)