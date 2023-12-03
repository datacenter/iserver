# Snapshot

## Command options

Filter options:
  - [name](./SnapshotFilterName.md)
  - [tenant](./SnapshotFilterTenant.md)
  - [volume](./SnapshotFilterVolume.md)

View options:
  - [state](./SnapshotViewState.md)
  - [id](./SnapshotViewId.md)
  - [all](./SnapshotViewAll.md)

Output options:
  - [default](./SnapshotOutputDefault.md)
  - [json](./SnapshotOutputJson.md)

Command options

```
# iserver get osp snap --help

Usage: iserver.py get osp snap [OPTIONS]

  Get osp snapshot

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by snapshot name
  --tenant TEXT                Filter by tenant name
  --vol TEXT                   Filter by volume name
  -v, --view TEXT              [state|id|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 49 ms and logs saved in /tmp/iserver\c3086991bbba
```

[[Back]](./README.md)