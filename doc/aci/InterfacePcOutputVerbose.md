# Node Interface - Port Channel (PC)

## Verbose output

```
# iserver get aci intf pc
    --apic apic11
    --node cl201-eu-spdc
    --id po1
    --view verbose

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
- PDU Sent             : 255324
- PDU Rcvd             : 255325
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
    "duration": 3363,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 2638,
        "total_time": 3055
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

True	417	-	connect apic11o.emea-sp.cisco.com
True	322	11	apic11o.emea-sp.cisco.com class fabricNode
True	351	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/68] query query-target=children&target-subtree-class=lacpAdjEp
True	397	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/68] query query-target=children&target-subtree-class=lacpIfStats
True	315	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpInst
True	318	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	302	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)