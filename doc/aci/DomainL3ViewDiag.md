# L3 Domain

## Diag view

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view diag

Apic: apic21 (mode:online, cache:off)

L3 Domain - Faults [#0]
-----------------------
None

L3 Domain - Fault Records last 10y [#0]
---------------------------------------
None

L3 Domain - Event Logs last 10y [#0]
------------------------------------
None

L3 Domain - Audit Logs last 10y [#2]
------------------------------------

+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
| Domain      | Sev  | Code     | Cause      | Created Time                  | Description              | Change Set                                                          |
+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
| UCSB1_L3Dom | Info | E4214354 | transition | 2022-11-03T20:05:44.726+02:00 | RsVlanNs created         | tDn:uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, userdom::all:common: | 
+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
| UCSB1_L3Dom | Info | E4212452 | transition | 2022-11-03T20:05:44.725+02:00 | DomP UCSB1_L3Dom created | name:UCSB1_L3Dom, userdom::all:common:                              | 
+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view diag

{
    "duration": 3996,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 478,
        "disconnect_time": 0,
        "mo_time": 3162,
        "total_time": 3640
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

True	478	-	connect apic21o.emea-sp.cisco.com:443
True	391	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	376	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=faults,no-scoped,subtree
True	780	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	813	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	802	13	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL3.md)