# Intersight Server

## Filter by model

```
# iserver get server --model m5sn

iaccount isctl (cache: off)
Select servers...
Selected servers: 10
Collect server api objects...


Server Summary [#10]
--------------------

+---------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
| SF      | MF  | Name                           | Tag         | Model              | Serial      | IP          | CPU        | Memory    |
+---------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
| P+ H    | CRi | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 
| P+ H L  | CRi | comp-3-p2b-eu-spdc-WZP23400AKL | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri | NX1-S1-eu-spdc-WZP24100SMV     |             | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.50.51 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri | NX1-S2-eu-spdc-WZP24100SN0     |             | (R) HXAF220C-M5SN  | WZP24100SN0 | 10.58.50.52 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri | NX1-S3-eu-spdc-WZP24100SML     |             | (R) HXAF220C-M5SN  | WZP24100SML | 10.58.50.53 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri | NX1-S4-eu-spdc-WZP24100SMP     |             | (R) HXAF220C-M5SN  | WZP24100SMP | 10.58.50.54 | 2S 40C 80T | 384 [GiB] | 
| P+ C(1) | CRi | POD-4A-AIO-1-WZP23400AK9       | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK9 | 10.58.29.55 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi | POD-4A-AIO-2-WZP23400AK7       | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK7 | 10.58.29.56 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi | POD-4A-AIO-3-WZP23400AM2       | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AM2 | 10.58.29.57 | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --model m5sn

{
    "duration": 12663,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 9593
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
        "lines": 47
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:09:13.912319	True	4124	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:09:17.019738	True	3098	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:09:19.600759	True	2371	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)