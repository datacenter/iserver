# Node Interface - Encapsulated Routed

## Filter by operational state

```
# iserver get aci intf l3e --apic apic11 --node any --oper down

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+------------+-------------+------------+-------------+--------+---------+------+
| Node                | Interface  | Admin State | Oper State | Reason      | Encap  | SR-MPLS | MTU  |
+---------------------+------------+-------------+------------+-------------+--------+---------+------+
| pod-1/rl301-eu-spdc | eth1/31.1  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl301-eu-spdc | eth1/32.2  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl301-eu-spdc | eth1/35.5  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl302-eu-spdc | eth1/31.1  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl302-eu-spdc | eth1/32.2  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl302-eu-spdc | eth1/35.5  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/13.13 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/7.7   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/8.8   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/13.13 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/7.7   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/8.8   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
+---------------------+------------+-------------+------------+-------------+--------+---------+------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node any --oper down

{
    "duration": 6358,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 441,
        "disconnect_time": 0,
        "mo_time": 5424,
        "total_time": 5865
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

True	441	-	connect apic11o.emea-sp.cisco.com
True	357	11	apic11o.emea-sp.cisco.com class fabricNode
True	300	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	308	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	290	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	380	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	288	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	316	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	299	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	319	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	306	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	302	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	315	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	306	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	295	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	347	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	360	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	336	42	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
```

[[Back]](./InterfaceL3e.md)