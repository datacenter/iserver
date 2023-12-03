# Intersight Server

## Filter by ucsm

```
# iserver get server --ucsm

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#16]
--------------------

+---------+----+----------------------+-----+--------------------+-------------+---------------+------------+-----------+
| SF      | MF | Name                 | Tag | Model              | Serial      | IP            | CPU        | Memory    |
+---------+----+----------------------+-----+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cu | berlin-ucsm-1        |     | (R) UCSC-C240-M5SX | WZP21490417 | 10.49.234.199 | 2S 28C 56T | 704 [GiB] | 
| P+ H    | Cu | berlin-ucsm-2        |     | (R) UCSC-C240-M4S  | FCH1930V0PH | 10.49.234.198 | 2S 24C 48T | 384 [GiB] | 
| P+ I(1) | Cu | berlin-ucsm-3        |     | (R) UCSC-C220-M4S  | FCH2031V0YM | 10.49.234.196 | 2S 28C 56T | 672 [GiB] | 
| P+ I(1) | Cu | berlin-ucsm-4        |     | (R) UCSC-C240-M4SX | FCH1916V1CT | 10.49.234.197 | 2S 24C 48T | 256 [GiB] | 
| P+ C(1) | Cu | berlin-ucsm-5        |     | (R) UCSC-C240-M4SX | FCH1916V0UY | 10.49.234.206 | 2S 24C 48T | 256 [GiB] | 
| P+ C(1) | Cu | berlin-ucsm-6        |     | (R) UCSC-C240-M4S  | FCH1930V0KM | 10.49.234.195 | 2S 24C 48T | 384 [GiB] | 
| P- H    | Cu | berlin-ucsm-7        |     | (R) UCSC-C240-M4S  | FCH1930V1LA | 10.49.234.205 | 2S 28C 56T | 768 [GiB] | 
| P- C(1) | Cu | berlin-ucsm-8        |     | (R) UCSC-C220-M4S  | FCH1849V26H | 10.49.234.194 | 2S 24C 48T | 256 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-1-1 |     | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33   | 2S 24C 48T | 512 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-1-2 |     | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34   | 2S 24C 48T | 512 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-1-3 |     | (B) UCSB-B200-M4   | FCH20437VXH | 10.58.52.35   | 2S 24C 48T | 256 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-1-4 |     | (B) UCSB-B200-M4   | FCH205371UU | 10.58.52.36   | 2S 24C 48T | 256 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-2-1 |     | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41   | 2S 40C 80T | 512 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-2-2 |     | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42   | 2S 40C 80T | 512 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-2-3 |     | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43   | 2S 40C 80T | 512 [GiB] | 
| P+ H    | Cu | FI-ucsb1-eu-spdc-2-4 |     | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44   | 2S 40C 80T | 512 [GiB] | 
+---------+----+----------------------+-----+--------------------+-------------+---------------+------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --ucsm

{
    "duration": 14129,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6259
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
        "lines": 596
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:17:52.673718	True	2989	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:17:54.387596	True	1706	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:17:56.038383	True	1564	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)