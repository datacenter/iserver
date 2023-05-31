# Endpoint

## Filter by node

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

Apic: apic11

+----+-------------------+--------------+-------------------------------------------+
| SF | MAC Address       | IP Address   | Fabric                                    |
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:01:E8 | 15.2.62.5    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:02:42 | 15.2.63.2    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:08:C6 | 15.2.64.4    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:0E:37 | 15.2.64.3    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:0E:D8 | 15.2.7.5     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:12:3C | 15.2.64.1    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:13:6E | 10.58.24.104 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:1D:A3 | 15.2.6.2     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:2A:D3 | 15.2.64.1    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:41:6B | 15.2.63.6    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:5E:1D | 15.2.62.1    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:62:BB | 15.2.7.4     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:68:C2 | 15.2.62.4    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:6B:0E | 15.2.64.6    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:72:36 | 15.2.61.1    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:73:48 | 15.2.63.4    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:77:0B | 15.2.7.3     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:7E:45 | 15.2.61.3    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:7E:F3 | 15.2.7.2     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:80:63 | 15.2.7.1     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:81:80 | 15.2.62.2    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:8D:98 | 10.58.24.134 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:8D:E9 | 15.2.64.11   | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:8F:CB | 15.2.7.6     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:91:22 | 15.2.6.1     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:94:45 | 10.58.24.106 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   | 10.58.24.99  | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:9F:42 | 10.58.24.103 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   | 10.58.24.98  | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:A8:0A | 15.2.62.3    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:A9:62 | 10.58.24.97  | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:B5:70 | 15.2.63.5    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:BD:72 | 15.2.63.1    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:BE:34 | 15.2.6.3     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:D4:07 | 15.2.64.2    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:D5:AB | 15.2.7.1     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:E3:FD | 10.58.24.102 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:E7:5B | 10.58.24.105 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| LV | 00:50:56:B2:EC:C0 | 15.2.6.6     | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:ED:D0 | 10.58.24.101 | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 00:50:56:B2:FD:8B | 15.2.61.2    | pod-1 node-206 eth1/1 (UCSB1-FI-A_PolGrp) | 
|    |                   |              | pod-1 node-205 eth1/1 (UCSB1-FI-A_PolGrp) | 
+----+-------------------+--------------+-------------------------------------------+
| L  | 3C:FD:FE:E2:EE:D8 | 10.58.24.130 | pod-1 node-205 eth1/16                    | 
+----+-------------------+--------------+-------------------------------------------+
Interface context: ep
```

Developer

```
# iserver get aci ep --apic apic11 --node 205 --view fabric

{
    "duration": 32494,
    "apic": {
        "read": true,
        "success": 63,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 62,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 30572,
        "total_time": 30954
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
    }
}

Log: apic
----------

True	382	-	connect apic11o.emea-sp.cisco.com
True	556	323	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	836	530	apic11o.emea-sp.cisco.com class fabricPathEp
True	3706	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	354	11	apic11o.emea-sp.cisco.com class fabricNode
True	416	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=206&target-path=AccBaseGrpToEthIf
True	410	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=205&target-path=AccBaseGrpToEthIf
True	402	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	419	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	406	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	417	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	423	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	410	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	415	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	429	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	452	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	416	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	414	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	418	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	455	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	436	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	434	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	423	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	452	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	439	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	479	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	431	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	417	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	434	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	437	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	446	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	435	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	408	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	415	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	452	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	466	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	451	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	432	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	436	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	420	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod1a-API_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	452	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	436	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod-4a-br-API query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	412	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	422	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-MX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	494	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=302&target-path=AccBaseGrpToEthIf
True	425	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=301&target-path=AccBaseGrpToEthIf
True	441	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	416	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	424	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	445	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	457	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	433	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	406	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	415	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	499	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	441	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	462	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
```

[[Back]](./Endpoint.md)