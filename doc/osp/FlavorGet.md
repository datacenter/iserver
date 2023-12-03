# Flavor

## Command options

Filter options:
  - [name](./FlavorFilterName.md)
  - [key](./FlavorFilterKey.md)
  - [value](./FlavorFilterValue.md)
  - [vm](./FlavorFilterVm.md)

View options:
  - [state](./FlavorViewState.md)
  - [id](./FlavorViewId.md)
  - [key](./FlavorViewKey.md)
  - [vm](./FlavorViewVm.md)
  - [all](./FlavorViewAll.md)

Output options:
  - [default](./FlavorOutputDefault.md)
  - [json](./FlavorOutputJson.md)

Command options

```
# iserver get osp flv --help

Usage: iserver.py get osp flv [OPTIONS]

  Get osp flavor

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by flavor name
  --vm TEXT                    Filter by virtual machine name
  --key TEXT                   Filter by key
  --value TEXT                 Filter by value
  -v, --view TEXT              [state|key|vm|id|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 106 ms and logs saved in /tmp/iserver\37e35145489a
```

[[Back]](./README.md)