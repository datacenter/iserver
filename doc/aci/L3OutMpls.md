# L3 Out

## Filter MPLS-enabled L3 outs

```
# iserver get aci l3out --apic apic11 --mpls

Apic: apic11

+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| L3Out                              | Tenant | PIM | BGP                            | VRF                     | Border Leaf     |
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| ECMP-demo/MPC-demo_CDDC-2_L3out    | V      | X   | ECMP-demo/ACC_VRF              |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| infra/CDC-2_SRL3out                | V      | V   | infra/overlay-1                | topology/pod-1/node-205 | 125.125.125.125 | 
|                                    |        |     |                                | topology/pod-1/node-206 | 126.126.126.126 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| infra/RDC-3_SRL3out                | V      | V   | infra/overlay-1                | topology/pod-1/node-302 | 132.132.132.132 | 
|                                    |        |     |                                | topology/pod-1/node-301 | 131.131.131.131 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| MPC-E/CU-DU-Infra-SR-Backbone      | V      | X   | MPC-E/CU-DU-Infra_VRF          |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| MPC-E/MPC-Residential-R3DC_SRL3out | V      | X   | MPC-E/MPC-Residential-R3DC_VRF |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| MPC/MPC-sPBR-IN_SRL3out            | V      | X   | MPC/MPC-sPBR-IN_VRF            |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| NXOS-HandOff_Test/SR_CORE          | V      | X   | NXOS-HandOff_Test/default      |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| SPIN_InnoLab/Calico_RDC3           | V      | X   | SPIN_InnoLab/SPIN_RDC3_VRF     |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| SPIN_InnoLab/Calico_SRL3Out        | V      | X   | SPIN_InnoLab/SPIN_VRF1         |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
| UC3-CL2023-Demo/SR_Backbone        | V      | X   | UC3-CL2023-Demo/default        |                         |                 | 
+------------------------------------+--------+-----+--------------------------------+-------------------------+-----------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --mpls

{
    "duration": 1334,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 792,
        "total_time": 1178
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

True	386	-	connect apic11o.emea-sp.cisco.com
True	463	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	329	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)