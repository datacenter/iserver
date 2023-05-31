# Node Interface - Virtual Port Channel (VPC)

## Multi-APIC

```
# iserver get aci intf vpc --apic dom:milan --node any

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| Apic   | Node                 | VPC Domain Id | Oper Role | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+--------+----------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| apic11 | pod-1/bl205-eu-spdc  | 105           | master    | configured-master,vpcs-reinited | up         | pass         | 5/5           | 5/5            | 
| apic11 | pod-1/bl206-eu-spdc  | 105           | slave     | vpcs-reinited                   | up         | pass         | 5/5           | 5/5            | 
| apic11 | pod-1/cl201-eu-spdc  | 100           | master    | configured-master,vpcs-reinited | up         | pass         | 27/28         | 25/28          | 
| apic11 | pod-1/cl202-eu-spdc  | 100           | slave     | vpcs-reinited                   | up         | pass         | 25/28         | 27/28          | 
| apic11 | pod-1/rl301-eu-spdc  | 300           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| apic11 | pod-1/rl302-eu-spdc  | 300           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
| apic21 | pod-1/bl2205-eu-spdc | 256           | master    | configured-master,vpcs-reinited | up         | pass         | 5/6           | 5/6            | 
| apic21 | pod-1/bl2206-eu-spdc | 256           | slave     | vpcs-reinited                   | up         | pass         | 5/6           | 5/6            | 
| apic21 | pod-1/cl2201-eu-spdc | 212           | master    | configured-master,vpcs-reinited | up         | pass         | 1/2           | 1/2            | 
| apic21 | pod-1/cl2202-eu-spdc | 212           | slave     | vpcs-reinited                   | up         | pass         | 1/2           | 1/2            | 
| apic21 | pod-1/cl2207-eu-spdc | 278           | master    | configured-master,vpcs-reinited | up         | pass         | 6/8           | 6/8            | 
| apic21 | pod-1/cl2208-eu-spdc | 278           | slave     | vpcs-reinited                   | up         | pass         | 6/8           | 6/8            | 
| apic21 | pod-1/rl2701-eu-spdc | 227           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| apic21 | pod-1/rl2702-eu-spdc | 227           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
+--------+----------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic dom:milan --node any

{
    "duration": 12012,
    "apic": {
        "read": true,
        "success": 36,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 34,
        "connect_time": 802,
        "disconnect_time": 0,
        "mo_time": 10841,
        "total_time": 11643
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	394	-	connect apic21o.emea-sp.cisco.com
True	327	11	apic11o.emea-sp.cisco.com class fabricNode
True	314	13	apic21o.emea-sp.cisco.com class fabricNode
True	300	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	309	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	301	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	308	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	303	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	304	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	346	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	320	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	311	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	333	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	307	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	335	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	331	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
True	392	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/vpcDom
True	313	6	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205/sys/vpc/inst/dom-256 query query-target=children&target-subtree-class=vpcIf
True	335	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/vpcDom
True	291	6	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206/sys/vpc/inst/dom-256 query query-target=children&target-subtree-class=vpcIf
True	322	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/vpcDom
True	315	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201/sys/vpc/inst/dom-212 query query-target=children&target-subtree-class=vpcIf
True	293	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/vpcDom
True	305	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202/sys/vpc/inst/dom-212 query query-target=children&target-subtree-class=vpcIf
True	345	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/vpcDom
True	331	8	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207/sys/vpc/inst/dom-278 query query-target=children&target-subtree-class=vpcIf
True	346	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/vpcDom
True	338	8	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208/sys/vpc/inst/dom-278 query query-target=children&target-subtree-class=vpcIf
True	288	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/vpcDom
True	335	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701/sys/vpc/inst/dom-227 query query-target=children&target-subtree-class=vpcIf
True	335	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/vpcDom
True	294	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702/sys/vpc/inst/dom-227 query query-target=children&target-subtree-class=vpcIf
True	335	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/vpcDom
True	299	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/vpcDom
```

[[Back]](./InterfaceVpc.md)