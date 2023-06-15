# Node Interface - Encapsulated Routed

## Filter by interface id

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc --id eth1/24*

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+------------+-------------+------------+---------+---------+------+
| Node                | Interface  | Admin State | Oper State | Encap   | SR-MPLS | MTU  |
+---------------------+------------+-------------+------------+---------+---------+------+
| pod-1/bl205-eu-spdc | eth1/24.46 | up          | up         | vlan-24 | no      | 9000 | 
| pod-1/bl205-eu-spdc | eth1/24.47 | up          | up         | vlan-20 | no      | 1500 | 
| pod-1/bl205-eu-spdc | eth1/24.48 | up          | up         | vlan-14 | no      | 9000 | 
| pod-1/bl205-eu-spdc | eth1/24.50 | up          | up         | vlan-15 | no      | 9216 | 
| pod-1/bl205-eu-spdc | eth1/24.51 | up          | up         | vlan-23 | no      | 9000 | 
| pod-1/bl205-eu-spdc | eth1/24.52 | up          | up         | vlan-21 | no      | 9000 | 
| pod-1/bl205-eu-spdc | eth1/24.53 | up          | up         | vlan-25 | no      | 9000 | 
| pod-1/bl205-eu-spdc | eth1/24.54 | up          | up         | vlan-11 | no      | 9216 | 
| pod-1/bl205-eu-spdc | eth1/24.55 | up          | up         | vlan-22 | no      | 9000 | 
+---------------------+------------+-------------+------------+---------+---------+------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc --id eth1/24*

{
    "duration": 1549,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 1063,
        "total_time": 1451
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

True	388	-	connect apic11o.emea-sp.cisco.com
True	297	13	apic11o.emea-sp.cisco.com class fabricNode
True	465	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	301	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
```

[[Back]](./InterfaceL3e.md)