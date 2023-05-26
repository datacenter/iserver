# Node Interface - Port Channel (PC)

## Verbose output

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1 -o verbose

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name          | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po1 | pod-4a-br-API | up    | enabled   | up    |        | active    | 100        | 1            | 
+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+

Interface Port Channel
----------------------
- Apic             : apic11
- Node             : pod-1/cl201-eu-spdc
- Id               : po1
- Name             : pod-4a-br-API
- Admin State      : up
- Switching State  : enabled
- Operational Mode : active
- Layer            : switched
- Min Links        : 1
- Max Links        : 16
- Active Links     : 1
- Mode             : trunk
- Speed            : 1G
- MAC Address      : 4C:71:0D:23:FA:7C
- vpcDomain        : 100


VLANs
-----
- Allowed VLANs          : 353-354
- Oper VLANs             : 353-354
- Configured Access VLAN : vlan-354
- Access VLAN            : vlan-354
- Configured Native VLAN : vlan-354
- Native VLAN            : vlan-354


LACP Settings
-------------
- Admin State    : enabled
- Admin Priority : 32768
- Oper Priority  : 32768
- Sys MAC        : 4C:71:0D:23:FA:E3


LACP Interface
--------------
- LACP Interface       : eth1/68
- Admin State          : enabled
- Local Port Num       : 324
- Local Port Priority  : 32768
- Local Activity Flags : active,aggregate,collect,distribute,sync
- Last Active          : 2023-03-03T01:23:45.000+02:00
- Key                  : 33119
- PDU Sent             : 216798
- PDU Rcvd             : 216799
- PDU Timeout          : 0
- Marker Sent          : 0
- Marker Rcvd          : 0
- Marker Rsp Sent      : 0
- Marker Rsp Rcvd      : 0
```

[[Back]](./InterfacePc.md)