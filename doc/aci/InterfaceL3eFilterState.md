# Node Interface - Encapsulated Routed

## Filter by operational state

```
# iserver get aci intf l3e --apic apic21 --node any --oper down

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

+----------------------+--------+---------+------------+-------+------+-------------+--------+---------+------+-------+-------------------+
| Node                 | Health | Faults  | Interface  | Admin | Oper | Reason      | Encap  | SR-MPLS | MTU  | Delay | Router MAC        |
+----------------------+--------+---------+------------+-------+------+-------------+--------+---------+------+-------+-------------------+
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | eth1/51.1  | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | eth1/51.1  | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/10.10 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/11.11 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/12.12 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/13.13 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/14.14 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/15.15 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/17.17 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/18.18 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/20.20 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/21.21 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/22.22 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/23.23 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/24.24 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/25.25 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/26.26 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/27.27 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/28.28 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/29.29 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/3.3   | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/30.30 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/31.31 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/32.32 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/33.33 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/34.34 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/4.4   | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/9.9   | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/10.10 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/11.11 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/12.12 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/13.13 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/14.14 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/15.15 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/17.17 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/18.18 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/19.19 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/21.21 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/22.22 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/23.23 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/24.24 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/25.25 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/26.26 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/27.27 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/28.28 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/29.29 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/3.3   | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/30.30 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/31.31 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/32.32 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/33.33 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/34.34 | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/4.4   | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/9.9   | up    | down | parent-down | vlan-4 | no      | 9150 | 1     | 00:00:00:00:00:00 | 
+----------------------+--------+---------+------------+-------+------+-------------+--------+---------+------+-------+-------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic21 --node any --oper down

{
    "duration": 13964,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 763,
        "disconnect_time": 0,
        "mo_time": 12297,
        "total_time": 13060
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

True	763	-	connect apic21o.emea-sp.cisco.com:443
True	422	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	489	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	388	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
True	1512	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	431	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4If
True	407	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	569	35	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4If
True	481	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	392	35	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4If
True	543	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	474	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4If
True	474	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	384	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4If
True	531	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	398	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4If
True	370	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	403	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4If
True	439	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	513	18	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4If
True	384	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	437	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4If
True	423	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	475	62	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4If
True	498	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	460	62	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4If
```

[[Back]](./InterfaceL3e.md)