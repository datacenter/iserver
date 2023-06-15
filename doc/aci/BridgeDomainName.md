# Bridge Domain

## Filter by bridge domain's name

Example: domain name value

```
# iserver get aci bd --apic apic21 --name *vk8s*

Apic: apic21 (mode:online, cache:off)

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_1_BD | 10.58.24.174/28 | 1/14  | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_2_BD | 10.58.24.190/28 | 1/14  | k8s/vk8s_2 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_3_BD | 10.58.24.206/28 | 1/14  | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 10.58.24.222/28 | 1/14  | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
```

Example: tenant and domain name value

```
# iserver get aci bd --apic apic21 --name k8s/vk8s*

Apic: apic21 (mode:online, cache:off)

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_1_BD | 10.58.24.174/28 | 1/14  | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_2_BD | 10.58.24.190/28 | 1/14  | k8s/vk8s_2 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_3_BD | 10.58.24.206/28 | 1/14  | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 10.58.24.222/28 | 1/14  | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --name *vk8s*

{
    "duration": 2181,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 428,
        "disconnect_time": 0,
        "mo_time": 1182,
        "total_time": 1610
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

True	428	-	connect apic21o.emea-sp.cisco.com
True	413	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	351	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	418	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)