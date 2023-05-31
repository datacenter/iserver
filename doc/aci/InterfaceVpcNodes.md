# Node Interface - Virtual Port Channel (VPC)

## Multiple nodes

```
# iserver get aci intf vpc --apic apic11 --node rl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| Node                | VPC Domain Id | Oper Role | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| pod-1/rl301-eu-spdc | 300           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| pod-1/rl302-eu-spdc | 300           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic11 --node rl

{
    "duration": 2075,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 1546,
        "total_time": 1950
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

True	404	-	connect apic11o.emea-sp.cisco.com
True	304	11	apic11o.emea-sp.cisco.com class fabricNode
True	294	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	345	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	303	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	300	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfaceVpc.md)