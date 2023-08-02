# L3 Out

## Filter by L3 out's tenant

```
# iserver get aci l3out --apic apic11 --tenant common

Apic: apic11 (mode:online, cache:off)

L3Out [#3]
----------

+---------+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| Faults  | L3Out                     | MPLS | PIM | BGP | OSPF | EIGRP | VRF                     | L3 Domain       |
+---------+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| 0 0 0 0 | common/default            | X    | X   | X   | X    | X     | common/default          | Infra-BGP_L3Dom | 
+---------+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| 0 0 0 0 | common/Infra_BGP_L3out    | X    | X   | V   | X    | X     | common/Infra_BGP_VRF    | Infra-BGP_L3Dom | 
+---------+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| 0 0 0 0 | common/Infra_privIP_L3out | X    | X   | V   | X    | X     | common/Infra_privIP_VRF | Infra-BGP_L3Dom | 
+---------+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --tenant common

{
    "duration": 2408,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 455,
        "disconnect_time": 0,
        "mo_time": 1787,
        "total_time": 2242
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

True	455	-	connect apic11o.emea-sp.cisco.com:443
True	1415	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	372	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)