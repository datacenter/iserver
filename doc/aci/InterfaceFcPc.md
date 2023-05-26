# Node Interface

## FC PC

Note: Feature *should* work. No environment available to test it (yet).

Node selection options:
  - single node
  - selected nodes
  - all nodes
  - [multi APIC](./InterfaceFcPcNodesApics.md)

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
# iserver get aci intf fcpc --help

Usage: iserver.py get aci intf fcpc [OPTIONS]

  Get aci node fcpc interface

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

Info: finished in 30 ms and logs saved in /tmp/iserver\e9bdfcaac4c8
```

[[Back]](./Interface.md)