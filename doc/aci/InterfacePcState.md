# Node Interface - Port Channel (PC)

## Filter by port channel state

```
# iserver get aci intf pc --apic apic11 --node any --state down

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

+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Node                | Id   | Name                 | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po12 | pod1a-NVBench_PolGrp | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po13 | pod4a-MX_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po24 | pod1a-MX_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po25 | pod1a-NVBench_PolGrp | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node any --state down

{
    "duration": 5684,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 483,
        "disconnect_time": 0,
        "mo_time": 4804,
        "total_time": 5287
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

True	483	-	connect apic11o.emea-sp.cisco.com
True	356	11	apic11o.emea-sp.cisco.com class fabricNode
True	396	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	418	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	508	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	422	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	340	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	359	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	308	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	337	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	378	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	322	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	340	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	320	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)