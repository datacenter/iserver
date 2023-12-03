# Intersight Server

## Filter by name

```
# iserver get server --name p2b

iaccount isctl (cache: off)
Select servers...
Selected servers: 7
Collect server api objects...


Server Summary [#7]
-------------------

+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | Name                           | Tag          | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H   | CRi | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H   | CRi | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | CRi | comp-3-p2b-eu-spdc-WZP23400AKL | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | CRi | comp-4-p2b-eu-spdc-WMP240400FM | psirt:ready  | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H   | CRi | comp-5-p2b-eu-spdc-WMP2404000R | User:vanniew | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 
|        |     |                                | psirt:ready  |                    |             |             |            |           | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H   | CRi | comp-6-p2b-eu-spdc-WMP24040059 | psirt:ready  | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | CRi | comp-7-p2b-eu-spdc-WMP24040061 | psirt:ready  | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 
+--------+-----+--------------------------------+--------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --name p2b

{
    "duration": 12679,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 9803
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
        "lines": 35
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:07:36.948655	True	4900	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:07:39.479675	True	2526	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:07:42.026155	True	2377	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)