# Node Protocol - ARP

## Session stats view

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view stats

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

BFD Session Stats [#9]
----------------------

+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| Node                | VRF                           | Local Address  | Remote Address | Up | Down | Rx Cnt  | Rx Interval [msec] | Min | Avg | Max  | Tx Cnt  | Tx Interval [msec] | Min  | Avg  | Max  |
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.0   | 15.100.103.41  | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 191816  | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.4   | 15.100.7.41    | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 272990  | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.191 | 1  | 0    | 1133154 | 500                | 1   | 465 | 1526 | 1098566 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.192 | 1  | 0    | 1131930 | 500                | 0   | 466 | 1139 | 1098574 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.191 | 1  | 0    | 1133214 | 500                | 0   | 465 | 2167 | 1098570 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.192 | 1  | 0    | 1131927 | 500                | 0   | 466 | 764  | 1098574 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.191 | 1  | 0    | 794297  | 500                | 1   | 466 | 1971 | 771622  | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.193 | 1  | 0    | 795574  | 500                | 1   | 466 | 1991 | 771586  | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.55  | 1  | 0    | 793441  | 500                | 4   | 467 | 1881 | 771776  | 500                | 480  | 480  | 480  | 
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view stats

{
    "duration": 2038,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 1124,
        "total_time": 1549
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

True	425	-	connect apic11o.emea-sp.cisco.com:443
True	342	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	389	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	393	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)