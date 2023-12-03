# Power Cycle

```
# iserver set power cycle --help

Usage: iserver.py set power cycle [OPTIONS]

  Power cycle

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
# iserver set power cycle --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W7   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W42  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
Power Cycle request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a0dc696f6e2d30f936c1  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a0dd696f6e2d30f936dd  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

## Verbose output

```
# iserver set power cycle --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W7   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W42  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6
	--AdminPowerState PowerCycle
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState PowerCycle
Power Cycle request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a0dc696f6e2d30f936c1  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a0dd696f6e2d30f936dd  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 6346a0dc696f6e2d30f936c1
- Name: Power Cycle
- Status: COMPLETED
- Create Time: 2022-10-12T11:11:25.073Z
- Start Time: 2022-10-12T11:11:25.229Z
- End Time: 2022-10-12T11:11:34.274Z
- Duration: 00:00:09


+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| Task Moid                 | Description                                        | Create Time               | Status     | Duration  | Details                           |
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| 6346a0dd696f6e2d30f936d4  | workflow.StartWorkflowTask                         | 2022-10-12T11:11:25.726Z  | COMPLETED  | 00:00:00  |                                   | 
| 6346a0de696f6e2d30f936ef  | Check and Execute Set One Time Boot Configuration  | 2022-10-12T11:11:26.412Z  | COMPLETED  | 00:00:01  | The task evaluated to case false  | 
| 6346a0e0696f6e2d30f93719  | Invoke Server Power Cycle                          | 2022-10-12T11:11:28.249Z  | COMPLETED  | 00:00:05  | Server power cycle is initiated   | 
| 6346a0e5696f6e2d30f93762  | Invoke the Server Power Cycle                      | 2022-10-12T11:11:33.237Z  | NO_OP      | 00:00:00  |                                   | 
| 6346a0e5696f6e2d30f9376f  | Invoke the Server Power Cycle                      | 2022-10-12T11:11:33.473Z  | NO_OP      | 00:00:00  |                                   | 
| 6346a0e5696f6e2d30f93779  | Update Server Inventory                            | 2022-10-12T11:11:33.756Z  | COMPLETED  | 00:00:01  | State synchronized.               | 
| 6346a0e6696f6e2d30f93783  | workflow.SuccessEndWorkflowTask                    | 2022-10-12T11:11:34.195Z  | COMPLETED  | 00:00:00  |                                   | 
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 6346a0dd696f6e2d30f936dd
- Name: Power Cycle
- Status: COMPLETED
- Create Time: 2022-10-12T11:11:26.045Z
- Start Time: 2022-10-12T11:11:26.146Z
- End Time: 2022-10-12T11:11:32.943Z
- Duration: 00:00:06


+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| Task Moid                 | Description                                        | Create Time               | Status     | Duration  | Details                           |
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| 6346a0de696f6e2d30f936f7  | workflow.StartWorkflowTask                         | 2022-10-12T11:11:26.712Z  | COMPLETED  | 00:00:00  |                                   | 
| 6346a0df696f6e2d30f93704  | Check and Execute Set One Time Boot Configuration  | 2022-10-12T11:11:27.12Z   | COMPLETED  | 00:00:01  | The task evaluated to case false  | 
| 6346a0e0696f6e2d30f93722  | Invoke Server Power Cycle                          | 2022-10-12T11:11:28.842Z  | COMPLETED  | 00:00:03  | Server power cycle is initiated   | 
| 6346a0e3696f6e2d30f9372c  | Invoke the Server Power Cycle                      | 2022-10-12T11:11:31.953Z  | NO_OP      | 00:00:01  |                                   | 
| 6346a0e4696f6e2d30f93739  | Invoke the Server Power Cycle                      | 2022-10-12T11:11:32.171Z  | NO_OP      | 00:00:00  |                                   | 
| 6346a0e4696f6e2d30f93743  | Update Server Inventory                            | 2022-10-12T11:11:32.524Z  | COMPLETED  | 00:00:00  | State synchronized.               | 
| 6346a0e4696f6e2d30f9374d  | workflow.SuccessEndWorkflowTask                    | 2022-10-12T11:11:32.866Z  | COMPLETED  | 00:00:00  |                                   | 
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
```

## Servers State

Before task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W7   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W42  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
| P+HRS W8   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W43  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
# iserver set power cycle --group self-test-power --no-confirm

Developer output

{
    "duration": 21854,
    "isctl": {
        "read": true,
        "calls": 13,
        "success": 13,
        "failed": 0,
        "total_time": 11744
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

2022-10-12 13:11:21.568057	True	1564	isctl get compute rackunit  -o json --top 100
2022-10-12 13:11:22.010414	True	441	isctl get compute blade  -o json --top 100
2022-10-12 13:11:23.026567	True	1013	isctl get compute serversetting  -o json --top 100
2022-10-12 13:11:23.771871	True	742	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:11:23.000Z" -o json --top 100
2022-10-12 13:11:24.256219	True	484	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:11:25.307065	True	1030	isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6 --AdminPowerState PowerCycle -o json
2022-10-12 13:11:26.124135	True	816	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState PowerCycle -o json
2022-10-12 13:11:27.118919	True	990	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:11:26.000Z" -o json --top 100
2022-10-12 13:11:28.140013	True	1016	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:11:27.000Z" -o json --top 100
2022-10-12 13:11:34.313832	True	1164	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:11:33.000Z" -o json --top 100
2022-10-12 13:11:40.451132	True	1126	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:11:39.000Z" -o json --top 100
2022-10-12 13:11:41.145214	True	691	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a0dc696f6e2d30f936c1'" -o json --top 100
2022-10-12 13:11:41.813875	True	667	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a0dd696f6e2d30f936dd'" -o json --top 100
```