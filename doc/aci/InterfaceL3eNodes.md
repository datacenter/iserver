# Node Interface - Encapsulated Routed

## Multiple nodes

```
# iserver get aci intf l3e --apic apic11 --node cl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc

+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
| Node                | Interface  | Admin State | Oper State | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
| pod-1/cl201-eu-spdc | eth1/107.7 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/108.8 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/107.7 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/108.8 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl209-eu-spdc | eth1/35.9  | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl210-eu-spdc | eth1/36.9  | up          | up         | vlan-2 | no      | 9366 | lo0                | 
+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node cl

{
    "duration": 3232,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 2640,
        "total_time": 3044
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

True	404	-	connect apic11o.emea-sp.cisco.com
True	306	13	apic11o.emea-sp.cisco.com class fabricNode
True	283	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	302	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	294	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	322	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	291	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4If
True	285	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	277	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4If
```

[[Back]](./InterfaceL3e.md)