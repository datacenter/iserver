# Intersight Server

## Default output

```
# iserver get server --group test

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Server Summary [#8]
-------------------

+--------+-----+--------------------------------+-------------+--------------------+-------------+-------------+-------------+-----------+
| SF     | MF  | Name                           | Tag         | Model              | Serial      | IP          | CPU         | Memory    |
+--------+-----+--------------------------------+-------------+--------------------+-------------+-------------+-------------+-----------+
| P+ H   | CRi | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T  | 384 [GiB] | 
| P+ H   | CRi | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T  | 384 [GiB] | 
| P+ H L | CRi | comp-3-p2b-eu-spdc-WZP23400AKL | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T  | 384 [GiB] | 
| P+ H   | CRi | comp3-p4b-eu-spdc-WZP262207UM  | psirt:ready | (R) UCSC-C225-M6S  | WZP262207UM | 10.58.53.35 | 1S 64C 128T | 512 [GiB] | 
| P+ H   | Cu  | FI-ucsb1-eu-spdc-2-1           |             | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41 | 2S 40C 80T  | 512 [GiB] | 
| P+ H   | Cu  | FI-ucsb1-eu-spdc-2-2           |             | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42 | 2S 40C 80T  | 512 [GiB] | 
| P+ H   | Cu  | FI-ucsb1-eu-spdc-2-3           |             | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43 | 2S 40C 80T  | 512 [GiB] | 
| P+ H   | Cu  | FI-ucsb1-eu-spdc-2-4           |             | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44 | 2S 40C 80T  | 512 [GiB] | 
+--------+-----+--------------------------------+-------------+--------------------+-------------+-------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --group test

{
    "duration": 8095,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6299
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
        "lines": 39
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:30:28.912169	True	3048	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:30:30.429496	True	1512	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:30:32.251272	True	1739	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)