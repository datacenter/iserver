# Node Protocol - ARP

## Session summary view

```
# iserver get aci proto bfd --apic apic11 --node any --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-------------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| Node                | Role        | HW               | Admin   | Health | Faults  | Echo Intf   | Sessions | Intf    | State   | Sessions |
+---------------------+-------------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| pod-1/bl205-eu-spdc | leaf        | N9K-C93600CD-GX  | enabled | 90     | 0 1 0 0 | unspecified | 0/1      | lo3     | enabled | 0/1      | 
| pod-1/bl206-eu-spdc | leaf        | N9K-C93600CD-GX  | enabled | 90     | 0 1 0 0 | unspecified | 0/1      | lo2     | enabled | 0/1      | 
| pod-1/cl201-eu-spdc | leaf        | N9K-C93360YC-FX2 | enabled | 93     | 0 2 0 0 | unspecified | 7/9      | vlan472 | enabled | 0/1      | 
|                     |             |                  |         |        |         |             |          | vlan473 | enabled | 3/3      | 
|                     |             |                  |         |        |         |             |          | vlan496 | enabled | 2/2      | 
| pod-1/cl202-eu-spdc | leaf        | N9K-C93360YC-FX2 | enabled | 100    | 0 0 0 0 | unspecified | 7/7      | vlan468 | enabled | 3/3      | 
|                     |             |                  |         |        |         |             |          | vlan488 | enabled | 2/2      | 
| pod-1/cl209-eu-spdc | leaf        | N9K-C93600CD-GX  | enabled | 100    | 0 0 0 0 | unspecified | 0/0      |         |         |          | 
| pod-1/cl210-eu-spdc | leaf        | N9K-C93600CD-GX  | enabled | 100    | 0 0 0 0 | unspecified | 0/0      |         |         |          | 
| pod-1/rl301-eu-spdc | remote leaf | N9K-C9336C-FX2   | enabled | 90     | 0 1 0 0 | unspecified | 0/1      | lo3     | enabled | 0/1      | 
| pod-1/rl302-eu-spdc | remote leaf | N9K-C9336C-FX2   | enabled | 90     | 0 1 0 0 | unspecified | 0/1      | lo3     | enabled | 0/1      | 
| pod-1/s101-eu-spdc  | spine       | N9K-C9316D-GX    | enabled | 100    | 0 0 0 0 | unspecified | 0/0      |         |         |          | 
| pod-1/s102-eu-spdc  | spine       | N9K-C9316D-GX    | enabled | 100    | 0 0 0 0 | unspecified | 0/0      |         |         |          | 
+---------------------+-------------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --view summary

{
    "duration": 10167,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 426,
        "disconnect_time": 0,
        "mo_time": 8213,
        "total_time": 8639
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

True	426	-	connect apic11o.emea-sp.cisco.com:443
True	463	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	339	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	345	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	339	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	359	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	321	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	391	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	355	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	354	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	350	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	460	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	309	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	340	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	351	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	343	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	348	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	354	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	361	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	328	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	320	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	395	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	330	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	358	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)