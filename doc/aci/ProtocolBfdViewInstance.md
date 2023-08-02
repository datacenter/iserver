# Node Protocol - BFD

## Inst view

```
# iserver get aci proto bfd --apic apic11 --node any --view inst

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
# iserver get aci proto bfd --apic apic11 --node any --view inst

{
    "duration": 7497,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 6577,
        "total_time": 6963
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

True	386	-	connect apic11o.emea-sp.cisco.com:443
True	308	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	276	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	286	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	263	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	279	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	291	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	301	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	271	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	338	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	306	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	286	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	277	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	264	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	309	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	287	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	282	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	284	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	269	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	289	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	297	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	276	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	270	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	268	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)