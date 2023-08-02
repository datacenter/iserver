# L3 Domain

## Audit view

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view audit

Apic: apic21 (mode:online, cache:off)

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
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view audit

{
    "duration": 2057,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 484,
        "disconnect_time": 0,
        "mo_time": 1179,
        "total_time": 1663
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

True	484	-	connect apic21o.emea-sp.cisco.com:443
True	353	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	826	13	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL3.md)