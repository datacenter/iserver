# VLAN Pool

## Fault view

```
# iserver get aci pool vlan --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)

Pool VLAN - Faults [#0]
-----------------------
None
```

Developer

```
# iserver get aci pool vlan --apic apic21 --view fault

{
    "duration": 1079,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 367,
        "disconnect_time": 0,
        "mo_time": 587,
        "total_time": 954
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

True	367	-	connect apic21o.emea-sp.cisco.com:443
True	301	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	286	0	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./PoolVlan.md)