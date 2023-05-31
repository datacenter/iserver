get_aci_bd# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated L3Out name

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

Apic: apic21

+----------+----------------+---------------+----------------+---------------+-----------------+------------------+
| VRF      | PCE Preference | PCE Direction | Associated EPG | Associated BD | BD Subnets      | Associated L3Out |
+----------+----------------+---------------+----------------+---------------+-----------------+------------------+
| mgmt/inb | enforced       | ingress       |                | mgmt/inb      | 10.58.50.190/27 | mgmt/INB_L3out   | 
+----------+----------------+---------------+----------------+---------------+-----------------+------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

{
    "duration": 4764,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 431,
        "disconnect_time": 0,
        "mo_time": 3874,
        "total_time": 4305
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

True	431	-	connect apic21o.emea-sp.cisco.com
True	339	23	apic21o.emea-sp.cisco.com class fvCtx
True	455	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	413	72	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	350	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	357	53	apic21o.emea-sp.cisco.com class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	312	13	apic21o.emea-sp.cisco.com class fabricNode
True	1339	14	apic21o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	309	17	apic21o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./Vrf.md)