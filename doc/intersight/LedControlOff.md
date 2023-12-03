# Locator LED Off

## Help output

```
# iserver set locator off --help

Usage: iserver.py set locator off [OPTIONS]

  Locator off

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
# iserver set locator off --group self-test-locator --no-confirm

+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags       | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRSL W34  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
Locator Off request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469e37696f6e2d30f92e2c  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

Server state

```
# iserver get servers --group self-test-locator

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W35  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

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
# iserver set locator off --group self-test-locator --no-confirm --dry-run

+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags       | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRSL W34  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminLocatorLedState Off
```

## Verbose

```
# iserver set locator off --group self-test-locator --no-confirm

+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags       | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRSL W34  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+-------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminLocatorLedState Off
Locator Off request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469e37696f6e2d30f92e2c  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 63469e37696f6e2d30f92e2c
- Name: Turn Off Locator
- Status: COMPLETED
- Create Time: 2022-10-12T11:00:07.761Z
- Start Time: 2022-10-12T11:00:08.075Z
- End Time: 2022-10-12T11:00:12.165Z
- Duration: 00:00:04


+---------------------------+----------------------------------+---------------------------+------------+-----------+----------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                    |
+---------------------------+----------------------------------+---------------------------+------------+-----------+----------------------------+
| 63469e38696f6e2d30f92e3d  | workflow.StartWorkflowTask       | 2022-10-12T11:00:08.189Z  | COMPLETED  | 00:00:00  |                            | 
| 63469e38696f6e2d30f92e46  | Turn off Locator LED             | 2022-10-12T11:00:08.26Z   | COMPLETED  | 00:00:02  | Locator LED is turned off  | 
| 63469e3a696f6e2d30f92e50  | Turn off the Locator LED         | 2022-10-12T11:00:10.423Z  | NO_OP      | 00:00:00  |                            | 
| 63469e3a696f6e2d30f92e5d  | Turn off the Locator LED         | 2022-10-12T11:00:10.624Z  | NO_OP      | 00:00:01  |                            | 
| 63469e3b696f6e2d30f92e67  | Update Server Inventory          | 2022-10-12T11:00:11.77Z   | COMPLETED  | 00:00:01  | State synchronized.        | 
| 63469e3c696f6e2d30f92e71  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:00:12.098Z  | COMPLETED  | 00:00:00  |                            | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+----------------------------+
```

## Developer

```
# iserver set locator off --group self-test-locator --no-confirm

Developer output

{
    "duration": 19594,
    "isctl": {
        "read": true,
        "calls": 10,
        "success": 10,
        "failed": 0,
        "total_time": 14514
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

2022-10-12 12:59:58.789800	True	2130	isctl get compute rackunit  -o json --top 100
2022-10-12 12:59:59.598072	True	806	isctl get compute blade  -o json --top 100
2022-10-12 13:00:00.756823	True	1156	isctl get compute serversetting  -o json --top 100
2022-10-12 13:00:01.433018	True	673	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:00:00.000Z" -o json --top 100
2022-10-12 13:00:01.946211	True	513	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:00:07.908332	True	5947	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminLocatorLedState Off -o json
2022-10-12 13:00:08.907114	True	995	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:00:07.000Z" -o json --top 100
2022-10-12 13:00:09.568003	True	657	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:00:08.000Z" -o json --top 100
2022-10-12 13:00:15.564474	True	988	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:00:14.000Z" -o json --top 100
2022-10-12 13:00:16.216243	True	649	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63469e37696f6e2d30f92e2c'" -o json --top 100
```

