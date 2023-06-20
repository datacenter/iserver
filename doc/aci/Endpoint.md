# Endpoint

Get default properties of [all](./EndpointAll.md) endpoints in selected APIC or in [multi-apic](./EndpointDom.md).

Filter options:
  - [mac](./EndpointMac.md)
  - [ip](./EndpointIp.md)
  - [subnet](./EndpointSubnet.md)
  - [tenant](./EndpointTenant.md)
  - [bridge domain](./EndpointBd.md)
  - [epg](./EndpointEpg.md)
  - [vlan](./EndpointVlan.md)
  - [application profile](./EndpointAp.md)
  - [vrf](./EndpointVrf.md)
  - [node](./EndpointNode.md)
  - [hypervisor](./EndpointHypervisor.md)
  - [vm](./EndpointVm.md)

Cross domain filter options:
  - [server](./EndpointServer.md)

View options:
  - [default](./EndpointAll.md)
  - [fabric](./EndpointOutputFabric.md)
  - [vm](./EndpointOutputVm.md)

Output options:
  - [default](./EndpointAll.md)
  - [json](./EndpointOutputJson.md)

Command options

```
# iserver get aci ep --help

Usage: iserver.py get aci ep [OPTIONS]

  Get aci endpoints

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --mac TEXT                      MAC filter
  --address TEXT                  IP address filter
  --subnet TEXT                   IP subnet filter
  --tenant TEXT                   Tenant filter
  --bd TEXT                       Bridge Domain filter
  --epg TEXT                      EPG filter
  --vlan TEXT                     VLAN filter
  --ap TEXT                       App filter
  --vrf TEXT                      VRF filter
  --node TEXT                     Node filter
  --vmm TEXT                      VMM filter
  --hv TEXT                       Hypevisor filter
  --vm TEXT                       VM filter
  --xd TEXT                       Cross domain filter
  -v, --view [default|vm|fabric]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 48 ms and logs saved in /tmp/iserver\889c7878b94e
```

[[Back]](./README.md)