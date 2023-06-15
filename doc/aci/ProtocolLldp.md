# Node Protocol

## LLDP

Node selection options:
  - [single node](./ProtocolLldpInstanceNode.md)
  - [selected nodes](./ProtocolLldpInstanceNodes.md)
  - [leaf nodes](./ProtocolLldpInstanceLeaf.md)

Filter options:
  - [device](./ProtocolLldpDevice.md)
  - [mac](./ProtocolLldpMac.md)
  - [server](./ProtocolLldpServer.md)

View options:
  - [summary](./ProtocolLldpInstanceNode.md)
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
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --device TEXT                   Filter neighbor by device name
  --mac TEXT                      Filter neighbor by mac address
  --xd TEXT                       Cross domain filter
  -v, --view [summary|stats|nei|verbose]
                                  [default: nei]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 39 ms and logs saved in /tmp/iserver\122cc0e3e946
```

[[Back]](./Protocol.md)