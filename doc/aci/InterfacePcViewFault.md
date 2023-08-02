# Node Interface - Port Channel (PC)

## Fault view

```
# iserver get aci intf pc --apic apic21 --node any --view fault

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

Interface Port Channel - Faults [#6]
------------------------------------

+----------------------+-----------+------+-------+-------------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code  | Cause                   | Created Time                  | Lifecycle | Description                                                                    |
+----------------------+-----------+------+-------+-------------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2023-06-18T09:16:16.465+02:00 | raised    | Port is down, reason being noOperMembers(connected), used by EPG on node 2208  | 
|                      |           |      |       |                         |                               |           | of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                            | 
| pod-1/cl2208-eu-spdc | po6       | Crit | F0532 | interface-physical-down | 2023-06-18T09:16:16.597+02:00 | raised    | Port is down, reason being noOperMembers(connected), used by EPG on node 2208  | 
|                      |           |      |       |                         |                               |           | of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                            | 
| pod-1/cl2202-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-18T09:18:22.038+02:00 | raised    | Port is down, reason being noOperMembers(connected), used by EPG on node 2202  | 
|                      |           |      |       |                         |                               |           | of fabric ACI2-EU-SPDC with hostname cl2202-eu-spdc                            | 
| pod-1/cl2207-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2023-06-18T09:44:12.283+02:00 | raised    | Port is down, reason being noOperMembers(connected), used by EPG on node 2207  | 
|                      |           |      |       |                         |                               |           | of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                            | 
| pod-1/cl2207-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-18T09:44:12.249+02:00 | raised    | Port is down, reason being noOperMembers(connected), used by EPG on node 2207  | 
|                      |           |      |       |                         |                               |           | of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                            | 
| pod-1/cl2201-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2023-06-18T09:44:36.588+02:00 | raised    | Port is down, reason being noOperMembers(connected), used by EPG on node 2201  | 
|                      |           |      |       |                         |                               |           | of fabric ACI2-EU-SPDC with hostname cl2201-eu-spdc                            | 
+----------------------+-----------+------+-------+-------------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node any --view fault

{
    "duration": 13725,
    "apic": {
        "read": true,
        "success": 36,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 35,
        "connect_time": 418,
        "disconnect_time": 0,
        "mo_time": 11910,
        "total_time": 12328
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

True	418	-	connect apic21o.emea-sp.cisco.com:443
True	308	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	482	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	302	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	269	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	321	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	447	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	308	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	273	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	334	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	318	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	304	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	311	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	309	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	431	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	312	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	313	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	343	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	500	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	312	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	322	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	399	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	466	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	309	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	353	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	357	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	339	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	313	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	352	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	319	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	353	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	347	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	277	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	287	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	304	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	316	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfacePc.md)