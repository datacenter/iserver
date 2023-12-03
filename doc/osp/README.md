# OpenStack

Uses OpenStack API calls to provide the state of OpenStack infrastructure via CLI.

## Cluster

OpenStack cluster must be [pre-defined](./Cluster.md) and then defined on very command using '--cluster <name>' option.

Last used OpenStack cluster name becomes default one.

Example:

```
# iserver get osp az --apic pod1
```

## Usage

Get command structure follows the following rules
- command starts with 'iserver get osp' followed with the object (abbreviated) name
- if no filtering option is defined, all objects are shown
- multiple filtering option can be defined with logic AND rule
- select view (-v) to get different set of properties of selected object
- filtering and view is orthogonal i.e. one can select filtering based property X and select view that does not show property X
- by default human-readable table output is provided
- use -o json to get json output

## Supported Objects

Name | Object | Get | Create | Set | Delete
--- | --- | --- | --- | --- | ---
az | Availability Zone | [link](./AvailabilityZoneGet.md) | -- | -- | --
flv | Flavor | [link](./FlavorGet.md) | -- | -- | --
fip | Floating IP | [link](./FloatingIpGet.md) | -- | -- | --
hv | Hypervisor | [link](./HypervisorGet.md) | -- | -- | --
img | Image | [link](./ImageGet.md) | -- | -- | --
net | Network | [link](./NetworkGet.md) | -- | -- | --
port | Port | [link](./PortGet.md) | -- | -- | --
quota | Quota | [link](./QuotaGet.md) | -- | -- | --
role | Role | [link](./RoleGet.md) | -- | -- | --
rtr | Router | [link](./RouterGet.md) | -- | -- | --
sg | Security Group | [link](./SecurityGroupGet.md) | -- | -- | --
snap | Snapshot | [link](./SnapshotGet.md) | -- | -- | --
sub | Subnet | [link](./SubnetGet.md) | -- | -- | --
tenant | Tenant | [link](./TenantGet.md) | -- | -- | --
user | User | [link](./UserGet.md) | -- | -- | --
vm | Virtual Machine | [link](./VirtualMachineGet.md) | -- | -- | --
vol | Volume | [link](./VolumeGet.md) | -- | -- | --

[[Back]](../../README.md)