# Node Protocol

## IPv4

### IPv4 Route Table

Show IPv4 route table entries for selected nodes.

Node selection options:
  - [single node](./ProtocolIpv4Node.md)
  - [selected nodes](./ProtocolIpv4Nodes.md)

Filter options:
  - [route type](./ProtocolIpv4Type.md)
  - [IP address](./ProtocolIpv4IP.md)
  - [IP subnet](./ProtocolIpv4Subnet.md)
  - [vrf](./ProtocolIpv4Vrf.md)

### IPv4 Route Table Summary

Show IPv4 route table summary for selected nodes.

Node selection options:
  - [single node](./ProtocolIpv4SummaryNode.md)
  - [selected nodes](./ProtocolIpv4SummaryNodes.md)

### Command options

```
# iserver get aci proto ipv4 --help

Usage: iserver.py get aci proto ipv4 [OPTIONS]

  Get aci node protocol ipv4

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --vrf TEXT                      VRF
  --type [ibgp|ebgp|bgp|static|local|direct]
  --ip TEXT                       IP Address filter
  --subnet TEXT                   IP Subnet filter
  --longer                        Match longer prefixes
  -o, --output [route|summary|json]
                                  [default: route]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 28 ms and logs saved in /tmp/iserver\9d618c6edc40
```

[[Back]](./Protocol.md)