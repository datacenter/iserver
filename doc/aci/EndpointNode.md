# Endpoint

## Filter by node

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

Apic: apic11 (mode:online, cache:off)

+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| SF | MAC Address       | IP Address      | EPG            | Encapsulation | Fabric                                    |
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:01:E8 | 15.2.62.5       |                | 2019          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:02:42 | 15.2.63.2       |                | 2018          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:03:17 | 15.2.61.4       |                | 2346          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:04:77 | 15.2.61.6       |                | 2346          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:04:AD | 15.2.63.1       |                | 2018          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:07:12 | 15.2.6.3        |                | 2017          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:08:C6 | 15.2.64.4       |                | 2179          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:0E:37 | 15.2.64.3       |                | 2179          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:0E:D8 | 15.2.7.5        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:12:3C | 15.2.64.1       | F5_IN          | 2008          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:2A:04 | 15.2.61.2       |                | 2346          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:2A:D3 | 15.2.64.1       |                | 2179          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:2F:12 |                 | F5_OUT         | 2009          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:3E:20 | 15.2.62.1       |                | 2019          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:40:96 | 15.2.6.5        |                | 2017          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:41:6B | 15.2.63.6       |                | 2018          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:5E:5B | 15.2.6.1        |                | 2017          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:62:BB | 15.2.7.4        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:68:C2 | 15.2.62.4       |                | 2019          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:6B:0E | 15.2.64.6       |                | 2179          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:71:15 | 15.2.63.3       |                | 2018          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:73:48 | 15.2.63.4       |                | 2018          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:73:C4 | 15.2.7.1        |                | 419           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:77:0B | 15.2.7.3        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:7E:F3 | 15.2.7.2        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:81:80 | 15.2.62.2       |                | 2019          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:8D:E9 | 15.2.64.11      | F5_IN          | 2008          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:8F:CB | 15.2.7.6        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:A1:06 | 15.2.61.1       |                | 2346          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:A2:F7 | 15.2.6.4        |                | 2017          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:A8:0A | 15.2.62.3       |                | 2019          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:B4:4F | 15.2.61.5       |                | 2346          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:B5:70 | 15.2.63.5       |                | 2018          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:B6:11 | 15.2.62.6       |                | 2019          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:BC:84 | 15.2.61.3       |                | 2346          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:D4:07 | 15.2.64.2       |                | 2179          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:D5:AB | 15.2.7.1        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:DB:49 | 15.2.6.2        |                | 2017          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:DC:A0 |                 | F5_IN          | 2008          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:EC:C0 | 15.2.6.6        |                | 2017          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:ED:0F | 15.2.64.5       |                | 2179          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.88  |                | 21            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.90  |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.92  |                | 22            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.94  |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.100 |                | 24            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.102 |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.96  |                | 23            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.98  |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.21  |                | 11            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.17  |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.45  |                | 15            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.41  |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.105 |                | 25            | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.107 |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:EE:D8 | 15.100.161.30   | P5G-F1C-NGC-N2 | 904           | pod-1 node-205 eth1/16                    | 
|    |                   | 15.100.161.31   |                |               |                                           | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:EE:D8 | 10.58.24.130    | P5G-mgmt       | 900           | pod-1 node-205 eth1/16                    | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:F4:F8 |                 | P5G-mgmt       | 900           | pod-1 node-205 eth1/19                    | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:F8:18 | 15.100.161.130  | P5G-F1U-NGU-N3 | 905           | pod-1 node-205 eth1/15                    | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
Interface context: ep
```

Developer

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

{
    "duration": 34807,
    "apic": {
        "read": true,
        "success": 63,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 62,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 32860,
        "total_time": 33245
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

True	385	-	connect apic11o.emea-sp.cisco.com:443
True	1675	362	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	380	602	apic11o.emea-sp.cisco.com:443 class fabricPathEp
True	3836	37	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	341	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	453	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	416	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	413	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	469	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	428	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	476	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	506	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	497	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	510	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	495	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	505	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	500	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	493	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	407	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	600	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	440	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	424	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	461	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	464	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	523	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	442	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	431	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	435	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=205&target-path=AccBaseGrpToEthIf
True	416	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=206&target-path=AccBaseGrpToEthIf
True	419	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	483	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	412	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	450	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	462	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	511	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	454	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=302&target-path=AccBaseGrpToEthIf
True	428	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=301&target-path=AccBaseGrpToEthIf
True	434	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	448	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	423	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	471	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	590	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	487	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	558	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	455	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	433	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	447	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	423	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	426	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	412	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	416	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	423	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	540	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	477	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	428	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	506	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	419	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	424	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	425	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	412	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	455	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	440	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	433	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
```

[[Back]](./Endpoint.md)