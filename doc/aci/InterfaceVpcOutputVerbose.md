# Node Interface - Virtual Port Channel (VPC)

## Verbose output

```
# iserver get aci intf vpc --apic apic11 --node any --id 100 --view verbose

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
+---------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+

Interface Virtual Port Channel
------------------------------
- Apic                       : apic11
- Node                       : pod-1/cl201-eu-spdc
- VPC Domain Id              : 100
- Oper Role                  : master
- Oper State                 : configured-master,vpcs-reinited
- Local MAC                  : 4C:71:0D:23:FA:E3
- Local Priority             : 201
- Peer State                 : up
- Reason                     : 
- Peer IP                    : 10.3.192.68/32
- Peer MAC                   : 10:B3:D5:B5:62:C7
- Peer Priority              : 202
- Peer Version               : 25
- Configuration Constistency : pass
- Reason                     : 
- VPC Priority               : 32667
- VPC MAC                    : 00:23:04:EE:BE:64
- Virtual IP                 : 10.3.40.67/32
- Local Members              : 27/28
- Peer Members               : 25/28


+-----+--------------------------+---------+-------------+--------------+
| ID  | Name                     | PC Mode | Local State | Remote State |
+-----+--------------------------+---------+-------------+--------------+
| 23  | pod4a-COMP-1-PET_PolGrp  | active  | up          | up           | 
| 689 | pod1a-COMP-1-SAMX_PolGrp | active  | up          | up           | 
| 26  | pod1a-AIO-1-SAMX_PolGrp  | active  | up          | up           | 
| 696 | pod4a-AIO-2-PET_PolGrp   | active  | up          | up           | 
| 25  | pod4a-COMP-2-PET_PolGrp  | active  | up          | up           | 
| 686 | pod1a-MX_PolGrp          | active  | up          | down         | 
| 687 | pod1a-NVBench_PolGrp     | active  | down        | down         | 
| 27  | pod1a-AIO-2-PET_PolGrp   | active  | up          | up           | 
| 697 | pod4a-COMP-1-SAMX_PolGrp | active  | up          | up           | 
| 351 | pod-4a-br-API            | active  | up          | up           | 
| 352 | pod1a-AIO-1-PET_PolGrp   | active  | up          | up           | 
| 21  | pod4a-AIO-3-SAMX_PolGrp  | active  | up          | up           | 
| 14  | pod4a-AIO-1-SAMX_PolGrp  | active  | up          | up           | 
| 353 | pod1a-AIO-3-SAMX_PolGrp  | active  | up          | up           | 
| 24  | pod4a-COMP-2-SAMX_PolGrp | active  | up          | up           | 
| 22  | pod4a-AIO-3-PET_PolGrp   | active  | up          | up           | 
| 685 | pod1a-API_PolGrp         | active  | up          | up           | 
| 356 | pod1a-COMP-2-PET_PolGrp  | active  | up          | up           | 
| 28  | pod1a-COMP-2-SAMX_PolGrp | active  | up          | up           | 
| 15  | pod4a-AIO-1-PET_PolGrp   | active  | up          | up           | 
| 688 | pod1a-AIO-2-SAMX_PolGrp  | active  | up          | up           | 
| 354 | pod1a-AIO-3-PET_PolGrp   | active  | up          | up           | 
| 695 | pod4a-COMP-3-SAMX_PolGrp | active  | up          | up           | 
| 16  | pod4a-AIO-2-SAMX_PolGrp  | active  | up          | up           | 
| 13  | pod4a-COMP-3-PET_PolGrp  | active  | up          | up           | 
| 343 | Infra_PolGrp             | active  | up          | up           | 
| 355 | pod1a-COMP-1-PET_PolGrp  | active  | up          | up           | 
| 684 | pod4a-MX_PolGrp          | active  | up          | down         | 
+-----+--------------------------+---------+-------------+--------------+

+---------------------+---------------+-----------+---------------+------------+--------------+---------------+----------------+
| Node                | VPC Domain Id | Oper Role | Oper State    | Peer State | Constistency | Local Members | Remote Members |
+---------------------+---------------+-----------+---------------+------------+--------------+---------------+----------------+
| pod-1/cl202-eu-spdc | 100           | slave     | vpcs-reinited | up         | pass         | 25/28         | 27/28          | 
+---------------------+---------------+-----------+---------------+------------+--------------+---------------+----------------+

Interface Virtual Port Channel
------------------------------
- Apic                       : apic11
- Node                       : pod-1/cl202-eu-spdc
- VPC Domain Id              : 100
- Oper Role                  : slave
- Oper State                 : vpcs-reinited
- Local MAC                  : 10:B3:D5:B5:62:C7
- Local Priority             : 202
- Peer State                 : up
- Reason                     : 
- Peer IP                    : 10.3.192.67/32
- Peer MAC                   : 4C:71:0D:23:FA:E3
- Peer Priority              : 201
- Peer Version               : 25
- Configuration Constistency : pass
- Reason                     : 
- VPC Priority               : 32667
- VPC MAC                    : 00:23:04:EE:BE:64
- Virtual IP                 : 10.3.40.67/32
- Local Members              : 25/28
- Peer Members               : 27/28


+-----+--------------------------+---------+-------------+--------------+
| ID  | Name                     | PC Mode | Local State | Remote State |
+-----+--------------------------+---------+-------------+--------------+
| 684 | pod4a-MX_PolGrp          | active  | down        | up           | 
| 697 | pod4a-COMP-1-SAMX_PolGrp | active  | up          | up           | 
| 28  | pod1a-COMP-2-SAMX_PolGrp | active  | up          | up           | 
| 689 | pod1a-COMP-1-SAMX_PolGrp | active  | up          | up           | 
| 22  | pod4a-AIO-3-PET_PolGrp   | active  | up          | up           | 
| 685 | pod1a-API_PolGrp         | active  | up          | up           | 
| 25  | pod4a-COMP-2-PET_PolGrp  | active  | up          | up           | 
| 24  | pod4a-COMP-2-SAMX_PolGrp | active  | up          | up           | 
| 353 | pod1a-AIO-3-SAMX_PolGrp  | active  | up          | up           | 
| 352 | pod1a-AIO-1-PET_PolGrp   | active  | up          | up           | 
| 16  | pod4a-AIO-2-SAMX_PolGrp  | active  | up          | up           | 
| 687 | pod1a-NVBench_PolGrp     | active  | down        | down         | 
| 23  | pod4a-COMP-1-PET_PolGrp  | active  | up          | up           | 
| 696 | pod4a-AIO-2-PET_PolGrp   | active  | up          | up           | 
| 354 | pod1a-AIO-3-PET_PolGrp   | active  | up          | up           | 
| 686 | pod1a-MX_PolGrp          | active  | down        | up           | 
| 13  | pod4a-COMP-3-PET_PolGrp  | active  | up          | up           | 
| 21  | pod4a-AIO-3-SAMX_PolGrp  | active  | up          | up           | 
| 351 | pod-4a-br-API            | active  | up          | up           | 
| 26  | pod1a-AIO-1-SAMX_PolGrp  | active  | up          | up           | 
| 688 | pod1a-AIO-2-SAMX_PolGrp  | active  | up          | up           | 
| 695 | pod4a-COMP-3-SAMX_PolGrp | active  | up          | up           | 
| 15  | pod4a-AIO-1-PET_PolGrp   | active  | up          | up           | 
| 343 | Infra_PolGrp             | active  | up          | up           | 
| 355 | pod1a-COMP-1-PET_PolGrp  | active  | up          | up           | 
| 356 | pod1a-COMP-2-PET_PolGrp  | active  | up          | up           | 
| 14  | pod4a-AIO-1-SAMX_PolGrp  | active  | up          | up           | 
| 27  | pod1a-AIO-2-PET_PolGrp   | active  | up          | up           | 
+-----+--------------------------+---------+-------------+--------------+
```

Developer

```
# iserver get aci intf vpc --apic apic11 --node any --id 100 --view verbose

{
    "duration": 4157,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 3472,
        "total_time": 3888
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

True	416	-	connect apic11o.emea-sp.cisco.com
True	319	11	apic11o.emea-sp.cisco.com class fabricNode
True	283	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	315	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	334	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	345	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	306	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	314	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	309	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	293	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	356	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	298	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
```

[[Back]](./InterfaceVpc.md)