# Node Interface - Tunnel

## Command options

Filter options:
  - [Interface ID](./InterfaceTunnelFilterId.md)
  - [Oper State](./InterfaceTunnelFilterState.md)
  - [Transport Layer](./InterfaceTunnelFilterLayer.md)
  - [VRF](./InterfaceTunnelFilterVrf.md)
  - [IP address](./InterfaceTunnelFilterIp.md)
  - [IP subnet](./InterfaceTunnelFilterSubnet.md)

View options:
  - [state](./InterfaceTunnelViewState.md)
  - [fault](./InterfaceTunnelViewFault.md)
  - [hfault](./InterfaceTunnelViewFaultHistory.md)
  - [event](./InterfaceTunnelViewEvent.md)
  - [audit](./InterfaceTunnelViewAudit.md)
  - [diag](./InterfaceTunnelViewDiag.md)
  - [all](./InterfaceTunnelViewAll.md)

Output options:
  - [default](./InterfaceTunnelOutputDefault.md)
  - [json](./InterfaceTunnelOutputJson.md)

Command options

```
# iserver get aci intf tun --help

Usage: iserver.py get aci intf tun [OPTIONS]

  Get aci node tunnel interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Port name
  --admin [any|up|down]           [default: any]
  --oper [any|up|down]            [default: any]
  --layer [any|l2|l3]             [default: any]
  --vrf TEXT                      Filter by vrf
  --address TEXT                  Filter by IP
  --subnet TEXT                   Filter by subnet
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|fault|hfault|event|audit|diag|all]
                                  [default: state]
  -r, --resolve                   Resolve identifiers
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 49 ms and logs saved in /tmp/iserver\3b00e8821b3b
```

[[Back]](./README.md)