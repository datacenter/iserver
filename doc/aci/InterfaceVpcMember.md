# Node Interface - Virtual Port Channel (VPC)

## Filter by member state

Example: up

```
# iserver get aci intf vpc --apic apic11 --node any --member up

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
| pod-1/rl301-eu-spdc | 300           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| pod-1/rl302-eu-spdc | 300           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Example: down

```
# iserver get aci intf vpc --apic apic11 --node any --member down --empty

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
| pod-1/cl201-eu-spdc | 100           | master    | configured-master,vpcs-reinited | up         | pass         | 27/28         | 25/28          | 
| pod-1/cl202-eu-spdc | 100           | slave     | vpcs-reinited                   | up         | pass         | 25/28         | 27/28          | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic11 --node any --member up

{
    "duration": 5501,
    "apic": {
        "read": true,
        "success": 16,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 15,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 4910,
        "total_time": 5311
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

True	401	-	connect apic11o.emea-sp.cisco.com
True	317	11	apic11o.emea-sp.cisco.com class fabricNode
True	307	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	303	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	283	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	322	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	327	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	348	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	335	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	363	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	323	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	371	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	295	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	411	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	311	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	294	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)