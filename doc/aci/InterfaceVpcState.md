# Node Interface - Virtual Port Channel (VPC)

## Filter by peer state

```
# iserver get aci intf vpc --apic apic11 --node any --state up

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
    "duration": 5153,
    "apic": {
        "read": true,
        "success": 16,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 15,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 4578,
        "total_time": 4987
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	309	11	apic11o.emea-sp.cisco.com class fabricNode
True	297	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	281	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	292	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	284	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	291	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	325	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	314	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	308	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	333	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	332	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	306	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	326	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)