# Taboo Contract

## Fault history view

```
# iserver get aci contract taboo
    --apic apic21
    --name k8s/my*
    --when any
    --view hfault

Apic: apic21 (mode:online, cache:off)

Taboo Contract - Fault Records last 10y [#0]
--------------------------------------------
None
```

Developer

```
# iserver get aci contract taboo
    --apic apic21
    --name k8s/my*
    --when any
    --view hfault

{
    "duration": 1978,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 432,
        "disconnect_time": 0,
        "mo_time": 1445,
        "total_time": 1877
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

True	432	-	connect apic21o.emea-sp.cisco.com:443
True	345	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	345	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	351	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	404	0	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ContractTaboo.md)