# Node Interface - Port Channel (PC)

## Filter by port speed

```
# iserver get aci intf pc --apic apic21 --node any --speed 40G

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

Interface Port Channel - State [#8]
-----------------------------------

+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name                | Protocol    | Admin | State | Reason                    | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po3 | HX1-FI-B_PolGrp     | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-A_PolGrp     | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po5 | ESX22-CDC-22_PolGrp | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-B_PolGrp     | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po5 | HX1-FI-A_PolGrp     | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po6 | ESX22-CDC-22_PolGrp | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/cl2207-eu-spdc | 0      | 1 0 0 0 | po1 | ESX21-CDC-22_PolGrp | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 40G   | 
| pod-1/cl2208-eu-spdc | 0      | 1 0 0 0 | po1 | ESX21-CDC-22_PolGrp | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 40G   | 
+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node any --speed 40G

{
    "duration": 8832,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 7525,
        "total_time": 7967
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

True	442	-	connect apic21o.emea-sp.cisco.com:443
True	314	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	501	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	321	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	312	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	480	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	313	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	336	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	344	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	365	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	494	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	314	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	391	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	491	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	285	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	291	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	304	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	289	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	373	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	386	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	304	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	317	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfacePc.md)