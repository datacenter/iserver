# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node any --id vlan35 -o verbose

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
- Input Octets             : 17783858718
- Input Unicast Packets    : 58572022
- Input Multicast Packets  : 0
- Input Discards           : 0
- Input Errors             : 0
- Output Octets            : 62876466581
- Output Unicast Packets   : 82864519
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

[[Back]](./InterfaceSvi.md)