# Node Interface

## FC

Note: Feature *should* work. No environment available to test it (yet).

Node selection options:
  - single node
  - selected nodes
  - all nodes
  - [multi APIC](./InterfaceVfcNodesApics.md)

Filter options:
  - Interface ID
  - Admin State
  - Oper State

Output options:
  - state
  - verbose
  - json

Command options

```
# iserver get aci intf vfc --help

Usage: iserver.py get aci intf vfc [OPTIONS]

  Get aci node vfc interface

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

Info: finished in 79 ms and logs saved in /tmp/iserver\064ad8fde0e0
```

[[Back]](./Interface.md)