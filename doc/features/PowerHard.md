# Hard Reset

```
# iserver set power hard --help

Usage: iserver.py set power hard [OPTIONS]

  Hard reset

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
# iserver set power hard --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W5   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W40  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
Hard Reset request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a013696f6e2d30f934bf  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a014696f6e2d30f934de  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

## Verbose output

```
# iserver set power hard --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W5   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W40  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6
	--AdminPowerState HardReset
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState HardReset
Hard Reset request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a013696f6e2d30f934bf  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a014696f6e2d30f934de  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 6346a013696f6e2d30f934bf
- Name: Hard Reset
- Status: COMPLETED
- Create Time: 2022-10-12T11:08:03.875Z
- Start Time: 2022-10-12T11:08:03.906Z
- End Time: 2022-10-12T11:08:31.248Z
- Duration: 00:00:28


+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                         |
+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------------+
| 6346a014696f6e2d30f934d0  | workflow.StartWorkflowTask       | 2022-10-12T11:08:04.01Z   | COMPLETED  | 00:00:00  |                                 | 
| 6346a014696f6e2d30f934d9  | Invoke Server Hard Reset         | 2022-10-12T11:08:04.084Z  | COMPLETED  | 00:00:26  | Server hard reset is initiated  | 
| 6346a02e696f6e2d30f93591  | Invoke the Server Hard Reset     | 2022-10-12T11:08:30.338Z  | NO_OP      | 00:00:00  |                                 | 
| 6346a02e696f6e2d30f9359e  | Invoke the Server Hard Reset     | 2022-10-12T11:08:30.584Z  | NO_OP      | 00:00:00  |                                 | 
| 6346a02e696f6e2d30f935a8  | Update Server Inventory          | 2022-10-12T11:08:30.826Z  | COMPLETED  | 00:00:01  | State synchronized.             | 
| 6346a02f696f6e2d30f935b2  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:08:31.18Z   | COMPLETED  | 00:00:00  |                                 | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 6346a014696f6e2d30f934de
- Name: Hard Reset
- Status: COMPLETED
- Create Time: 2022-10-12T11:08:04.33Z
- Start Time: 2022-10-12T11:08:04.358Z
- End Time: 2022-10-12T11:08:28.263Z
- Duration: 00:00:24


+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                         |
+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------------+
| 6346a014696f6e2d30f934ee  | workflow.StartWorkflowTask       | 2022-10-12T11:08:04.456Z  | COMPLETED  | 00:00:00  |                                 | 
| 6346a014696f6e2d30f934f7  | Invoke Server Hard Reset         | 2022-10-12T11:08:04.54Z   | COMPLETED  | 00:00:23  | Server hard reset is initiated  | 
| 6346a02b696f6e2d30f9355b  | Invoke the Server Hard Reset     | 2022-10-12T11:08:27.319Z  | NO_OP      | 00:00:00  |                                 | 
| 6346a02b696f6e2d30f93568  | Invoke the Server Hard Reset     | 2022-10-12T11:08:27.522Z  | NO_OP      | 00:00:00  |                                 | 
| 6346a02b696f6e2d30f93572  | Update Server Inventory          | 2022-10-12T11:08:27.835Z  | COMPLETED  | 00:00:01  | State synchronized.             | 
| 6346a02c696f6e2d30f9357c  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:08:28.194Z  | COMPLETED  | 00:00:00  |                                 | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+---------------------------------+
```

## Servers State

Before task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W5   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W40  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
| P+HRS W6   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W41  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
# iserver set power hard --group self-test-power --no-confirm

Developer output

{
    "duration": 40690,
    "isctl": {
        "read": true,
        "calls": 16,
        "success": 16,
        "failed": 0,
        "total_time": 15555
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

2022-10-12 13:08:00.055557	True	1862	isctl get compute rackunit  -o json --top 100
2022-10-12 13:08:00.801255	True	745	isctl get compute blade  -o json --top 100
2022-10-12 13:08:01.799910	True	996	isctl get compute serversetting  -o json --top 100
2022-10-12 13:08:02.920241	True	1116	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:01.000Z" -o json --top 100
2022-10-12 13:08:03.413117	True	492	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:08:03.903603	True	472	isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6 --AdminPowerState HardReset -o json
2022-10-12 13:08:04.358484	True	455	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState HardReset -o json
2022-10-12 13:08:05.156646	True	793	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:04.000Z" -o json --top 100
2022-10-12 13:08:06.265007	True	1104	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:05.000Z" -o json --top 100
2022-10-12 13:08:12.418384	True	1143	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:11.000Z" -o json --top 100
2022-10-12 13:08:18.539056	True	1111	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:17.000Z" -o json --top 100
2022-10-12 13:08:24.693114	True	1144	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:23.000Z" -o json --top 100
2022-10-12 13:08:30.817478	True	1114	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:29.000Z" -o json --top 100
2022-10-12 13:08:37.493223	True	1665	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:08:35.000Z" -o json --top 100
2022-10-12 13:08:38.144626	True	649	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a013696f6e2d30f934bf'" -o json --top 100
2022-10-12 13:08:38.840926	True	694	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a014696f6e2d30f934de'" -o json --top 100
```