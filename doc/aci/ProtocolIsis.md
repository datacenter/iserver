# Node Protocol

## IS-IS

View options:
  - [inst](./ProtocolIsisViewInstance.md)
  - [intf](./ProtocolIsisViewInterface.md)
  - [lsp](./ProtocolIsisViewLsp.md)
  - [nei](./ProtocolIsisViewNeighbor.md)
  - [route](./ProtocolIsisViewRoute.md)
  - [tree](./ProtocolIsisViewTree.md)
  - [tun](./ProtocolIsisViewTunnel.md)
  - [fault](./ProtocolIsisViewFault.md)
  - [hfault](./ProtocolIsisViewFaultHistory.md)
  - [event](./ProtocolIsisViewEvent.md)
  - [diag](./ProtocolIsisViewDiag.md)
  - [all](./ProtocolIsisViewAll.md)

Output options:
  - [default](./ProtocolIsisOutputDefault.md)
  - [json](./ProtocolIsisOutputJson.md)

Command options

```
# iserver get aci proto isis --help

Usage: iserver.py get aci proto isis [OPTIONS]

  Get aci node protocol isis

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --port INTEGER               APIC Port  [default: 443]
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --pod TEXT                   Pod ID
  --node TEXT                  Node name patterns
  --role [any|leaf|spine]      [default: any]
  --domain TEXT                Filter by domain name
  --when TEXT                  Filter faults by timestamp  [default: 7d]
  -v, --view TEXT              [inst|intf|lsp|nei|route|tree|tun|fault|hfault|
                               event|diag|all]  [default: inst]
  -o, --output [default|json]  [default: default]
  --no-cache                   Disable cache
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 43 ms and logs saved in /tmp/iserver\4a113fd7d51e
```

[[Back]](./README.md)