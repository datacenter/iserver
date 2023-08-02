# L3 Out

## Filter by L3 out's name

Example: name

```
# iserver get aci l3out --apic apic11 --name Calico*

Apic: apic11 (mode:online, cache:off)

L3Out [#4]
----------

+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| Faults  | L3Out                         | MPLS | PIM | BGP | OSPF | EIGRP | VRF                        | L3 Domain                     |
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_L3Out     | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_VRF1     | SPIN_InnoLab_Calico_L3Dom     | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC3      | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF |                               | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC_L3Out | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF | SPIN_InnoLab_Calico_RDC_L3Dom | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_SRL3Out   | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_VRF1     |                               | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
```

Example: tenant and name

```
# iserver get aci l3out --apic apic11 --name SPIN*/Calico*

Apic: apic11 (mode:online, cache:off)

L3Out [#4]
----------

+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| Faults  | L3Out                         | MPLS | PIM | BGP | OSPF | EIGRP | VRF                        | L3 Domain                     |
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_L3Out     | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_VRF1     | SPIN_InnoLab_Calico_L3Dom     | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC3      | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF |                               | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC_L3Out | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF | SPIN_InnoLab_Calico_RDC_L3Dom | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_SRL3Out   | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_VRF1     |                               | 
+---------+-------------------------------+------+-----+-----+------+-------+----------------------------+-------------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --name Calico*

{
    "duration": 2423,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 474,
        "disconnect_time": 0,
        "mo_time": 1792,
        "total_time": 2266
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

True	474	-	connect apic11o.emea-sp.cisco.com:443
True	446	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	1346	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)