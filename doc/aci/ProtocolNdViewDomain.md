# Node Protocol - ND

## Inst view

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view dom

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Domain [#25]
--------------------------

+-------------------------------+--------+---------+-----------+
| VRF                           | Health | Faults  | Neighbors |
+-------------------------------+--------+---------+-----------+
| common:Infra_BGP_VRF          | 100    | 0 0 0 0 | 0         | 
| common:Infra_privIP_VRF       | 100    | 0 0 0 0 | 0         | 
| common:Infra_VRF              | 100    | 0 0 0 0 | 0         | 
| common:smi5Gc-cvim1-N3-N4_VRF | 100    | 0 0 0 0 | 0         | 
| common:smi5Gc-cvim1_VRF       | 100    | 0 0 0 0 | 0         | 
| common:smi5Gc-cvim4-N3-N4_VRF | 100    | 0 0 0 0 | 0         | 
| common:smi5Gc-cvim4_VRF       | 100    | 0 0 0 0 | 0         | 
| ECMP-demo:ACC_VRF             | 100    | 0 0 0 0 | 0         | 
| ECMP-demo:INT-ext_VRF         | 100    | 0 0 0 0 | 0         | 
| ECMP-demo:MPC-CDC-2_VRF       | 100    | 0 0 0 0 | 0         | 
| iks-monitoring:iks-mon_VRF    | 100    | 0 0 0 0 | 0         | 
| management                    | 100    | 0 0 0 0 | 0         | 
| mgmt:EU-SPDC-ERSPAN-VRF       | 100    | 0 0 0 0 | 0         | 
| mgmt:inb                      | 100    | 0 0 0 0 | 0         | 
| MPC-E:CU-DU-Infra_VRF         | 100    | 0 0 0 0 | 0         | 
| MPC-E:MPC-E-sPBR-IN_VRF       | 100    | 0 0 0 0 | 0         | 
| MPC-F5T:F5-IN_VRF             | 100    | 0 0 0 0 | 0         | 
| MPC-F5T:F5-OUT_VRF            | 100    | 0 0 0 0 | 0         | 
| MPC:MPC-sPBR-IN_VRF           | 100    | 0 0 0 0 | 0         | 
| MPC:MPC-sPBR-OUT_VRF          | 100    | 0 0 0 0 | 0         | 
| NXOS-HandOff_Test:default     | 100    | 0 0 0 0 | 0         | 
| P5G:P5G_VRF                   | 100    | 0 0 0 0 | 0         | 
| SPIN_InnoLab:SPIN_VRF1        | 100    | 0 0 0 0 | 0         | 
| SPN_IntraLab:SPN_VRF1         | 100    | 0 0 0 0 | 0         | 
| UC3-CL2023-Demo:default       | 100    | 0 0 0 0 | 0         | 
+-------------------------------+--------+---------+-----------+
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view dom

{
    "duration": 1722,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 1154,
        "total_time": 1542
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

True	388	-	connect apic11o.emea-sp.cisco.com:443
True	294	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query query-target=children&rsp-subtree-include=health,fault-count
True	304	25	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	275	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
```

[[Back]](./ProtocolNd.md)