# Bridge Domain

## Filter by bridge domain's IP address

Bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci bd --apic apic21 --ip 10.58.24.209

Apic: apic21

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 10.58.24.222/28 | 10/14 | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --ip 10.58.24.209

{
    "duration": 2012,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 632,
        "disconnect_time": 0,
        "mo_time": 1190,
        "total_time": 1822
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
    }
}

Log: apic
----------

True	632	-	connect apic21o.emea-sp.cisco.com
True	439	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	358	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	393	72	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./BridgeDomain.md)