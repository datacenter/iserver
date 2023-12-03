# Intersight Server

## Filter by locator led

```
# iserver get server --loc on

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#6]
-------------------

+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| SF        | MF  | Name                           | Tag            | Model              | Serial      | IP          | CPU        | Memory    |
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L    | CRi | apic13-eu-spdc-WZP234408PR     | psirt:ready    | (R) APIC-SERVER-M3 | WZP234408PR | 10.58.28.39 | 2S 16C 16T | 96 [GiB]  | 
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L    | CRi | apic21-eu-spdc-WZP24171PHT     | psirt:ready    | (R) APIC-SERVER-M3 | WZP24171PHT | 10.58.29.45 | 2S 16C 16T | 96 [GiB]  | 
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L    | CRi | comp-3-p2b-eu-spdc-WZP23400AKL | psirt:ready    | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L    | CRi | comp-4-p2b-eu-spdc-WMP240400FM | psirt:ready    | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L    | CRi | comp-7-p2b-eu-spdc-WMP24040061 | psirt:ready    | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+
| P+ I(1) L | Cri | esx92-eu-spdc-FCH2017V2AF      | LAB-ID:DMZ     | (R) UCSC-C220-M4S  | FCH2017V2AF | 10.58.25.34 | 2S 28C 56T | 256 [GiB] | 
|           |     |                                | POD:ESXZ-Racks |                    |             |             |            |           | 
+-----------+-----+--------------------------------+----------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --loc on

{
    "duration": 14047,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6249
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
        "lines": 606
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:13:01.291373	True	3218	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:13:02.764862	True	1460	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:13:04.428750	True	1571	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)