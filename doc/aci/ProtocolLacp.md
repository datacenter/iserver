# Node Protocol

## LACP

Node selection options:
  - [single node](./ProtocolLacpInstanceNode.md)
  - [selected nodes](./ProtocolLacpInstanceNodes.md)
  - [leaf nodes](./ProtocolLacpInstanceLeaf.md)

Output options:
  - [instances](./ProtocolLacpInstanceNode.md) (default)
  - [intf](./ProtocolLacpInterfaceNode.md)
  - [stats](./ProtocolLacpOutputVerbose.md)
  - [verbose](./ProtocolLacpOutputVerbose.md)
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
  -o, --output [instance|intf|stats|verbose|json]
                                  [default: instance]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 32 ms and logs saved in /tmp/iserver\4f521cfcea56
```

[[Back]](./Protocol.md)