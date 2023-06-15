# Node Interface - Virtual Port Channel (VPC)

## Multiple nodes

```
# iserver get aci intf vpc --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
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
    "duration": 1975,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 384,
        "disconnect_time": 0,
        "mo_time": 1468,
        "total_time": 1852
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

True	384	-	connect apic11o.emea-sp.cisco.com
True	295	13	apic11o.emea-sp.cisco.com class fabricNode
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	308	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	291	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	287	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfaceVpc.md)