# Bridge Domain

## Node view

```
# iserver get aci bd --apic apic21 --name *vk8s* --view node

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Nodes [#4]
--------------------------

+---------+---------------+----------------+------------+
| Faults  | Bridge Domain | Node           | Interfaces |
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_1_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_2_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_3_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_4_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
```

Developer

```
# iserver get aci bd --apic apic21 --name *vk8s* --view node

{
    "duration": 4990,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 523,
        "disconnect_time": 0,
        "mo_time": 3712,
        "total_time": 4235
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

True	523	-	connect apic21o.emea-sp.cisco.com:443
True	477	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	501	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	380	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	887	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	372	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_1_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
True	334	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_3_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
True	351	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_4_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
True	410	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_2_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
```

[[Back]](./BridgeDomain.md)