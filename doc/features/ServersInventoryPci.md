# Filter by PCI device name

Use --pci option to select servers with PCI device model name matching provided value. Select based on case-insensite loose match rule.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --pci 710

+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+------------------------------------------------------------------+
| SF     | MF  | WF | Name                         | Model              | Serial      | IP          | CPU        | Memory    | PCI                                                              |
+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+------------------------------------------------------------------+
| P+ H L | cri |    | core-p5g-eu-spdc-WZP23440N02 | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50 | 2S 48C 96T | 512 [GiB] | Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC               | 
|        |     |    |                              |                    |             |             |            |           | Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC               | 
|        |     |    |                              |                    |             |             |            |           | Cisco UCS VIC 1387 MLOM                                          | 
|        |     |    |                              |                    |             |             |            |           | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 
|        |     |    |                              |                    |             |             |            |           | Intel X550 LOM                                                   | 
+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+------------------------------------------------------------------+
```

Developer output

```
# iserver get servers --pci 710

Developer output

{
    "duration": 11427,
    "isctl": {
        "read": true,
        "calls": 11,
        "success": 11,
        "failed": 0,
        "total_time": 10461
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

2022-12-13 17:00:18.261932	True	2519	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:00:18.779258	True	515	10	isctl get compute blade   -o json --top 100
2022-12-13 17:00:19.204677	True	374	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T17:00:18.000Z"  -o json --top 100
2022-12-13 17:00:19.400299	True	574	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 17:00:20.063697	True	1201	100	isctl get pci device   -o json --top 100
2022-12-13 17:00:20.235045	True	1413	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 17:00:20.659012	True	423	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
2022-12-13 17:00:20.897564	True	831	100	isctl get pci device   -o json --top 100 --skip 100
2022-12-13 17:00:21.914519	True	1015	100	isctl get pci device   -o json --top 100 --skip 200
2022-12-13 17:00:22.608734	True	692	100	isctl get pci device   -o json --top 100 --skip 300
2022-12-13 17:00:23.514560	True	904	57	isctl get pci device   -o json --top 100 --skip 400
```
