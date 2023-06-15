# Node Protocol - BFD

## Get BFD sessions from selected nodes

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --node bl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc

+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
| Node                | Local Address | State | Session Id | Remote Address | State | Session Id | Type     | VRF       | Interface |
+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
| pod-1/bl205-eu-spdc | 172.31.2.25   | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop | overlay-1 | lo3       | 
| pod-1/bl206-eu-spdc | 172.31.2.26   | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop | overlay-1 | lo2       | 
+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --node bl

{
    "duration": 3715,
    "apic": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 10,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 3061,
        "total_time": 3473
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

True	412	-	connect apic11o.emea-sp.cisco.com
True	296	13	apic11o.emea-sp.cisco.com class fabricNode
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	308	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	286	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	310	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	314	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	332	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)