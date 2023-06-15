# Node Interface - Encapsulated Routed

## All nodes

```
# iserver get aci intf l3e --apic apic11 --node any

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

+---------------------+------------+-------------+------------+-------------+---------+---------+------+--------------------+
| Node                | Interface  | Admin State | Oper State | Reason      | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+------------+-------------+------------+-------------+---------+---------+------+--------------------+
| pod-1/bl205-eu-spdc | eth1/24.46 | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.47 | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.48 | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.50 | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.51 | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.52 | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.53 | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.54 | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.55 | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl205-eu-spdc | eth1/36.10 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl206-eu-spdc | eth1/24.54 | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.55 | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.56 | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.59 | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.60 | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.61 | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.62 | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.63 | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.64 | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl206-eu-spdc | eth1/36.10 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/107.7 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/108.8 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/107.7 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/108.8 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl209-eu-spdc | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl210-eu-spdc | eth1/36.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl301-eu-spdc | eth1/31.1  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl301-eu-spdc | eth1/32.2  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl301-eu-spdc | eth1/33.7  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl301-eu-spdc | eth1/34.8  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl301-eu-spdc | eth1/35.5  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl301-eu-spdc | eth1/36.6  | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/31.1  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/32.2  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/33.7  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl302-eu-spdc | eth1/34.8  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl302-eu-spdc | eth1/35.5  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/36.6  | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/1.18  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/13.22 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/16.16 | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/2.17  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/5.19  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/6.20  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/7.7   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/8.8   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/1.18  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/13.22 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/16.16 | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/2.17  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/5.19  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/6.20  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/7.7   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/8.8   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
+---------------------+------------+-------------+------------+-------------+---------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node any

{
    "duration": 7351,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 6452,
        "total_time": 6852
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	302	13	apic11o.emea-sp.cisco.com class fabricNode
True	285	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	297	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	331	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	287	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	279	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	307	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	296	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	295	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	285	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	309	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4If
True	298	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	280	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4If
True	287	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	401	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	299	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	348	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	351	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	312	44	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	308	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	295	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
```

[[Back]](./InterfaceL3e.md)