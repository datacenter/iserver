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

  Output options:
  - [instances](./ProtocolLldpInstanceNode.md) (default)
  - [nei](./ProtocolLldpNeighborNodes.md)
  - [stats](./ProtocolLldpOutputVerbose.md)
  - [verbose](./ProtocolLldpOutputVerbose.md)
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
  -o, --output [instance|nei|stats|verbose|json]
                                  [default: instance]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 41 ms and logs saved in /tmp/iserver\a4a54de83b9a
```

[[Back]](./Protocol.md)