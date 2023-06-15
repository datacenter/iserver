# Node Protocol

## LACP

Node selection options:
  - [single node](./ProtocolLacpInstanceNode.md)
  - [selected nodes](./ProtocolLacpInstanceNodes.md)
  - [leaf nodes](./ProtocolLacpInstanceLeaf.md)

View options:
  - [default](./ProtocolLacpInstanceNode.md)
  - [intf](./ProtocolLacpInterfaceNode.md)
  - [stats](./ProtocolLacpOutputVerbose.md)
  - [verbose](./ProtocolLacpOutputVerbose.md)

Output options:
  - [default](./ProtocolLacpInstanceNode.md)
  - [json](./ProtocolLacpOutputJson.md)

Command options

```
# iserver get aci proto lacp --help

Usage: iserver.py get aci proto lacp [OPTIONS]

  Get aci node protocol lacp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  -v, --view [default|intf|stats|verbose]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 231 ms and logs saved in /tmp/iserver\704b95e76e1e
```

[[Back]](./Protocol.md)