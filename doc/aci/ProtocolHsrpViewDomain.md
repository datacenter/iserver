# Node Protocol - HSRP

## Inst view

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view dom

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Domain [#10]
----------------------------

+---------------------+-------------------------------+--------+---------+
| Node                | VRF                           | Health | Faults  |
+---------------------+-------------------------------+--------+---------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 100    | 0 0 0 0 | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 100    | 0 0 0 0 | 
+---------------------+-------------------------------+--------+---------+
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view dom

{
    "duration": 3165,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 1740,
        "total_time": 2146
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

True	406	-	connect apic11o.emea-sp.cisco.com:443
True	1297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	443	10	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/hsrpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolHsrp.md)