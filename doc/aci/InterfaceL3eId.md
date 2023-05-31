# Node Interface - Encapsulated Routed

## Filter by interface id

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc --id eth1/36.83

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
| Node                | Interface  | Admin State | Oper State | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
| pod-1/bl205-eu-spdc | eth1/36.83 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc --id eth1/36.83

{
    "duration": 1475,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 940,
        "total_time": 1326
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

True	386	-	connect apic11o.emea-sp.cisco.com
True	316	11	apic11o.emea-sp.cisco.com class fabricNode
True	310	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	314	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
```

[[Back]](./InterfaceL3e.md)