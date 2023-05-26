# Node Protocol

## ND

Node selection options:
  - [single node](./ProtocolNdNode.md)
  - [selected nodes](./ProtocolNdNodes.md)
  - [leaf nodes](./ProtocolNdLeaf.md)

Output options:
  - [instance](./ProtocolNdNode.md) (default)
  - [verbose](./ProtocolNdOutputVerbose.md)
  - [json](./ProtocolNdOutputJson.md)

Command options

```
# iserver get aci proto nd --help

Usage: iserver.py get aci proto nd [OPTIONS]

  Get aci node protocol nd

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  -o, --output [instance|verbose|json]
                                  [default: instance]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 128 ms and logs saved in /tmp/iserver\786cc500dc5a
```

[[Back]](./Protocol.md)