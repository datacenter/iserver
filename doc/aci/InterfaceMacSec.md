# Node Interface

## MACsec

Node selection options:
  - [single node](./InterfaceMacSecNode.md)
  - [selected nodes](./InterfaceMacSecNodes.md)
  - [all nodes](./InterfaceMacSecNodesAll.md)
  - [multi APIC](./InterfaceMacSecNodesApics.md)

Filter options:
  - [Interface ID](./InterfaceMacSecId.md)

Output options:
  - [state](./InterfaceMacSecOutputState.md) (default)
  - [verbose](./InterfaceMacSecOutputVerbose.md)
  - [json](./InterfaceMacSecOutputJson.md)

Command options

```
# iserver get aci intf macsec --help

Usage: iserver.py get aci intf macsec [OPTIONS]

  Get aci node macsec interface

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
  --type [any|leaf|fabric]        [default: any]
  -o, --output [default|verbose|json]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 31 ms and logs saved in /tmp/iserver\bfa9b9f83697
```

[[Back]](./Interface.md)