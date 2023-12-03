# Power On

```
# iserver set power on --help

Usage: iserver.py set power on [OPTIONS]

  Power on

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
# iserver set power on --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS W1   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS W36  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
Power On request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 63469eb7696f6e2d30f930c3  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469eb8696f6e2d30f930ee  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

## Verbose output

```
# iserver set power on --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS W1   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS W36  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6
	--AdminPowerState PowerOn
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState PowerOn
Power On request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 63469eb7696f6e2d30f930c3  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63469eb8696f6e2d30f930ee  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 63469eb7696f6e2d30f930c3
- Name: Power On
- Status: COMPLETED
- Create Time: 2022-10-12T11:02:15.872Z
- Start Time: 2022-10-12T11:02:15.9Z
- End Time: 2022-10-12T11:02:19.217Z
- Duration: 00:00:04


+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| Task Moid                 | Description                                        | Create Time               | Status     | Duration  | Details                           |
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| 63469eb8696f6e2d30f930d4  | workflow.StartWorkflowTask                         | 2022-10-12T11:02:16.015Z  | COMPLETED  | 00:00:00  |                                   | 
| 63469eb8696f6e2d30f930dd  | Check and Execute Set One Time Boot Configuration  | 2022-10-12T11:02:16.105Z  | COMPLETED  | 00:00:00  | The task evaluated to case false  | 
| 63469eb8696f6e2d30f930fe  | Invoke Server Power On                             | 2022-10-12T11:02:16.392Z  | COMPLETED  | 00:00:02  | Server power on is initiated      | 
| 63469eba696f6e2d30f9312a  | Invoke the Server Power On                         | 2022-10-12T11:02:18.218Z  | NO_OP      | 00:00:00  |                                   | 
| 63469eba696f6e2d30f93137  | Invoke the Server Power On                         | 2022-10-12T11:02:18.463Z  | NO_OP      | 00:00:00  |                                   | 
| 63469eba696f6e2d30f93141  | Update Server Inventory                            | 2022-10-12T11:02:18.764Z  | COMPLETED  | 00:00:01  | State synchronized.               | 
| 63469ebb696f6e2d30f93155  | workflow.SuccessEndWorkflowTask                    | 2022-10-12T11:02:19.136Z  | COMPLETED  | 00:00:00  |                                   | 
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 63469eb8696f6e2d30f930ee
- Name: Power On
- Status: COMPLETED
- Create Time: 2022-10-12T11:02:16.314Z
- Start Time: 2022-10-12T11:02:16.343Z
- End Time: 2022-10-12T11:02:20.189Z
- Duration: 00:00:04


+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| Task Moid                 | Description                                        | Create Time               | Status     | Duration  | Details                           |
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| 63469eb8696f6e2d30f93104  | workflow.StartWorkflowTask                         | 2022-10-12T11:02:16.448Z  | COMPLETED  | 00:00:00  |                                   | 
| 63469eb8696f6e2d30f9310d  | Check and Execute Set One Time Boot Configuration  | 2022-10-12T11:02:16.546Z  | COMPLETED  | 00:00:00  | The task evaluated to case false  | 
| 63469eb8696f6e2d30f9311f  | Invoke Server Power On                             | 2022-10-12T11:02:16.771Z  | COMPLETED  | 00:00:02  | Server power on is initiated      | 
| 63469ebb696f6e2d30f9314f  | Invoke the Server Power On                         | 2022-10-12T11:02:19.094Z  | NO_OP      | 00:00:00  |                                   | 
| 63469ebb696f6e2d30f9316d  | Invoke the Server Power On                         | 2022-10-12T11:02:19.303Z  | NO_OP      | 00:00:00  |                                   | 
| 63469ebb696f6e2d30f93177  | Update Server Inventory                            | 2022-10-12T11:02:19.729Z  | COMPLETED  | 00:00:01  | State synchronized.               | 
| 63469ebc696f6e2d30f93181  | workflow.SuccessEndWorkflowTask                    | 2022-10-12T11:02:20.106Z  | COMPLETED  | 00:00:00  |                                   | 
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
```

## Servers State

Before task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS W1   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS W36  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
| P+HRS W2   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W37  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
# iserver set power on --group self-test-power --no-confirm

Developer output

{
    "duration": 14245,
    "isctl": {
        "read": true,
        "calls": 12,
        "success": 12,
        "failed": 0,
        "total_time": 9154
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

2022-10-12 13:02:13.083084	True	1853	isctl get compute rackunit  -o json --top 100
2022-10-12 13:02:13.524579	True	440	isctl get compute blade  -o json --top 100
2022-10-12 13:02:14.298707	True	772	isctl get compute serversetting  -o json --top 100
2022-10-12 13:02:14.948132	True	647	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:02:14.000Z" -o json --top 100
2022-10-12 13:02:15.291550	True	343	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:02:15.907039	True	597	isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6 --AdminPowerState PowerOn -o json
2022-10-12 13:02:16.359498	True	452	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState PowerOn -o json
2022-10-12 13:02:17.303291	True	939	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:02:16.000Z" -o json --top 100
2022-10-12 13:02:17.970833	True	663	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:02:17.000Z" -o json --top 100
2022-10-12 13:02:24.221453	True	1241	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:02:22.000Z" -o json --top 100
2022-10-12 13:02:24.855287	True	631	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63469eb7696f6e2d30f930c3'" -o json --top 100
2022-10-12 13:02:25.433300	True	576	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63469eb8696f6e2d30f930ee'" -o json --top 100
```