# Bridge Domain

## Filter by bridge domain's subnet

Bridge domain with IP subnet that contains provided IP subnet will be shown.

```
# iserver get aci bd --apic apic21 --subnet 10.58.24.206/28

Apic: apic21

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_3_BD | 10.58.24.206/28 | 10/14 | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --subnet 10.58.24.206/28

{
    "duration": 2613,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 1975,
        "total_time": 2395
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

True	420	-	connect apic21o.emea-sp.cisco.com
True	1245	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	362	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	368	73	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./BridgeDomain.md)