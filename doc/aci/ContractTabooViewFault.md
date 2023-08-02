# Taboo Contract

## Fault view

```
# iserver get aci contract taboo --apic apic21 --name k8s/my* --view fault

Apic: apic21 (mode:online, cache:off)

Taboo Contract - Faults [#0]
----------------------------
None
```

Developer

```
# iserver get aci contract taboo --apic apic21 --name k8s/my* --view fault

{
    "duration": 1885,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 1353,
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

True	425	-	connect apic21o.emea-sp.cisco.com:443
True	332	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	328	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	365	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	328	0	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ContractTaboo.md)