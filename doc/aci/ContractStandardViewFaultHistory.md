# Standard Contract

## Fault history view

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --when any
    --view hfault

Apic: apic21 (mode:online, cache:off)

Standard Contract - Fault Records last 10y [#0]
-----------------------------------------------
None
```

Developer

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --when any
    --view hfault

{
    "duration": 3069,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 477,
        "disconnect_time": 0,
        "mo_time": 2269,
        "total_time": 2746
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

True	477	-	connect apic21o.emea-sp.cisco.com:443
True	439	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	410	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	427	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	993	9	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ContractStandard.md)