# Node Interface - Port Channel (PC)

## Filter by port channel state

```
# iserver get aci intf pc --apic apic11 --node any --state down

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

+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Node                | Id   | Name                 | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po3  | pod1a-NVBench_PolGrp | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po1  | pod1a-NVBench_PolGrp | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po8  | pod1a-MX_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po16 | pod4a-MX_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node any --state down

{
    "duration": 5045,
    "apic": {
        "read": true,
        "success": 16,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 15,
        "connect_time": 377,
        "disconnect_time": 0,
        "mo_time": 4476,
        "total_time": 4853
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

True	377	-	connect apic11o.emea-sp.cisco.com
True	293	13	apic11o.emea-sp.cisco.com class fabricNode
True	344	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	298	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	329	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	276	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	302	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	332	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	277	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	301	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	281	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	272	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	286	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	286	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	318	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	281	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)