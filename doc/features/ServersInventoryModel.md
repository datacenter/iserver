# Filter by server model

Define --model value for case-insensite loose match of server's model.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --model m5sx

+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP            | CPU         | Memory    |
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+
| P+ H    | Cri |    |  C220-WZP23350ZAQ              | (R) UCSC-C220-M5SX | WZP23350ZAQ | 10.58.244.186 | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | Cri |    |  C220-WZP23360FH9              | (R) UCSC-C220-M5SX | WZP23360FH9 | 10.58.244.70  | 2S 40C 80T  | 384 [GiB] | 
| P+ C(1) | Cri |    | C220-231                       | (R) UCSC-C220-M5SX | WZP23240NNZ | 10.58.250.241 | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | Cri |    | C240-WZP232102PH               | (R) UCSC-C240-M5SX | WZP232102PH | 10.58.244.236 | 2S 56C 112T | 512 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-5                  | (R) HXAF240C-M5SX  | WMP250901B0 | 10.58.24.58   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-6                  | (R) HXAF240C-M5SX  | WMP250901AY | 10.58.24.59   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-7                  | (R) HXAF240C-M5SX  | WMP2509019D | 10.58.24.54   | 2S 52C 104T | 768 [GiB] | 
| P+ H    | Cri |    | aio-1-p1-eu-spdc-WZP22490ZCU   | (R) UCSC-C220-M5SX | WZP22490ZCU | 10.58.28.41   | 2S 44C 88T  | 256 [GiB] | 
| P+ H    | Cri |    | aio-2-p1-eu-spdc-WZP22520Y69   | (R) UCSC-C220-M5SX | WZP22520Y69 | 10.58.28.42   | 2S 28C 56T  | 256 [GiB] | 
| P+ H    | Cri |    | aio-3-p1-eu-spdc-WZP22520Y54   | (R) UCSC-C220-M5SX | WZP22520Y54 | 10.58.28.43   | 2S 44C 88T  | 256 [GiB] | 
| P- H    | cri |    | aio1-p5g-eu-spdc-WZP23450C7D   | (R) UCSC-C240-M5SX | WZP23450C7D | 10.58.25.41   | 2S 48C 96T  | 512 [GiB] | 
| P- H    | cri |    | aio2-p5g-eu-spdc-WZP23450C8M   | (R) UCSC-C240-M5SX | WZP23450C8M | 10.58.25.42   | 2S 48C 96T  | 512 [GiB] | 
| P+ H    | CRi |    | aio3-p5g-eu-spdc-WZP23450C8K   | (R) UCSC-C240-M5SX | WZP23450C8K | 10.58.50.51   | 2S 48C 96T  | 384 [GiB] | 
| P- H    | Cu  |    | berlin-ucsm-1                  | (R) UCSC-C240-M5SX | WZP21490417 | 10.49.234.199 | 2S 28C 56T  | 704 [GiB] | 
| P- H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46   | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47   | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | Cri |    | comp1-p1-eu-spdc-WZP22520Y9J   | (R) UCSC-C220-M5SX | WZP22520Y9J | 10.58.28.44   | 2S 48C 96T  | 256 [GiB] | 
| P- C(1) | Cri |    | comp1-p2a-eu-spdc-WZP22511E6V  | (R) UCSC-C240-M5SX | WZP22511E6V | 10.58.28.51   | 2S 24C 48T  | 192 [GiB] | 
| P+ H    | Cri |    | comp1-p4A-eu-spdc              | (R) UCSC-C220-M5SX | WMP24040045 | 10.58.29.54   | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | Cri |    | comp2-p1-spdc-WZP22520Y95      | (R) UCSC-C220-M5SX | WZP22520Y95 | 10.58.28.45   | 2S 48C 96T  | 256 [GiB] | 
| P- H    | Cri |    | comp2-p2a-eu-spdc-WZP22511E6G  | (R) UCSC-C240-M5SX | WZP22511E6G | 10.58.28.52   | 2S 24C 48T  | 192 [GiB] | 
| P+ H    | Cri |    | comp2-p4a-eu-spdc-WZP22520B04  | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58   | 2S 48C 96T  | 256 [GiB] | 
| P- C(1) | cri |    | comp3-p2a-eu-spdc-WZP2335149W  | (R) UCSC-C220-M5SX | WZP2335149W | 10.58.28.53   | 2S 16C 32T  | 192 [GiB] | 
| P+ H    | Cri |    | comp3-p4a-eu-spdc-WZP22520Y8X  | (R) UCSC-C220-M5SX | WZP22520Y8X | 10.58.29.59   | 2S 24C 48T  | 256 [GiB] | 
| P- H    | Cri |    | comp4-p2a-eu-spdc-WZP22520Y8W  | (R) UCSC-C220-M5SX | WZP22520Y8W | 10.58.28.54   | 2S 24C 48T  | 192 [GiB] | 
| P+ H L  | cri |    | core-p5g-eu-spdc-WZP23440N02   | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50   | 2S 48C 96T  | 512 [GiB] | 
| P+ H    | Cri |    | cu-p5g-eu-spdc-WZP23440N11     | (R) UCSC-C220-M5SX | WZP23440N11 | 10.58.29.49   | 2S 48C 96T  | 384 [GiB] | 
| P+ H    | Cri |    | du-p5g-eu-spdc-WZP2526088F     | (R) UCSC-C240-M5SX | WZP2526088F | 10.58.29.48   | 2S 48C 48T  | 384 [GiB] | 
| P+ H    | Cri |    | esx00-eu-spdc-WZP22520AXQ      | (R) UCSC-C220-M5SX | WZP22520AXQ | 10.58.29.36   | 2S 48C 96T  | 512 [GiB] | 
| P+ H    | Cri |    | esx01-eu-spdc-WZP22520Y99      | (R) UCSC-C220-M5SX | WZP22520Y99 | 10.58.29.37   | 2S 24C 48T  | 384 [GiB] | 
| P+ H    | CRi |    | esx20-eu-spdc-WMP24040053      | (R) UCSC-C220-M5SX | WMP24040053 | 10.58.50.40   | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | CRi |    | esx21-eu-spdc-WZP23440N1P      | (R) UCSC-C220-M5SX | WZP23440N1P | 10.58.50.38   | 2S 48C 96T  | 512 [GiB] | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y      | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39   | 2S 48C 96T  | 512 [GiB] | 
| P+ H    | Cri |    | esx91-eu-spdc-WZP234411LW      | (R) UCSC-C240-M5SX | WZP234411LW | 10.58.25.33   | 2S 28C 56T  | 256 [GiB] | 
| P+ H    | Cri |    | mgmt-p1-eu-spdc-WZP2252176Z    | (R) UCSC-C220-M5SX | WZP2252176Z | 10.58.28.40   | 2S 48C 96T  | 256 [GiB] | 
| P+ H    | Cri |    | mgmt-p4a-eu-spdc-WZP22520Y9D   | (R) UCSC-C220-M5SX | WZP22520Y9D | 10.58.29.60   | 2S 48C 96T  | 256 [GiB] | 
| P+ H    | Cri |    | tnas-eu-spdc-WZP22511E68       | (R) UCSC-C240-M5SX | WZP22511E68 | 10.58.25.52   | 2S 28C 56T  | 256 [GiB] | 
| P+ H    | cri |    | znas-eu-spdc-WZP22511E3P       | (R) UCSC-C240-M5SX | WZP22511E3P | 10.58.28.56   | 2S 24C 48T  | 256 [GiB] | 
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+
```

Developer output

```
# iserver get servers --model m5sx

Developer output

{
    "duration": 5666,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 6024
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

2022-12-13 16:58:46.981810	True	2449	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:58:47.781142	True	797	10	isctl get compute blade   -o json --top 100
2022-12-13 16:58:48.224225	True	395	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:58:48.419231	True	580	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:58:47.000Z"  -o json --top 100
2022-12-13 16:58:48.909086	True	1086	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:58:49.626399	True	717	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
```
