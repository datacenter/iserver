# Endpoint

## Fabric specific output

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24 --view fabric

Apic: apic11

+----+-------------------+---------------+--------------------------------------------------+
| SF | MAC Address       | IP Address    | Fabric                                           |
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:3E | 15.100.100.62 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:3F | 15.100.100.63 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:40 | 15.100.100.64 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:41 | 15.100.100.65 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:42 | 15.100.100.66 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:43 | 15.100.100.67 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:44 | 15.100.100.68 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:47 | 15.100.100.71 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:52 | 15.100.100.82 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:53 | 15.100.100.83 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:54 | 15.100.100.84 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:55 | 15.100.100.85 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:56 | 15.100.100.86 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:57 | 15.100.100.87 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:58 | 15.100.100.88 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:5B | 15.100.100.91 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:5C | 15.100.100.92 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:69:DE:1D | 15.100.100.80 | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:A2:04:47 | 15.100.100.2  | pod-1 node-202 eth1/56 (pod4a-AIO-3-PET_PolGrp)  | 
|    |                   |               | pod-1 node-201 eth1/56 (pod4a-AIO-3-PET_PolGrp)  | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:A6:8C:AC | 15.100.100.1  | pod-1 node-202 eth1/53 (pod4a-AIO-2-PET_PolGrp)  | 
|    |                   |               | pod-1 node-201 eth1/53 (pod4a-AIO-2-PET_PolGrp)  | 
+----+-------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:BA:5C:58 | 15.100.100.70 | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------------------------------+
Interface context: ep
```

Developer

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24 --view fabric

{
    "duration": 9116,
    "apic": {
        "read": true,
        "success": 13,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 12,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 8381,
        "total_time": 8781
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	546	322	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	355	530	apic11o.emea-sp.cisco.com class fabricPathEp
True	3659	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	338	11	apic11o.emea-sp.cisco.com class fabricNode
True	422	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	431	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	407	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	406	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	496	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	434	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	427	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
```

[[Back]](./Endpoint.md)