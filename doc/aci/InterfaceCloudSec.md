# Node Interface

## CloudSec

Note: Feature *should* work. No environment available to test it (yet).

Node selection options:
  - single node
  - selected nodes
  - all nodes
  - [multi APIC](./InterfaceCloudSecNodesApics.md)

Filter options:
  - Interface ID
  - Admin State
  - Oper State

View options:
  - state
  - verbose

Output options
  - default
  - json

Command options

```
# iserver get aci intf cloudsec --help

Usage: iserver.py get aci intf cloudsec [OPTIONS]

  Get aci node cloudsec interface

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

Info: finished in 30 ms and logs saved in /tmp/iserver\7c2156cbd9a9
```

[[Back]](./Interface.md)