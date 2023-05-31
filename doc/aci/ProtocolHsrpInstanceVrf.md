# Node Protocol - HSRP

## Show HSRP selected VRF domains for selected nodes

```
# iserver get aci proto hsrp --apic apic11 --node rl --vrf *mpc* --view vrf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+------------+
| Node                | VRF                            | Interfaces |
+---------------------+--------------------------------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 0          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 0          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 0          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 0          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 0          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 0          | 
+---------------------+--------------------------------+------------+
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node rl --vrf *mpc* --view vrf

{
    "duration": 2706,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 2095,
        "total_time": 2505
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

True	410	-	connect apic11o.emea-sp.cisco.com
True	313	11	apic11o.emea-sp.cisco.com class fabricNode
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=hsrpEntity
True	302	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpDom
True	306	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=hsrpEntity
True	283	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpDom
True	307	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolHsrp.md)