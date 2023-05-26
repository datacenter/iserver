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

Output options:
  - [state](./InterfaceTunnelOutputState.md) (default)
  - [verbose](./InterfaceTunnelOutputVerbose.md)
  - [json](./InterfaceTunnelOutputJson.md)

Command options

```
# iserver get aci intf tun --help

Usage: iserver.py get aci intf tun [OPTIONS]

  Get aci node tunnel interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
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
  --ip TEXT                       Filter by IP
  --subnet TEXT                   Filter by subnet
  -o, --output [default|verbose|json]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 42 ms and logs saved in /tmp/iserver\067b6e64bad6
```

[[Back]](./Interface.md)