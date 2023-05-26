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

Output options:
  - [default output](./VrfAllDefault.md)
  - [properties](./VrfAllProps.md)
  - [references](./VrfAllRefs.md)
  - [verbose](./VrfVerbose.md)
  - [route](./VrfRoute.md) output to get route table of selected VRF
  - [json](./VrfJson.md) output

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
  -o, --output [default|json|verbose|route|props|refs]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\192a46014050
```

[[Back]](./README.md)