# Node Interface

## Loopback

Node selection options:
  - [single node](./InterfaceLoopbackNode.md)
  - [selected nodes](./InterfaceLoopbackNodes.md)
  - [all nodes](./InterfaceLoopbackNodesAll.md)
  - [multi APIC](./InterfaceLoopbackNodesApics.md)

Filter options:
  - [Interface ID](./InterfaceLoopbackId.md)
  - [IP](./InterfaceLoopbackIp.md)
  - [Subnet](./InterfaceLoopbackSubnet.md)

View options:
  - [default](./InterfaceLoopbackOutputState.md)
  - [verbose](./InterfaceLoopbackOutputVerbose.md)

Output options:
  - [default](./InterfaceLoopbackOutputState.md)
  - [json](./InterfaceLoopbackOutputJson.md)

Command options

```
# iserver get aci intf lb --help

Usage: iserver.py get aci intf lb [OPTIONS]

  Get aci node loobpack interface

Options:
  --apic TEXT                   APIC name
  --ip TEXT                     APIC IP
  --username TEXT               APIC Username
  --password TEXT               APIC Password
  --pod TEXT                    Pod ID
  --node TEXT                   Node name patterns
  --role [any|leaf|spine]       [default: any]
  --id TEXT                     Port name
  --address TEXT                Filter by IP
  --subnet TEXT                 Filter by subnet
  -v, --view [default|verbose]
  -o, --output [default|json]   [default: default]
  --no-cache                    Disable cache
  --empty                       No error on empty result
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 31 ms and logs saved in /tmp/iserver\efa31d2ec039
```

[[Back]](./Interface.md)