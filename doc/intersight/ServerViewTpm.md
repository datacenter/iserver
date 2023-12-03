# Intersight Server

## tpm view

```
# iserver get server --group test -v tpm

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Trusted Platform Module [#4]
----------------------------

+--------------------------------+----------+-------------------+-------------+---------+------------------+-------------------+-------------+------------------+
| Server                         | TPM      | Activation Status | Admin State | Version | Model            | Vendor            | Serial      | Firmware Version |
+--------------------------------+----------+-------------------+-------------+---------+------------------+-------------------+-------------+------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | empty    | unknown           | unknown     | NA      | NA               | NA                | NA          | NA               | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | empty    | unknown           | unknown     | NA      | NA               | NA                | NA          | NA               | 
| comp-3-p2b-eu-spdc-WZP23400AKL | empty    | unknown           | unknown     | NA      | NA               | NA                | NA          | NA               | 
| comp3-p4b-eu-spdc-WZP262207UM  | equipped | activated         | enabled     | 2.0     | UCSX-TPM2-002B-C | Cisco Systems Inc | FCH262076M1 | 7.85             | 
+--------------------------------+----------+-------------------+-------------+---------+------------------+-------------------+-------------+------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v tpm

{
    "duration": 12442,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 10815
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
        "lines": 33
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:29:34.562190	True	2238	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:29:35.861668	True	1297	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:29:37.332756	True	1415	12	isctl get compute blade   -o json --top 100
2023-12-03 15:29:39.464644	True	2101	4	isctl get compute board --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:29:41.309800	True	1836	4	isctl get compute board --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:29:43.269861	True	1928	4	isctl get equipment tpm --filter "Moid in ('5fdf9c186176752d35e4503a', '5fdf9c8f6176752d35e47b82', '5fdf9d196176752d35e4b797', '638501fa76752d313964c6f7')"  -o json --top 100
```

[[Back]](./ServerInventory.md)