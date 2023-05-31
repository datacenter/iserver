# Node Interface - Port Channel (PC)

## All nodes

```
# iserver get aci intf pc --apic apic11 --node any

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

+---------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Node                | Id   | Name                     | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+---------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| pod-1/bl205-eu-spdc | po1  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po2  | SPN_PolGrp               | up    | enabled   | up    |                           | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po3  | UCSB1-FI-B_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po4  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po5  | UCSB1-FI-A_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po1  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po2  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po3  | UCSB1-FI-B_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po4  | UCSB1-FI-A_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po5  | SPN_PolGrp               | up    | enabled   | up    |                           | active    | 105        | 1            | 
| pod-1/cl201-eu-spdc | po1  | pod-4a-br-API            | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po2  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po3  | pod4a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po4  | pod1a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po5  | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po6  | pod4a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po7  | pod4a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po8  | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po9  | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po10 | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po11 | pod4a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po12 | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl201-eu-spdc | po13 | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po14 | pod4a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po15 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po16 | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po17 | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po18 | pod4a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po19 | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po20 | pod4a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po21 | pod4a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po22 | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po23 | pod4a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po24 | pod4a-COMP-3-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po25 | pod4a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po26 | pod4a-COMP-3-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po27 | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po28 | pod4a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po1  | pod4a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po2  | pod4a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po3  | pod4a-COMP-3-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po4  | pod4a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po5  | pod4a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po6  | pod4a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po7  | pod4a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po8  | pod4a-COMP-3-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po9  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po10 | pod4a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po11 | pod4a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po12 | pod4a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po13 | pod4a-MX_PolGrp          | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po14 | pod-4a-br-API            | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po15 | pod4a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po16 | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po17 | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po18 | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po19 | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po20 | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po21 | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po22 | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po23 | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po24 | pod1a-MX_PolGrp          | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po25 | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po26 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po27 | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl202-eu-spdc | po28 | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/rl301-eu-spdc | po1  | UCSB1-R3DC-FI-A_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| pod-1/rl301-eu-spdc | po2  | UCSB1-R3DC-FI-B_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| pod-1/rl302-eu-spdc | po1  | UCSB1-R3DC-FI-B_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| pod-1/rl302-eu-spdc | po2  | UCSB1-R3DC-FI-A_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
+---------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node any

{
    "duration": 8216,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 7137,
        "total_time": 7545
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	318	11	apic11o.emea-sp.cisco.com class fabricNode
True	365	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	296	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	300	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	354	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	340	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	289	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	384	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	302	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	419	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	388	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	373	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	388	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	314	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	306	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	337	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	340	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	357	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	325	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	341	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	301	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)