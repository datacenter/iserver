# L3 Out

## Filter MPLS-enabled L3 outs

```
# iserver get aci l3out --apic apic11 --mpls

Apic: apic11 (mode:online, cache:off)

L3Out - MPLS [#10]
------------------

+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| Faults  | L3Out                              | Tenant | PIM | BGP                            | VRF                     | Border Leaf     |
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | ECMP-demo/MPC-demo_CDDC-2_L3out    | V      | X   | ECMP-demo/ACC_VRF              |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | infra/CDC-2_SRL3out                | V      | V   | infra/overlay-1                | topology/pod-1/node-205 | 125.125.125.125 | 
|         |                                    |        |     |                                | topology/pod-1/node-206 | 126.126.126.126 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 1 | infra/RDC-3_SRL3out                | V      | V   | infra/overlay-1                | topology/pod-1/node-302 | 132.132.132.132 | 
|         |                                    |        |     |                                | topology/pod-1/node-301 | 131.131.131.131 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | MPC-E/CU-DU-Infra-SR-Backbone      | V      | X   | MPC-E/CU-DU-Infra_VRF          |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | MPC-E/MPC-Residential-R3DC_SRL3out | V      | X   | MPC-E/MPC-Residential-R3DC_VRF |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | MPC/MPC-sPBR-IN_SRL3out            | V      | X   | MPC/MPC-sPBR-IN_VRF            |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | NXOS-HandOff_Test/SR_CORE          | V      | X   | NXOS-HandOff_Test/default      |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC3           | V      | X   | SPIN_InnoLab/SPIN_RDC3_VRF     |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_SRL3Out        | V      | X   | SPIN_InnoLab/SPIN_VRF1         |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| 0 0 0 0 | UC3-CL2023-Demo/SR_Backbone        | V      | X   | UC3-CL2023-Demo/default        |                         |                 | 
+---------+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --mpls

{
    "duration": 1498,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 475,
        "disconnect_time": 0,
        "mo_time": 834,
        "total_time": 1309
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

True	475	-	connect apic11o.emea-sp.cisco.com:443
True	465	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	369	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)