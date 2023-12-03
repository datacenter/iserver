# Intersight Server

## boot view

```
# iserver get server --group test -v boot

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Boot [#8]
---------

+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server                         | Configured Boot Mode | Actual Boot Mode | Secure Boot | Order | Name           | Type     | State    |
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Legacy               | Legacy           | disabled    | 1     | localhdd       | LOCALHDD | Disabled | 
|                                |                      |                  |             | 2     | pxeboot        | PXE      | Disabled | 
|                                |                      |                  |             | 3     | vmedia         | VMEDIA   | Disabled | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Uefi                 | Uefi             | disabled    | 1     | localhdd       | LOCALHDD | Enabled  | 
|                                |                      |                  |             | 2     | pxeboot        | PXE      | Enabled  | 
|                                |                      |                  |             | 3     | vmedia         | VMEDIA   | Enabled  | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Uefi                 | Uefi             | disabled    | 1     | localhdd       | LOCALHDD | Enabled  | 
|                                |                      |                  |             | 2     | pxeboot        | PXE      | Enabled  | 
|                                |                      |                  |             | 3     | vmedia         | VMEDIA   | Enabled  | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| comp3-p4b-eu-spdc-WZP262207UM  | Uefi                 | Uefi             | disabled    | 1     | KVM-Mapped-DVD | VMEDIA   | Enabled  | 
|                                |                      |                  |             | 2     | M2-boot        | LOCALHDD | Enabled  | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| FI-ucsb1-eu-spdc-2-1           | None                 | None             | None        |       |                |          |          | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| FI-ucsb1-eu-spdc-2-2           | None                 | None             | None        |       |                |          |          | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| FI-ucsb1-eu-spdc-2-3           | None                 | None             | None        |       |                |          |          | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| FI-ucsb1-eu-spdc-2-4           | None                 | None             | None        |       |                |          |          | 
+--------------------------------+----------------------+------------------+-------------+-------+----------------+----------+----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v boot

{
    "duration": 19785,
    "isctl": {
        "read": true,
        "calls": 11,
        "success": 11,
        "failed": 0,
        "total_time": 17984
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
        "lines": 45
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:20:10.723249	True	2478	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:20:12.084063	True	1359	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:20:13.623792	True	1476	12	isctl get compute blade   -o json --top 100
2023-12-03 15:20:15.234489	True	1584	4	isctl get bios bootmode --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:20:16.820820	True	1578	0	isctl get bios bootmode --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:20:18.421245	True	1592	4	isctl get boot devicebootmode --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:20:19.898762	True	1469	0	isctl get boot devicebootmode --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:20:21.405956	True	1498	4	isctl get boot devicebootsecurity --filter "ComputePhysical/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:20:23.072506	True	1650	4	isctl get boot hdddevice --filter "Moid in ('60000c0b6176752d35b76e3e', '60000c066176752d35b76c32', '60000c046176752d35b76bd5', '6543c32276752d39014afb27')"  -o json --top 100
2023-12-03 15:20:24.648403	True	1533	3	isctl get boot pxedevice --filter "Moid in ('60000c046176752d35b76bb3', '60000bff6176752d35b769c9', '60000bfd6176752d35b7692a')"  -o json --top 100
2023-12-03 15:20:26.472323	True	1767	4	isctl get boot vmediadevice --filter "Moid in ('6013f1496176752d35458e49', '6013f1466176752d35458cdb', '6013f1486176752d35458daf', '656a0dbf76752d39014f335a')"  -o json --top 100
```

[[Back]](./ServerInventory.md)