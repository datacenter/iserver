# Bridge Domain

## Filter by bridge domain's vrf name

```
# iserver get aci bd --apic apic21 --vrf *mgmt*

Apic: apic21 (mode:online, cache:off)

+------------------+-------------------+------------------------+
| Bridge Domain    | EPG               | VRF                    |
+------------------+-------------------+------------------------+
| mgmt/EU-SPDC-BD1 | mgmt/EU-SPDC-MGMT | mgmt/EU-SPDC-MGMT-VRF1 | 
+------------------+-------------------+------------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --vrf *mgmt*

{
    "duration": 2248,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 418,
        "disconnect_time": 0,
        "mo_time": 1211,
        "total_time": 1629
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

True	418	-	connect apic21o.emea-sp.cisco.com
True	408	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	371	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	432	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)