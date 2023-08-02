# Node Interface - Port Channel (PC)

## State view

```
# iserver get aci intf pc --apic apic21 --node any

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

Interface Port Channel - State [#36]
------------------------------------

+----------------------+--------+---------+-----+------------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name                   | Protocol    | Admin | State | Reason                    | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+------------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po1 | SPN_PolGrp             | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 10G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po2 | UCSB1-FI-A_PolGrp      | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po3 | HX1-FI-B_PolGrp        | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-A_PolGrp        | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po5 | ESX22-CDC-22_PolGrp    | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po6 | UCSB1-FI-B_PolGrp      | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po1 | UCSB1-FI-B_PolGrp      | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po2 | SPN_PolGrp             | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 10G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po3 | UCSB1-FI-A_PolGrp      | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-B_PolGrp        | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po5 | HX1-FI-A_PolGrp        | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po6 | ESX22-CDC-22_PolGrp    | lacp-active | up    | up    |                           | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/cl2201-eu-spdc | 0      | 1 0 0 0 | po1 | ESX20-CDC-22_PolGrp    | lacp-active | up    | down  | port-channel-members-down | 212 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | po2 | Infra_PolGrp           | lacp-active | up    | up    |                           | 212 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | po1 | Infra_PolGrp           | lacp-active | up    | up    |                           | 212 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2202-eu-spdc | 0      | 1 0 0 0 | po2 | ESX20-CDC-22_PolGrp    | lacp-active | up    | down  | port-channel-members-down | 212 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 0      | 1 0 0 0 | po1 | ESX21-CDC-22_PolGrp    | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 40G   | 
| pod-1/cl2207-eu-spdc | 0      | 1 0 0 0 | po2 | k8s_ocp_bm_3_PolGrp    | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | po3 | k8s_ocp_bm_4_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | po4 | k8s_ocp_bm_5_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | po5 | k8s_esx71_PolGrp       | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | po6 | k8s_esx72_PolGrp       | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | po7 | k8s_ocp_bm_1_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | po8 | k8s_ocp_bm_2_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 0      | 1 0 0 0 | po1 | ESX21-CDC-22_PolGrp    | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 40G   | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | po2 | k8s_esx71_PolGrp       | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | po3 | k8s_esx72_PolGrp       | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | po4 | k8s_ocp_bm_1_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | po5 | k8s_ocp_bm_2_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 0      | 1 0 0 0 | po6 | k8s_ocp_bm_3_PolGrp    | lacp-active | up    | down  | port-channel-members-down | 278 | 0/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | po7 | k8s_ocp_bm_4_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | po8 | k8s_ocp_bm_5_PolGrp    | lacp-active | up    | up    |                           | 278 | 1/1     | switched | trunk | 10G   | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | po1 | UCSB1-R7DC-FI-B_PolGrp | lacp-active | up    | up    |                           | 227 | 1/1     | switched | trunk | 10G   | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | po2 | UCSB1-R7DC-FI-A_PolGrp | lacp-active | up    | up    |                           | 227 | 1/1     | switched | trunk | 10G   | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | po1 | UCSB1-R7DC-FI-A_PolGrp | lacp-active | up    | up    |                           | 227 | 1/1     | switched | trunk | 10G   | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | po2 | UCSB1-R7DC-FI-B_PolGrp | lacp-active | up    | up    |                           | 227 | 1/1     | switched | trunk | 10G   | 
+----------------------+--------+---------+-----+------------------------+-------------+-------+-------+---------------------------+-----+---------+----------+-------+-------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node any

{
    "duration": 10999,
    "apic": {
        "read": true,
        "success": 28,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 27,
        "connect_time": 432,
        "disconnect_time": 0,
        "mo_time": 9434,
        "total_time": 9866
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

True	432	-	connect apic21o.emea-sp.cisco.com:443
True	317	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	449	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	297	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	280	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	464	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	312	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	345	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	357	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	319	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	310	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	405	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	309	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	302	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	495	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	340	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	318	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	548	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	333	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	332	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	316	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	308	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	378	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	326	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	414	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	312	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	273	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	275	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfacePc.md)