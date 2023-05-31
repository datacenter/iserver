# Node Protocol

## HSRP

Node selection options:
  - [single node](./ProtocolHsrpNode.md)
  - [selected nodes](./ProtocolHsrpInstanceNodes.md)
  - [all nodes](./ProtocolHsrpNodesAll.md)

Filter options:
  - [vrf](./ProtocolHsrpInstanceVrf.md)

View options:
  - [default](./ProtocolHsrpNode.md)
  - [vrf](./ProtocolHsrpInstanceVrf.md)

Output options:
  - [default](./ProtocolHsrpNode.md)
  - [json](./ProtocolHsrpJson.md)

Command options

```
# iserver get aci proto hsrp --help

Usage: iserver.py get aci proto hsrp [OPTIONS]

  Get aci node protocol hsrp

Options:
  --apic TEXT                    APIC name
  --ip TEXT                      APIC IP
  --username TEXT                APIC Username
  --password TEXT                APIC Password
  --pod TEXT                     Pod ID
  --node TEXT                    Node name patterns
  --role [any|leaf|spine]        [default: any]
  --vrf TEXT                     Filter by VRF name
  --id TEXT                      Filter by neighbor
  -v, --view [default|vrf|intf]
  -o, --output [default|json]    [default: default]
  --devel                        Developer output
  --help                         Show this message and exit.

Info: finished in 54 ms and logs saved in /tmp/iserver\7fbed1c0ee6e
```

[[Back]](./Protocol.md)