# Node Interface

## Tunnel

Node selection options:
  - [single node](./InterfaceTunnelNode.md)
  - [selected nodes](./InterfaceTunnelNodes.md)
  - [all nodes](./InterfaceTunnelNodesAll.md)
  - [multi APIC](./InterfaceTunnelNodesApics.md)

Filter options:
  - [Interface ID](./InterfaceTunnelId.md)
  - [Oper State](./InterfaceTunnelState.md)
  - [Transport Layer](./InterfaceTunnelLayer.md)
  - [VRF](./InterfaceTunnelVrf.md)
  - [IP address](./InterfaceTunnelIp.md)
  - [IP subnet](./InterfaceTunnelSubnet.md)

View options:
  - [default](./InterfaceTunnelOutputState.md)
  - [verbose](./InterfaceTunnelOutputVerbose.md)

Output options:
  - [default](./InterfaceTunnelOutputState.md)
  - [json](./InterfaceTunnelOutputJson.md)

Command options

```
# iserver get aci intf tun --help

Usage: iserver.py get aci intf tun [OPTIONS]

  Get aci node tunnel interface

Options:
  --apic TEXT                   APIC name
  --ip TEXT                     APIC IP
  --username TEXT               APIC Username
  --password TEXT               APIC Password
  --pod TEXT                    Pod ID
  --node TEXT                   Node name patterns
  --role [any|leaf|spine]       [default: any]
  --id TEXT                     Port name
  --admin [any|up|down]         [default: any]
  --oper [any|up|down]          [default: any]
  --layer [any|l2|l3]           [default: any]
  --vrf TEXT                    Filter by vrf
  --ip TEXT                     Filter by IP
  --subnet TEXT                 Filter by subnet
  -v, --view [default|verbose]
  -o, --output [default|json]   [default: default]
  --empty                       No error on empty result
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 38 ms and logs saved in /tmp/iserver\deb73b2e7560
```

[[Back]](./Interface.md)