# L3Out

## Event view

```
# iserver get aci l3out --apic apic11 --when any --view event

Apic: apic11 (mode:online, cache:off)

L3Out - Event Logs last 10y [#1]
--------------------------------

+----------------+------+----------+------------+-------------------------------+---------------------+------------------------------------------------------------+
| L3Out          | Sev  | Code     | Cause      | Created Time                  | Description         | Change Set                                                 |
+----------------+------+----------+------------+-------------------------------+---------------------+------------------------------------------------------------+
| common/default | Info | E4212482 | transition | 2020-03-02T12:38:34.918+02:00 | Out default created | enforceRtctrl:export, name:default, targetDscp:unspecified | 
+----------------+------+----------+------------+-------------------------------+---------------------+------------------------------------------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --when any --view event

{
    "duration": 5295,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 461,
        "disconnect_time": 0,
        "mo_time": 4606,
        "total_time": 5067
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

True	461	-	connect apic11o.emea-sp.cisco.com:443
True	464	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	365	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	3777	2	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./L3Out.md)