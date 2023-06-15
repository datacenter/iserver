# Node Interface

## MACsec

Node selection options:
  - [single node](./InterfaceMacSecNode.md)
  - [selected nodes](./InterfaceMacSecNodes.md)
  - [all nodes](./InterfaceMacSecNodesAll.md)
  - [multi APIC](./InterfaceMacSecNodesApics.md)

Filter options:
  - [Interface ID](./InterfaceMacSecId.md)

View options:
  - [default](./InterfaceMacSecOutputState.md)
  - [verbose](./InterfaceMacSecOutputVerbose.md)

Output options:
  - [default](./InterfaceMacSecOutputState.md)
  - [json](./InterfaceMacSecOutputJson.md)

Command options

```
# iserver get aci intf macsec --help

Usage: iserver.py get aci intf macsec [OPTIONS]

  Get aci node macsec interface

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
  --type [any|leaf|fabric]      [default: any]
  -v, --view [default|verbose]
  -o, --output [default|json]   [default: default]
  --no-cache                    Disable cache
  --empty                       No error on empty result
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\e3c3491022ac
```

[[Back]](./Interface.md)