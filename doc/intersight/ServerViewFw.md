# Intersight Server

## fw view

```
# iserver get server --group test -v fw

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

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v fw

{
    "duration": 10121,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 8577
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
        "lines": 23
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:22:01.526037	True	2115	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:22:03.128695	True	1600	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:22:04.770075	True	1573	12	isctl get compute blade   -o json --top 100
2023-12-03 15:22:06.427486	True	1617	100	isctl get firmware runningfirmware --filter "Component eq 'system' and Type eq 'blade-controller'"  -o json --top 100
2023-12-03 15:22:08.119709	True	1672	21	isctl get firmware runningfirmware --filter "Component eq 'system' and Type eq 'blade-controller'"  -o json --top 100 --skip 100
```

[[Back]](./ServerInventory.md)