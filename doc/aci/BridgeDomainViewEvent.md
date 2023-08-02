# Bridge Domain

## Event view

```
# iserver get aci bd --apic apic21 --when any --view event

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Event Logs last 10y [#6]
----------------------------------------

+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| Bridge Domain        | Sev  | Code     | Cause      | Created Time                  | Description            | Change Set                                                                       |
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| common/default       | Info | E4211945 | transition | 2020-12-15T12:33:29.451+02:00 | BD default created     | OptimizeWanBandwidth:no, arpFlood:no, bcastP:225.1.84.112, epClear:no,           | 
|                      |      |          |            |                               |                        | hostBasedRouting:no, intersiteBumTrafficAllow:no, intersiteL2Stretch:no,         | 
|                      |      |          |            |                               |                        | ipLearning:yes, ipv6McastAllow:no, limitIpLearnToSubnets:yes, llAddr:::,         | 
|                      |      |          |            |                               |                        | mac:00:22:BD:F8:19:FF, mcastAllow:no, mtu:inherit, multiDstPktAct:bd-flood,      | 
|                      |      |          |            |                               |                        | name:default, pcTag:49153, scope:3014656, seg:15728622, type:regular,            | 
|                      |      |          |            |                               |                        | unicastRoute:yes, unkMacUcastAct:proxy, unkMcastAct:flood, v6unkMcastAct:flood,  | 
|                      |      |          |            |                               |                        | vmac:not-applicable                                                              | 
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| infra/ave-ctrl       | Info | E4216052 | transition | 2020-12-09T20:07:28.284+02:00 | RsMldsn created        | forceResolve:yes, rType:mo, state:formed, stateQual:default-target,              | 
|                      |      |          |            |                               |                        | tCl:mldSnoopPol, tDn:uni/tn-infra/mldsnoopPol-default, tRn:mldsnoopPol-default,  | 
|                      |      |          |            |                               |                        | tType:name                                                                       | 
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| infra/default        | Info | E4214156 | transition | 2020-12-15T12:33:31.176+02:00 | RsBdToEpRet created    | forceResolve:yes, rType:mo, resolveAct:resolve, state:formed,                    | 
|                      |      |          |            |                               |                        | stateQual:default-target, tCl:fvEpRetPol, tDn:uni/tn-common/epRPol-default,      | 
|                      |      |          |            |                               |                        | tRn:epRPol-default, tType:name                                                   | 
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| k8s/bmk8s_1_BD       | Info | E4211946 | transition | 2023-06-18T01:02:31.469+02:00 | BD bmk8s_1_BD modified | mcastARPDrop (Old: yes, New: no)                                                 | 
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| mgmt/inb             | Info | E4214165 | transition | 2020-12-15T12:33:29.119+02:00 | RsCtx created          | forceResolve:yes, rType:mo, state:formed, stateQual:none, tCl:fvCtx,             | 
|                      |      |          |            |                               |                        | tDn:uni/tn-mgmt/ctx-inb, tRn:ctx-inb, tType:name, tnFvCtxName:inb                | 
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
| SPN_IntraLab/SPN_BD1 | Info | E4211946 | transition | 2022-09-14T20:07:58.810+02:00 | BD SPN_BD1 modified    | mcastARPDrop (Old: yes, New: no)                                                 | 
+----------------------+------+----------+------------+-------------------------------+------------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --when any --view event

{
    "duration": 6476,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 471,
        "disconnect_time": 0,
        "mo_time": 5345,
        "total_time": 5816
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

True	471	-	connect apic21o.emea-sp.cisco.com:443
True	491	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	2561	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	357	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	500	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	1436	70	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./BridgeDomain.md)