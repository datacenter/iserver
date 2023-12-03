# Intersight Server

## summary view

```
# iserver get server --group test -v summary

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Selected servers count: 8

Type
- Rack  : 4
- Blade : 4

Models
- UCSB-B200-M5   : 4
- UCSC-C225-M6S  : 1
- UCSC-C240-M5SN : 3

Power
- On  : 8
- Off : 0

Maximum
- CpuSockets : 2
- CpuCores   : 64
- CpuThreads : 128
- Memory     : 512

Health
- Healthy  : 8
- Warning  : 0
- Critical : 0

Management Mode
- Standalone : 4
- UCSM       : 4


Tag
- psirt:ready: 4
```

Developer

```
# iserver get server --group test -v summary

{
    "duration": 7941,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6107
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
        "lines": 15
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:29:54.286504	True	2377	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:29:55.928734	True	1638	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:29:58.074941	True	2092	12	isctl get compute blade   -o json --top 100
```

[[Back]](./ServerInventory.md)