# Node Protocol - ARP

## Verbose output

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 -o verbose

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

BFD Session
-----------
- Node                                 : pod-1/cl201-eu-spdc
- Local Address                        : 15.254.103.252
- Local State                          : up
- Local Session Id                     : 1090519045
- Local MAC                            : 00:22:BD:F8:19:FF
- Remote Address                       : 15.254.103.192
- Remote State                         : up
- Remote Session Id                    : 3
- Remote MAC                           : FA:16:3E:C4:FE:86
- VRF                                  : common:smi5Gc-cvim1-N3-N4_VRF
- Interface                            : vlan469
- Session Type                         : singlehop
- IOD                                  : 217
- Last Down Time                       : 2023-03-03T01:23:40.000+02:00
- Last Trans Time                      : 2023-03-03T01:23:51.000+02:00
- Last Diag Code                       : none
- Authentication Sequence Number       : 596516649
- Async mode source port               : 49156
- Protocol diag code                   : none
- Detect Multiplier                    : 3
- Local Detect Multiplier              : 3
- Active Receive Interval (msec)       : 500
- Active Transmit Interval (msec)      : 500
- Active Slow Interval (msec)          : 2000
- Local Receive Interval (msec)        : 500
- Local Transmit Interval (msec)       : 500
- Echo mode source port                : unspecified
- Active Echo Transmit Interval (msec) : 0


BFD Peer
--------
- Oper State                   : up
- Diag Code                    : none
- BFD Flags                    : 
- Detect Multiplier            : 500
- Min Receive Interval (msec)  : 500
- Min Transmit Interval (msec) : 500
- Min Echo Interval (msec)     : 0
- My discriminator             : 3
- Your discriminator           : 1090519045
- C-Bit                        : disabled


BFD Session Stats
-----------------
- Up State Counts                      : 1
- Down State Counts                    : 0
- Last packet received                 : 2023-05-24T11:13:02.606+02:00
- Last packet transmitted              : 2023-05-24T11:13:02.332+02:00
- Packets Received                     : 15273596
- Average Received Packets Interval    : 466
- Maximum Received Packets Interval    : 1042
- Minimum Received Packets Interval    : 0
- Packets Transmitted                  : 15769194
- Average Transmitted Packets Interval : 451
- Maximum Transmitted Packets Interval : 451
- Minimum Transmitted Packets Interval : 451
```

[[Back]](./ProtocolBfd.md)