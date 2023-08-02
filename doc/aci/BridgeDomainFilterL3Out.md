# Bridge Domain

## Filter by bridge domain's L3Out name

```
# iserver get aci bd --apic apic21 --l3out k8s/*

Apic: apic21 (mode:online, cache:off)

Bridge Domain [#2]
------------------

+--------+---------+-------------------+----------+----------+-----------------+-------+-----+------------------+--------------+
| Health | Faults  | Bridge Domain     | Class ID | VNID     | Subnet          | Usage | EPG | VRF              | L3Out        |
+--------+---------+-------------------+----------+----------+-----------------+-------+-----+------------------+--------------+
| 100    | 0 0 0 0 | k8s/bml3outk8s_BD | 32770    | 14712830 | 10.58.24.126/28 | 1/14  |     | common/Infra_VRF | k8s/bml3_k8s | 
+--------+---------+-------------------+----------+----------+-----------------+-------+-----+------------------+--------------+
| 100    | 0 0 0 0 | k8s/vl3outk8s_BD  | 49161    | 14909416 | 10.58.24.110/28 | 1/14  |     | common/Infra_VRF | k8s/vl3_k8s  | 
+--------+---------+-------------------+----------+----------+-----------------+-------+-----+------------------+--------------+
```

Developer

```
# iserver get aci bd --apic apic21 --l3out k8s/*

{
    "duration": 2717,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 493,
        "disconnect_time": 0,
        "mo_time": 1794,
        "total_time": 2287
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

True	493	-	connect apic21o.emea-sp.cisco.com:443
True	522	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	541	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	317	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	414	87	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)