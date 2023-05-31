# Bridge Domain (BD)

Get default properties of [all](./BridgeDomainAllDefault.md) BDs in selected APIC.

Filter options:
  - [name](./BridgeDomainName.md)
  - [tenant](./BridgeDomainTenant.md)
  - [vrf](./BridgeDomainVrf.md)
  - [epg](./BridgeDomainEpg.md)
  - [subnet](./BridgeDomainSubnet.md)
  - [IP address](./BridgeDomainIp.md)
  - [l3out](./BridgeDomainL3Out.md)

View options:
  - [default](./BridgeDomainAllDefault.md)
  - [l2 properties](./BridgeDomainAllL2.md)
  - [l3 properties](./BridgeDomainAllL3.md)
  - [mcast properties](./BridgeDomainAllMcast.md)
  - [vrf properties](./BridgeDomainAllVrf.md)
  - [verbose](./BridgeDomainVerbose.md)

Output options:
  - [default](./BridgeDomainAllDefault.md)
  - [json](./BridgeDomainJson.md)

Command options

```
# iserver get aci bd --help

Usage: iserver.py get aci bd [OPTIONS]

  Get aci bridge domain

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by bridge domain name
  --tenant TEXT                   Filter by tenant name
  --vrf TEXT                      Filter by vrf name
  --epg TEXT                      Filter by epg name
  --ip TEXT                       Filter by subnet with IP
  --subnet TEXT                   Filter by subnet within subnet
  --l3out TEXT                    Filter by l3out name
  -v, --view [default|l2|l3|mcast|vrf|verbose]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\f48ffc45dbc8
```

[[Back]](./README.md)