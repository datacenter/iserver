# Node Protocol

## IPv4

Node selection options:
  - [single node](./ProtocolIpv4Node.md)
  - [selected nodes](./ProtocolIpv4Nodes.md)

Filter options:
  - [route type](./ProtocolIpv4Type.md)
  - [IP address](./ProtocolIpv4IP.md)
  - [IP subnet](./ProtocolIpv4Subnet.md)
  - [vrf](./ProtocolIpv4Vrf.md)

View options:
  - [default](./ProtocolIpv4Node.md)
  - [summary](./ProtocolIpv4SummaryNode.md)

Output options:
  - [default](./ProtocolIpv4Node.md)
  - [json](./ProtocolIpv4Json.md)

Command options

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
  --address TEXT                  IP Address filter
  --subnet TEXT                   IP Subnet filter
  --longer                        Match longer prefixes
  -v, --view [default|summary]    [default: default]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 111 ms and logs saved in /tmp/iserver\6960aac78678
```

[[Back]](./Protocol.md)