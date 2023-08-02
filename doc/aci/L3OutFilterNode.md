# L3 Out

## Filter by L3 out's border leaf ID

```
# iserver get aci l3out --apic apic11 --node 301

Apic: apic11 (mode:online, cache:off)

L3Out - Node [#8]
-----------------

+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| Faults  | L3Out                         | MPLS | PIM | BGP | OSPF | EIGRP | Border Leaf             | Router ID       | Loopback |
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | ECMP-demo/L3OUT-ACC_L3out     | X    | X   | V   | X    | X     | topology/pod-1/node-301 | 31.31.31.1      | yes      | 
|         |                               |      |     |     |      |       | topology/pod-1/node-302 | 32.32.32.1      | yes      | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | ECMP-demo/L3OUT-INT_L3out     | X    | X   | V   | X    | X     | topology/pod-1/node-301 | 31.31.31.2      | yes      | 
|         |                               |      |     |     |      |       | topology/pod-1/node-302 | 32.32.32.2      | yes      | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 1 | infra/RDC-3_SRL3out           | V    | X   | V   | X    | X     | topology/pod-1/node-302 | 132.132.132.132 | no       | 
|         |                               |      |     |     |      |       | topology/pod-1/node-301 | 131.131.131.131 | no       | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | infra/RL-L3Out                | X    | X   | V   | V    | X     | topology/pod-1/node-301 | 131.131.131.131 | yes      | 
|         |                               |      |     |     |      |       | topology/pod-1/node-302 | 132.132.132.132 | yes      | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | MPC-E/MPC-E-Residential-IN    | X    | X   | X   | X    | X     | topology/pod-1/node-301 | 131.131.131.131 | yes      | 
|         |                               |      |     |     |      |       | topology/pod-1/node-302 | 132.132.132.132 | yes      | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | MPC-E/MPC-E-sPBR-IN           | X    | X   | X   | X    | X     | topology/pod-1/node-301 | 131.131.131.131 | yes      | 
|         |                               |      |     |     |      |       | topology/pod-1/node-302 | 132.132.132.132 | yes      | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | MPC-E/MPC-E-sPBR-OUT          | X    | X   | V   | X    | X     | topology/pod-1/node-302 | 132.132.132.132 | no       | 
|         |                               |      |     |     |      |       | topology/pod-1/node-301 | 131.131.131.131 | no       | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC_L3Out | X    | X   | V   | X    | X     | topology/pod-1/node-301 | 1.1.1.3         | no       | 
|         |                               |      |     |     |      |       | topology/pod-1/node-302 | 1.1.1.4         | no       | 
+---------+-------------------------------+------+-----+-----+------+-------+-------------------------+-----------------+----------+
```

Developer

```
# iserver get aci l3out --apic apic11 --node 301

{
    "duration": 1506,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 449,
        "disconnect_time": 0,
        "mo_time": 860,
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

True	449	-	connect apic11o.emea-sp.cisco.com:443
True	477	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	383	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)