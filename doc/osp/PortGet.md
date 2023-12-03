# Port

## Command options

Filter options:
  - [name](./PortFilterName.md)
  - [state](./PortFilterState.md)
  - [type](./PortFilterType.md)
  - [tenant](./PortFilterTenant.md)
  - [net](./PortFilterNet.md)
  - [subnet](./PortFilterSubnet.md)
  - [address](./PortFilterAddress.md)
  - [mac](./PortFilterMac.md)
  - [vm](./PortFilterVm.md)
  - [hv](./PortFilterHv.md)
  - [sg](./PortFilterSg.md)

View options:
  - [state](./PortViewState.md)
  - [id](./PortViewId.md)
  - [sec](./PortViewSec.md)
  - [hv](./PortViewHv.md)
  - [all](./PortViewAll.md)

Output options:
  - [default](./PortOutputDefault.md)
  - [json](./PortOutputJson.md)

Command options

```
# iserver get osp port --help

Usage: iserver.py get osp port [OPTIONS]

  Get osp port

Options:
  --cluster TEXT                  Openstack cluster name
  --name TEXT                     Filter by port name
  --state [active|down|any]       [default: any]
  --type [compute|dhcp|floating|gateway|ha|any]
                                  [default: any]
  --tenant TEXT                   Filter by tenant name
  --net TEXT                      Filter by network name
  --subnet TEXT                   Filter by subnet name
  --address TEXT                  Filter by ip address
  --mac TEXT                      Filter by mac address
  --hv TEXT                       Filter by hypervisor
  --vm TEXT                       Filter by virtual machine
  --sg TEXT                       Filter by security group
  -v, --view TEXT                 [state|id|sec|hv|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 36 ms and logs saved in /tmp/iserver\7bbf3ff408d7
```

[[Back]](./README.md)