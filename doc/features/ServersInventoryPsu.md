# Filter by power supply state

Use --psu option to select servers with power supply reporting unhealthy state.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --psu

+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+-----+
| SF      | MF  | WF | Name                          | Model              | Serial      | IP            | CPU        | Memory    | Psu |
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+-----+
| P+ H    | Cri |    | aio-2-p1-eu-spdc-WZP22520Y69  | (R) UCSC-C220-M5SX | WZP22520Y69 | 10.58.28.42   | 2S 28C 56T | 256 [GiB] | 0/2 | 
| P+ W(2) | Cu  |    | berlin-ucsm-5                 | (R) UCSC-C240-M4SX | FCH1916V0UY | 10.49.234.206 | 2S 24C 48T | 256 [GiB] | 1/2 | 
| P- H    | CRi |    | comp1-p3b-eu-spdc-FCH2017V1J7 | (R) UCSC-C240-M4SX | FCH2017V1J7 | 10.58.50.48   | 2S 16C 32T | 128 [GiB] | 0/2 | 
| P- H    | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8 | (R) UCSC-C240-M4SX | FCH2017V1J8 | 10.58.50.49   | 2S 16C 32T | 128 [GiB] | 0/2 | 
| P- H    | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5 | (R) UCSC-C240-M4SX | FCH2017V1J5 | 10.58.50.50   | 2S 16C 32T | 128 [GiB] | 0/2 | 
| P+ H    | cri |    | comp4-p1-eu-spdc-FCH2016V23J  | (R) UCSC-C220-M4S  | FCH2016V23J | 10.58.28.47   | 2S 28C 56T | 256 [GiB] | 1/2 | 
| P- H    | Cri |    | comp4-p3b-eu-spdc-FCH2108V1FC | (R) UCSC-C220-M4S  | FCH2108V1FC | 10.58.50.57   | 2S 28C 56T | 256 [GiB] | 0/2 | 
| P+ H    | cri |    | comp5-p1-eu-spdc-FCH2017V0TN  | (R) UCSC-C220-M4S  | FCH2017V0TN | 10.58.28.48   | 2S 28C 56T | 256 [GiB] | 1/2 | 
| P- H    | Cri |    | comp5-p3b-eu-spdc-FCH2017V1Y6 | (R) UCSC-C220-M4S  | FCH2017V1Y6 | 10.58.50.58   | 2S 28C 56T | 256 [GiB] | 0/2 | 
| P- H    | CRi |    | comp6-p3b-eu-spdc-FCH2017V24J | (R) UCSC-C220-M4S  | FCH2017V24J | 10.58.50.59   | 2S 28C 56T | 256 [GiB] | 0/2 | 
| P- W(2) | Cri |    | esx94-eu-spdc-FCH2017V2AH     | (R) UCSC-C220-M4S  | FCH2017V2AH | 10.58.25.36   | 2S 28C 56T | 256 [GiB] | 0/2 | 
| P- H    | Cri |    | esx95-eu-spdc-FCH2017V241     | (R) UCSC-C220-M4S  | FCH2017V241 | 10.58.25.37   | 2S 16C 32T | 256 [GiB] | 0/2 | 
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+-----+
```

Developer output

```
# iserver get servers --psu

Developer output

{
    "duration": 8074,
    "isctl": {
        "read": true,
        "calls": 9,
        "success": 9,
        "failed": 0,
        "total_time": 9166
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

2022-12-13 16:59:48.226747	True	2508	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:59:49.045611	True	817	10	isctl get compute blade   -o json --top 100
2022-12-13 16:59:49.656923	True	565	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:59:49.662935	True	567	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:59:49.000Z"  -o json --top 100
2022-12-13 16:59:50.431322	True	1261	100	isctl get equipment psu   -o json --top 100
2022-12-13 16:59:50.471724	True	1388	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:59:50.904504	True	431	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
2022-12-13 16:59:51.431079	True	997	100	isctl get equipment psu   -o json --top 100 --skip 100
2022-12-13 16:59:52.064530	True	632	26	isctl get equipment psu   -o json --top 100 --skip 200
```
