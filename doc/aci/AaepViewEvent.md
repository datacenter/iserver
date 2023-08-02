# Attachable Access Entity Profile (AAEP)

## Event view

```
# iserver get aci aaep --apic apic11 --when any --view event

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - Event Logs last 10y [#1]
------------------------------------------------------------------

+---------+------+----------+------------+-------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------+
| Name    | Sev  | Code     | Cause      | Created Time                  | Description                                            | Change Set                                                                 |
+---------+------+----------+------------+-------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------+
| default | Info | E4214291 | transition | 2020-03-02T12:38:35.002+02:00 | RsFuncToEpg uni/tn-infra/ap-access/epg-default created | encap:vlan-4093, forceResolve:yes, instrImedcy:lazy, mode:regular,         | 
|         |      |          |            |                               |                                                        | primaryEncap:unknown, rType:mo, state:formed, stateQual:none, tCl:fvAEPg,  | 
|         |      |          |            |                               |                                                        | tDn:uni/tn-infra/ap-access/epg-default, tType:mo                           | 
+---------+------+----------+------------+-------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------+
```

Developer

```
# iserver get aci aaep --apic apic11 --when any --view event

{
    "duration": 3117,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 376,
        "disconnect_time": 0,
        "mo_time": 2600,
        "total_time": 2976
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

True	376	-	connect apic11o.emea-sp.cisco.com:443
True	406	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	318	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	1876	4	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./Aaep.md)