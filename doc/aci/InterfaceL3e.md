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

View options:
  - [default](./InterfaceL3eNode.md)
  - [verbose](./InterfaceL3eOutputVerbose.md)

Output options:
  - [default](./InterfaceL3eOutputState.md)
  - [json](./InterfaceL3eOutputJson.md)

Command options

```
# iserver get aci intf l3e --help

Usage: iserver.py get aci intf l3e [OPTIONS]

  Get aci node encapsulated routed interface

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
  -v, --view [default|verbose]
  -o, --output [default|json]   [default: default]
  --no-cache                    Disable cache
  --empty                       No error on empty result
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 37 ms and logs saved in /tmp/iserver\92e56e200f45
```

[[Back]](./Interface.md)