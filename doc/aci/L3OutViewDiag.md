# L3Out

## Diag view

```
# iserver get aci l3out --apic apic11 --name *mpc-out* --when 7d --view diag

Apic: apic11 (mode:online, cache:off)

L3Out - Faults [#0]
-------------------
None

L3Out - Fault Records last 7d [#0]
----------------------------------
None

L3Out - Event Logs last 7d [#0]
-------------------------------
None

L3Out - Audit Logs last 7d [#2]
-------------------------------

+-------------+------+----------+------------+-------------------------------+------------------------------+--------------------------------------------------------------------+
| L3Out       | Sev  | Code     | Cause      | Created Time                  | Description                  | Change Set                                                         |
+-------------+------+----------+------------+-------------------------------+------------------------------+--------------------------------------------------------------------+
| MPC/MPC-OUT | Info | E4214389 | transition | 2023-07-26T16:05:22.794+02:00 | Subnet 15.2.10.11/32 deleted |                                                                    | 
+-------------+------+----------+------------+-------------------------------+------------------------------+--------------------------------------------------------------------+
| MPC/MPC-OUT | Info | E4214387 | transition | 2023-07-26T16:04:41.416+02:00 | Subnet 15.2.10.11/32 created | ip:15.2.10.11/32, name:GamingServer,                               | 
|             |      |          |            |                               |                              | scope:import-security,shared-rtctrl,shared-security, userdom::all: | 
+-------------+------+----------+------------+-------------------------------+------------------------------+--------------------------------------------------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --name *mpc-out* --when 7d --view diag

{
    "duration": 14460,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 464,
        "disconnect_time": 0,
        "mo_time": 11152,
        "total_time": 11616
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

True	464	-	connect apic11o.emea-sp.cisco.com:443
True	482	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	364	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	354	1	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=faults,no-scoped,subtree
True	4966	3981	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1813	2	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	3173	4931	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./L3Out.md)