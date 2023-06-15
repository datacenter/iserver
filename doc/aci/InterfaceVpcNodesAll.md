# Node Interface - Virtual Port Channel (VPC)

## All nodes

```
# iserver get aci intf vpc --apic apic11 --node any

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

+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| Node                | VPC Domain Id | Oper Role | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| pod-1/bl205-eu-spdc | 105           | master    | configured-master,vpcs-reinited | up         | pass         | 5/5           | 5/5            | 
| pod-1/bl206-eu-spdc | 105           | slave     | vpcs-reinited                   | up         | pass         | 5/5           | 5/5            | 
| pod-1/cl201-eu-spdc | 100           | master    | configured-master,vpcs-reinited | up         | pass         | 27/28         | 25/28          | 
| pod-1/cl202-eu-spdc | 100           | slave     | vpcs-reinited                   | up         | pass         | 25/28         | 27/28          | 
| pod-1/rl301-eu-spdc | 300           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| pod-1/rl302-eu-spdc | 300           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic11 --node any

{
    "duration": 5677,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 5061,
        "total_time": 5470
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	317	13	apic11o.emea-sp.cisco.com class fabricNode
True	284	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	294	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	288	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	290	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	284	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	316	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	275	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	291	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	294	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/vpcDom
True	279	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/vpcDom
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	282	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	349	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	313	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	308	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	317	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)