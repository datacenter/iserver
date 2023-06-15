# Node Protocol

## IPv6

Node selection options:
  - [single node](./ProtocolIpv6SummaryNode.md)
  - [selected nodes](./ProtocolIpv6SummaryNodes.md)

Filter options:
  - route type
  - IP address
  - IP subnet
  - vrf

View options:
  - default
  - [summary](./ProtocolIpv6SummaryNode.md)

Output options:
  - [default](./ProtocolIpv6SummaryNode.md)
  - [json](./ProtocolIpv6Json.md)

Command options

```
# iserver get aci proto ipv6 --help

Usage: iserver.py get aci proto ipv6 [OPTIONS]

  Get aci node protocol ipv6

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

Info: finished in 62 ms and logs saved in /tmp/iserver\26185e796382
```

[[Back]](./Protocol.md)