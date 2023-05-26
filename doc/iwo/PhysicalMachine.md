# Intersight Workload Optimizer

## Physical Machine (Host)

```
# iserver get iwo phy --help

Usage: iserver.py get iwo phy [OPTIONS]

  Get iwo physical machine

Options:
  --iaccount TEXT              Intersight account  [default: isctl]
  --name TEXT                  Filter by name
  --vm TEXT                    Filter by vm name
  --vdc TEXT                   Filter by vdc name
  --storage TEXT               Filter by storage name
  --stale                      Select stale
  --inactive                   Select inactive
  --critical                   Select critical
  --major                      Select major or critical
  --minor                      Select minor, major or critical
  --show-dep                   Show dependencies
  --show-vm                    Show virtual machines
  --show-vdc                   Show virtual data center
  --show-storage               Show storage
  --show-actions               Show actions
  -o, --output [default|json]  [default: default]
  --verbose                    Verbose output
  --debug                      Debug output
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 39 ms and logs saved in /tmp/iserver\2718492ac80b
```

Usage examples:
- [List of physical machine](../iwo/PhysicalMachineList.md)
- [List of physical machines with dependencies severity summary](../iwo/PhysicalMachineDep.md)
- [Filter by physical machine severity](../iwo/PhysicalMachineSeverity.md)
- [Filter by physical machine name](../iwo/PhysicalMachineName.md)
- [Show virtual machines using physical machine](../iwo/PhysicalMachineVm.md)
- [Filter by virtual machine name](../iwo/PhysicalMachineVmFilter.md)
- [Show virtual data center using physical machine](../iwo/PhysicalMachineVdc.md)
- [Filter by virtual data center name](../iwo/PhysicalMachineVdcFilter.md)
- [Show storaged used by physical machine](../iwo/PhysicalMachineStorage.md)
- [Filter by storage name](../iwo/PhysicalMachineStorageFilter.md)
- [Show selected storage devices with action details](../iwo/PhysicalMachineAction.md)