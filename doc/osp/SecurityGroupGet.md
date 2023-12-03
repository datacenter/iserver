# Security Group

## Command options

Filter options:
  - [name](./SecurityGroupFilterName.md)
  - [tenant](./SecurityGroupFilterTenant.md)
  - [mac](./SecurityGroupFilterMac.md)
  - [vm](./SecurityGroupFilterVm.md)

View options:
  - [state](./SecurityGroupViewState.md)
  - [id](./SecurityGroupViewId.md)
  - [rule](./SecurityGroupViewRule.md)
  - [port](./SecurityGroupViewPort.md)
  - [all](./SecurityGroupViewAll.md)

Output options:
  - [default](./SecurityGroupOutputDefault.md)
  - [json](./SecurityGroupOutputJson.md)

Command options

```
# iserver get osp sg --help

Usage: iserver.py get osp sg [OPTIONS]

  Get osp security group

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by name
  --tenant TEXT                Filter by tenant
  --mac TEXT                   Filter by port mac address
  --vm TEXT                    Filter by virtual machine
  -v, --view TEXT              [state|id|rule|port|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 65 ms and logs saved in /tmp/iserver\f4c49de2e5ba
```

[[Back]](./README.md)