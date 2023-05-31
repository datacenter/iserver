# Node Interface - Virtual Port Channel (VPC)

## Single node

```
# iserver get aci intf vpc --apic apic11 --node cl201-eu-spdc

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| Node                | VPC Domain Id | Oper Role | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| pod-1/cl201-eu-spdc | 100           | master    | configured-master,vpcs-reinited | up         | pass         | 27/28         | 25/28          | 
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic11 --node cl201-eu-spdc

{
    "duration": 1439,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 914,
        "total_time": 1324
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

True	410	-	connect apic11o.emea-sp.cisco.com
True	309	11	apic11o.emea-sp.cisco.com class fabricNode
True	306	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	299	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfaceVpc.md)