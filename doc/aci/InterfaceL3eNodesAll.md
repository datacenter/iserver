# Node Interface - Encapsulated Routed

## All nodes

```
# iserver get aci intf l3e --apic apic11 --node any

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

+---------------------+--------------+-------------+------------+-------------+---------+---------+------+--------------------+
| Node                | Interface    | Admin State | Oper State | Reason      | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+--------------+-------------+------------+-------------+---------+---------+------+--------------------+
| pod-1/bl205-eu-spdc | eth1/24.36   | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.60   | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.62   | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.64   | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.65   | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.66   | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.67   | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.68   | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.71   | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/35.9    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl205-eu-spdc | eth1/36.83   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl206-eu-spdc | eth1/24.38   | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.40   | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.43   | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.44   | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.45   | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.46   | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.47   | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.48   | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| pod-1/bl206-eu-spdc | eth1/24.49   | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| pod-1/bl206-eu-spdc | eth1/35.10   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl206-eu-spdc | eth1/36.74   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/107.7   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/108.504 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/107.8   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/108.500 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl301-eu-spdc | eth1/31.1    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl301-eu-spdc | eth1/32.2    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl301-eu-spdc | eth1/33.47   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl301-eu-spdc | eth1/34.48   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl301-eu-spdc | eth1/35.5    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl301-eu-spdc | eth1/36.6    | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/31.1    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/32.2    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/33.7    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl302-eu-spdc | eth1/34.8    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/rl302-eu-spdc | eth1/35.5    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/rl302-eu-spdc | eth1/36.6    | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/1.21    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/10.10   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/11.11   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/12.12   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/13.13   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/14.14   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/15.15   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/16.16   | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/2.23    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/3.3     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/4.4     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/5.20    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/6.22    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s101-eu-spdc  | eth1/7.7     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/8.8     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s101-eu-spdc  | eth1/9.9     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/1.28    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/10.10   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/11.11   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/12.12   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/13.13   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/14.14   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/15.15   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/16.16   | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/2.27    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/3.3     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/4.4     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/5.29    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/6.26    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| pod-1/s102-eu-spdc  | eth1/7.7     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/8.8     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| pod-1/s102-eu-spdc  | eth1/9.9     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
+---------------------+--------------+-------------+------------+-------------+---------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node any

{
    "duration": 6373,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 5395,
        "total_time": 5797
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

True	402	-	connect apic11o.emea-sp.cisco.com
True	354	11	apic11o.emea-sp.cisco.com class fabricNode
True	296	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	311	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	319	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	350	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	299	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	304	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	291	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	324	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	308	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	330	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	291	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	309	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	357	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	329	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	316	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	307	42	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
```

[[Back]](./InterfaceL3e.md)