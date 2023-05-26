# Filter by location led

Use --loc option to select servers with location led turned on.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --loc

+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | WF | Name                         | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | cri |    | core-p5g-eu-spdc-WZP23440N02 | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50 | 2S 48C 96T | 512 [GiB] | 
+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+
```

Developer output

```
# iserver get servers --loc

Developer output

{
    "duration": 6469,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 6027
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
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
        "lines": 48
    }
}

Log: isctl
-----------

2022-12-13 16:59:08.022709	True	2216	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:59:08.872130	True	848	10	isctl get compute blade   -o json --top 100
2022-12-13 16:59:09.326316	True	405	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:59:08.000Z"  -o json --top 100
2022-12-13 16:59:09.332714	True	414	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:59:10.361204	True	1450	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:59:11.056270	True	694	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
```
