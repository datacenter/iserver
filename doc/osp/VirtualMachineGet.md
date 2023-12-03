# Virtual Machine

## Command options

Filter options:
  - [name](./VirtualMachineFilterName.md)
  - [tenant](./VirtualMachineFilterTenant.md)
  - [img](./VirtualMachineFilterImg.md)
  - [flv](./VirtualMachineFilterFlv.md)
  - [net](./VirtualMachineFilterNet.md)
  - [address](./VirtualMachineFilterAddress.md)
  - [mac](./VirtualMachineFilterMac.md)
  - [hv](./VirtualMachineFilterHv.md)

View options:
  - [state](./VirtualMachineViewState.md)
  - [id](./VirtualMachineViewId.md)
  - [net](./VirtualMachineViewNet.md)
  - [all](./VirtualMachineViewAll.md)

Output options:
  - [default](./VirtualMachineOutputDefault.md)
  - [json](./VirtualMachineOutputJson.md)

Command options

```
# iserver get osp vm --help

Usage: iserver.py get osp vm [OPTIONS]

  Get osp virtual machine

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by name
  --tenant TEXT                Filter by tenant
  --img TEXT                   Filter by image
  --flv TEXT                   Filter by flavor
  --net TEXT                   Filter by network
  --address TEXT               Filter by ip address
  --mac TEXT                   Filter by mac address
  --hv TEXT                    Filter by hypervisor
  -v, --view TEXT              [state|id|net|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 40 ms and logs saved in /tmp/iserver\a46331a1d64c
```

[[Back]](./README.md)