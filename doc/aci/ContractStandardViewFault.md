# Standard Contract

## Fault view

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --view fault

Apic: apic21 (mode:online, cache:off)

Standard Contract - Faults [#0]
-------------------------------
None
```

Developer

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --view fault

{
    "duration": 2496,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 481,
        "disconnect_time": 0,
        "mo_time": 1700,
        "total_time": 2181
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

True	481	-	connect apic21o.emea-sp.cisco.com:443
True	440	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	434	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	420	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	406	0	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ContractStandard.md)