# Node Interface

## Management

Node selection options:
  - [single node](./InterfaceMgmtNode.md)
  - [selected nodes](./InterfaceMgmtNodes.md)
  - [all nodes](./InterfaceMgmtNodesAll.md)
  - [multi APIC](./InterfaceMgmtNodesApics.md)

View options:
  - [default](./InterfaceMgmtOutputState.md)
  - [address](./InterfaceMgmtOutputAddress.md)
  - [neighbor](./InterfaceMgmtOutputNeighbor.md)
  - [verbose](./InterfaceMgmtOutputVerbose.md)

Output options:
  - [default](./InterfaceMgmtOutputState.md)
  - [json](./InterfaceMgmtOutputJson.md)

Command options

```
# iserver get aci intf mgmt --help

Usage: iserver.py get aci intf mgmt [OPTIONS]

  Get aci node management interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  -v, --view [default|addr|nei|verbose]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --empty                         No error on empty result
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\b97f4d860c9d
```

[[Back]](./Interface.md)