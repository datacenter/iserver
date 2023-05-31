# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node any --id vlan35 --view verbose

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

Interface SVI
-------------
- Interface     : vlan35
- Admin State   : up
- Oper State    : up
- Reason        : 
- Vlan ID       : 35
- Vlan Type     : bd-external
- Medium        : bcast
- Multicast     : no
- MTU           : 9000
- MAC           : 00:22:BD:F8:19:FF
- Bandwidth     : 10000000
- Carrier Delay : 10
- Delay         : 1
- Fabric Encap  : vxlan-15040482


+-----------------+------------+-----------+
| Address         | Oper State | Type      |
+-----------------+------------+-----------+
| 10.58.24.110/28 | up         | secondary | 
| 10.58.24.109/28 | up         | primary   | 
+-----------------+------------+-----------+

Interface Traffic Counters
--------------------------
- Input Octets             : 20798131025
- Input Unicast Packets    : 71250722
- Input Multicast Packets  : 0
- Input Discards           : 0
- Input Errors             : 0
- Output Octets            : 85580623891
- Output Unicast Packets   : 107484844
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
- MAC           : 00:22:BD:F5:AA:FF
- Bandwidth     : 10000000
- Carrier Delay : 10
- Delay         : 1
- Fabric Encap  : vxlan-16089039


+----------------+------------+---------+
| Address        | Oper State | Type    |
+----------------+------------+---------+
| 15.2.64.254/24 | up         | primary | 
+----------------+------------+---------+

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
    "duration": 7266,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 435,
        "disconnect_time": 0,
        "mo_time": 6189,
        "total_time": 6624
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

True	435	-	connect apic11o.emea-sp.cisco.com
True	315	11	apic11o.emea-sp.cisco.com class fabricNode
True	455	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	314	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	414	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	311	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	463	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	349	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	493	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	308	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	398	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	374	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	417	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	315	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	346	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	343	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	285	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	289	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)