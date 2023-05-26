# Intersight Workload Optimizer

## Storage Device

```
# iserver get iwo storage --help

Usage: iserver.py get iwo storage [OPTIONS]

  Get iwo storage device

Options:
  --iaccount TEXT              Intersight account  [default: isctl]
  --name TEXT                  Filter by name
  --vm TEXT                    Filter by vm name
  --phy TEXT                   Filter by phy name
  --stale                      Select stale
  --inactive                   Select inactive
  --critical                   Select critical
  --major                      Select major or critical
  --minor                      Select minor, major or critical
  --show-dep                   Show dependencies
  --show-vm                    Show virtual machines
  --show-phy                   Show physical machines
  --show-actions               Show actions
  -o, --output [default|json]  [default: default]
  --verbose                    Verbose output
  --debug                      Debug output
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\183e7cc1eee5
```

Usage examples:
- [List of storage devices](../iwo/StorageDeviceList.md)
- [List of storage devices with dependencies severity summary](../iwo/StorageDeviceDep.md)
- [Filter by storage device severity](../iwo/StorageDeviceSeverity.md)
- [Filter by storage device name](../iwo/StorageDeviceName.md)
- [Show virtual machines using storage device](../iwo/StorageDeviceVm.md)
- [Filter by virtual machine name](../iwo/StorageDeviceVmFilter.md)
- [Show physical machines using storage device](../iwo/StorageDevicePhy.md)
- [Filter by physical machine name](../iwo/StorageDevicePhyFilter.md)
- [Show selected storage devices With action details](../iwo/StorageDeviceAction.md)