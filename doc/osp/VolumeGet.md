# Volume

## Command options

Filter options:
  - [name](./VolumeFilterName.md)
  - [tenant](./VolumeFilterTenant.md)
  - [hv](./VolumeFilterHv.md)
  - [vm](./VolumeFilterVm.md)

View options:
  - [state](./VolumeViewState.md)
  - [id](./VolumeViewId.md)
  - [all](./VolumeViewAll.md)

Output options:
  - [default](./VolumeOutputDefault.md)
  - [json](./VolumeOutputJson.md)

Command options

```
# iserver get osp vol --help

Usage: iserver.py get osp vol [OPTIONS]

  Get osp volume

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by name
  --tenant TEXT                Filter by tenant name
  --hv TEXT                    Filter by hypervisor
  --vm TEXT                    Filter by virtual machine
  -v, --view TEXT              [state|id|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 70 ms and logs saved in /tmp/iserver\0478614ffe02
```

[[Back]](./README.md)