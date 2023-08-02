# Node Interface - Port Channel (PC)

## Filter by domain

```
# iserver get aci intf pc --apic apic21 --node any --domain 256

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

Interface Port Channel - State [#12]
------------------------------------

+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name                | Protocol    | Admin | State | Reason | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po1 | SPN_PolGrp          | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 10G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po2 | UCSB1-FI-A_PolGrp   | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po3 | HX1-FI-B_PolGrp     | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-A_PolGrp     | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po5 | ESX22-CDC-22_PolGrp | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po6 | UCSB1-FI-B_PolGrp   | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po1 | UCSB1-FI-B_PolGrp   | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po2 | SPN_PolGrp          | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 10G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po3 | UCSB1-FI-A_PolGrp   | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 100G  | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-B_PolGrp     | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po5 | HX1-FI-A_PolGrp     | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | po6 | ESX22-CDC-22_PolGrp | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
+----------------------+--------+---------+-----+---------------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node any --domain 256

{
    "duration": 10844,
    "apic": {
        "read": true,
        "success": 28,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 27,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 9319,
        "total_time": 9749
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
True	322	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	471	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	304	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	303	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	456	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	339	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	341	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	352	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	307	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	300	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	344	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	332	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	282	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	477	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	311	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	302	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	490	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	321	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	314	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	327	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	304	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	350	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	311	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	370	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	349	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	317	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	323	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfacePc.md)