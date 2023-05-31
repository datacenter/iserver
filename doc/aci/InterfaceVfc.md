# Node Interface

## VFC

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

View options:
  - default
  - verbose

Output options:
  - default
  - json

Command options

```
# iserver get aci intf vfc --help

Usage: iserver.py get aci intf vfc [OPTIONS]

  Get aci node vfc interface

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

Info: finished in 66 ms and logs saved in /tmp/iserver\42b4599d12a4
```

[[Back]](./Interface.md)