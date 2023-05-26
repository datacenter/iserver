# Node Interface - Management

## Verbose output

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc -o verbose

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

[[Back]](./InterfaceMgmt.md)