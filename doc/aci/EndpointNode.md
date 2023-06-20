# Endpoint

## Filter by node

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

Apic: apic11 (mode:online, cache:off)

+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| SF | MAC Address       | IP Address      | EPG            | Encapsulation | Fabric                                    |
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:01:E8 | 15.2.62.5       |                | 2354          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:02:42 | 15.2.63.2       |                | 2005          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:03:17 | 15.2.61.4       |                | 2020          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:04:77 | 15.2.61.6       |                | 2020          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:0E:D8 | 15.2.7.5        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:12:3C | 15.2.64.1       | F5_IN          | 2008          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:2A:D3 |                 |                | 2010          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:2F:12 |                 | F5_OUT         | 2009          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:40:96 | 15.2.6.5        |                | 2004          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:41:6B | 15.2.63.6       |                | 2005          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:68:C2 | 15.2.62.4       |                | 2354          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:6B:0E | 15.2.64.6       |                | 2010          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:71:15 | 15.2.63.3       |                | 2005          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:73:48 | 15.2.63.4       |                | 2005          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:73:C4 | 15.2.7.1        |                | 419           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:81:80 | 15.2.62.2       |                | 2354          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:8D:E9 | 15.2.64.11      | F5_IN          | 2008          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| L  | 00:50:56:B2:8F:CB | 15.2.7.6        |                | 403           | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:A2:F7 | 15.2.6.4        |                | 2004          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:A8:0A | 15.2.62.3       |                | 2354          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:B4:4F | 15.2.61.5       |                | 2020          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:B5:70 | 15.2.63.5       |                | 2005          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:B6:11 | 15.2.62.6       |                | 2354          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:DC:A0 |                 | F5_IN          | 2008          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:EC:C0 | 15.2.6.6        |                | 2004          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 |                |               | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+----------------+---------------+-------------------------------------------+
| LV | 00:50:56:B2:ED:0F | 15.2.64.5       |                | 2010          | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
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
    "duration": 26771,
    "apic": {
        "read": true,
        "success": 41,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 40,
        "connect_time": 658,
        "disconnect_time": 0,
        "mo_time": 24762,
        "total_time": 25420
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

True	658	-	connect apic11o.emea-sp.cisco.com:443
True	1107	210	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	796	602	apic11o.emea-sp.cisco.com:443 class fabricPathEp
True	3758	37	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	403	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	474	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	468	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	466	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	429	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	437	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	477	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	459	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	423	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	439	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	512	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	426	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	940	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	956	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=205&target-path=AccBaseGrpToEthIf
True	444	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=206&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	886	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	731	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	435	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	461	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	459	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=302&target-path=AccBaseGrpToEthIf
True	433	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=301&target-path=AccBaseGrpToEthIf
True	456	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	444	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	443	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	465	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	596	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	617	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	688	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	479	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	689	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	449	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	437	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	444	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	416	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	466	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
```

[[Back]](./Endpoint.md)