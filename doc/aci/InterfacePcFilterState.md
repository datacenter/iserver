# Node Interface - Port Channel (PC)

## Filter by port channel state

```
# iserver get aci intf pc --apic apic21 --node any --state down

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

Interface Port Channel - State [#6]
-----------------------------------

+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name                | Protocol    | Admin | State | Reason                    | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
| pod-1/cl2201-eu-spdc | 0      | 1 0 0 0 | po1 | ESX20-CDC-22_PolGrp | lacp-active | up    | down  | port-channel-members-down | 212 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2202-eu-spdc | 0      | 1 0 0 0 | po2 | ESX20-CDC-22_PolGrp | lacp-active | up    | down  | port-channel-members-down | 212 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 0      | 1 0 0 0 | po1 | ESX21-CDC-22_PolGrp | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 40G   | 
| pod-1/cl2207-eu-spdc | 0      | 1 0 0 0 | po2 | k8s_ocp_bm_3_PolGrp | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 0      | 1 0 0 0 | po1 | ESX21-CDC-22_PolGrp | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 40G   | 
| pod-1/cl2208-eu-spdc | 0      | 1 0 0 0 | po6 | k8s_ocp_bm_3_PolGrp | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 10G   | 
+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node any --state down

{
    "duration": 8750,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 7419,
        "total_time": 7849
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

True	430	-	connect apic21o.emea-sp.cisco.com:443
True	332	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	437	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	466	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	343	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	301	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	308	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	335	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	352	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	336	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	486	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	348	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	283	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	532	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	317	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	289	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	303	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	302	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	351	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	357	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	324	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	317	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfacePc.md)