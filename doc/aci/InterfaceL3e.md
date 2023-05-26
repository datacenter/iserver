# Node Interface

## Encapsulated Routed

Node selection options:
  - [single node](./InterfaceL3eNode.md)
  - [selected nodes](./InterfaceL3eNodes.md)
  - [all nodes](./InterfaceL3eNodesAll.md)
  - [multi APIC](./InterfaceL3eNodesApics.md)

Filter options:
  - [Interface ID](./InterfaceL3eId.md)
  - [Oper State](./InterfaceL3eState.md)

Output options:
  - [state](./InterfaceL3eOutputState.md) (default)
  - [verbose](./InterfaceL3eOutputVerbose.md)
  - [json](./InterfaceL3eOutputJson.md)

Command options

```
# iserver get aci intf l3e --help

Usage: iserver.py get aci intf l3e [OPTIONS]

  Get aci node encapsulated routed interface

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
  -o, --output [default|verbose|json]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 28 ms and logs saved in /tmp/iserver\299f2d369bbc
```

[[Back]](./Interface.md)