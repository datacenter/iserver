# Filter by server's health

Use --health option to select servers with any warnings or critical alarms.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --health

+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+
| SF      | MF  | WF | Name                          | Model              | Serial      | IP            | CPU        | Memory    |
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+
| P+ C(1) | Cri |    | C220-231                      | (R) UCSC-C220-M5SX | WZP23240NNZ | 10.58.250.241 | 2S 40C 80T | 384 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1          | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33   | 2S 24C 48T | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2          | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34   | 2S 24C 48T | 512 [GiB] | 
| P- C(2) | Cu  |    | HX1-eu-spdc-1                 | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.24.56   | 2S 40C 80T | 384 [GiB] | 
| P+ C(3) | Cu  |    | HX1-eu-spdc-4                 | (R) HXAF220C-M5SN  | WZP24100SMP | 10.58.24.57   | 2S 40C 80T | 384 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-2                 | (R) UCSC-C240-M4S  | FCH1930V0PH | 10.49.234.198 | 2S 24C 48T | 384 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-3                 | (R) UCSC-C220-M4S  | FCH2031V0YM | 10.49.234.196 | 2S 28C 56T | 672 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-4                 | (R) UCSC-C240-M4SX | FCH1916V1CT | 10.49.234.197 | 2S 24C 48T | 256 [GiB] | 
| P+ W(2) | Cu  |    | berlin-ucsm-5                 | (R) UCSC-C240-M4SX | FCH1916V0UY | 10.49.234.206 | 2S 24C 48T | 256 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-6                 | (R) UCSC-C240-M4S  | FCH1930V0KM | 10.49.234.195 | 2S 24C 48T | 384 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-7                 | (R) UCSC-C240-M4S  | FCH1930V1LA | 10.49.234.205 | 2S 28C 56T | 768 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-8                 | (R) UCSC-C220-M4S  | FCH1849V26H | 10.49.234.194 | 2S 24C 48T | 256 [GiB] | 
| P- C(1) | Cri |    | comp1-p2a-eu-spdc-WZP22511E6V | (R) UCSC-C240-M5SX | WZP22511E6V | 10.58.28.51   | 2S 24C 48T | 192 [GiB] | 
| P- C(1) | cri |    | comp3-p2a-eu-spdc-WZP2335149W | (R) UCSC-C220-M5SX | WZP2335149W | 10.58.28.53   | 2S 16C 32T | 192 [GiB] | 
| P+ C(1) | CRi |    | comp7-p3b-eu-spdc-FCH2023V2A4 | (R) UCSC-C220-M4S  | FCH2023V2A4 | 10.58.50.60   | 2S 28C 56T | 256 [GiB] | 
| P+ W(1) | Cri |    | esx13-eu-spdc-FCH2018V027     | (R) UCSC-C220-M4S  | FCH2018V027 | 10.58.29.53   | 2S 16C 32T | 256 [GiB] | 
| P+ C(1) | Cri |    | esx7-eu-spdc-FCH2004V0M6      | (R) UCSC-C220-M4S  | FCH2004V0M6 | 10.58.28.58   | 2S 16C 32T | 256 [GiB] | 
| P+ W(1) | Cri |    | esx92-eu-spdc-FCH2017V2AF     | (R) UCSC-C220-M4S  | FCH2017V2AF | 10.58.25.34   | 2S 28C 56T | 256 [GiB] | 
| P- W(2) | Cri |    | esx94-eu-spdc-FCH2017V2AH     | (R) UCSC-C220-M4S  | FCH2017V2AH | 10.58.25.36   | 2S 28C 56T | 256 [GiB] | 
| P+ C(1) | Cri |    | sn13-eu-spdc-WZP234301R9      | (R) SE-NODE-G2     | WZP234301R9 | 10.58.29.35   | 2S 20C 40T | 256 [GiB] | 
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+
```

Developer output

```
# iserver get servers --health

Developer output

{
    "duration": 5442,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 5337
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

2022-12-13 16:59:22.605230	True	2265	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:59:23.141505	True	535	10	isctl get compute blade   -o json --top 100
2022-12-13 16:59:23.719424	True	539	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:59:23.758924	True	571	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:59:23.000Z"  -o json --top 100
2022-12-13 16:59:24.219948	True	1041	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:59:24.606729	True	386	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
```
