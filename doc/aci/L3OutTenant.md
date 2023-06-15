# L3 Out

## Filter by L3 out's tenant

```
# iserver get aci l3out --apic apic11 --tenant common

Apic: apic11 (mode:online, cache:off)

+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| L3Out                     | MPLS | PIM | BGP | OSPF | EIGRP | VRF                     | L3 Domain       |
+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| common/default            | X    | X   | X   | X    | X     | common/default          | Infra-BGP_L3Dom | 
+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| common/Infra_BGP_L3out    | X    | X   | V   | X    | X     | common/Infra_BGP_VRF    | Infra-BGP_L3Dom | 
|                           |      |     |     |      |       |                         |                 | 
+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
| common/Infra_privIP_L3out | X    | X   | V   | X    | X     | common/Infra_privIP_VRF | Infra-BGP_L3Dom | 
|                           |      |     |     |      |       |                         |                 | 
+---------------------------+------+-----+-----+------+-------+-------------------------+-----------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --tenant common

{
    "duration": 1591,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 487,
        "disconnect_time": 0,
        "mo_time": 766,
        "total_time": 1253
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

True	487	-	connect apic11o.emea-sp.cisco.com
True	418	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	348	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)