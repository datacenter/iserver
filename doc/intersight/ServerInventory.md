# Intersight Server Inventory

## Command options

Base filter options:
  - [name](ServerFilterName.md)
  - [ip](ServerFilterIp.md)
  - [serial](ServerFilterSerials.md)
  - [model](ServerFilterModel.md)
  - [type](ServerFilterType.md)

Other filter options:
  - [alarm](ServerFilterAlarm.md)
  - [cpu](ServerFilterCpu.md)
  - [disconnected](ServerFilterDisconnected.md)
  - [fan](ServerFilterFans.md)
  - [loc](ServerFilterLed.md)
  - [mem](ServerFilterMemory.md)
  - [pci](ServerFilterPci.md)
  - [power](ServerFilterPower.md)
  - [psu](ServerFilterPsu.md)
  - [standalone](ServerFilterStandalone.md)
  - [ucsm](ServerFilterUcsm.md)

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
  - [json](./ServerOutputJson.md)

```
# iserver get server --help

Usage: iserver.py get server [OPTIONS]

  Get server details

Options:
  --iaccount TEXT               Intersight account  [default: isctl]
  --ip TEXT                     Select by IP or subnet
  --name TEXT                   Select by name
  --serial TEXT                 Select by serial
  --model TEXT                  Select by model
  --type [any|blade|rack]       Select by type  [default: any]
  --group TEXT                  Select by group name
  --loc [any|on|off]            Filter by locator led state  [default: any]
  --power [any|on|off]          Filter by power state  [default: any]
  --psu TEXT                    Filter by psu
  --fan                         Filter unhealthy fans
  --alarm [any|info|warn|crit]  Filter by alarm severity  [default: any]
  --ucsm                        Filter UCSM managed
  --disconnected                Filter disconnected
  --standalone                  Filter standalone servers
  --cname TEXT                  Chassis name loose match filter
  --cmodel TEXT                 Chassis model loose match filter
  --cserial TEXT                Chassis serial strict match filter
  --pci TEXT                    Pci model loose match filter
  --mac TEXT                    MAC address loose match filter
  --cpu TEXT                    CPU cores filter
  --mem TEXT                    Memory [GiB] filter
  -v, --view TEXT               [state|adv|alarm|board|boot|connector|contract
                                |cpu|env|fan|fw|gpu|hcl|hw|inv|istate|kvm|lic|
                                mem|net|pci|power|profile|psu|storage|sw|therm
                                al|tpm|workflow|summary]  [default: state]
  --days INTEGER                Last <n> days workflows
  --ttl TEXT                    Cache TTL
  --inventory TEXT              Inventory CSV filename
  --set TEXT                    Set as group
  -o, --output [default|json]   [default: default]
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 87 ms and logs saved in /tmp/iserver\595d0aa97005
```

## Servers Group

Create named servers group and use them later for filtering or server tasks.
- [Create group](./ServerGroupSet.md)
- [Get servers in group](./ServerGroupGet.md)
- [Add servers to group](./ServerGroupAdd.md)
- [Remove servers from group](./ServerGroupRemove.md)

[[Back]](./README.md)