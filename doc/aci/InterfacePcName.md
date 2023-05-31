# Node Interface - Port Channel (PC)

## Filter by port channel name

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --name *pod1a*

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Node                | Id   | Name                     | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+---------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po4  | pod1a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po5  | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po8  | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po9  | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po10 | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po12 | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl201-eu-spdc | po13 | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po15 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po16 | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po17 | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po19 | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po22 | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| pod-1/cl201-eu-spdc | po27 | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
+---------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --name *pod1a*

{
    "duration": 1995,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1377,
        "total_time": 1775
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	334	11	apic11o.emea-sp.cisco.com class fabricNode
True	423	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	323	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	297	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)