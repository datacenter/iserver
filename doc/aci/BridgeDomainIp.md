# Bridge Domain

## Filter by bridge domain's IP address

Bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci bd --apic apic21 --address 10.58.24.209

Apic: apic21 (mode:online, cache:off)

Bridge Domain Summary
---------------------

+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Class ID | VNID     | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 32776    | 14843889 | 10.58.24.222/28 | 2/14  | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --address 10.58.24.209

{
    "duration": 2258,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 1427,
        "total_time": 1826
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

True	399	-	connect apic21o.emea-sp.cisco.com:443
True	385	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	387	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	289	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	366	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)