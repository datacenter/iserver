# Policy Group - Access Interface - Leaf Access Port

## Event view

```
# iserver get aci pg access intf port --apic apic21 --when any --view event

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface Port - Event Logs last 10y [#1]
---------------------------------------------------------------

+--------------------------+------+----------+------------+-------------------------------+-----------------------+-------------------------------------------------------------------------+
| PG Name                  | Sev  | Code     | Cause      | Created Time                  | Description           | Change Set                                                              |
+--------------------------+------+----------+------------+-------------------------------+-----------------------+-------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp | Info | E4214324 | transition | 2023-06-18T01:02:31.456+02:00 | RsQosDppIfPol created | forceResolve:yes, rType:mo, state:formed, stateQual:default-target,     | 
|                          |      |          |            |                               |                       | tCl:qosDppPol, tDn:uni/infra/qosdpppol-default, tRn:qosdpppol-default,  | 
|                          |      |          |            |                               |                       | tType:name, userdom:all                                                 | 
+--------------------------+------+----------+------------+-------------------------------+-----------------------+-------------------------------------------------------------------------+
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --when any --view event

{
    "duration": 1612,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 884,
        "total_time": 1299
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

True	415	-	connect apic21o.emea-sp.cisco.com:443
True	358	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	526	8	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./PgAccessInterfacePort.md)