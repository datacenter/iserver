# L3 Out

## Filter by L3 out's border leaf ID

```
# iserver get aci l3out --apic apic11 --node 301

Apic: apic11

+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| L3Out                         | MPLS | PIM | BGP | OSPF | EIGRP | Border Leaf             | Router ID       | Loopback |
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| ECMP-demo/L3OUT-ACC_L3out     | X    | X   | V   | X    | X     | topology/pod-1/node-301 | 31.31.31.1      | yes      | 
|                               |      |     |     |      |       | topology/pod-1/node-302 | 32.32.32.1      | yes      | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| ECMP-demo/L3OUT-INT_L3out     | X    | X   | V   | X    | X     | topology/pod-1/node-302 | 32.32.32.2      | yes      | 
|                               |      |     |     |      |       | topology/pod-1/node-301 | 31.31.31.2      | yes      | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| infra/RDC-3_SRL3out           | V    | X   | V   | X    | X     | topology/pod-1/node-302 | 132.132.132.132 | no       | 
|                               |      |     |     |      |       | topology/pod-1/node-301 | 131.131.131.131 | no       | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| infra/RL-L3Out                | X    | X   | V   | V    | X     | topology/pod-1/node-301 | 131.131.131.131 | yes      | 
|                               |      |     |     |      |       | topology/pod-1/node-302 | 132.132.132.132 | yes      | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| MPC-E/MPC-E-Residential-IN    | X    | X   | X   | X    | X     | topology/pod-1/node-302 | 132.132.132.132 | yes      | 
|                               |      |     |     |      |       | topology/pod-1/node-301 | 131.131.131.131 | yes      | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| MPC-E/MPC-E-sPBR-IN           | X    | X   | X   | X    | X     | topology/pod-1/node-301 | 131.131.131.131 | yes      | 
|                               |      |     |     |      |       | topology/pod-1/node-302 | 132.132.132.132 | yes      | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| MPC-E/MPC-E-sPBR-OUT          | X    | X   | V   | X    | X     | topology/pod-1/node-301 | 131.131.131.131 | no       | 
|                               |      |     |     |      |       | topology/pod-1/node-302 | 132.132.132.132 | no       | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| SPIN_InnoLab/Calico_RDC_L3Out | X    | X   | V   | X    | X     | topology/pod-1/node-301 | 1.1.1.3         | no       | 
|                               |      |     |     |      |       | topology/pod-1/node-302 | 1.1.1.4         | no       | 
+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
```

Developer

```
# iserver get aci l3out --apic apic11 --node 301

{
    "duration": 2414,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 1836,
        "total_time": 2226
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

True	390	-	connect apic11o.emea-sp.cisco.com
True	1490	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	346	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)