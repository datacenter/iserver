# Floating IP

## Command options

Filter options:
  - [floating](./FloatingIpFilterFloating.md)
  - [fixed](./FloatingIpFilterFixed.md)
  - [floating-net](./FloatingIpFilterFloatingNet.md)
  - [fixed-net](./FloatingIpFilterFixedNet.md)
  - [mac](./FloatingIpFilterMac.md)
  - [router](./FloatingIpFilterRouter.md)
  - [tenant](./FloatingIpFilterTenant.md)
  - [vm](./FloatingIpFilterVm.md)

View options:
  - [state](./FloatingIpViewState.md)
  - [id](./FloatingIpViewId.md)
  - [all](./FloatingIpViewAll.md)

Output options:
  - [default](./FloatingIpOutputDefault.md)
  - [json](./FloatingIpOutputJson.md)

Command options

```
# iserver get osp fip --help

Usage: iserver.py get osp fip [OPTIONS]

  Get osp floating ip

Options:
  --cluster TEXT               Openstack cluster name
  --floating TEXT              Filter by floating ip address
  --fixed TEXT                 Filter by fixed ip address
  --mac TEXT                   Filter by mac address
  --router TEXT                Filter by router name
  --tenant TEXT                Filter by tenant name
  --floating-net TEXT          Filter by floating network name
  --fixed-net TEXT             Filter by fixed network name
  --vm TEXT                    Filter by vm name
  -v, --view TEXT              [state|id|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 185 ms and logs saved in /tmp/iserver\cb9e0a1b5bed
```

[[Back]](./README.md)