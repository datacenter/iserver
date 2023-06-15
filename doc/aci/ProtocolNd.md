# Node Protocol

## ND

Node selection options:
  - [single node](./ProtocolNdNode.md)
  - [selected nodes](./ProtocolNdNodes.md)
  - [leaf nodes](./ProtocolNdLeaf.md)

View options:
  - [default](./ProtocolNdNode.md)
  - [verbose](./ProtocolNdOutputVerbose.md)

Output options:
  - [default](./ProtocolNdNode.md)
  - [json](./ProtocolNdOutputJson.md)

Command options

```
# iserver get aci proto nd --help

Usage: iserver.py get aci proto nd [OPTIONS]

  Get aci node protocol nd

Options:
  --apic TEXT                   APIC name
  --ip TEXT                     APIC IP
  --username TEXT               APIC Username
  --password TEXT               APIC Password
  --pod TEXT                    Pod ID
  --node TEXT                   Node name patterns
  --role [any|leaf|spine]       [default: any]
  -v, --view [default|verbose]  [default: default]
  -o, --output [default|json]   [default: default]
  --no-cache                    Disable cache
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 74 ms and logs saved in /tmp/iserver\2df81750041d
```

[[Back]](./Protocol.md)