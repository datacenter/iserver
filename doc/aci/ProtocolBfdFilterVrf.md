# Node Protocol - BFD

## Filter sessions by vrf name

```
# iserver get aci proto bfd --apic apic11 --node any --vrf *common*

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

BFD Sessions [#16]
------------------

+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF                           | Interface | Type      | Local Address  | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan471   | singlehop | 15.254.101.0   | 00:22:BD:F8:19:FF | down  | 1090519046 | 15.100.103.41  | FA:16:3E:D6:A8:CB | down  | 0          | 
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan472   | singlehop | 15.254.101.4   | 00:22:BD:F8:19:FF | down  | 1090519045 | 15.100.7.41    | FA:16:3E:BC:A6:70 | down  | 0          | 
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

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --vrf *common*

{
    "duration": 10316,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 468,
        "disconnect_time": 0,
        "mo_time": 8204,
        "total_time": 8672
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

True	468	-	connect apic11o.emea-sp.cisco.com:443
True	409	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	310	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	381	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	463	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	340	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	348	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	328	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	314	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	358	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	355	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	347	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	329	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	338	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	339	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	350	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	346	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	354	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	333	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	360	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	381	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	357	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	384	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	380	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)