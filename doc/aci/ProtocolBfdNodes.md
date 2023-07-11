# Node Protocol - BFD

## Selected nodes

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --node bl
    --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc

+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| Node                | Role | HW               | Admin   | Health | Faults  | Echo Intf   | Sessions | Intf    | State   | Sessions |
+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| pod-1/bl205-eu-spdc | leaf | N9K-C93600CD-GX  | enabled | 90     | 0 1 0 0 | unspecified | 0/1      | lo3     | enabled | 0/1      | 
| pod-1/bl206-eu-spdc | leaf | N9K-C93600CD-GX  | enabled | 90     | 0 1 0 0 | unspecified | 0/1      | lo2     | enabled | 0/1      | 
| pod-1/cl201-eu-spdc | leaf | N9K-C93360YC-FX2 | enabled | 93     | 0 2 0 0 | unspecified | 7/9      | vlan472 | enabled | 0/1      | 
|                     |      |                  |         |        |         |             |          | vlan473 | enabled | 3/3      | 
|                     |      |                  |         |        |         |             |          | vlan496 | enabled | 2/2      | 
+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
```

Developer

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --node bl
    --view summary

{
    "duration": 3272,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 413,
        "disconnect_time": 0,
        "mo_time": 2325,
        "total_time": 2738
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

True	413	-	connect apic11o.emea-sp.cisco.com:443
True	324	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	321	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	339	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	324	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	330	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	338	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	349	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)