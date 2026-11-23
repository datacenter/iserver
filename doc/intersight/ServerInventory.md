# Intersight Server Inventory

Use 'get server' command to get servers' details that are connected to Intersight.

Add [filtering options](./ServerFilteringExamples.md) to select subset of servers. All servers are selected by default.

Use view parameter to control the properties to be shown on the screen for the selected servers. State view is selected by default.

## Command options

Base filter options:
  - [name](ServerFilterName.md)
  - [ip](ServerFilterIp.md)
  - [serial](ServerFilterSerial.md)
  - [model](ServerFilterModel.md)
  - [type](ServerFilterType.md)

Advanced filter options:
  - [alarm](ServerFilterAlarm.md)
  - [cpu](ServerFilterCpu.md)
  - [gpu](ServerFilterGpu.md)
  - [disc](ServerFilterDisconnected.md)
  - [fan](ServerFilterFans.md)
  - [led](ServerFilterLed.md)
  - [mac](ServerFilterMac.md)
  - [mem](ServerFilterMemory.md)
  - [mode](ServerFilterMode.md)
  - [pci](ServerFilterPci.md)
  - [pd](ServerFilterPhysicalDisk.md)
  - [power](ServerFilterPower.md)
  - [psu](ServerFilterPsu.md)
  - [sc](ServerFilterStorageController.md)
  - [vd](ServerFilterVirtualDrive.md)

View options with supported output types

Name | Default | JSON | CSV
--- | --- | --- | ---
[adv](./ServerViewAdv.md) | V | V |
[alarm](./ServerViewAlarm.md) | V | V |
[board](./ServerViewBoard.md) | V | V |
[boot](./ServerViewBoot.md) | V | V |
[connector](./ServerViewConnector.md) | V | V |
[contract](./ServerViewContract.md) | V | V | V
[cpu](./ServerViewCpu.md) | V | V |
[env](./ServerViewEnv.md) | V | V |
[fan](./ServerViewFan.md) | V | V |
[fw](./ServerViewFw.md) | V | V |
[gpu](./ServerViewGpu.md) | V | V |
[hcl](./ServerViewHcl.md) | V | V |
[hw](./ServerViewHw.md) | V | V |
[inv](./ServerViewInv.md) | V | V | V
[istate](./ServerViewIstate.md) | V | V |
[kvm](./ServerViewKvm.md) | V | V |
[lic](./ServerViewLic.md) | V | V |
[mem](./ServerViewMem.md) | V | V |
[net](./ServerViewNet.md) | V | V |
[pci](./ServerViewPci.md) | V | V |
[power](./ServerViewPower.md) | V | V |
[profile](./ServerViewProfile.md) | V | V |
[psu](./ServerViewPsu.md) | V | V |
[state (default)](./ServerViewState.md) | V | V |
[storage](./ServerViewStorage.md) | V | V |
[summary](./ServerViewSummary.md) | V | V |
[sw](./ServerViewSw.md) | V | V |
[thermal](./ServerViewThermal.md) | V | V |
[tpm](./ServerViewTpm.md) | V | V |
[workflow](./ServerViewWorkflow.md) | V | V |

Output options:
  - [default](./ServerOutputDefault.md)
  - json
  - csv (using --csv filename)

```
# iserver get server --help

Usage: iserver.py get server [OPTIONS]

  Get server details

Options:
  --iaccount TEXT               Intersight account  [default: demo]
  --ip TEXT                     Select by IP or subnet
  --name TEXT                   Select by name
  --serial TEXT                 Select by serial
  --model TEXT                  Select by model
  --type [any|blade|rack]       Select by type  [default: any]
  --group TEXT                  Select by group name
  --tag TEXT                    Tag filter
  --led [any|on|off]            Filter by locator led state  [default: any]
  --power [any|on|off]          Filter by power state  [default: any]
  --alarm [any|info|warn|crit]  Filter by alarm severity  [default: any]
  --mode [any|imm|ucsm]         Filter by management mode  [default: any]
  --disc                        Filter disconnected
  --cname TEXT                  Chassis name loose match filter
  --cmodel TEXT                 Chassis model loose match filter
  --cserial TEXT                Chassis serial strict match filter
  --cpu TEXT                    CPU filter
  --gpu TEXT                    GPU filter
  --mem TEXT                    Memory filter
  --pci TEXT                    PCI filter
  --mac TEXT                    MAC address filter
  --sc TEXT                     Storage controller filter
  --pd TEXT                     Physical disk filter
  --vd TEXT                     Virtual drive filter
  --fan TEXT                    Fan filter
  --psu TEXT                    Psu filter
  --vc TEXT                     vCenter name
  -v, --view TEXT               [state|adv|alarm|board|boot|connector|contract
                                |cpu|env|fan|fanm|fw|gpu|hcl|hw|inv|istate|kvm
                                |lic|mac|mem|net|pci|power|profile|psu|sc|pd|v
                                d|storage|sw|thermal|tpm|workflow|vc|summary]
                                [default: state]
  --days INTEGER                Last <n> days workflows
  --ttl TEXT                    Cache TTL
  --csv TEXT                    CSV filename supported for selected views
  --set TEXT                    Set as group
  -o, --output [default|json]   [default: default]
  --anonymize                   Anonymized output
  --devel                       Developer output
  --help                        Show this message and exit.
```

## Servers Group

Create named servers group and use them later for filtering or server tasks.
- [Create group](./ServerGroupSet.md)
- [Get servers in group](./ServerGroupGet.md)
- [Add servers to group](./ServerGroupAdd.md)
- [Remove servers from group](./ServerGroupDelete.md)

[[Back]](./README.md)