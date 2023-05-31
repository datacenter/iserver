# Endpoint

Get default properties of [all](./EndpointAll.md) endpoints in selected APIC or in [multi-apic](./EndpointDom.md).

Filter options:
  - [mac](./EndpointMac.md)
  - [ip](./EndpointIp.md)
  - [subnet](./EndpointSubnet.md)
  - [tenant](./EndpointTenant.md)
  - [bridge domain](./EndpointBd.md)
  - [epg](./EndpointEpg.md)
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
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --mac TEXT                      MAC filter
  --address TEXT                  IP address filter
  --subnet TEXT                   IP subnet filter
  --tenant TEXT                   Tenant filter
  --bd TEXT                       Bridge Domain filter
  --epg TEXT                      EPG filter
  --ap TEXT                       App filter
  --vrf TEXT                      VRF filter
  --node TEXT                     Node filter
  --vmm TEXT                      VMM filter
  --hv TEXT                       Hypevisor filter
  --vm TEXT                       VM filter
  --xd TEXT                       Cross domain filter
  -v, --view [default|vm|fabric]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 23 ms and logs saved in /tmp/iserver\585c8268ec6d
```

[[Back]](./README.md)