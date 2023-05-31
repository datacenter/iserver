# Node Protocol

## CDP

Node selection options:
  - [single node](./ProtocolCdpNode.md)
  - [selected nodes](./ProtocolCdpNeighborNodes.md)
  - [all nodes](./ProtocolCdpNodesAll.md)

Filter options:
  - [node local interface](./ProtocolCdpInterfaceName.md)
  - [neighbor system name](./ProtocolCdpNeighborSystem.md)
  - [neighbor platform](./ProtocolCdpNeighborPlatform.md)
  - [neighbor capabilities](./ProtocolCdpNeighborCapabilities.md)
  - [neighbor node local interface](./ProtocolCdpNeighborInterface.md)

View options:
  - [default](./ProtocolCdpNeighborNode.md)
  - [intf](./ProtocolCdpInterfaceNode.md)
  - [instance](./ProtocolCdpNodesAll.md)

Output options:
  - [default](./ProtocolCdpNeighborNode.md)
  - [instance](./ProtocolCdpNodesAll.md)

Command options

```
# iserver get aci proto cdp --help

Usage: iserver.py get aci proto cdp [OPTIONS]

  Get aci node protocol cdp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --sys TEXT                      Filter by system name
  --platform TEXT                 Filter by platform name
  --cap TEXT                      Filter by capabilities
  --intf TEXT                     Filter by interface name
  -v, --view [default|intf|instance]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\1eb7f33483fe
```

[[Back]](./Protocol.md)