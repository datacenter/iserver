# Bridge Domain

## Fault view

```
# iserver get aci bd --apic apic21 --name *vk8s* --view fault

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Faults [#0]
---------------------------
None
```

Developer

```
# iserver get aci bd --apic apic21 --name *vk8s* --view fault

{
    "duration": 4153,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 3107,
        "total_time": 3550
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

True	443	-	connect apic21o.emea-sp.cisco.com:443
True	1416	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	492	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	341	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	518	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	340	0	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./BridgeDomain.md)