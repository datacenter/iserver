# Virtual Routing and Forwarding (VRF)

Get default properties of [all](./VrfAllDefault.md) VRFs in selected APIC.

Filter options:
  - [name](./VrfName.md)
  - [tenant](./VrfTenant.md)
  - [bridge domain](./VrfBridgeDomain.md)
  - [epg](./VrfEpg.md)
  - [subnet](./VrfSubnet.md)
  - [IP address](./VrfIp.md)
  - [l3out](./VrfL3Out.md)

View options:
  - [default](./VrfAllDefault.md)
  - [properties](./VrfAllProps.md)
  - [references](./VrfAllRefs.md)
  - [verbose](./VrfVerbose.md)
  - [route](./VrfRoute.md) output to get route table of selected VRF

Output options:
  - [default](./VrfAllDefault.md)
  - [json](./VrfJson.md)

Command options

```
# iserver get aci vrf --help

Usage: iserver.py get aci vrf [OPTIONS]

  Get aci vrfs

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     VRF name
  --tenant TEXT                   Tenant name
  --bd TEXT                       Filter by bridge domain name
  --epg TEXT                      Filter by epg name
  --ip TEXT                       Filter by subnet with IP
  --subnet TEXT                   Filter by subnet within subnet
  --l3out TEXT                    Filter by l3out name
  -v, --view [default|route|props|refs|verbose]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 32 ms and logs saved in /tmp/iserver\e6631f16bb40
```

[[Back]](./README.md)