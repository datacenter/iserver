# Bridge Domain

## Filter by bridge domain's vrf name

```
# iserver get aci bd --apic apic21 --vrf *mgmt*

Apic: apic21

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
    "duration": 1887,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1230,
        "total_time": 1666
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

True	436	-	connect apic21o.emea-sp.cisco.com
True	473	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	378	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	379	73	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./BridgeDomain.md)