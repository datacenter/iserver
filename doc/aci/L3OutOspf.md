# L3 Out

## Filter OSPF-enabled L3 outs

```
# iserver get aci l3out --apic apic11 --ospf

Apic: apic11 (mode:online, cache:off)

+---------------------+-------------+------+----------+-----------+-----------+----------------------------+-----------------------+-------------------------+-------------------------+-----------------+
| L3Out               | Target DSCP | OSPF | Area ID  | Area Type | Area Cost | Redistribute LSA into NSSA | Originate Summary LSA | Suppress translated LSA | Border Leaf             | Router ID       |
+---------------------+-------------+------+----------+-----------+-----------+----------------------------+-----------------------+-------------------------+-------------------------+-----------------+
| infra/multipodL3Out | unspecified | V    | backbone | regular   | 1         | V                          | V                     | X                       | topology/pod-1/node-101 | 101.101.101.101 | 
|                     |             |      |          |           |           |                            |                       |                         | topology/pod-1/node-102 | 102.102.102.102 | 
+---------------------+-------------+------+----------+-----------+-----------+----------------------------+-----------------------+-------------------------+-------------------------+-----------------+
| infra/RL-L3Out      | unspecified | V    | backbone | regular   | 1         | V                          | V                     | X                       | topology/pod-1/node-301 | 131.131.131.131 | 
|                     |             |      |          |           |           |                            |                       |                         | topology/pod-1/node-302 | 132.132.132.132 | 
+---------------------+-------------+------+----------+-----------+-----------+----------------------------+-----------------------+-------------------------+-------------------------+-----------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --ospf

{
    "duration": 1496,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 429,
        "disconnect_time": 0,
        "mo_time": 785,
        "total_time": 1214
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

True	429	-	connect apic11o.emea-sp.cisco.com
True	425	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	360	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)