# Node Protocol - BFD

## Filter sessions by session id

```
# iserver get aci proto bfd --apic apic11 --node any --id *45 --view session

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

Protocol BFD - Session [#2]
---------------------------

+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF                           | Interface | Type      | Local Address  | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan472   | singlehop | 15.254.101.4   | 00:22:BD:F8:19:FF | down  | 1090519045 | 15.100.7.41    | FA:16:3E:BC:A6:70 | down  | 0          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan468   | singlehop | 15.254.134.253 | 00:22:BD:F8:19:FF | up    | 1090519045 | 15.254.134.55  | FA:16:3E:F3:E3:8C | up    | 2          | 
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+

Protocol BFD - Session Stats [#2]
---------------------------------

+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| Node                | VRF                           | Local Address  | Remote Address | Up | Down | Rx Cnt  | Rx Interval [msec] | Min | Avg | Max  | Tx Cnt  | Tx Interval [msec] | Min  | Avg  | Max  |
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.4   | 15.100.7.41    | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 1242305 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.55  | 1  | 0    | 4805518 | 500                | 2   | 467 | 1242 | 4961314 | 500                | 452  | 452  | 452  | 
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --id *45 --view session

{
    "duration": 4076,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 413,
        "disconnect_time": 0,
        "mo_time": 3208,
        "total_time": 3621
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
True	330	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	284	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	280	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	316	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	306	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	276	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	270	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	296	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	291	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	276	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	283	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)