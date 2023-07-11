# Node Protocol - BFD

## Selected node

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| Node                | Role | HW               | Admin   | Health | Faults  | Echo Intf   | Sessions | Intf    | State   | Sessions |
+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| pod-1/cl201-eu-spdc | leaf | N9K-C93360YC-FX2 | enabled | 93     | 0 2 0 0 | unspecified | 7/9      | vlan472 | enabled | 0/1      | 
|                     |      |                  |         |        |         |             |          | vlan473 | enabled | 3/3      | 
|                     |      |                  |         |        |         |             |          | vlan496 | enabled | 2/2      | 
+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view summary

{
    "duration": 1926,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 433,
        "disconnect_time": 0,
        "mo_time": 1109,
        "total_time": 1542
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

True	433	-	connect apic11o.emea-sp.cisco.com:443
True	422	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	329	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	358	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)