# Node Interface - Port Channel (PC)

## Verbose output

```
# iserver get aci intf pc
    --apic apic11
    --node cl201-eu-spdc
    --id po1
    --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-----+-------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name                    | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+-------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po1 | pod1a-AIO-2-SAMX_PolGrp | up    | enabled   | up    |        | active    | 100        | 1            | 
+---------------------+-----+-------------------------+-------+-----------+-------+--------+-----------+------------+--------------+

Interface Port Channel
----------------------
- Apic             : apic11
- Node             : pod-1/cl201-eu-spdc
- Id               : po1
- Name             : pod1a-AIO-2-SAMX_PolGrp
- Admin State      : up
- Switching State  : enabled
- Operational Mode : active
- Layer            : switched
- Min Links        : 1
- Max Links        : 16
- Active Links     : 1
- Mode             : trunk
- Speed            : inherit
- MAC Address      : 4C:71:0D:23:FA:3C
- vpcDomain        : 100


VLANs
-----
- Allowed VLANs          : 32-33,74-75,330-331,469-470,472,492-493,496-497
- Oper VLANs             : 32-33,74-75,330-331,469-470,472,492-493,496-497
- Configured Access VLAN : vlan-75
- Access VLAN            : vlan-75
- Configured Native VLAN : vlan-75
- Native VLAN            : vlan-75


LACP Settings
-------------
- Admin State    : enabled
- Admin Priority : 32768
- Oper Priority  : 32768
- Sys MAC        : 4C:71:0D:23:FA:E3


LACP Interface
--------------
- LACP Interface       : eth1/4
- Admin State          : enabled
- Local Port Num       : 260
- Local Port Priority  : 32768
- Local Activity Flags : active,aggregate,collect,distribute,sync
- Last Active          : 2023-06-12T16:52:40.000+02:00
- Key                  : 33456
- Nbr Port Num         : 2
- Nbr Port Priority    : 255
- Nbr System Id        : 3C:FD:FE:CB:F5:B0
- Nbr Activity Flags   : active,aggregate,collect,distribute,sync
- Nbr Key              : 2
- PDU Sent             : 3815
- PDU Rcvd             : 3778
- PDU Timeout          : 0
- Marker Sent          : 0
- Marker Rcvd          : 0
- Marker Rsp Sent      : 0
- Marker Rsp Rcvd      : 0
```

Developer

```
# iserver get aci intf pc
    --apic apic11
    --node cl201-eu-spdc
    --id po1
    --view verbose

{
    "duration": 2909,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 2369,
        "total_time": 2756
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

True	387	-	connect apic11o.emea-sp.cisco.com
True	304	13	apic11o.emea-sp.cisco.com class fabricNode
True	340	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	283	27	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	289	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	283	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpIfStats
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpInst
True	286	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	303	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)