# Node Interface - Virtual Port Channel (VPC)

## Fault view

```
# iserver get aci intf vpc --apic apic21 --view fault --node any

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

Interface Virtual Port Channel - Faults [#6]
--------------------------------------------

+----------------------+--------+-----------+-----+-------+--------------------+-------------------------------+-----------+---------------------------------------------------------------------+
| Node                 | Domain | Interface | Sev | Code  | Cause              | Created Time                  | Lifecycle | Description                                                         |
+----------------------+--------+-----------+-----+-------+--------------------+-------------------------------+-----------+---------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | 278    | 686       | Maj | F1296 | interface-vpc-down | 2023-06-18T09:16:15.179+02:00 | raised    | vPC ESX21-CDC-22_PolGrp is down in Pod 1 node 2208 fabric hostname  | 
|                      |        |           |     |       |                    |                               |           | cl2208-eu-spdc                                                      | 
| pod-1/cl2208-eu-spdc | 278    | 345       | Maj | F1296 | interface-vpc-down | 2023-06-18T09:16:15.241+02:00 | raised    | vPC k8s_ocp_bm_3_PolGrp is down in Pod 1 node 2208 fabric hostname  | 
|                      |        |           |     |       |                    |                               |           | cl2208-eu-spdc                                                      | 
| pod-1/cl2202-eu-spdc | 212    | 344       | Maj | F1296 | interface-vpc-down | 2023-06-18T09:18:19.916+02:00 | raised    | vPC ESX20-CDC-22_PolGrp is down in Pod 1 node 2202 fabric hostname  | 
|                      |        |           |     |       |                    |                               |           | cl2202-eu-spdc                                                      | 
| pod-1/cl2207-eu-spdc | 278    | 686       | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:11.082+02:00 | raised    | vPC ESX21-CDC-22_PolGrp is down in Pod 1 node 2207 fabric hostname  | 
|                      |        |           |     |       |                    |                               |           | cl2207-eu-spdc                                                      | 
| pod-1/cl2207-eu-spdc | 278    | 345       | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:11.056+02:00 | raised    | vPC k8s_ocp_bm_3_PolGrp is down in Pod 1 node 2207 fabric hostname  | 
|                      |        |           |     |       |                    |                               |           | cl2207-eu-spdc                                                      | 
| pod-1/cl2201-eu-spdc | 212    | 344       | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:34.467+02:00 | raised    | vPC ESX20-CDC-22_PolGrp is down in Pod 1 node 2201 fabric hostname  | 
|                      |        |           |     |       |                    |                               |           | cl2201-eu-spdc                                                      | 
+----------------------+--------+-----------+-----+-------+--------------------+-------------------------------+-----------+---------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf vpc --apic apic21 --view fault --node any

{
    "duration": 12345,
    "apic": {
        "read": true,
        "success": 38,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 37,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 11296,
        "total_time": 11695
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

True	399	-	connect apic21o.emea-sp.cisco.com:443
True	301	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	426	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	271	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	274	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	263	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	417	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	264	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	270	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	270	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	295	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	265	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	284	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	265	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	306	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	293	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	278	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	258	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	423	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	399	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	299	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	314	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	473	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	289	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	337	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	321	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	314	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	298	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	257	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	272	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	336	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	277	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	271	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	318	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree-include=faults,no-scoped,subtree
True	259	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	287	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceVpc.md)