# Power Off

```
# iserver set power off --help

Usage: iserver.py set power off [OPTIONS]

  Power off

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

## Basic execution

```
# iserver set power off --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W3   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W38  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
Power Off request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 63469f69696f6e2d30f9331a  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469f69696f6e2d30f93339  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

## Verbose output

```
# iserver set power off --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W3   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W38  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6
	--AdminPowerState PowerOff
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState PowerOff
Power Off request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 63469f69696f6e2d30f9331a  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469f69696f6e2d30f93339  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 63469f69696f6e2d30f9331a
- Name: Power Off
- Status: COMPLETED
- Create Time: 2022-10-12T11:05:13.22Z
- Start Time: 2022-10-12T11:05:13.261Z
- End Time: 2022-10-12T11:05:17.089Z
- Duration: 00:00:04


+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                        |
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| 63469f69696f6e2d30f9332b  | workflow.StartWorkflowTask       | 2022-10-12T11:05:13.365Z  | COMPLETED  | 00:00:00  |                                | 
| 63469f69696f6e2d30f93334  | Invoke Server Power Off          | 2022-10-12T11:05:13.44Z   | COMPLETED  | 00:00:03  | Server power off is initiated  | 
| 63469f6c696f6e2d30f9335d  | Invoke the Server Power Off      | 2022-10-12T11:05:16.158Z  | NO_OP      | 00:00:00  |                                | 
| 63469f6c696f6e2d30f9336a  | Invoke the Server Power Off      | 2022-10-12T11:05:16.362Z  | NO_OP      | 00:00:00  |                                | 
| 63469f6c696f6e2d30f93374  | Update Server Inventory          | 2022-10-12T11:05:16.637Z  | COMPLETED  | 00:00:00  | State synchronized.            | 
| 63469f6d696f6e2d30f9337e  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:05:17.014Z  | COMPLETED  | 00:00:00  |                                | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 63469f69696f6e2d30f93339
- Name: Power Off
- Status: COMPLETED
- Create Time: 2022-10-12T11:05:13.674Z
- Start Time: 2022-10-12T11:05:13.707Z
- End Time: 2022-10-12T11:05:18.89Z
- Duration: 00:00:05


+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                        |
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| 63469f69696f6e2d30f93349  | workflow.StartWorkflowTask       | 2022-10-12T11:05:13.808Z  | COMPLETED  | 00:00:00  |                                | 
| 63469f69696f6e2d30f93352  | Invoke Server Power Off          | 2022-10-12T11:05:13.892Z  | COMPLETED  | 00:00:04  | Server power off is initiated  | 
| 63469f6e696f6e2d30f93393  | Invoke the Server Power Off      | 2022-10-12T11:05:18.014Z  | NO_OP      | 00:00:00  |                                | 
| 63469f6e696f6e2d30f933a0  | Invoke the Server Power Off      | 2022-10-12T11:05:18.233Z  | NO_OP      | 00:00:00  |                                | 
| 63469f6e696f6e2d30f933aa  | Update Server Inventory          | 2022-10-12T11:05:18.476Z  | COMPLETED  | 00:00:00  | State synchronized.            | 
| 63469f6e696f6e2d30f933b4  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:05:18.822Z  | COMPLETED  | 00:00:00  |                                | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
```

## Servers State

Before task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W3   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W38  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

After task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS W4   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Developers output

```
# iserver set power off --group self-test-power --no-confirm

Developer output

{
    "duration": 14832,
    "isctl": {
        "read": true,
        "calls": 12,
        "success": 12,
        "failed": 0,
        "total_time": 9741
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

2022-10-12 13:05:09.603406	True	1586	isctl get compute rackunit  -o json --top 100
2022-10-12 13:05:10.347037	True	742	isctl get compute blade  -o json --top 100
2022-10-12 13:05:11.366247	True	1016	isctl get compute serversetting  -o json --top 100
2022-10-12 13:05:12.459476	True	1090	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:05:11.000Z" -o json --top 100
2022-10-12 13:05:12.793771	True	334	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:05:13.255791	True	443	isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6 --AdminPowerState PowerOff -o json
2022-10-12 13:05:13.739183	True	482	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState PowerOff -o json
2022-10-12 13:05:14.427750	True	684	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:05:13.000Z" -o json --top 100
2022-10-12 13:05:15.542583	True	1110	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:05:14.000Z" -o json --top 100
2022-10-12 13:05:21.496953	True	944	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:05:20.000Z" -o json --top 100
2022-10-12 13:05:22.152650	True	653	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63469f69696f6e2d30f9331a'" -o json --top 100
2022-10-12 13:05:22.810883	True	657	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63469f69696f6e2d30f93339'" -o json --top 100
```