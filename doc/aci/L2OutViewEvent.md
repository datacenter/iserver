# L2Out

## Event view

```
# iserver get aci l2out --apic apic21 --when any --view event

Apic: apic21 (mode:online, cache:off)

L2Out - Event Logs last 10y [#2]
--------------------------------

+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
| L2Out          | Sev  | Code     | Cause      | Created Time                  | Description   | Change Set                                                         |
+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
| common/default | Info | E4212437 | transition | 2020-12-15T12:33:29.587+02:00 | RsEBd created | encap:unknown, forceResolve:yes, rType:mo, state:formed,           | 
|                |      |          |            |                               |               | stateQual:default-target, tCl:fvBD, tDn:uni/tn-common/BD-default,  | 
|                |      |          |            |                               |               | tRn:BD-default, tType:name                                         | 
+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
| common/default | Info | E4212437 | transition | 2020-12-09T20:07:28.270+02:00 | RsEBd created | encap:unknown, forceResolve:yes, rType:mo, state:formed,           | 
|                |      |          |            |                               |               | stateQual:default-target, tCl:fvBD, tDn:uni/tn-common/BD-default,  | 
|                |      |          |            |                               |               | tRn:BD-default, tType:name                                         | 
+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --when any --view event

{
    "duration": 2227,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 528,
        "disconnect_time": 0,
        "mo_time": 1177,
        "total_time": 1705
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

True	528	-	connect apic21o.emea-sp.cisco.com:443
True	360	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	374	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	443	4	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./L2Out.md)