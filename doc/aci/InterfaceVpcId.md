# Node Interface - Virtual Port Channel (VPC)

## Filter by domain id

```
# iserver get aci intf vpc --apic apic11 --node any --id 100

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
# iserver get aci intf vpc --apic apic11 --node any --id 100

{
    "duration": 4100,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 3533,
        "total_time": 3930
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	313	11	apic11o.emea-sp.cisco.com class fabricNode
True	289	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	298	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	292	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	318	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	312	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	322	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	302	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	328	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	408	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	351	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)