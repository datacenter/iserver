# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node any --id vlan35 --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

Interface SVI
-------------
- Interface     : vlan35
- Admin State   : up
- Oper State    : up
- Reason        : 
- Vlan ID       : 35
- Vlan Type     : bd-regular
- Medium        : bcast
- Multicast     : no
- MTU           : 9000
- MAC           : 00:22:BD:FE:FF:FF
- Bandwidth     : 10000000
- Carrier Delay : 10
- Delay         : 1
- Fabric Encap  : vxlan-16613250


+-----------------+------------+---------+
| Address         | Oper State | Type    |
+-----------------+------------+---------+
| 99.99.99.254/24 | up         | primary | 
+-----------------+------------+---------+

Interface Traffic Counters
--------------------------
- Input Octets             : 0
- Input Unicast Packets    : 0
- Input Multicast Packets  : 0
- Input Discards           : 0
- Input Errors             : 0
- Output Octets            : 0
- Output Unicast Packets   : 0
- Output Multicast Packets : 0
- Output Discards          : 0
- Output Errors            : 0


Interface SVI
-------------
- Interface     : vlan35
- Admin State   : up
- Oper State    : up
- Reason        : 
- Vlan ID       : 35
- Vlan Type     : bd-regular
- Medium        : bcast
- Multicast     : no
- MTU           : 9000
- MAC           : 00:22:BD:3D:C1:CC
- Bandwidth     : 10000000
- Carrier Delay : 10
- Delay         : 1
- Fabric Encap  : vxlan-15531940


+---------------+------------+---------+
| Address       | Oper State | Type    |
+---------------+------------+---------+
| 15.3.6.254/24 | up         | primary | 
+---------------+------------+---------+

Interface Traffic Counters
--------------------------
- Input Octets             : 0
- Input Unicast Packets    : 0
- Input Multicast Packets  : 0
- Input Discards           : 0
- Input Errors             : 0
- Output Octets            : 0
- Output Unicast Packets   : 0
- Output Multicast Packets : 0
- Output Discards          : 0
- Output Errors            : 0


Interface SVI
-------------
- Interface     : vlan35
- Admin State   : up
- Oper State    : up
- Reason        : 
- Vlan ID       : 35
- Vlan Type     : bd-regular
- Medium        : bcast
- Multicast     : no
- MTU           : 9000
- MAC           : 00:22:BD:AA:CC:FF
- Bandwidth     : 10000000
- Carrier Delay : 10
- Delay         : 1
- Fabric Encap  : vxlan-15368120


+-----------------+------------+---------+
| Address         | Oper State | Type    |
+-----------------+------------+---------+
| 10.58.24.158/27 | up         | primary | 
+-----------------+------------+---------+

Interface Traffic Counters
--------------------------
- Input Octets             : 0
- Input Unicast Packets    : 0
- Input Multicast Packets  : 0
- Input Discards           : 0
- Input Errors             : 0
- Output Octets            : 0
- Output Unicast Packets   : 0
- Output Multicast Packets : 0
- Output Discards          : 0
- Output Errors            : 0
```

Developer

```
# iserver get aci intf svi --apic apic11 --node any --id vlan35 --view verbose

{
    "duration": 7885,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 6970,
        "total_time": 7366
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

True	396	-	connect apic11o.emea-sp.cisco.com
True	314	13	apic11o.emea-sp.cisco.com class fabricNode
True	413	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	325	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	391	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	336	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	501	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	311	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	444	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	299	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	281	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	277	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	334	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	286	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	352	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	294	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	361	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	298	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	287	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	312	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	277	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	277	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)