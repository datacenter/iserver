# Node Protocol - BFD

## Fault view

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol BFD - Faults [#2]
--------------------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.050+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:57:16.415+02:00 | raised    | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |           | is down. Reason: No Diagnostic.                                                  | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view fault

{
    "duration": 1542,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 923,
        "total_time": 1319
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

True	396	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	298	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	328	2	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolBfd.md)