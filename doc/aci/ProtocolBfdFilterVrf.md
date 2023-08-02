# Node Protocol - BFD

## Filter sessions by vrf name

```
# iserver get aci proto bfd
    --apic apic11
    --node any
    --vrf *common*
    --view session

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

Protocol BFD - Session [#16]
----------------------------

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

Protocol BFD - Session Stats [#16]
----------------------------------

+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| Node                | VRF                           | Local Address  | Remote Address | Up | Down | Rx Cnt  | Rx Interval [msec] | Min | Avg | Max  | Tx Cnt  | Tx Interval [msec] | Min  | Avg  | Max  |
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.0   | 15.100.103.41  | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 1161137 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.4   | 15.100.7.41    | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 1242311 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.191 | 1  | 0    | 5156076 | 500                | 1   | 465 | 1526 | 4998919 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.192 | 1  | 0    | 5152566 | 500                | 0   | 466 | 1139 | 4998927 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.191 | 1  | 0    | 5156140 | 500                | 0   | 465 | 2167 | 4998923 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.192 | 1  | 0    | 5152514 | 500                | 0   | 466 | 764  | 4998927 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.191 | 1  | 0    | 4809478 | 500                | 1   | 466 | 1971 | 4671975 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.193 | 1  | 0    | 4817224 | 500                | 1   | 466 | 1991 | 4671939 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.55  | 1  | 0    | 4805446 | 500                | 4   | 467 | 1881 | 4672129 | 500                | 480  | 480  | 480  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.253 | 15.254.104.191 | 1  | 0    | 5156113 | 500                | 1   | 465 | 1967 | 5308350 | 500                | 452  | 452  | 452  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.253 | 15.254.104.192 | 1  | 0    | 5152313 | 500                | 0   | 466 | 1446 | 5308354 | 500                | 452  | 452  | 452  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.253 | 15.254.107.191 | 1  | 0    | 5156134 | 500                | 1   | 465 | 1839 | 5308354 | 500                | 452  | 452  | 452  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.253 | 15.254.107.192 | 1  | 0    | 5152530 | 500                | 0   | 466 | 2344 | 5308354 | 500                | 452  | 452  | 452  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.191 | 1  | 0    | 4809729 | 500                | 1   | 466 | 1694 | 4961164 | 500                | 452  | 452  | 452  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.193 | 1  | 0    | 4817210 | 500                | 1   | 466 | 2100 | 4961132 | 500                | 452  | 452  | 452  | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.55  | 1  | 0    | 4805544 | 500                | 2   | 467 | 1242 | 4961340 | 500                | 452  | 452  | 452  | 
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
```

Developer

```
# iserver get aci proto bfd
    --apic apic11
    --node any
    --vrf *common*
    --view session

{
    "duration": 4304,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 3417,
        "total_time": 3828
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

True	411	-	connect apic11o.emea-sp.cisco.com:443
True	302	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	301	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	303	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	322	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	346	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	298	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	290	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	326	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	319	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	291	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	319	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)