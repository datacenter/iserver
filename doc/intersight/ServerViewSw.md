# Intersight Server

## sw view

```
# iserver get server --group test -v sw

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Firmware [#8]
-------------

+--------------------------------+-----------------+-----------+------------------+----------------+---------+--------------------------------------+
| Server                         | Name            | Component | Type             | PackageVersion | Version | Dn                                   |
+--------------------------------+-----------------+-----------+------------------+----------------+---------+--------------------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | CIMC Controller | system    | blade-controller |                | 4.2(2a) | sys/rack-unit-1/mgmt/fw-system       | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | CIMC Controller | system    | blade-controller |                | 4.2(2a) | sys/rack-unit-1/mgmt/fw-system       | 
| comp-3-p2b-eu-spdc-WZP23400AKL | CIMC Controller | system    | blade-controller |                | 4.2(3d) | sys/rack-unit-1/mgmt/fw-system       | 
| comp3-p4b-eu-spdc-WZP262207UM  | CIMC Controller | system    | blade-controller |                | 4.2(3h) | sys/rack-unit-1/mgmt/fw-system       | 
| FI-ucsb1-eu-spdc-2-1           | CIMC Controller | system    | blade-controller | 4.2(3d)B       | 4.2(3c) | sys/chassis-2/blade-1/mgmt/fw-system | 
| FI-ucsb1-eu-spdc-2-2           | CIMC Controller | system    | blade-controller | 4.2(3d)B       | 4.2(3c) | sys/chassis-2/blade-2/mgmt/fw-system | 
| FI-ucsb1-eu-spdc-2-3           | CIMC Controller | system    | blade-controller | 4.2(3d)B       | 4.2(3c) | sys/chassis-2/blade-3/mgmt/fw-system | 
| FI-ucsb1-eu-spdc-2-4           | CIMC Controller | system    | blade-controller | 4.2(3d)B       | 4.2(3c) | sys/chassis-2/blade-4/mgmt/fw-system | 
+--------------------------------+-----------------+-----------+------------------+----------------+---------+--------------------------------------+

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

KVM [#8]
--------

+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| Server                         | Kvm Server Enabled | Kvm Vendor    | Tunneled Kvm | Address Name | Address     | Subnet          | Gateway     | Http Port | Https Port | Kvm Port | Kvm Vlan |
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | False              | Avocent       | True         | Outband      | 10.58.50.41 | 255.255.255.224 | 10.58.50.62 | 80        | 443        | 2068     | 1        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | False              | Avocent       | True         | Outband      | 10.58.50.42 | 255.255.255.224 | 10.58.50.62 | 80        | 443        | 2068     | 1        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| comp-3-p2b-eu-spdc-WZP23400AKL | False              | Avocent       | False        | Outband      | 10.58.50.43 | 255.255.255.224 | 10.58.50.62 | 80        | 443        | 2068     | 1        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| comp3-p4b-eu-spdc-WZP262207UM  | True               | Cisco Systems | False        | Outband      | 10.58.53.35 | 255.255.255.224 | 10.58.53.62 | 80        | 443        | 2068     | 1        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| FI-ucsb1-eu-spdc-2-1           | False              |               | False        | Outband      | 10.58.52.41 | 255.255.255.224 | 10.58.52.62 | 80        | 443        | 2068     | 0        | 
|                                |                    |               |              | Outband      | 10.58.26.5  | 255.255.255.192 | 10.58.26.62 | 80        | 443        | 2068     | 0        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| FI-ucsb1-eu-spdc-2-2           | False              |               | False        | Outband      | 10.58.52.42 | 255.255.255.224 | 10.58.52.62 | 80        | 443        | 2068     | 0        | 
|                                |                    |               |              | Outband      | 10.58.26.6  | 255.255.255.192 | 10.58.26.62 | 80        | 443        | 2068     | 0        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| FI-ucsb1-eu-spdc-2-3           | False              |               | False        | Outband      | 10.58.52.43 | 255.255.255.0   | 10.58.52.62 | 80        | 443        | 2068     | 0        | 
|                                |                    |               |              | Outband      | 10.58.26.7  | 255.255.255.192 | 10.58.26.62 | 80        | 443        | 2068     | 0        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| FI-ucsb1-eu-spdc-2-4           | False              |               | False        | Outband      | 10.58.52.44 | 255.255.255.224 | 10.58.52.62 | 80        | 443        | 2068     | 0        | 
|                                |                    |               |              | Outband      | 10.58.26.8  | 255.255.255.192 | 10.58.26.62 | 80        | 443        | 2068     | 0        | 
+--------------------------------+--------------------+---------------+--------------+--------------+-------------+-----------------+-------------+-----------+------------+----------+----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v sw

{
    "duration": 24374,
    "isctl": {
        "read": true,
        "calls": 13,
        "success": 13,
        "failed": 0,
        "total_time": 22229
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
        "lines": 53
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:28:44.675851	True	2494	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:28:46.382558	True	1705	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:28:48.056990	True	1612	12	isctl get compute blade   -o json --top 100
2023-12-03 15:28:50.016612	True	1932	100	isctl get firmware runningfirmware --filter "Component eq 'system' and Type eq 'blade-controller'"  -o json --top 100
2023-12-03 15:28:51.553283	True	1523	21	isctl get firmware runningfirmware --filter "Component eq 'system' and Type eq 'blade-controller'"  -o json --top 100 --skip 100
2023-12-03 15:28:53.194598	True	1614	4	isctl get bios bootmode --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:28:54.810275	True	1591	0	isctl get bios bootmode --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:28:56.433250	True	1600	4	isctl get boot devicebootmode --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:28:58.059098	True	1553	0	isctl get boot devicebootmode --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:28:59.552217	True	1471	4	isctl get boot devicebootsecurity --filter "ComputePhysical/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:29:01.199133	True	1614	4	isctl get boot hdddevice --filter "Moid in ('60000c0b6176752d35b76e3e', '60000c066176752d35b76c32', '60000c046176752d35b76bd5', '6543c32276752d39014afb27')"  -o json --top 100
2023-12-03 15:29:03.005137	True	1743	3	isctl get boot pxedevice --filter "Moid in ('60000c046176752d35b76bb3', '60000bff6176752d35b769c9', '60000bfd6176752d35b7692a')"  -o json --top 100
2023-12-03 15:29:04.888663	True	1777	4	isctl get boot vmediadevice --filter "Moid in ('6013f1496176752d35458e49', '6013f1466176752d35458cdb', '6013f1486176752d35458daf', '656a0dbf76752d39014f335a')"  -o json --top 100
```

[[Back]](./ServerInventory.md)