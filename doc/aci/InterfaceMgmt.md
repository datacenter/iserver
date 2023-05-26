# Node Interface

## Management

Node selection options:
  - [single node](./InterfaceMgmtNode.md)
  - [selected nodes](./InterfaceMgmtNodes.md)
  - [all nodes](./InterfaceMgmtNodesAll.md)
  - [multi APIC](./InterfaceMgmtNodesApics.md)

Output options:
  - [state](./InterfaceMgmtOutputState.md) (default)
  - [address](./InterfaceMgmtOutputAddress.md)
  - [neighbor](./InterfaceMgmtOutputNeighbor.md)
  - [verbose](./InterfaceMgmtOutputVerbose.md)
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
  -o, --output [state|addr|nei|verbose|json]
                                  [default: state]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 31 ms and logs saved in /tmp/iserver\15e7b2bebbc7
```

[[Back]](./Interface.md)