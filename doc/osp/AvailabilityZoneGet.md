# Availability Zone

## Command options

Filter options:
  - [name](./AvailabilityZoneFilterName.md)
  - [hv](./AvailabilityZoneFilterHv.md)

View options:
  - [state](./AvailabilityZoneViewState.md)
  - [hv](./AvailabilityZoneViewHv.md)
  - [all](./AvailabilityZoneViewAll.md)

Output options:
  - [default](./AvailabilityZoneOutputDefault.md)
  - [json](./AvailabilityZoneOutputJson.md)

Command options

```
# iserver get osp az --help

Usage: iserver.py get osp az [OPTIONS]

  Get osp availability zone

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by az name
  --hv TEXT                    Filter by hypervisor
  -v, --view TEXT              [state|hv|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 246 ms and logs saved in /tmp/iserver\685a2d48c473
```

[[Back]](./README.md)