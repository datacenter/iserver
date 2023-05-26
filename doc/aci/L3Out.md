# L3 Out

Get default properties of [all](./L3OutAllDefault.md) L3Outs in selected APIC.

Filter options:
  - [name](./L3OutName.md)
  - [tenant](./L3OutTenant.md)
  - [vrf](./L3OutVrf.md)
  - [domain](./L3OutDomain.md)
  - [node](./L3OutNode.md)
  - [bgp](./L3OutBgp.md)
  - [eigrp](./L3OutEigrp.md)
  - [ospf](./L3OutOspf.md)
  - [pim](./L3OutPim.md)
  - [mpls](./L3OutMpls.md)

Output options:
  - [default output](./L3OutAllDefault.md)
  - [epg](./L3OutAllEpg.md)
  - [node](./L3OutAllNode.md)
  - [json](./L3OutJson.md)

Command options

```
# iserver get aci l3out --help

Usage: iserver.py get aci l3out [OPTIONS]

  Get aci l3out

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by l3out name
  --tenant TEXT                   Filter by tenant name
  --vrf TEXT                      Filter by vrf name
  --domain TEXT                   Filter by domain name
  --node TEXT                     Filter by node id
  --bgp                           Filter bgp protocol
  --eigrp                         Filter eigrp protocol
  --ospf                          Filter osfp protocol
  --pim                           Filter pim enabled
  --mpls                          Filter mpls enabled
  -o, --output [default|json|epg|node]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\c47393da9e07
```

[[Back]](./README.md)