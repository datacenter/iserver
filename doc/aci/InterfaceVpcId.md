# Node Interface - Virtual Port Channel (VPC)

## Filter by domain id

```
# iserver get aci intf vpc --apic apic11 --node any --id 100

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
# iserver get aci intf vpc --apic apic11 --node any --id 100

{
    "duration": 4352,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 3796,
        "total_time": 4181
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

True	385	-	connect apic11o.emea-sp.cisco.com
True	297	13	apic11o.emea-sp.cisco.com class fabricNode
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	290	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	357	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	285	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/vpcDom
True	292	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/vpcDom
True	283	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	297	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	284	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	279	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)