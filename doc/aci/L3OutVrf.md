# L3 Out

## Filter by L3 out's VRF

```
# iserver get aci l3out --apic apic11 --vrf MPC-E/*

Apic: apic11 (mode:online, cache:off)

+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| L3Out                              | MPLS | PIM | BGP | OSPF | EIGRP | VRF                            | L3 Domain   |
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| MPC-E/CU-DU-Infra-SR-Backbone      | V    | X   | X   | X    | X     | MPC-E/CU-DU-Infra_VRF          |             | 
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| MPC-E/MPC-E-OUT                    | X    | X   | X   | X    | X     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom | 
|                                    |      |     |     |      |       |                                |             | 
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| MPC-E/MPC-E-Residential-IN         | X    | X   | X   | X    | X     | MPC-E/MPC-Residential-R3DC_VRF | Infra_L3Dom | 
|                                    |      |     |     |      |       |                                |             | 
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| MPC-E/MPC-E-sPBR-IN                | X    | X   | X   | X    | X     | MPC-E/MPC-E-sPBR-IN_VRF        | Infra_L3Dom | 
|                                    |      |     |     |      |       |                                |             | 
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| MPC-E/MPC-E-sPBR-OUT               | X    | X   | V   | X    | X     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom | 
|                                    |      |     |     |      |       |                                |             | 
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
| MPC-E/MPC-Residential-R3DC_SRL3out | V    | X   | X   | X    | X     | MPC-E/MPC-Residential-R3DC_VRF |             | 
+------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --vrf MPC-E/*

{
    "duration": 1634,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 477,
        "disconnect_time": 0,
        "mo_time": 857,
        "total_time": 1334
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

True	477	-	connect apic11o.emea-sp.cisco.com
True	428	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	429	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)