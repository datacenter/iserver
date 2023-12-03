# Router

## Command options

Filter options:
  - [name](./RouterFilterName.md)

View options:
  - [state](./RouterViewState.md)
  - [id](./RouterViewId.md)
  - [port](./RouterViewPort.md)
  - [all](./RouterViewAll.md)

Output options:
  - [default](./RouterOutputDefault.md)
  - [json](./RouterOutputJson.md)

Command options

```
# iserver get osp rtr --help

Usage: iserver.py get osp rtr [OPTIONS]

  Get osp router

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by router name
  -v, --view TEXT              [state|id|port|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 40 ms and logs saved in /tmp/iserver\a9472323f844
```

[[Back]](./README.md)