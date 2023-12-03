# Intersight Server

## cpu view

```
# iserver get server --group test -v cpu

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


CPU [#16]
---------

+--------------------------------+-------+--------+--------+------------------------------+------+-------------------------------------------------+-------+-------------+-------------+-------------+-------------+----------+-----------+---------+
| Server                         | State | CPU Id | Socket | Vendor                       | Arch | Model                                           | Cores | Enabled     | Threads     | Speed [GHz] | Stepping    | Presence | OperState | Thermal |
+--------------------------------+-------+--------+--------+------------------------------+------+-------------------------------------------------+-------+-------------+-------------+-------------+-------------+----------+-----------+---------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 1      | CPU1   | Advanced Micro Devices, Inc. | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64          | 128         | 2.45        | 1           | equipped | operable  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 2      | CPU2   |                              | any  |                                                 | 0     | unspecified | unspecified | 0           | unspecified | missing  | removed   |         | 
| FI-ucsb1-eu-spdc-2-1           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
+--------------------------------+-------+--------+--------+------------------------------+------+-------------------------------------------------+-------+-------------+-------------+-------------+-------------+----------+-----------+---------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v cpu

{
    "duration": 8581,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 7095
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
        "lines": 24
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:21:03.679855	True	2172	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:21:05.066958	True	1382	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:21:06.931791	True	1789	12	isctl get compute blade   -o json --top 100
2023-12-03 15:21:08.705514	True	1752	16	isctl get processor unit --filter "ComputeBoard/Moid in ('5fdf9c056176752d35e44930', '5fdf9c7c6176752d35e472bd', '5fdf9d066176752d35e4aebe', '6385021176752d313964cbe0', '6501db4c76752d3901eb3890', '6501db4c76752d3901eb381d', '6501db4c76752d3901eb3882', '6501db4c76752d3901eb38a9')"  -o json --top 100
```

[[Back]](./ServerInventory.md)