# Locator LED On

## Help output

```
# iserver set locator on --help

Usage: iserver.py set locator on [OPTIONS]

  Locator on

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --group TEXT     Group name
  --serial TEXT    Serial numbers
  --name TEXT      Name loose match
  --ip TEXT        Management IP address or subnet filter
  --no-confirm     Confirmation mode  [default: False]
  --no-wait        Wait mode  [default: False]
  --dry-run        Dry run  [default: False]
  --verbose        Verbose output  [default: False]
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

## Default output

```
# iserver set locator on --group self-test-locator --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W33  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
Locator On request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469e09696f6e2d30f92dce  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

Server state

```
# iserver get servers --group self-test-locator

+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags       | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRSL W34  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Dry run

```
# iserver set locator on --group self-test-locator --no-confirm --dry-run

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W33  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminLocatorLedState On
```

## Verbose

```
# iserver set locator on --group self-test-locator --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W33  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminLocatorLedState On
Locator On request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469e09696f6e2d30f92dce  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 63469e09696f6e2d30f92dce
- Name: Turn On Locator
- Status: COMPLETED
- Create Time: 2022-10-12T10:59:21.835Z
- Start Time: 2022-10-12T10:59:22.015Z
- End Time: 2022-10-12T10:59:28.951Z
- Duration: 00:00:06


+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                   |
+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------+
| 63469e0a696f6e2d30f92ddf  | workflow.StartWorkflowTask       | 2022-10-12T10:59:22.453Z  | COMPLETED  | 00:00:00  |                           | 
| 63469e0a696f6e2d30f92de8  | Turn on Locator LED              | 2022-10-12T10:59:22.944Z  | COMPLETED  | 00:00:03  | Locator LED is turned on  | 
| 63469e0d696f6e2d30f92df8  | Turn on the Locator LED          | 2022-10-12T10:59:25.834Z  | NO_OP      | 00:00:01  |                           | 
| 63469e0e696f6e2d30f92e06  | Turn on the Locator LED          | 2022-10-12T10:59:26.315Z  | NO_OP      | 00:00:02  |                           | 
| 63469e10696f6e2d30f92e10  | Update Server Inventory          | 2022-10-12T10:59:28.497Z  | COMPLETED  | 00:00:00  | State synchronized.       | 
| 63469e10696f6e2d30f92e1a  | workflow.SuccessEndWorkflowTask  | 2022-10-12T10:59:28.883Z  | COMPLETED  | 00:00:00  |                           | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------+
```

## Developer

```
# iserver set locator on --group self-test-locator --no-confirm

Developer output

{
    "duration": 14134,
    "isctl": {
        "read": true,
        "calls": 10,
        "success": 10,
        "failed": 0,
        "total_time": 9046
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
        "read": false,
        "lines": 0
    }
}

Log: isctl
-----------

2022-10-12 12:59:17.629120	True	1583	isctl get compute rackunit  -o json --top 100
2022-10-12 12:59:18.197222	True	567	isctl get compute blade  -o json --top 100
2022-10-12 12:59:18.935930	True	736	isctl get compute serversetting  -o json --top 100
2022-10-12 12:59:20.024561	True	1085	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T12:59:18.000Z" -o json --top 100
2022-10-12 12:59:20.367527	True	343	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 12:59:22.141318	True	1756	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminLocatorLedState On -o json
2022-10-12 12:59:23.190230	True	1045	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T12:59:22.000Z" -o json --top 100
2022-10-12 12:59:23.829429	True	635	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T12:59:23.000Z" -o json --top 100
2022-10-12 12:59:29.708858	True	870	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T12:59:28.000Z" -o json --top 100
2022-10-12 12:59:30.137071	True	426	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63469e09696f6e2d30f92dce'" -o json --top 100
```

