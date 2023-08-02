# Bridge Domain

## Diag view

```
# iserver get aci bd --apic apic21 --when 60d --view diag

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Faults [#0]
---------------------------
None

Bridge Domain - Fault Records last 60d [#0]
-------------------------------------------
None

Bridge Domain - Event Logs last 60d [#1]
----------------------------------------

+----------------+------+----------+------------+-------------------------------+------------------------+----------------------------------+
| Bridge Domain  | Sev  | Code     | Cause      | Created Time                  | Description            | Change Set                       |
+----------------+------+----------+------------+-------------------------------+------------------------+----------------------------------+
| k8s/bmk8s_1_BD | Info | E4211946 | transition | 2023-06-18T01:02:31.469+02:00 | BD bmk8s_1_BD modified | mcastARPDrop (Old: yes, New: no) | 
+----------------+------+----------+------------+-------------------------------+------------------------+----------------------------------+

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
# iserver get aci bd --apic apic21 --when 60d --view diag

{
    "duration": 8994,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 489,
        "disconnect_time": 0,
        "mo_time": 6746,
        "total_time": 7235
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

True	489	-	connect apic21o.emea-sp.cisco.com:443
True	485	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	488	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	362	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	505	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	449	0	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=faults,no-scoped,subtree
True	1309	18	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1297	70	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1851	1711	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./BridgeDomain.md)