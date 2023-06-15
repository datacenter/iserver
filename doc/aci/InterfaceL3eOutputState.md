# Node Interface - Encapsulated Routed

## Default state output

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+------------+-------------+------------+---------+---------+------+--------------------+
| Node                | Interface  | Admin State | Oper State | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+------------+-------------+------------+---------+---------+------+--------------------+
| pod-1/bl205-eu-spdc | eth1/24.46 | up          | up         | vlan-24 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.47 | up          | up         | vlan-20 | no      | 1500 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.48 | up          | up         | vlan-14 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.50 | up          | up         | vlan-15 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.51 | up          | up         | vlan-23 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.52 | up          | up         | vlan-21 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.53 | up          | up         | vlan-25 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.54 | up          | up         | vlan-11 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.55 | up          | up         | vlan-22 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/35.9  | up          | up         | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl205-eu-spdc | eth1/36.10 | up          | up         | vlan-2  | no      | 9366 | lo0                | 
+---------------------+------------+-------------+------------+---------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc

{
    "duration": 1402,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 890,
        "total_time": 1286
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

True	396	-	connect apic11o.emea-sp.cisco.com
True	305	13	apic11o.emea-sp.cisco.com class fabricNode
True	285	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	300	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
```

[[Back]](./InterfaceL3e.md)