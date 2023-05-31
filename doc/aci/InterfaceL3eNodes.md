# Node Interface - Encapsulated Routed

## Multiple nodes

```
# iserver get aci intf l3e --apic apic11 --node cl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+--------------+-------------+------------+--------+---------+------+--------------------+
| Node                | Interface    | Admin State | Oper State | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+--------------+-------------+------------+--------+---------+------+--------------------+
| pod-1/cl201-eu-spdc | eth1/107.7   | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/108.504 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/107.8   | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/108.500 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
+---------------------+--------------+-------------+------------+--------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node cl

{
    "duration": 2179,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1580,
        "total_time": 1978
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	318	11	apic11o.emea-sp.cisco.com class fabricNode
True	292	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	299	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	305	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	366	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
```

[[Back]](./InterfaceL3e.md)