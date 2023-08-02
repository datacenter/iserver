# Node Protocol - BFD

## Filter sessions by interface name

```
# iserver get aci proto bfd --apic apic11 --node any --intf lo* --view session

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

Protocol BFD - Session [#4]
---------------------------

+---------------------+--------+---------+-----------+-----------+----------+---------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF       | Interface | Type     | Local Address | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-----------+-----------+----------+---------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/bl205-eu-spdc | 90     | 0 1 0 0 | overlay-1 | lo3       | multihop | 172.31.2.25   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.2.54    | 00:00:00:00:00:00 | down  | 0          | 
| pod-1/bl206-eu-spdc | 90     | 0 1 0 0 | overlay-1 | lo2       | multihop | 172.31.2.26   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.2.54    | 00:00:00:00:00:00 | down  | 0          | 
| pod-1/rl301-eu-spdc | 90     | 0 1 0 0 | overlay-1 | lo3       | multihop | 172.31.3.31   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.3.35    | 00:00:00:00:00:00 | down  | 0          | 
| pod-1/rl302-eu-spdc | 90     | 0 1 0 0 | overlay-1 | lo3       | multihop | 172.31.3.32   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.3.35    | 00:00:00:00:00:00 | down  | 0          | 
+---------------------+--------+---------+-----------+-----------+----------+---------------+-------------------+-------+------------+----------------+-------------------+-------+------------+

Protocol BFD - Session Stats [#4]
---------------------------------

+---------------------+-----------+---------------+----------------+----+------+--------+--------------------+-----+-----+-----+---------+--------------------+------+------+------+
| Node                | VRF       | Local Address | Remote Address | Up | Down | Rx Cnt | Rx Interval [msec] | Min | Avg | Max | Tx Cnt  | Tx Interval [msec] | Min  | Avg  | Max  |
+---------------------+-----------+---------------+----------------+----+------+--------+--------------------+-----+-----+-----+---------+--------------------+------+------+------+
| pod-1/bl205-eu-spdc | overlay-1 | 172.31.2.25   | 172.31.2.54    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2525758 | 2000               | 1750 | 1750 | 1750 | 
| pod-1/bl206-eu-spdc | overlay-1 | 172.31.2.26   | 172.31.2.54    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2415324 | 2000               | 1830 | 1830 | 1830 | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.31.3.31   | 172.31.3.35    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2343597 | 2000               | 1886 | 1886 | 1886 | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.31.3.32   | 172.31.3.35    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2509947 | 2000               | 1761 | 1761 | 1761 | 
+---------------------+-----------+---------------+----------------+----+------+--------+--------------------+-----+-----+-----+---------+--------------------+------+------+------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --intf lo* --view session

{
    "duration": 4160,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 3318,
        "total_time": 3726
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

True	408	-	connect apic11o.emea-sp.cisco.com:443
True	303	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	280	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	297	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	305	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	324	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	321	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	290	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	296	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	304	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	291	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	307	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)