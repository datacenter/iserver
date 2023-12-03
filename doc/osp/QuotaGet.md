# Quota

## Command options

Filter options:
  - [name](./QuotaFilterName.md)

View options:
  - [state](./QuotaViewState.md)

Output options:
  - [default](./QuotaOutputDefault.md)
  - [json](./QuotaOutputJson.md)

Command options

```
# iserver get osp quota --help

Usage: iserver.py get osp quota [OPTIONS]

  Get osp quota

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by tenant name
  -v, --view TEXT              [state]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 25 ms and logs saved in /tmp/iserver\2309bdaeace3
```

[[Back]](./README.md)