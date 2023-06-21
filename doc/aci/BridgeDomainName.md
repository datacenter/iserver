# Bridge Domain

## Filter by bridge domain's name

Example: domain name value

```
# iserver get aci bd --apic apic21 --name *vk8s*

Apic: apic21 (mode:online, cache:off)

Bridge Domain Summary
---------------------

+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Class ID | VNID     | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_1_BD | 16399    | 15007706 | 10.58.24.174/28 | 2/14  | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_2_BD | 32777    | 14745597 | 10.58.24.190/28 | 1/14  | k8s/vk8s_2 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_3_BD | 16400    | 15335346 | 10.58.24.206/28 | 2/14  | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 32776    | 14843889 | 10.58.24.222/28 | 2/14  | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
```

Example: tenant and domain name value

```
# iserver get aci bd --apic apic21 --name k8s/vk8s*

Apic: apic21 (mode:online, cache:off)

Bridge Domain Summary
---------------------

+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Class ID | VNID     | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_1_BD | 16399    | 15007706 | 10.58.24.174/28 | 2/14  | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_2_BD | 32777    | 14745597 | 10.58.24.190/28 | 1/14  | k8s/vk8s_2 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_3_BD | 16400    | 15335346 | 10.58.24.206/28 | 2/14  | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 32776    | 14843889 | 10.58.24.222/28 | 2/14  | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --name *vk8s*

{
    "duration": 2776,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 426,
        "disconnect_time": 0,
        "mo_time": 1561,
        "total_time": 1987
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

True	426	-	connect apic21o.emea-sp.cisco.com:443
True	410	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	418	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	319	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	414	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)