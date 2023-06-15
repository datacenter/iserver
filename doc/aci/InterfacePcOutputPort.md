# Node Interface - Port Channel (PC)

## Port focused view

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --view port

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+------+--------------------------+-------+--------+-------+---------+
| Node                | Id   | Name                     | State | Mode   | Speed | Ports   |
+---------------------+------+--------------------------+-------+--------+-------+---------+
| pod-1/cl201-eu-spdc | po1  | pod1a-AIO-2-SAMX_PolGrp  | up    | trunk  | 10G   | eth1/4  | 
| pod-1/cl201-eu-spdc | po2  | pod1a-AIO-3-SAMX_PolGrp  | up    | trunk  | 10G   | eth1/7  | 
| pod-1/cl201-eu-spdc | po3  | pod1a-NVBench_PolGrp     | down  | access | auto  |         | 
| pod-1/cl201-eu-spdc | po4  | pod1a-COMP-2-PET_PolGrp  | up    | trunk  | 10G   | eth1/14 | 
| pod-1/cl201-eu-spdc | po5  | pod1a-COMP-2-SAMX_PolGrp | up    | trunk  | 10G   | eth1/13 | 
| pod-1/cl201-eu-spdc | po6  | pod1a-AIO-2-PET_PolGrp   | up    | trunk  | 10G   | eth1/5  | 
| pod-1/cl201-eu-spdc | po7  | pod1a-AIO-1-PET_PolGrp   | up    | trunk  | 10G   | eth1/2  | 
| pod-1/cl201-eu-spdc | po8  | pod1a-COMP-1-PET_PolGrp  | up    | trunk  | 10G   | eth1/11 | 
| pod-1/cl201-eu-spdc | po9  | pod1a-COMP-1-SAMX_PolGrp | up    | trunk  | 10G   | eth1/10 | 
| pod-1/cl201-eu-spdc | po10 | pod1a-AIO-3-PET_PolGrp   | up    | trunk  | 10G   | eth1/8  | 
| pod-1/cl201-eu-spdc | po11 | pod1a-MX_PolGrp          | up    | trunk  | 10G   | eth1/23 | 
| pod-1/cl201-eu-spdc | po12 | pod1a-API_PolGrp         | up    | trunk  | 1G    | eth1/24 | 
| pod-1/cl201-eu-spdc | po13 | pod-4a-br-API            | up    | trunk  | 1G    | eth1/68 | 
| pod-1/cl201-eu-spdc | po14 | pod1a-AIO-1-SAMX_PolGrp  | up    | trunk  | 10G   | eth1/1  | 
| pod-1/cl201-eu-spdc | po15 | pod4a-AIO-3-SAMX_PolGrp  | up    | trunk  | 10G   | eth1/55 | 
| pod-1/cl201-eu-spdc | po16 | pod4a-COMP-2-SAMX_PolGrp | up    | trunk  | 10G   | eth1/61 | 
| pod-1/cl201-eu-spdc | po17 | pod4a-AIO-2-PET_PolGrp   | up    | trunk  | 10G   | eth1/53 | 
| pod-1/cl201-eu-spdc | po18 | pod4a-COMP-1-PET_PolGrp  | up    | trunk  | 10G   | eth1/59 | 
| pod-1/cl201-eu-spdc | po19 | pod4a-AIO-1-SAMX_PolGrp  | up    | trunk  | 10G   | eth1/49 | 
| pod-1/cl201-eu-spdc | po20 | pod4a-AIO-2-SAMX_PolGrp  | up    | trunk  | 10G   | eth1/52 | 
| pod-1/cl201-eu-spdc | po21 | pod4a-AIO-1-PET_PolGrp   | up    | trunk  | 10G   | eth1/50 | 
| pod-1/cl201-eu-spdc | po22 | pod4a-MX_PolGrp          | up    | trunk  | 10G   | eth1/67 | 
| pod-1/cl201-eu-spdc | po23 | pod4a-COMP-3-SAMX_PolGrp | up    | trunk  | 10G   | eth1/64 | 
| pod-1/cl201-eu-spdc | po24 | pod4a-COMP-3-PET_PolGrp  | up    | trunk  | 10G   | eth1/65 | 
| pod-1/cl201-eu-spdc | po25 | pod4a-AIO-3-PET_PolGrp   | up    | trunk  | 10G   | eth1/56 | 
| pod-1/cl201-eu-spdc | po26 | Infra_PolGrp             | up    | trunk  | 10G   | eth1/96 | 
| pod-1/cl201-eu-spdc | po27 | pod4a-COMP-2-PET_PolGrp  | up    | trunk  | 10G   | eth1/62 | 
| pod-1/cl201-eu-spdc | po28 | pod4a-COMP-1-SAMX_PolGrp | up    | trunk  | 10G   | eth1/58 | 
+---------------------+------+--------------------------+-------+--------+-------+---------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --view port

{
    "duration": 1762,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 1218,
        "total_time": 1612
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

True	394	-	connect apic11o.emea-sp.cisco.com
True	298	13	apic11o.emea-sp.cisco.com class fabricNode
True	333	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	285	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	302	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)