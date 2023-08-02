# Node Protocol - BFD

## Verbose output

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol BFD - Session
----------------------
- Node                                 : pod-1/cl201-eu-spdc
- Health                               : 90
- Faults                               : 0 1 0 0
- Local Address                        : 15.254.101.4
- Local State                          : down
- Local Session Id                     : 1090519045
- Local MAC                            : 00:22:BD:F8:19:FF
- Remote Address                       : 15.100.7.41
- Remote State                         : down
- Remote Session Id                    : 0
- Remote MAC                           : FA:16:3E:BC:A6:70
- VRF                                  : common:smi5Gc-cvim1-N3-N4_VRF
- Interface                            : vlan472
- Session Type                         : singlehop
- IOD                                  : 207
- Last Down Time                       : 2023-07-05T19:21:03.000+02:00
- Last Trans Time                      : 2023-07-05T19:21:03.000+02:00
- Last Diag Code                       : none
- Authentication Sequence Number       : 596516649
- Async mode source port               : 49156
- Protocol diag code                   : none
- Detect Multiplier                    : 3
- Local Detect Multiplier              : 3
- Active Receive Interval (msec)       : 2000
- Active Transmit Interval (msec)      : 2000
- Active Slow Interval (msec)          : 0
- Local Receive Interval (msec)        : 2000
- Local Transmit Interval (msec)       : 2000
- Echo mode source port                : unspecified
- Active Echo Transmit Interval (msec) : 0


Protocol BFD - Peer
-------------------
- Oper State                   : 
- Diag Code                    : 
- BFD Flags                    : 
- Detect Multiplier            : 
- Min Receive Interval (msec)  : 
- Min Transmit Interval (msec) : 
- Min Echo Interval (msec)     : 
- My discriminator             : 
- Your discriminator           : 
- C-Bit                        : 


Protocol BFD - Session Stats
----------------------------
- Up State Counts                      : 0
- Down State Counts                    : 0
- Last packet received                 : 2023-07-05T19:21:21.249+02:00
- Last packet transmitted              : 2023-08-02T14:37:28.758+02:00
- Packets Received                     : 0
- Average Received Packets Interval    : 0
- Maximum Received Packets Interval    : 0
- Minimum Received Packets Interval    : 0
- Packets Transmitted                  : 1242376
- Average Transmitted Packets Interval : 1933
- Maximum Transmitted Packets Interval : 1933
- Minimum Transmitted Packets Interval : 1933


Protocol BFD - Event Logs last 7d [#0]
--------------------------------------
None

Protocol BFD - Faults [#1]
--------------------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.050+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+

Protocol BFD - Fault Records last 7d [#0]
-----------------------------------------
None
```

Developer

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 --view verbose

{
    "duration": 4640,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 481,
        "disconnect_time": 0,
        "mo_time": 3162,
        "total_time": 3643
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

True	481	-	connect apic11o.emea-sp.cisco.com:443
True	368	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	292	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	334	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	361	2	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=faults,no-scoped,subtree
True	1018	1000	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	789	1000	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolBfd.md)