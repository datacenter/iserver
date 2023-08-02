# L3Out

## Audit view

```
# iserver get aci l3out --apic apic11 --name *mpc-out* --when 7d --view audit

Apic: apic11 (mode:online, cache:off)

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
# iserver get aci l3out --apic apic11 --name *mpc-out* --when 7d --view audit

{
    "duration": 6509,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 4971,
        "total_time": 5417
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

True	446	-	connect apic11o.emea-sp.cisco.com:443
True	458	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	365	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	4148	4931	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./L3Out.md)