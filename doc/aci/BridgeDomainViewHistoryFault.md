# Bridge Domain

## History fault view

```
# iserver get aci bd --apic apic21 --when any --view hfault

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Fault Records last 10y [#18]
--------------------------------------------

+----------------------+------+-------+-------------------+-------------------------------+-----------+------------------------------------------------------------------------------+
| Bridge Domain        | Sev  | Code  | Cause             | Created Time                  | Lifecycle | Description                                                                  |
+----------------------+------+-------+-------------------+-------------------------------+-----------+------------------------------------------------------------------------------+
| hefernan_ni-demo/BD1 | --   | F1534 | resolution-failed | 2021-10-27T17:20:40.153+02:00 |           | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| hefernan_ni-demo/BD1 | --   | F0953 | resolution-failed | 2021-10-27T17:20:40.151+02:00 |           | Failed to form relation to MO snPol-default of class igmpSnoopPol in context | 
| hefernan_ni-demo/BD1 | --   | F3302 | resolution-failed | 2021-10-27T17:20:40.148+02:00 |           | Failed to form relation to MO mldsnoopPol-default of class mldSnoopPol in    | 
|                      |      |       |                   |                               |           | context                                                                      | 
| hefernan_ni-demo/BD1 | --   | F1534 | resolution-failed | 2021-10-27T16:20:31.472+02:00 | retaining | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| hefernan_ni-demo/BD1 | Warn | F1534 | resolution-failed | 2021-10-27T16:20:31.470+02:00 | raised    | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| hefernan_ni-demo/BD1 | --   | F0953 | resolution-failed | 2021-10-27T16:20:31.468+02:00 | retaining | Failed to form relation to MO snPol-default of class igmpSnoopPol in context | 
| hefernan_ni-demo/BD1 | Warn | F0953 | resolution-failed | 2021-10-27T16:20:31.466+02:00 | raised    | Failed to form relation to MO snPol-default of class igmpSnoopPol in context | 
| hefernan_ni-demo/BD1 | --   | F3302 | resolution-failed | 2021-10-27T16:20:31.464+02:00 | retaining | Failed to form relation to MO mldsnoopPol-default of class mldSnoopPol in    | 
|                      |      |       |                   |                               |           | context                                                                      | 
| hefernan_ni-demo/BD1 | Warn | F3302 | resolution-failed | 2021-10-27T16:20:31.460+02:00 | raised    | Failed to form relation to MO mldsnoopPol-default of class mldSnoopPol in    | 
|                      |      |       |                   |                               |           | context                                                                      | 
| infra/ave-ctrl       | --   | F1534 | resolution-failed | 2020-12-09T21:08:00.942+02:00 |           | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| infra/ave-ctrl       | --   | F1534 | resolution-failed | 2020-12-09T20:07:36.360+02:00 | retaining | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| infra/ave-ctrl       | Warn | F1534 | resolution-failed | 2020-12-09T20:07:33.128+02:00 | raised    | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| infra/default        | --   | F1534 | resolution-failed | 2020-12-09T21:08:00.942+02:00 |           | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| infra/default        | --   | F0951 | resolution-failed | 2020-12-09T21:08:00.941+02:00 |           | Failed to form relation to MO epRPol-default of class fvEpRetPol in context  | 
| infra/default        | --   | F1534 | resolution-failed | 2020-12-09T20:07:36.329+02:00 | retaining | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| infra/default        | --   | F0951 | resolution-failed | 2020-12-09T20:07:36.327+02:00 | retaining | Failed to form relation to MO epRPol-default of class fvEpRetPol in context  | 
| infra/default        | Warn | F1534 | resolution-failed | 2020-12-09T20:07:33.126+02:00 | raised    | Failed to form relation to MO ndifpol-default of class ndIfPol in context    | 
| infra/default        | Warn | F0951 | resolution-failed | 2020-12-09T20:07:33.124+02:00 | raised    | Failed to form relation to MO epRPol-default of class fvEpRetPol in context  | 
+----------------------+------+-------+-------------------+-------------------------------+-----------+------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --when any --view hfault

{
    "duration": 4307,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 479,
        "disconnect_time": 0,
        "mo_time": 2997,
        "total_time": 3476
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

True	479	-	connect apic21o.emea-sp.cisco.com:443
True	468	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	478	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	333	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	454	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	1264	18	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./BridgeDomain.md)