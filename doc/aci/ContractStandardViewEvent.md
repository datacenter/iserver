# Standard Contract

## Event view

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --when any
    --view event

Apic: apic21 (mode:online, cache:off)

Standard Contract - Event Logs last 10y [#0]
--------------------------------------------
None
```

Developer

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --when any
    --view event

{
    "duration": 3120,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 479,
        "disconnect_time": 0,
        "mo_time": 2251,
        "total_time": 2730
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

True	479	-	connect apic21o.emea-sp.cisco.com:443
True	457	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	378	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	445	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	971	6	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ContractStandard.md)