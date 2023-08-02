# Node Protocol - BFD

## Filter sessions by state

State 'up'

```
# iserver get aci proto bfd --apic apic11 --node any --state up --view session

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

Protocol BFD - Session [#14]
----------------------------

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

Protocol BFD - Session Stats [#14]
----------------------------------

+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+-----+-----+-----+
| Node                | VRF                           | Local Address  | Remote Address | Up | Down | Rx Cnt  | Rx Interval [msec] | Min | Avg | Max  | Tx Cnt  | Tx Interval [msec] | Min | Avg | Max |
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+-----+-----+-----+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.191 | 1  | 0    | 5155986 | 500                | 1   | 465 | 1526 | 4998832 | 500                | 480 | 480 | 480 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.192 | 1  | 0    | 5152475 | 500                | 0   | 466 | 1139 | 4998840 | 500                | 480 | 480 | 480 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.191 | 1  | 0    | 5156050 | 500                | 0   | 465 | 2167 | 4998836 | 500                | 480 | 480 | 480 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.192 | 1  | 0    | 5152425 | 500                | 0   | 466 | 764  | 4998840 | 500                | 480 | 480 | 480 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.191 | 1  | 0    | 4809387 | 500                | 1   | 466 | 1971 | 4671888 | 500                | 480 | 480 | 480 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.193 | 1  | 0    | 4817134 | 500                | 1   | 466 | 1991 | 4671852 | 500                | 480 | 480 | 480 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.55  | 1  | 0    | 4805356 | 500                | 4   | 467 | 1881 | 4672042 | 500                | 480 | 480 | 480 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.253 | 15.254.104.191 | 1  | 0    | 5156023 | 500                | 1   | 465 | 1967 | 5308258 | 500                | 452 | 452 | 452 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.253 | 15.254.104.192 | 1  | 0    | 5152223 | 500                | 0   | 466 | 1446 | 5308262 | 500                | 452 | 452 | 452 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.253 | 15.254.107.191 | 1  | 0    | 5156043 | 500                | 1   | 465 | 1839 | 5308262 | 500                | 452 | 452 | 452 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.253 | 15.254.107.192 | 1  | 0    | 5152441 | 500                | 0   | 466 | 2344 | 5308262 | 500                | 452 | 452 | 452 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.191 | 1  | 0    | 4809639 | 500                | 1   | 466 | 1694 | 4961072 | 500                | 452 | 452 | 452 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.193 | 1  | 0    | 4817119 | 500                | 1   | 466 | 2100 | 4961040 | 500                | 452 | 452 | 452 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.253 | 15.254.134.55  | 1  | 0    | 4805454 | 500                | 2   | 467 | 1242 | 4961248 | 500                | 452 | 452 | 452 | 
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+-----+-----+-----+
```

State 'down'

```
# iserver get aci proto bfd --apic apic11 --node any --state down --view session

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

Protocol BFD - Session [#6]
---------------------------

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

Protocol BFD - Session Stats [#6]
---------------------------------

+---------------------+-------------------------------+---------------+----------------+----+------+--------+--------------------+-----+-----+-----+---------+--------------------+------+------+------+
| Node                | VRF                           | Local Address | Remote Address | Up | Down | Rx Cnt | Rx Interval [msec] | Min | Avg | Max | Tx Cnt  | Tx Interval [msec] | Min  | Avg  | Max  |
+---------------------+-------------------------------+---------------+----------------+----+------+--------+--------------------+-----+-----+-----+---------+--------------------+------+------+------+
| pod-1/bl205-eu-spdc | overlay-1                     | 172.31.2.25   | 172.31.2.54    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2525753 | 2000               | 1750 | 1750 | 1750 | 
| pod-1/bl206-eu-spdc | overlay-1                     | 172.31.2.26   | 172.31.2.54    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2415318 | 2000               | 1830 | 1830 | 1830 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.0  | 15.100.103.41  | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 1161120 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.4  | 15.100.7.41    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 1242294 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 172.31.3.31   | 172.31.3.35    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2343592 | 2000               | 1886 | 1886 | 1886 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 172.31.3.32   | 172.31.3.35    | 0  | 0    | 0      | 2000               | 0   | 0   | 0   | 2509941 | 2000               | 1761 | 1761 | 1761 | 
+---------------------+-------------------------------+---------------+----------------+----+------+--------+--------------------+-----+-----+-----+---------+--------------------+------+------+------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --state up --view session

{
    "duration": 4385,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 441,
        "disconnect_time": 0,
        "mo_time": 3463,
        "total_time": 3904
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

True	441	-	connect apic11o.emea-sp.cisco.com:443
True	324	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	311	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	314	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	315	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	348	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	308	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	281	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	292	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	336	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	334	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	300	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```


[[Back]](./ProtocolBfd.md)