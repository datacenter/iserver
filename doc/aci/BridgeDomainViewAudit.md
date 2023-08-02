# Bridge Domain

## Audit view

```
# iserver get aci bd --apic apic21 --when 60d --view audit

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Audit Logs last 60d [#4]
----------------------------------------

+---------------+------+----------+------------+-------------------------------+-----------------------------------+---------------------------------------------------------------------------------+
| Bridge Domain | Sev  | Code     | Cause      | Created Time                  | Description                       | Change Set                                                                      |
+---------------+------+----------+------------+-------------------------------+-----------------------------------+---------------------------------------------------------------------------------+
| k8s/Test      | Info | E4211946 | transition | 2023-06-21T16:45:26.385+02:00 | BD Test modified From:10.61.75.82 | unkMcastAct (Old: flood, New: opt-flood)                                        | 
+---------------+------+----------+------------+-------------------------------+-----------------------------------+---------------------------------------------------------------------------------+
| k8s/Test      | Info | E4211946 | transition | 2023-06-21T16:14:43.611+02:00 | BD Test modified From:10.61.75.82 | multiDstPktAct (Old: encap-flood, New: bd-flood)                                | 
+---------------+------+----------+------------+-------------------------------+-----------------------------------+---------------------------------------------------------------------------------+
| k8s/Test      | Info | E4211946 | transition | 2023-06-21T16:12:59.156+02:00 | BD Test modified From:10.61.75.82 | multiDstPktAct (Old: drop, New: encap-flood), unkMacUcastAct (Old: proxy, New:  | 
|               |      |          |            |                               |                                   | flood)                                                                          | 
+---------------+------+----------+------------+-------------------------------+-----------------------------------+---------------------------------------------------------------------------------+
| k8s/Test      | Info | E4211946 | transition | 2023-06-21T16:11:00.823+02:00 | BD Test modified From:10.61.75.82 | multiDstPktAct (Old: bd-flood, New: drop)                                       | 
+---------------+------+----------+------------+-------------------------------+-----------------------------------+---------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --when 60d --view audit

{
    "duration": 5494,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 3572,
        "total_time": 4015
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

True	443	-	connect apic21o.emea-sp.cisco.com:443
True	513	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	518	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	336	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	463	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	1742	1711	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./BridgeDomain.md)