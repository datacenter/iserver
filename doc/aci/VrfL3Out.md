get_aci_bd# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated L3Out name

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

Apic: apic21 (mode:online, cache:off)

+----------+----------------+---------------+----------+---------+----------------+---------------+-----------------+------------------+
| VRF      | PCE Preference | PCE Direction | Class ID | VNID    | Associated EPG | Associated BD | BD Subnets      | Associated L3Out |
+----------+----------------+---------------+----------+---------+----------------+---------------+-----------------+------------------+
| mgmt/inb | enforced       | ingress       | 16386    | 3080192 |                | mgmt/inb      | 10.58.50.190/27 | mgmt/INB_L3out   | 
+----------+----------------+---------------+----------+---------+----------------+---------------+-----------------+------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

{
    "duration": 4294,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 459,
        "disconnect_time": 0,
        "mo_time": 2984,
        "total_time": 3443
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

True	459	-	connect apic21o.emea-sp.cisco.com:443
True	327	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	446	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	359	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	351	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	404	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	413	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	317	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	367	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)