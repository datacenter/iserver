# Subnet

## Command options

Filter options:
  - [name](./SubnetFilterName.md)
  - [tenant](./SubnetFilterTenant.md)
  - [address](./SubnetFilterAddress.md)
  - [mac](./SubnetFilterMac.md)
  - [vm](./SubnetFilterVm.md)
  - [hv](./SubnetFilterHv.md)

View options:
  - [state](./SubnetViewState.md)
  - [id](./SubnetViewId.md)
  - [port](./SubnetViewPort.md)
  - [all](./SubnetViewAll.md)

Output options:
  - [default](./SubnetOutputDefault.md)
  - [json](./SubnetOutputJson.md)

Command options

```
# iserver get osp sub --help

Usage: iserver.py get osp sub [OPTIONS]

  Get osp subnet

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by subnet name
  --tenant TEXT                Filter by tenant name
  --address TEXT               Filter by ip address
  --mac TEXT                   Filter by mac address
  --vm TEXT                    Filter by virtual machine
  --hv TEXT                    Filter by hypervisor
  -v, --view TEXT              [state|id|port|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 61 ms and logs saved in /tmp/iserver\5a659e6006e1
```

[[Back]](./README.md)