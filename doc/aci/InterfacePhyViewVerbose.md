# Node Interface - Physical

## Verbose output

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --id 1/1
    --view verbose

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Fabric Port Details
-------------------
- Node                          : pod-1/bl2205-eu-spdc
- Port                          : eth1/1
- Admin State                   : up
- Usage                         : discovery
- Oper Speed                    : 100G
- Oper State                    : up
- Oper State Reason             : connected
- Backplane Mac                 : 3C:13:CC:B9:ED:B1
- Last Link State Change        : 2023-06-18T09:47:22.654+02:00
- Oper Router Mac               : 00:00:00:00:00:00
- Oper Mdix                     : auto
- Oper Mode                     : trunk
- Access VLAN                   : unknown
- Native VLAN                   : unknown
- Reset Counter                 : 1
- Operational VLANs             : 
- Allowed VLANs                 : 
- Port Channel                  : po2
- Bandwidth (kb)                : 0
- Delay (usec)                  : 1
- Mdix                          : auto
- Medium                        : broadcast
- MTU                           : 9000
- Router Mac                    : not-applicable
- Speed                         : inherit
- Forward Error Correction      : inherit
- Auto Negotiation              : on
- Link Debounce Interval (msec) : 100
- Dot1Q Ether Type              : 0x8100
- Layer                         : switched
- Mode                          : trunk
- Switching State               : disabled
- Destination SPAN Mode         : not-a-span-dest
- Channeling State              : channeling

Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --id 1/1
    --view verbose

{
    "duration": 3222,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 2374,
        "total_time": 2784
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

True	410	-	connect apic21o.emea-sp.cisco.com:443
True	314	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1143	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	298	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	316	42	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=ethpmPortCap
True	303	36	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=pcAggrMbrIf
```

[[Back]](./InterfacePhy.md)