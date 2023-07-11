# Node Protocol - ARP

## Verbose output

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

BFD Session
-----------
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


BFD Peer
--------
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


BFD Session Stats
-----------------
- Up State Counts                      : 0
- Down State Counts                    : 0
- Last packet received                 : 2023-07-05T19:21:07.713+02:00
- Last packet transmitted              : 2023-07-11T22:00:29.554+02:00
- Packets Received                     : 0
- Average Received Packets Interval    : 0
- Maximum Received Packets Interval    : 0
- Minimum Received Packets Interval    : 0
- Packets Transmitted                  : 273052
- Average Transmitted Packets Interval : 1933
- Maximum Transmitted Packets Interval : 1933
- Minimum Transmitted Packets Interval : 1933


BFD Event Logs last 7d [#4]
---------------------------

+---------------------+------------+----------+----------+-------------------+-------------------------------+-------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code     | Cause             | Created Time                  | Description                                                                   |
+---------------------+------------+----------+----------+-------------------+-------------------------------+-------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-07-05T19:21:04.006+02:00 | BFD session to neighbor 15.100.7.41 on interface vlan472 has been created     | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-07-05T19:21:04.009+02:00 | Active parameter of BFD session 1090519045 has changed Disc 1090519045        | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-07-05T19:21:17.054+02:00 | Local parameter of BFD session 1090519045 has changed TX(2000): RX(2000):     | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4215661 | oper-state-change | 2023-07-05T19:21:23.058+02:00 | BFD session 1090519045 to neighbor 15.100.7.41 on interface vlan472 is down.  | 
|                     |            |          |          |                   |                               | Reason: No Diagnostic.                                                        | 
+---------------------+------------+----------+----------+-------------------+-------------------------------+-------------------------------------------------------------------------------+

BFD Faults [#1]
---------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.050+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+

BFD Fault Records last 7d [#2]
------------------------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.051+02:00 | soaking   | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:23:34.715+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 --view verbose

{
    "duration": 10207,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 459,
        "disconnect_time": 0,
        "mo_time": 4816,
        "total_time": 5275
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

True	459	-	connect apic11o.emea-sp.cisco.com:443
True	332	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	328	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	364	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	2078	2215	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=faults,fault-records,no-scoped,subtree
True	1714	4050	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=event-logs,no-scoped,subtree
```

[[Back]](./ProtocolBfd.md)