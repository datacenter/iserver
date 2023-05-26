# Servers Inventory

## Full inventory

- all servers in [default](ServersInventoryAllDefault.md), [json](ServersInventoryAllJson.md), [yaml](ServersInventoryAllYaml.md)
- [summary](ServersInventorySummary.md)

## Select servers

Supported filtering options:
- [Type](ServersInventoryType.md)
- [Name](ServersInventoryName.md)
- [Model](ServersInventoryModel.md)
- [Serial number](ServersInventorySerials.md)
- [IP address](ServersInventoryIp.md)
- [Location led on](ServersInventoryLed.md)
- [Powered off](ServersInventoryOff.md)
- [Warnings or Critical Alerts](ServersInventoryHealth.md)
- [Unhealthy fans](ServersInventoryFans.md)
- [Unhealthy psu](ServersInventoryPsu.md)
- [UCSM managed servers](ServersInventoryUcsm.md)
- [Intersight Managed servers](ServersInventoryStandalone.md)
- [Servers with PCI device](ServersInventoryPci.md)
- [CPU-based filtering](ServersInventoryCpu.md)
- [Memory-based filtering](ServersInventoryMemory.md)

## Servers Group

Create named servers group and use them later for filtering or server tasks.
- [Create group](./ServersInventoryGroupSet.md)
- [Get servers in group](./ServersInventoryGroupGet.md)
- [Add servers to group](./ServersInventoryGroupAdd.md)
- [Remove servers from group](./ServersInventoryGroupRemove.md)

## Custom outputs

- use -c|--column options to extend per server information from the base output
- use comma (,) seperation for multiple extra columns
- no limit in extra columns other than your terminal width
- the more information you request, the longer it may take to collect the data

Supported options:
- [Base](ServersInventoryColumnsBase.md)
- [Server ID](ServersInventoryColumnsId.md)
- [Firmware Version](ServersInventoryColumnsFw.md)
- [PCI devices](ServersInventoryColumnsPci.md)
- [Fan state](ServersInventoryColumnsFan.md)
- [Psu state](ServersInventoryColumnsPsu.md)
- [Storage state](ServersInventoryColumnsStorage.md)
- [Power](ServersInventoryColumnsPower.md)
- [Thermal](ServersInventoryColumnsThermal.md)
- [Environmental](ServersInventoryColumnsEnv.md)
- [Multiple](ServersInventoryColumnsMulti.md)
