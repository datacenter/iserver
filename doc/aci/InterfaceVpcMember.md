# Node Interface - Virtual Port Channel (VPC)

## Filter by member state

Example: up

```
# iserver get aci intf vpc --apic apic11 --node any --member up

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
| pod-1/rl301-eu-spdc | 300           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| pod-1/rl302-eu-spdc | 300           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Example: down

```
# iserver get aci intf vpc --apic apic11 --node any --member down --empty

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
| pod-1/cl201-eu-spdc | 100           | master    | configured-master,vpcs-reinited | up         | pass         | 27/28         | 25/28          | 
| pod-1/cl202-eu-spdc | 100           | slave     | vpcs-reinited                   | up         | pass         | 25/28         | 27/28          | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic11 --node any --member up

{
    "duration": 6728,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 545,
        "disconnect_time": 0,
        "mo_time": 6004,
        "total_time": 6549
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

True	545	-	connect apic11o.emea-sp.cisco.com
True	532	13	apic11o.emea-sp.cisco.com class fabricNode
True	437	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	484	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	421	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	450	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	446	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	305	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	271	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	302	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	320	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/vpcDom
True	276	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/vpcDom
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	285	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	296	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	292	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	308	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	292	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)