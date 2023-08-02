# VRF

## Event view

```
# iserver get aci vrf --apic apic21 --name *infra* --when 7d --view event

Apic: apic21 (mode:online, cache:off)

VRF - Event Logs last 7d [#0]
-----------------------------
None
```

Developer

```
# iserver get aci vrf --apic apic21 --name *infra* --when 7d --view event

{
    "duration": 9625,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 456,
        "disconnect_time": 0,
        "mo_time": 8142,
        "total_time": 8598
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

True	456	-	connect apic21o.emea-sp.cisco.com:443
True	442	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	461	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	374	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	384	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	452	87	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	464	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	364	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	401	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	4800	4371	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./Vrf.md)