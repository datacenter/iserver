get_aci_bd# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated L3Out name

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

Apic: apic21 (mode:online, cache:off)

VRF [#1]
--------

+--------+---------+----------+----------+---------+----------------+---------------+----------------+---------------+-----------------+------------------+
| Health | Faults  | VRF      | Class ID | VNID    | PCE Preference | PCE Direction | Associated EPG | Associated BD | BD Subnets      | Associated L3Out |
+--------+---------+----------+----------+---------+----------------+---------------+----------------+---------------+-----------------+------------------+
| 100    | 0 0 0 0 | mgmt/inb | 16386    | 3080192 | enforced       | ingress       |                | mgmt/inb      | 10.58.50.190/27 | mgmt/INB_L3out   | 
+--------+---------+----------+----------+---------+----------------+---------------+----------------+---------------+-----------------+------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

{
    "duration": 4027,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 454,
        "disconnect_time": 0,
        "mo_time": 3139,
        "total_time": 3593
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

True	454	-	connect apic21o.emea-sp.cisco.com:443
True	456	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	436	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	356	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	362	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	439	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	433	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	316	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	341	154	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)