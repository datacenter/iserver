# Intersight Server

## Filter by alarm level

- Allowed values: any (default), info, warn, crit
- 'any' selects all servers
- 'info' value select servers with alarms of at least info severity

```
# iserver get server --alarm info -v alarm

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Alarm [#22]
-----------

+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| Server                        | Severity | Description                              | Create Time              | Affected Type                  | Affected Name                                                                            |
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
|  C220-WZP23350ZAQ             | Warning  | Storage Virtual Drive 0 Degraded:        | 2023-09-14T01:00:19.684Z | storage.VirtualDrive           | C220-WZP23350ZAQ/sys/rack-unit-1/board/storage-SAS-MRAID/vd-0                            | 
|                               |          | please check the storage controller, or  |                          |                                |                                                                                          | 
|                               |          | reseat the storage drive                 |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
|  C220-WZP23350ZAQ             | Warning  | HDD6_STATUS: Storage Local disk is       | 2023-10-19T09:20:31.997Z | compute.Board                  | C220-WZP23350ZAQ/sys/rack-unit-1/board                                                   | 
|                               |          | degraded: please take appropriate        |                          |                                |                                                                                          | 
|                               |          | action by checking the detailed drive    |                          |                                |                                                                                          | 
|                               |          | status                                   |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| ant1-eu-spdc-FCH2017V2GH      | Info     | Flex Flash Local disk 2 is inoperable:   | 2023-02-14T12:59:38.667Z | storage.FlexFlashPhysicalDrive | ant1-eu-spdc-FCH2017V2GH/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2      | 
|                               |          | reseat or replace the local disk 2       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| apic22-eu-spdc-WMP2519006W    | Warning  | HDD2_STATUS: Storage Local disk is       | 2023-11-23T10:38:29.999Z | compute.Board                  | apic22-eu-spdc-WMP2519006W/sys/rack-unit-1/board                                         | 
|                               |          | degraded: please take appropriate        |                          |                                |                                                                                          | 
|                               |          | action by checking the detailed drive    |                          |                                |                                                                                          | 
|                               |          | status                                   |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| apic22-eu-spdc-WMP2519006W    | Warning  | Storage Local disk 2 is degraded:        | 2023-11-23T10:39:44.089Z | storage.PhysicalDisk           | apic22-eu-spdc-WMP2519006W/sys/rack-unit-1/board/storage-SAS-MRAID/pd-2                  | 
|                               |          | please take appropriate action by        |                          |                                |                                                                                          | 
|                               |          | checking the detailed drive status       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| berlin-ucsm-3                 | Info     | Log capacity on Management Controller    | 2022-09-02T07:11:00.22Z  | management.Controller          | berlin-ucsm/sys/rack-unit-3/mgmt/log-SEL-0                                               | 
|                               |          | on server 3  is full                     |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| berlin-ucsm-4                 | Info     | Log capacity on Management Controller    | 2023-11-16T08:54:06.468Z | management.Controller          | berlin-ucsm/sys/rack-unit-4/mgmt/log-SEL-0                                               | 
|                               |          | on server 4  is low                      |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| berlin-ucsm-5                 | Info     | Log capacity on Management Controller    | 2022-07-20T14:29:25.042Z | management.Controller          | berlin-ucsm/sys/rack-unit-5/mgmt/log-SEL-0                                               | 
|                               |          | on server 5  is full                     |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| berlin-ucsm-5                 | Critical | Server 5 (service profile:               | 2023-11-16T08:54:06.435Z | management.Controller          | berlin-ucsm/sys/rack-unit-5/mgmt/actual-mount-list/actual-mount-entry-1                  | 
|                               |          | org-root/ls-esxi-245) vmedia mapping     |                          |                                |                                                                                          | 
|                               |          | rhcos-live has  failed.                  |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| berlin-ucsm-6                 | Critical | Server 6 (service profile:               | 2023-11-16T08:54:06.808Z | management.Controller          | berlin-ucsm/sys/rack-unit-6/mgmt/actual-mount-list/actual-mount-entry-1                  | 
|                               |          | org-root/ls-openstack-243) vmedia        |                          |                                |                                                                                          | 
|                               |          | mapping rhcos-live has  failed.          |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| berlin-ucsm-8                 | Critical | Server 8 (service profile:               | 2023-11-16T08:54:06.867Z | management.Controller          | berlin-ucsm/sys/rack-unit-8/mgmt/actual-mount-list/actual-mount-entry-1                  | 
|                               |          | org-root/ls-openstack-249) vmedia        |                          |                                |                                                                                          | 
|                               |          | mapping rhcos-live has  failed.          |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| comp3-p3b-eu-spdc-FCH2017V1J5 | Info     | SEL_FULLNESS: System Event log capacity  | 2023-12-01T17:05:02.016Z | management.Controller          | comp3-p3b-eu-spdc-FCH2017V1J5/sys/rack-unit-1/mgmt/log-SEL-0                             | 
|                               |          | is very low                              |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| comp7-p3b-eu-spdc-FCH2023V2A4 | Info     | Flex Flash Local disk 2 is inoperable:   | 2022-11-24T11:40:33.912Z | storage.FlexFlashPhysicalDrive | comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2 | 
|                               |          | reseat or replace the local disk 2       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| esx13-eu-spdc-FCH2018V027     | Info     | Flex Flash Local disk 2 is inoperable:   | 2022-11-22T11:12:55.559Z | storage.FlexFlashPhysicalDrive | esx13-eu-spdc-FCH2018V027/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2     | 
|                               |          | reseat or replace the local disk 2       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| esx21-eu-spdc-WZP23440N1P     | Critical | PS_RDNDNT_MODE: Power Supply redundancy  | 2023-11-14T15:31:20.403Z | compute.RackUnit               | esx21-eu-spdc-WZP23440N1P/sys/rack-unit-1                                                | 
|                               |          | is lost : Check Redundancy Policy or     |                          |                                |                                                                                          | 
|                               |          | reseat/replace Power Supply              |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| esx21-eu-spdc-WZP23440N1P     | Critical | PSU2_STATUS: Power Supply 2 has lost     | 2023-11-14T15:33:11.588Z | equipment.Psu                  | esx21-eu-spdc-WZP23440N1P/sys/rack-unit-1/psu-2                                          | 
|                               |          | input or input is out of range : Check   |                          |                                |                                                                                          | 
|                               |          | input to PS or replace PS 2              |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| esx92-eu-spdc-FCH2017V2AF     | Info     | Flex Flash Local disk 2 is inoperable:   | 2021-09-15T09:57:33.306Z | storage.FlexFlashPhysicalDrive | esx92-eu-spdc-FCH2017V2AF/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2     | 
|                               |          | reseat or replace the local disk 2       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| esx94-eu-spdc-FCH2017V2AH     | Info     | Flex Flash Local disk 2 is inoperable:   | 2021-09-15T09:58:51.244Z | storage.FlexFlashPhysicalDrive | esx94-eu-spdc-FCH2017V2AH/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2     | 
|                               |          | reseat or replace the local disk 2       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| esx96-eu-spdc-FCH2016V2FX     | Info     | SEL_FULLNESS: System Event log capacity  | 2023-07-14T15:20:36.615Z | management.Controller          | esx96-eu-spdc-FCH2016V2FX/sys/rack-unit-1/mgmt/log-SEL-0                                 | 
|                               |          | is low                                   |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| mgmt-p1-eu-spdc-WZP2252176Z   | Critical | Storage Local disk 8 is degraded:        | 2023-11-06T15:07:34.195Z | storage.PhysicalDisk           | mgmt-p1-eu-spdc-WZP2252176Z/sys/rack-unit-1/board/storage-SAS-MRAID/pd-8                 | 
|                               |          | please take appropriate action by        |                          |                                |                                                                                          | 
|                               |          | checking the detailed drive status       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| mgmt-p4a-eu-spdc-WZP22520Y9D  | Critical | Storage Local disk 8 is degraded:        | 2023-09-26T06:33:47.177Z | storage.PhysicalDisk           | mgmt-p4a-eu-spdc-WZP22520Y9D/sys/rack-unit-1/board/storage-SAS-MRAID/pd-8                | 
|                               |          | please take appropriate action by        |                          |                                |                                                                                          | 
|                               |          | checking the detailed drive status       |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+
| POD-4A-AIO-1-WZP23400AK9      | Critical | ADDDC Bank-level adaptive virtual        | 2023-11-12T07:49:23.299Z | memory.Unit                    | POD-4A-AIO-1-WZP23400AK9/sys/rack-unit-1/board/memarray-1/mem-11                         | 
|                               |          | lockstep is activated on DIMM            |                          |                                |                                                                                          | 
|                               |          | DDR4_P1_F1_ECC. Post Package Repair      |                          |                                |                                                                                          | 
|                               |          | will be performed on this DIMM during    |                          |                                |                                                                                          | 
|                               |          | the next system reboot.                  |                          |                                |                                                                                          | 
+-------------------------------+----------+------------------------------------------+--------------------------+--------------------------------+------------------------------------------------------------------------------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --alarm info -v alarm

{
    "duration": 19851,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11766
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 353
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:10:30.518917	True	2857	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:10:32.073596	True	1551	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:10:33.781951	True	1652	12	isctl get compute blade   -o json --top 100
2023-12-03 15:10:36.052615	True	1824	100	isctl get cond alarm   -o json --top 100
2023-12-03 15:10:38.021624	True	1965	100	isctl get cond alarm   -o json --top 100 --skip 100
2023-12-03 15:10:39.941519	True	1917	91	isctl get cond alarm   -o json --top 100 --skip 200
```

[[Back]](./ServerInventory.md)