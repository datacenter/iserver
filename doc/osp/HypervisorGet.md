# Hypervisor

## Command options

Filter options:
  - [name](./HypervisorFilterName.md)
  - [address](./HypervisorFilterAddress.md)
  - [vm](./HypervisorFilterVm.md)

View options:
  - [state](./HypervisorViewState.md)
  - [vm](./HypervisorViewVm.md)
  - [all](./HypervisorViewAll.md)

Output options:
  - [default](./HypervisorOutputDefault.md)
  - [json](./HypervisorOutputJson.md)

Command options

```
# iserver get osp hv --help

Usage: iserver.py get osp hv [OPTIONS]

  Get osp hypervisor

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by name
  --address TEXT               Filter by ip address
  --vm TEXT                    Filter by virtual machine
  -v, --view TEXT              [state|vm|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 61 ms and logs saved in /tmp/iserver\30efda06698e
```

[[Back]](./README.md)