# Bridge Domain

## Filter by bridge domain's L3Out name

```
# iserver get aci bd --apic apic21 --l3out k8s/*

Apic: apic21 (mode:online, cache:off)

+-------------------+-----------------+-------+------------------+--------------+
| Bridge Domain     | Subnet          | Usage | VRF              | L3Out        |
+-------------------+-----------------+-------+------------------+--------------+
| k8s/bml3outk8s_BD | 10.58.24.126/28 | 1/14  | common/Infra_VRF | k8s/bml3_k8s | 
+-------------------+-----------------+-------+------------------+--------------+
| k8s/vl3outk8s_BD  | 10.58.24.110/28 | 1/14  | common/Infra_VRF | k8s/vl3_k8s  | 
+-------------------+-----------------+-------+------------------+--------------+
```

Developer

```
# iserver get aci bd --apic apic21 --l3out k8s/*

{
    "duration": 2136,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 1210,
        "total_time": 1635
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

True	425	-	connect apic21o.emea-sp.cisco.com
True	412	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	375	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	423	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)