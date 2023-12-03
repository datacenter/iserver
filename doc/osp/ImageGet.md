# Image

## Command options

Filter options:
  - [name](./ImageFilterName.md)
  - [vm](./ImageFilterVm.md)

View options:
  - [state](./ImageViewState.md)
  - [vm](./ImageViewVm.md)
  - [all](./ImageViewAll.md)

Output options:
  - [default](./ImageOutputDefault.md)
  - [json](./ImageOutputJson.md)

Command options

```
# iserver get osp img --help

Usage: iserver.py get osp img [OPTIONS]

  Get osp image

Options:
  --cluster TEXT               Openstack cluster name
  --name TEXT                  Filter by image name
  --vm TEXT                    Filter by virtual machine name
  -v, --view TEXT              [state|id|vm|all]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 58 ms and logs saved in /tmp/iserver\400c9a9ce511
```

[[Back]](./README.md)