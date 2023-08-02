# Node Protocol - IPv6

## Command options

Filter options:
  - route type
  - IP address
  - IP subnet
  - vrf

View options:
  - [inst](./ProtocolIpv6ViewInstance.md)
  - [dom](./ProtocolIpv6ViewDomain.md)
  - [route](./ProtocolIpv6ViewRoute.md)
  - [fault](./ProtocolIpv6ViewFault.md)
  - [hfault](./ProtocolIpv6ViewFaultHistory.md)
  - [event](./ProtocolIpv6ViewEvent.md)
  - [diag](./ProtocolIpv6ViewDiag.md)
  - [all](./ProtocolIpv6ViewAll.md)

Output options:
  - [default](./ProtocolIpv6OutputDefault.md)
  - [json](./ProtocolIpv6OutputJson.md)

Command options

```
# iserver get aci proto ipv6 --help

Usage: iserver.py get aci proto ipv6 [OPTIONS]

  Get aci node protocol ipv6

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
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
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [inst|dom|route|fault|hfault|event|diag|all]
                                  [default: route]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 66 ms and logs saved in /tmp/iserver\708b3cc6751e
```

[[Back]](./README.md)