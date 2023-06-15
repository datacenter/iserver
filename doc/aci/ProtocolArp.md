# Node Protocol

## ARP

Node selection options:
  - [single node](./ProtocolArpNode.md)
  - [selected nodes](./ProtocolArpNodes.md)
  - [leaf nodes](./ProtocolArpLeaf.md)
  - [spine nodes](./ProtocolArpSpine.md)

Filter options:
  - [VRF name](./ProtocolArpVrf.md)
  - [MAC Address](./ProtocolArpMac.md)
  - [IP Address](./ProtocolArpIp.md)
  - [IP Subnet](./ProtocolArpSubnet.md)

View options:
  - [default](./ProtocolArpNode.md)
  - [verbose](./ProtocolArpOutputVerbose.md)

Output options:
  - [default](./ProtocolArpNode.md)
  - [json](./ProtocolArpOutputJson.md)

Command options

```
# iserver get aci proto arp --help

Usage: iserver.py get aci proto arp [OPTIONS]

  Get aci node protocol arp

Options:
  --apic TEXT                   APIC name
  --ip TEXT                     APIC IP
  --username TEXT               APIC Username
  --password TEXT               APIC Password
  --pod TEXT                    Pod ID
  --node TEXT                   Node name patterns
  --role [any|leaf|spine]       [default: any]
  --vrf TEXT                    Filter by VRF name
  --mac TEXT                    Filter by MAC address
  --ip TEXT                     Filter by IP
  --subnet TEXT                 Filter by subnet
  -v, --view [default|verbose]
  -o, --output [default|json]   [default: default]
  --no-cache                    Disable cache
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 131 ms and logs saved in /tmp/iserver\26a247cb18a2
```

[[Back]](./Protocol.md)