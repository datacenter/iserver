# Intersight Server

## board view

```
# iserver get server --group test -v board

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Motherboard Hardware Summary [#8]
---------------------------------

+--------------------------------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| Server                         | Board Id | Vendor            | CPU | MemArr | PCI Switch | PCI Cooprocessor | Graphics | Storage Ctrl | FlexFlash Ctrl | FlexUtil Ctrl | Sec | TPM |
+--------------------------------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| comp-1-p2b-eu-spdc-WZP23400AJW | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   | 
| comp3-p4b-eu-spdc-WZP262207UM  | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 1        | 2            | 0              | 0             | 0   | 1   | 
| FI-ucsb1-eu-spdc-2-1           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
| FI-ucsb1-eu-spdc-2-2           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
| FI-ucsb1-eu-spdc-2-3           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
| FI-ucsb1-eu-spdc-2-4           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
+--------------------------------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v board

{
    "duration": 10194,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 8760
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
        "lines": 25
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:19:55.268485	True	2514	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:19:56.825245	True	1552	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:19:58.365484	True	1486	12	isctl get compute blade   -o json --top 100
2023-12-03 15:20:00.027908	True	1639	4	isctl get compute board --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:20:01.609517	True	1569	4	isctl get compute board --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
```

[[Back]](./ServerInventory.md)