# Node Interface - Management

## Verbose view

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc --view verbose

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

Node Interface Management: mgmt0
--------------------------------
- Management Interface Name   : mgmt0
- Admin State                 : up
- Switching State             : disabled
- OperState                   : up
- Auto Negotiation            : on
- Duplex                      : full
- MTU                         : 1500
- Speed                       : 1G
- MAC Address                 : 4C:71:0D:23:FA:38
- IP Address                  : 10.58.28.141/27
- Router MAC                  : 4C:71:0D:23:FA:38
- CDP Neighbor - Platform     : N9K-C92348GC-X
- CDP Neighbor - System Name  : r22-eu-spdc
- CDP Neighbor - Port         : Ethernet1/25
- LLDP Neighbor - System Name : r22-eu-spdc.emea-sp.cisco.com
- LLDP Neighbor - Port        : Ethernet1/25
- Last Link State Change      : 2023-03-03T01:15:14.143+02:00
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc --view verbose

{
    "duration": 2982,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 2364,
        "total_time": 2761
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	333	11	apic11o.emea-sp.cisco.com class fabricNode
True	300	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	344	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	366	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0]/fltCnts
True	374	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)