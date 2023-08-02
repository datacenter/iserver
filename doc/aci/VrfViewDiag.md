# VRF

## Diag view

```
# iserver get aci vrf --apic apic21 --name *infra* --when 7d --view diag

Apic: apic21 (mode:online, cache:off)

VRF - Faults [#0]
-----------------
None

VRF - Fault Records last 7d [#0]
--------------------------------
None

VRF - Event Logs last 7d [#0]
-----------------------------
None

VRF - Audit Logs last 7d [#0]
-----------------------------
None
```

Developer

```
# iserver get aci vrf --apic apic21 --name *infra* --when 7d --view diag

{
    "duration": 14958,
    "apic": {
        "read": true,
        "success": 13,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 12,
        "connect_time": 470,
        "disconnect_time": 0,
        "mo_time": 12313,
        "total_time": 12783
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

True	470	-	connect apic21o.emea-sp.cisco.com:443
True	480	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	488	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	394	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	360	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	426	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	468	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	337	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	389	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	365	0	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree-include=faults,no-scoped,subtree
True	2126	89	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	4246	4371	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	2234	598	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./Vrf.md)