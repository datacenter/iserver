# Node Protocol - IPv4

## Command options

Filter options:
  - [route type](./ProtocolIpv4FilterType.md)
  - [IP address](./ProtocolIpv4FilterIP.md)
  - [IP subnet](./ProtocolIpv4FilterSubnet.md)
  - [vrf](./ProtocolIpv4FilterVrf.md)

View options:
  - [inst](./ProtocolIpv4ViewInstance.md)
  - [dom](./ProtocolIpv4ViewDomain.md)
  - [route](./ProtocolIpv4ViewRoute.md)
  - [fault](./ProtocolIpv4ViewFault.md)
  - [hfault](./ProtocolIpv4ViewFaultHistory.md)
  - [event](./ProtocolIpv4ViewEvent.md)
  - [diag](./ProtocolIpv4ViewDiag.md)
  - [all](./ProtocolIpv4ViewAll.md)

Output options:
  - [default](./ProtocolIpv4OutputDefault.md)
  - [json](./ProtocolIpv4OutputJson.md)

Command options

```
# iserver get aci proto ipv4 --help

Usage: iserver.py get aci proto ipv4 [OPTIONS]

  Get aci node protocol ipv4

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

Info: finished in 66 ms and logs saved in /tmp/iserver\3aeba073f130
```

[[Back]](./README.md)