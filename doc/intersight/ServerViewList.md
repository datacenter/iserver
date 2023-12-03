# Intersight Server

## list view

```
# iserver get server --group test

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Server Summary [#8]
-------------------

+--------+-----+---------+--------------------------------+-------------+--------------------+-------------+-------------+-------------+-----------+
| SF     | MF  | WF (7d) | Name                           | Tag         | Model              | Serial      | IP          | CPU         | Memory    |
+--------+-----+---------+--------------------------------+-------------+--------------------+-------------+-------------+-------------+-----------+
| P+ H   | CRi | --      | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T  | 384 [GiB] | 
| P+ H   | CRi | --      | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T  | 384 [GiB] | 
| P+ H L | CRi | --      | comp-3-p2b-eu-spdc-WZP23400AKL | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T  | 384 [GiB] | 
| P+ H   | CRi | C4      | comp3-p4b-eu-spdc-WZP262207UM  | psirt:ready | (R) UCSC-C225-M6S  | WZP262207UM | 10.58.53.35 | 1S 64C 128T | 512 [GiB] | 
| P+ H   | Cu  | --      | FI-ucsb1-eu-spdc-2-1           |             | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41 | 2S 40C 80T  | 512 [GiB] | 
| P+ H   | Cu  | --      | FI-ucsb1-eu-spdc-2-2           |             | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42 | 2S 40C 80T  | 512 [GiB] | 
| P+ H   | Cu  | --      | FI-ucsb1-eu-spdc-2-3           |             | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43 | 2S 40C 80T  | 512 [GiB] | 
| P+ H   | Cu  | --      | FI-ucsb1-eu-spdc-2-4           |             | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44 | 2S 40C 80T  | 512 [GiB] | 
+--------+-----+---------+--------------------------------+-------------+--------------------+-------------+-------------+-------------+-----------+
```

Developer

```
# iserver get server --group test

{
    "duration": 10379,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 8430
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

2023-12-01 19:07:10.821100	True	3206	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-01 19:07:12.654752	True	1829	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-01 19:07:14.490503	True	1721	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-01 19:07:16.208817	True	1674	28	isctl get workflow workflowinfo --filter "CreateTime gt 2023-11-24T19:07:14.000Z"  -o json --top 100
```

[[Back]](./ServerIntentory.md)