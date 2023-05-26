# Node Protocol

## IPv6

### IPv6 Route Table Summary

Show IPv6 route table summary for selected nodes.

Node selection options:
  - [single node](./ProtocolIpv6SummaryNode.md)
  - [selected nodes](./ProtocolIpv6SummaryNodes.md)

### Command options

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
  --ip TEXT                       IP Address filter
  --subnet TEXT                   IP Subnet filter
  --longer                        Match longer prefixes
  -o, --output [route|summary|json]
                                  [default: route]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 32 ms and logs saved in /tmp/iserver\dc0442209a60
```

[[Back]](./Protocol.md)