# Node Interface - Virtual Port Channel (VPC)

## Filter by peer state

```
# iserver get aci intf vpc --apic apic11 --node any --state up

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
# iserver get aci intf vpc --apic apic11 --node any --state up

{
    "duration": 5564,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 4979,
        "total_time": 5367
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
True	284	13	apic11o.emea-sp.cisco.com class fabricNode
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	310	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	299	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	305	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	294	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	311	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	287	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	288	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/vpcDom
True	280	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/vpcDom
True	295	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	284	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	318	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	300	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	283	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	281	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)