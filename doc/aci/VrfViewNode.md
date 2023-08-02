# VRF

## Node view

```
# iserver get aci vrf --apic apic21 --name *infra* --view node

Apic: apic21 (mode:online, cache:off)

VRF - Nodes [#2]
----------------

+--------+---------+-------------------------+----------------+------------+
| Health | Faults  | VRF                     | Node           | Interfaces |
+--------+---------+-------------------------+----------------+------------+
| 100    | 0 0 0 0 | common/Infra_privIP_VRF | bl2205-eu-spdc | 3          | 
|        |         |                         | bl2206-eu-spdc | 3          | 
|        |         |                         | cl2201-eu-spdc | 14         | 
|        |         |                         | cl2202-eu-spdc | 14         | 
|        |         |                         | cl2207-eu-spdc | 1          | 
|        |         |                         | cl2208-eu-spdc | 1          | 
|        |         |                         | rl2701-eu-spdc | 1          | 
|        |         |                         | rl2702-eu-spdc | 1          | 
+--------+---------+-------------------------+----------------+------------+
| 100    | 0 0 0 0 | common/Infra_VRF        | bl2205-eu-spdc | 5          | 
|        |         |                         | bl2206-eu-spdc | 5          | 
|        |         |                         | cl2201-eu-spdc | 18         | 
|        |         |                         | cl2202-eu-spdc | 18         | 
|        |         |                         | cl2207-eu-spdc | 24         | 
|        |         |                         | cl2208-eu-spdc | 23         | 
+--------+---------+-------------------------+----------------+------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --name *infra* --view node

{
    "duration": 5315,
    "apic": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 10,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 4276,
        "total_time": 4722
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

True	446	-	connect apic21o.emea-sp.cisco.com:443
True	481	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	490	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	365	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	388	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	504	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	479	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	354	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	361	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	464	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/ctx-Infra_VRF query rsp-subtree-include=full-deployment&target-node=all&target-path=CtxToNwIf
True	390	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/ctx-Infra_privIP_VRF query rsp-subtree-include=full-deployment&target-node=all&target-path=CtxToNwIf
```

[[Back]](./Vrf.md)