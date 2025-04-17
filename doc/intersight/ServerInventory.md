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

View options:
  - [adv](./ServerViewAdv.md)
  - [alarm](./ServerViewAlarm.md)
  - [board](./ServerViewBoard.md)
  - [boot](./ServerViewBoot.md)
  - [connector](./ServerViewConnector.md)
  - [contract](./ServerViewContract.md)
  - [cpu](./ServerViewCpu.md)
  - [env](./ServerViewEnv.md)
  - [fan](./ServerViewFan.md)
  - [fw](./ServerViewFw.md)
  - [gpu](./ServerViewGpu.md)
  - [hcl](./ServerViewHcl.md)
  - [hw](./ServerViewHw.md)
  - [inv](./ServerViewInv.md)
  - [istate](./ServerViewIstate.md)
  - [kvm](./ServerViewKvm.md)
  - [lic](./ServerViewLic.md)
  - [mem](./ServerViewMem.md)
  - [net](./ServerViewNet.md)
  - [pci](./ServerViewPci.md)
  - [power](./ServerViewPower.md)
  - [profile](./ServerViewProfile.md)
  - [psu](./ServerViewPsu.md)
  - [state (default)](./ServerViewState.md)
  - [storage](./ServerViewStorage.md)
  - [summary](./ServerViewSummary.md)
  - [sw](./ServerViewSw.md)
  - [thermal](./ServerViewThermal.md)
  - [tpm](./ServerViewTpm.md)
  - [workflow](./ServerViewWorkflow.md)

Output options:
  - [default](./ServerOutputDefault.md)
  - json

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
  --inventory TEXT              Inventory CSV filename
  --set TEXT                    Set as group
  -o, --output [default|json]   [default: default]
  --anonymize                   Anonymized output
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 139 ms and logs saved in /tmp/iserver\50005c7daef0
```

## Servers Group

Create named servers group and use them later for filtering or server tasks.
- [Create group](./ServerGroupSet.md)
- [Get servers in group](./ServerGroupGet.md)
- [Add servers to group](./ServerGroupAdd.md)
- [Remove servers from group](./ServerGroupDelete.md)

[[Back]](./README.md)