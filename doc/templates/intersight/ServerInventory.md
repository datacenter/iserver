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
DOC_TEMPLATE:get_server_filter.help:output
```

## Servers Group

Create named servers group and use them later for filtering or server tasks.
- [Create group](./ServerGroupSet.md)
- [Get servers in group](./ServerGroupGet.md)
- [Add servers to group](./ServerGroupAdd.md)
- [Remove servers from group](./ServerGroupRemove.md)

[[Back]](./README.md)