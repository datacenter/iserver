# Node Protocol

## IS-IS

Node selection options:
  - [single node](./ProtocolIsisInstanceNode.md)
  - [selected nodes](./ProtocolIsisInstanceNodes.md)
  - [all nodes](./ProtocolIsisInstanceNodesAll.md)

Output options:
  - [instance](./ProtocolIsisInstanceNode.md) (default)
  - [intf](./ProtocolIsisInterfaceNode.md)
  - [lsp](./ProtocolIsisLspNode.md)
  - [neighbor](./ProtocolIsisNeighborNode.md)
  - [route](./ProtocolIsisRouteNode.md)
  - [tree](./ProtocolIsisTreeNode.md)
  - [tunnel](./ProtocolIsisTunnelNode.md)
  - [verbose](./ProtocolIsisVerbose.md)

Command options

```
# iserver get aci proto isis --help

Usage: iserver.py get aci proto isis [OPTIONS]

  Get aci node protocol isis

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --domain TEXT                   Filter by domain name
  -o, --output [instance|intf|lsp|neighbor|route|tree|tunnel|verbose|json]
                                  [default: instance]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 72 ms and logs saved in /tmp/iserver\8c630be71c0f
```

[[Back]](./Protocol.md)