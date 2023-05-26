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

Output options:
  - [nbr](./ProtocolCdpNeighborNode.md) (default)
  - [intf](./ProtocolCdpInterfaceNode.md)
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
  -o, --output [nbr|intf|instance|json]
                                  [default: nbr]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 34 ms and logs saved in /tmp/iserver\a11071786566
```

[[Back]](./Protocol.md)