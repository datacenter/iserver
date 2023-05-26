# Servers filtering by serial number

Use --serial option to provide comma (,) separated list of serial numbers you want to get.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P- H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 
| P- H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
```

Developer output

```
# iserver get servers --serial WMP24040059,WMP240400FM

Developer output

{
    "duration": 4077,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4971
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
        "lines": 51
    }
}

Log: isctl
-----------

2022-12-13 16:58:53.525414	True	2344	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:58:54.419841	True	891	10	isctl get compute blade   -o json --top 100
2022-12-13 16:58:55.026505	True	561	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:58:55.030179	True	557	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:58:54.000Z"  -o json --top 100
2022-12-13 16:58:55.075465	True	618	2	isctl get asset deviceregistration --filter "Moid in ('5fdfa1686f72612d300b383f', '5fdfe4666f72612d30130510')"  -o json --top 100
```
