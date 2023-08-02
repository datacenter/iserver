# VRF

## Interface view

```
# iserver get aci vrf --apic apic21 --name *infra* --view intf

Apic: apic21 (mode:online, cache:off)

VRF - Interfaces [#2]
---------------------

+--------+---------+-------------------------+----------------+---------------+
| Health | Faults  | VRF                     | Node           | Interface     |
+--------+---------+-------------------------+----------------+---------------+
| 100    | 0 0 0 0 | common/Infra_privIP_VRF | bl2205-eu-spdc | vxlan-2326529 | 
|        |         |                         | bl2205-eu-spdc | vxlan-2326529 | 
|        |         |                         | bl2205-eu-spdc | vxlan-2326529 | 
|        |         |                         | bl2206-eu-spdc | vxlan-2326529 | 
|        |         |                         | bl2206-eu-spdc | vxlan-2326529 | 
|        |         |                         | bl2206-eu-spdc | vxlan-2326529 | 
|        |         |                         | cl2201-eu-spdc | eth1/34       | 
|        |         |                         | cl2201-eu-spdc | eth1/35       | 
|        |         |                         | cl2201-eu-spdc | eth1/36       | 
|        |         |                         | cl2201-eu-spdc | eth1/37       | 
|        |         |                         | cl2201-eu-spdc | eth1/38       | 
|        |         |                         | cl2201-eu-spdc | eth1/39       | 
|        |         |                         | cl2201-eu-spdc | eth1/40       | 
|        |         |                         | cl2201-eu-spdc | eth1/41       | 
|        |         |                         | cl2201-eu-spdc | eth1/42       | 
|        |         |                         | cl2201-eu-spdc | eth1/43       | 
|        |         |                         | cl2201-eu-spdc | eth1/45       | 
|        |         |                         | cl2201-eu-spdc | eth1/46       | 
|        |         |                         | cl2201-eu-spdc | eth1/47       | 
|        |         |                         | cl2201-eu-spdc | vxlan-2326529 | 
|        |         |                         | cl2202-eu-spdc | eth1/34       | 
|        |         |                         | cl2202-eu-spdc | eth1/35       | 
|        |         |                         | cl2202-eu-spdc | eth1/36       | 
|        |         |                         | cl2202-eu-spdc | eth1/37       | 
|        |         |                         | cl2202-eu-spdc | eth1/38       | 
|        |         |                         | cl2202-eu-spdc | eth1/39       | 
|        |         |                         | cl2202-eu-spdc | eth1/40       | 
|        |         |                         | cl2202-eu-spdc | eth1/41       | 
|        |         |                         | cl2202-eu-spdc | eth1/42       | 
|        |         |                         | cl2202-eu-spdc | eth1/43       | 
|        |         |                         | cl2202-eu-spdc | eth1/45       | 
|        |         |                         | cl2202-eu-spdc | eth1/46       | 
|        |         |                         | cl2202-eu-spdc | eth1/47       | 
|        |         |                         | cl2202-eu-spdc | vxlan-2326529 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2326529 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2326529 | 
|        |         |                         | rl2701-eu-spdc | vxlan-2326529 | 
|        |         |                         | rl2702-eu-spdc | vxlan-2326529 | 
+--------+---------+-------------------------+----------------+---------------+
| 100    | 0 0 0 0 | common/Infra_VRF        | bl2205-eu-spdc | eth1/19       | 
|        |         |                         | bl2205-eu-spdc | po5           | 
|        |         |                         | bl2205-eu-spdc | vxlan-2818048 | 
|        |         |                         | bl2205-eu-spdc | vxlan-2818048 | 
|        |         |                         | bl2205-eu-spdc | vxlan-2818048 | 
|        |         |                         | bl2206-eu-spdc | eth1/19       | 
|        |         |                         | bl2206-eu-spdc | po6           | 
|        |         |                         | bl2206-eu-spdc | vxlan-2818048 | 
|        |         |                         | bl2206-eu-spdc | vxlan-2818048 | 
|        |         |                         | bl2206-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2201-eu-spdc | eth1/31       | 
|        |         |                         | cl2201-eu-spdc | eth1/32       | 
|        |         |                         | cl2201-eu-spdc | eth1/33       | 
|        |         |                         | cl2201-eu-spdc | eth1/34       | 
|        |         |                         | cl2201-eu-spdc | eth1/35       | 
|        |         |                         | cl2201-eu-spdc | eth1/36       | 
|        |         |                         | cl2201-eu-spdc | eth1/37       | 
|        |         |                         | cl2201-eu-spdc | eth1/38       | 
|        |         |                         | cl2201-eu-spdc | eth1/39       | 
|        |         |                         | cl2201-eu-spdc | eth1/40       | 
|        |         |                         | cl2201-eu-spdc | eth1/41       | 
|        |         |                         | cl2201-eu-spdc | eth1/42       | 
|        |         |                         | cl2201-eu-spdc | eth1/43       | 
|        |         |                         | cl2201-eu-spdc | eth1/44       | 
|        |         |                         | cl2201-eu-spdc | eth1/45       | 
|        |         |                         | cl2201-eu-spdc | eth1/46       | 
|        |         |                         | cl2201-eu-spdc | eth1/47       | 
|        |         |                         | cl2201-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2202-eu-spdc | eth1/31       | 
|        |         |                         | cl2202-eu-spdc | eth1/32       | 
|        |         |                         | cl2202-eu-spdc | eth1/33       | 
|        |         |                         | cl2202-eu-spdc | eth1/34       | 
|        |         |                         | cl2202-eu-spdc | eth1/35       | 
|        |         |                         | cl2202-eu-spdc | eth1/36       | 
|        |         |                         | cl2202-eu-spdc | eth1/37       | 
|        |         |                         | cl2202-eu-spdc | eth1/38       | 
|        |         |                         | cl2202-eu-spdc | eth1/39       | 
|        |         |                         | cl2202-eu-spdc | eth1/40       | 
|        |         |                         | cl2202-eu-spdc | eth1/41       | 
|        |         |                         | cl2202-eu-spdc | eth1/42       | 
|        |         |                         | cl2202-eu-spdc | eth1/43       | 
|        |         |                         | cl2202-eu-spdc | eth1/44       | 
|        |         |                         | cl2202-eu-spdc | eth1/45       | 
|        |         |                         | cl2202-eu-spdc | eth1/46       | 
|        |         |                         | cl2202-eu-spdc | eth1/47       | 
|        |         |                         | cl2202-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | eth1/1/1      | 
|        |         |                         | cl2207-eu-spdc | eth1/1/2      | 
|        |         |                         | cl2207-eu-spdc | eth1/1/3      | 
|        |         |                         | cl2207-eu-spdc | eth1/1/4      | 
|        |         |                         | cl2207-eu-spdc | eth1/2/1      | 
|        |         |                         | cl2207-eu-spdc | eth1/2/2      | 
|        |         |                         | cl2207-eu-spdc | eth1/2/3      | 
|        |         |                         | cl2207-eu-spdc | po2           | 
|        |         |                         | cl2207-eu-spdc | po3           | 
|        |         |                         | cl2207-eu-spdc | po4           | 
|        |         |                         | cl2207-eu-spdc | po5           | 
|        |         |                         | cl2207-eu-spdc | po6           | 
|        |         |                         | cl2207-eu-spdc | po7           | 
|        |         |                         | cl2207-eu-spdc | po8           | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2207-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | eth1/1/1      | 
|        |         |                         | cl2208-eu-spdc | eth1/1/2      | 
|        |         |                         | cl2208-eu-spdc | eth1/1/3      | 
|        |         |                         | cl2208-eu-spdc | eth1/1/4      | 
|        |         |                         | cl2208-eu-spdc | eth1/2/1      | 
|        |         |                         | cl2208-eu-spdc | eth1/2/2      | 
|        |         |                         | cl2208-eu-spdc | eth1/2/3      | 
|        |         |                         | cl2208-eu-spdc | po2           | 
|        |         |                         | cl2208-eu-spdc | po3           | 
|        |         |                         | cl2208-eu-spdc | po4           | 
|        |         |                         | cl2208-eu-spdc | po5           | 
|        |         |                         | cl2208-eu-spdc | po6           | 
|        |         |                         | cl2208-eu-spdc | po7           | 
|        |         |                         | cl2208-eu-spdc | po8           | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
|        |         |                         | cl2208-eu-spdc | vxlan-2818048 | 
+--------+---------+-------------------------+----------------+---------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --name *infra* --view intf

{
    "duration": 6386,
    "apic": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 10,
        "connect_time": 448,
        "disconnect_time": 0,
        "mo_time": 5081,
        "total_time": 5529
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

True	448	-	connect apic21o.emea-sp.cisco.com:443
True	484	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	466	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	411	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	391	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	442	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	512	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	465	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	969	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	540	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/ctx-Infra_VRF query rsp-subtree-include=full-deployment&target-node=all&target-path=CtxToNwIf
True	401	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/ctx-Infra_privIP_VRF query rsp-subtree-include=full-deployment&target-node=all&target-path=CtxToNwIf
```

[[Back]](./Vrf.md)