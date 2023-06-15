# Node Interface - Encapsulated Routed

## Filter by operational state

```
# iserver get aci intf l3e --apic apic11 --node any --oper down

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
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
    "duration": 6968,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 6194,
        "total_time": 6586
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

True	392	-	connect apic11o.emea-sp.cisco.com
True	290	13	apic11o.emea-sp.cisco.com class fabricNode
True	294	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	299	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	294	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	292	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	286	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	287	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	290	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	296	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	274	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	280	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4If
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	285	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4If
True	287	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	292	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	333	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	294	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	344	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	308	44	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	294	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	288	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
```

[[Back]](./InterfaceL3e.md)