# Node Protocol

## LLDP

Node selection options:
  - [single node](./ProtocolLldpInstanceNode.md)
  - [selected nodes](./ProtocolLldpInstanceNodes.md)
  - [leaf nodes](./ProtocolLldpInstanceLeaf.md)

Filter options:
  - [device](./ProtocolLldpDevice.md)
  - [mac](./ProtocolLldpMac.md)

Cross domain filter options:
  - [server](./ProtocolLldpServer.md)

View options:
  - [default](./ProtocolLldpInstanceNode.md)
  - [nei](./ProtocolLldpNeighborNodes.md)
  - [stats](./ProtocolLldpOutputVerbose.md)
  - [verbose](./ProtocolLldpOutputVerbose.md)

Output options:
  - [default](./ProtocolLldpInstanceNode.md)
  - [json](./ProtocolLldpOutputJson.md)

Command options

```
# iserver get aci proto lldp --help

Usage: iserver.py get aci proto lldp [OPTIONS]

  Get aci node protocol lldp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --device TEXT                   Filter neighbor by device name
  --mac TEXT                      Filter neighbor by mac address
  --xd TEXT                       Cross domain filter
  -v, --view [default|nei|stats|verbose]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 49 ms and logs saved in /tmp/iserver\0461e2de387e
```

[[Back]](./Protocol.md)