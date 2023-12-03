# Network

## Command options

Filter options:
  - [name](./NetworkFilterName.md)
  - [tenant](./NetworkFilterTenant.md)
  - [address](./NetworkFilterAddress.md)
  - [mac](./NetworkFilterMac.md)
  - [vm](./NetworkFilterVm.md)
  - [hv](./NetworkFilterHv.md)
  - [vlan](./NetworkFilterVlan.md)

View options:
  - [state](./NetworkViewState.md)
  - [id](./NetworkViewId.md)
  - [port](./NetworkViewPort.md)
  - [phy](./NetworkViewPhy.md)
  - [all](./NetworkViewAll.md)

Output options:
  - [default](./NetworkOutputDefault.md)
  - [json](./NetworkOutputJson.md)

Command options

```
# iserver get osp net --help

Usage: iserver.py get osp net [OPTIONS]

  Get osp network

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by network name
  --tenant TEXT                Filter by tenant name
  --address TEXT               Filter by ip address
  --mac TEXT                   Filter by mac address
  --vm TEXT                    Filter by virtual machine
  --hv TEXT                    Filter by hypervisor
  --vlan TEXT                  Filter by vlan
  -v, --view TEXT              [state|id|port|phy|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 48 ms and logs saved in /tmp/iserver\6e59104443b7
```

[[Back]](./README.md)