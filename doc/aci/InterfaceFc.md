# Node Interface

## FC

Note: Feature *should* work. No environment available to test it (yet).

Node selection options:
  - single node
  - selected nodes
  - all nodes
  - [multi APIC](./InterfaceFcNodesApics.md)

Filter options:
  - Interface ID
  - Admin State
  - Oper State

View options:
  - state
  - verbose

Output options:
  - default
  - json

Command options

```
# iserver get aci intf fc --help

Usage: iserver.py get aci intf fc [OPTIONS]

  Get aci node fc interface

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --pod TEXT                   Pod ID
  --node TEXT                  Node name patterns
  --role [any|leaf|spine]      [default: any]
  --id TEXT                    Port name
  --admin [any|up|down]        [default: any]
  --oper [any|up|down]         [default: any]
  -o, --output [default|json]  [default: default]
  --empty                      No error on empty result
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 38 ms and logs saved in /tmp/iserver\465b3d6a9fdf
```

[[Back]](./Interface.md)