# Endpoint

## Filter by node

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

Apic: apic11 (mode:online, cache:off)

+----+-------------------+-----------------+-------------------------------------------+
| SF | MAC Address       | IP Address      | Fabric                                    |
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:01:E8 | 15.2.62.5       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:02:42 | 15.2.63.2       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:40:96 | 15.2.6.5        | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:41:6B | 15.2.63.6       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:68:C2 | 15.2.62.4       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:73:48 | 15.2.63.4       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:81:80 | 15.2.62.2       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:B4:4F | 15.2.61.5       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:B5:70 | 15.2.63.5       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| LV | 00:50:56:B2:B6:11 | 15.2.62.6       | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |                 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.88  | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.90  |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.92  | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.94  |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.100 | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.102 |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.96  | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.98  |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.21  | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.17  |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 00:A3:8E:EB:B3:3F | 192.168.254.45  | pod-1 node-205 eth1/24                    | 
|    |                   | 192.168.254.41  |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:EE:D8 | 15.100.161.30   | pod-1 node-205 eth1/16                    | 
|    |                   | 15.100.161.31   |                                           | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:EE:D8 | 10.58.24.130    | pod-1 node-205 eth1/16                    | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:F4:F8 |                 | pod-1 node-205 eth1/19                    | 
+----+-------------------+-----------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:F8:18 | 15.100.161.130  | pod-1 node-205 eth1/15                    | 
+----+-------------------+-----------------+-------------------------------------------+
Interface context: ep
```

Developer

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

{
    "duration": 26062,
    "apic": {
        "read": true,
        "success": 41,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 40,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 23474,
        "total_time": 23908
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

True	434	-	connect apic11o.emea-sp.cisco.com
True	554	192	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	484	602	apic11o.emea-sp.cisco.com class fabricPathEp
True	3828	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	397	13	apic11o.emea-sp.cisco.com class fabricNode
True	462	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	461	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	470	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	494	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	474	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	499	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	509	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	567	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	494	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	462	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	523	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	471	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=205&target-path=AccBaseGrpToEthIf
True	473	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=206&target-path=AccBaseGrpToEthIf
True	422	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	435	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	465	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	511	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	726	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	595	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	453	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=302&target-path=AccBaseGrpToEthIf
True	447	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=301&target-path=AccBaseGrpToEthIf
True	487	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	485	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	590	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	506	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	586	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	524	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	646	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	585	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	507	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	473	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	451	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	449	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	532	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	517	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
```

[[Back]](./Endpoint.md)