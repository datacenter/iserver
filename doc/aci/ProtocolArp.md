# Node Protocol - ARP

## Command options

Filter options:
  - [VRF name](./ProtocolArpFilterVrf.md)
  - [MAC Address](./ProtocolArpFilterMac.md)
  - [IP Address](./ProtocolArpFilterIp.md)
  - [IP Subnet](./ProtocolArpFilterSubnet.md)

View options:
  - [inst](./ProtocolArpViewInstance.md)
  - [dom](./ProtocolArpViewDomain.md)
  - [adj](./ProtocolArpViewAdjacency.md)
  - [fault](./ProtocolArpViewFault.md)
  - [hfault](./ProtocolArpViewFaultHistory.md)
  - [event](./ProtocolArpViewEvent.md)
  - [diag](./ProtocolArpViewDiag.md)
  - [all](./ProtocolArpViewAll.md)

Output options:
  - [default](./ProtocolArpOutputDefault.md)
  - [json](./ProtocolArpOutputJson.md)

Command options

```
# iserver get aci proto arp --help

Usage: iserver.py get aci proto arp [OPTIONS]

  Get aci node protocol arp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --vrf TEXT                      Filter by VRF name
  --mac TEXT                      Filter by MAC address
  --ip TEXT                       Filter by IP
  --subnet TEXT                   Filter by subnet
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [inst|dom|adj|fault|hfault|event|diag|all]
                                  [default: adj]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\c2ceaafaf965
```

[[Back]](./README.md)