# Node Protocol - BFD

## Filter sessions by state

State 'up'

```
# iserver get aci proto bfd --apic apic11 --node any --state up

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

BFD Sessions [#14]
------------------

+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF                           | Interface | Type      | Local Address  | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan496   | singlehop | 15.254.103.252 | 00:22:BD:F8:19:FF | up    | 1090519044 | 15.254.103.191 | FA:16:3E:B6:A6:15 | up    | 3          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan496   | singlehop | 15.254.103.252 | 00:22:BD:F8:19:FF | up    | 1090519042 | 15.254.103.192 | FA:16:3E:C4:FE:86 | up    | 3          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N6_VRF    | vlan492   | singlehop | 15.254.106.252 | 00:22:BD:F8:19:FF | up    | 1090519043 | 15.254.106.191 | FA:16:3E:B6:A6:15 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N6_VRF    | vlan492   | singlehop | 15.254.106.252 | 00:22:BD:F8:19:FF | up    | 1090519041 | 15.254.106.192 | FA:16:3E:C4:FE:86 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan473   | singlehop | 15.254.133.252 | 00:22:BD:F8:19:FF | up    | 1090519048 | 15.254.133.191 | FA:16:3E:45:71:99 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan473   | singlehop | 15.254.133.252 | 00:22:BD:F8:19:FF | up    | 1090519049 | 15.254.133.193 | FA:16:3E:AE:9D:45 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan473   | singlehop | 15.254.133.252 | 00:22:BD:F8:19:FF | up    | 1090519047 | 15.254.133.55  | FA:16:3E:8C:96:73 | up    | 1          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan488   | singlehop | 15.254.104.253 | 00:22:BD:F8:19:FF | up    | 1090519044 | 15.254.104.191 | FA:16:3E:72:79:10 | up    | 4          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan488   | singlehop | 15.254.104.253 | 00:22:BD:F8:19:FF | up    | 1090519041 | 15.254.104.192 | FA:16:3E:CB:11:71 | up    | 4          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N6_VRF    | vlan472   | singlehop | 15.254.107.253 | 00:22:BD:F8:19:FF | up    | 1090519043 | 15.254.107.191 | FA:16:3E:72:79:10 | up    | 2          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N6_VRF    | vlan472   | singlehop | 15.254.107.253 | 00:22:BD:F8:19:FF | up    | 1090519042 | 15.254.107.192 | FA:16:3E:CB:11:71 | up    | 2          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan468   | singlehop | 15.254.134.253 | 00:22:BD:F8:19:FF | up    | 1090519046 | 15.254.134.191 | FA:16:3E:B5:89:41 | up    | 2          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan468   | singlehop | 15.254.134.253 | 00:22:BD:F8:19:FF | up    | 1090519047 | 15.254.134.193 | FA:16:3E:15:47:1D | up    | 2          | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan468   | singlehop | 15.254.134.253 | 00:22:BD:F8:19:FF | up    | 1090519045 | 15.254.134.55  | FA:16:3E:F3:E3:8C | up    | 2          | 
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
```

State 'down'

```
# iserver get aci proto bfd --apic apic11 --node any --state down

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

BFD Sessions [#6]
-----------------

+---------------------+--------+---------+-------------------------------+-----------+-----------+---------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF                           | Interface | Type      | Local Address | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-------------------------------+-----------+-----------+---------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/bl205-eu-spdc | 90     | 0 1 0 0 | overlay-1                     | lo3       | multihop  | 172.31.2.25   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.2.54    | 00:00:00:00:00:00 | down  | 0          | 
| pod-1/bl206-eu-spdc | 90     | 0 1 0 0 | overlay-1                     | lo2       | multihop  | 172.31.2.26   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.2.54    | 00:00:00:00:00:00 | down  | 0          | 
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan471   | singlehop | 15.254.101.0  | 00:22:BD:F8:19:FF | down  | 1090519046 | 15.100.103.41  | FA:16:3E:D6:A8:CB | down  | 0          | 
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan472   | singlehop | 15.254.101.4  | 00:22:BD:F8:19:FF | down  | 1090519045 | 15.100.7.41    | FA:16:3E:BC:A6:70 | down  | 0          | 
| pod-1/rl301-eu-spdc | 90     | 0 1 0 0 | overlay-1                     | lo3       | multihop  | 172.31.3.31   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.3.35    | 00:00:00:00:00:00 | down  | 0          | 
| pod-1/rl302-eu-spdc | 90     | 0 1 0 0 | overlay-1                     | lo3       | multihop  | 172.31.3.32   | 00:00:00:00:00:00 | down  | 1090519041 | 172.31.3.35    | 00:00:00:00:00:00 | down  | 0          | 
+---------------------+--------+---------+-------------------------------+-----------+-----------+---------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --state up

{
    "duration": 9123,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 7552,
        "total_time": 7979
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

True	427	-	connect apic11o.emea-sp.cisco.com:443
True	321	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	311	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	337	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	320	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	334	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	311	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	342	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	316	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	360	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	327	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	308	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	313	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	380	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	331	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	349	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	329	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	336	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	325	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	311	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	299	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	339	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	335	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	318	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```


[[Back]](./ProtocolBfd.md)