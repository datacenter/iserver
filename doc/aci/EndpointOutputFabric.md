# Endpoint

## Fabric specific output

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24 --view fabric

Apic: apic11 (mode:online, cache:off)

+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| SF | MAC Address       | IP Address    | EPG                      | Encapsulation | Fabric                                           |
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:3E | 15.100.100.62 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:3F | 15.100.100.63 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:40 | 15.100.100.64 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:41 | 15.100.100.65 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:42 | 15.100.100.66 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:43 | 15.100.100.67 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:44 | 15.100.100.68 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:47 | 15.100.100.71 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:52 | 15.100.100.82 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:53 | 15.100.100.83 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:54 | 15.100.100.84 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:55 | 15.100.100.85 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:56 | 15.100.100.86 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:57 | 15.100.100.87 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:58 | 15.100.100.88 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:5B | 15.100.100.91 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | 02:42:0F:64:64:5C | 15.100.100.92 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:69:DE:1D | 15.100.100.80 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/62 (pod4a-COMP-2-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:A2:04:47 | 15.100.100.2  | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-201 eth1/56 (pod4a-AIO-3-PET_PolGrp)  | 
|    |                   |               |                          |               | pod-1 node-202 eth1/56 (pod4a-AIO-3-PET_PolGrp)  | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:A6:8C:AC | 15.100.100.1  | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/53 (pod4a-AIO-2-PET_PolGrp)  | 
|    |                   |               |                          |               | pod-1 node-201 eth1/53 (pod4a-AIO-2-PET_PolGrp)  | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
| L  | FA:16:3E:BA:5C:58 | 15.100.100.70 | smi5Gc-cvim4-Control-SBI | 2704          | pod-1 node-202 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
|    |                   |               |                          |               | pod-1 node-201 eth1/59 (pod4a-COMP-1-PET_PolGrp) | 
+----+-------------------+---------------+--------------------------+---------------+--------------------------------------------------+
Interface context: ep
```

Developer

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24 --view fabric

{
    "duration": 10450,
    "apic": {
        "read": true,
        "success": 13,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 12,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 9598,
        "total_time": 10006
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

True	408	-	connect apic11o.emea-sp.cisco.com:443
True	1380	358	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	375	602	apic11o.emea-sp.cisco.com:443 class fabricPathEp
True	3797	37	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	334	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	479	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	506	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	429	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	462	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	507	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	499	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
True	415	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=202&target-path=AccBaseGrpToEthIf
True	415	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp query rsp-subtree-include=full-deployment&target-node=201&target-path=AccBaseGrpToEthIf
```

[[Back]](./Endpoint.md)