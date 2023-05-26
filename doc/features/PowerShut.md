# OS Shutdown

```
# iserver set power shut --help

Usage: iserver.py set power shut [OPTIONS]

  Operating system shutdown

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
# iserver set power shut --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W9   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W44  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
OS Shutdown request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a190696f6e2d30f9386f  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a191696f6e2d30f9388b  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

## Verbose output

```
# iserver set power shut --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W9   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W44  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6
	--AdminPowerState Shutdown
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState Shutdown
OS Shutdown request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a190696f6e2d30f9386f  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a191696f6e2d30f9388b  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 6346a190696f6e2d30f9386f
- Name: Shut Down OS
- Status: COMPLETED
- Create Time: 2022-10-12T11:14:24.523Z
- Start Time: 2022-10-12T11:14:24.627Z
- End Time: 2022-10-12T11:14:32.531Z
- Duration: 00:00:08


+---------------------------+----------------------------------+---------------------------+------------+-----------+-------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                       |
+---------------------------+----------------------------------+---------------------------+------------+-----------+-------------------------------+
| 6346a191696f6e2d30f9387d  | workflow.StartWorkflowTask       | 2022-10-12T11:14:25.035Z  | COMPLETED  | 00:00:00  |                               | 
| 6346a191696f6e2d30f93886  | Invoke Server Shutdown           | 2022-10-12T11:14:25.551Z  | COMPLETED  | 00:00:04  | Server shutdown is initiated  | 
| 6346a195696f6e2d30f938b7  | Invoke the Server Shutdown       | 2022-10-12T11:14:29.82Z   | NO_OP      | 00:00:01  |                               | 
| 6346a197696f6e2d30f938cb  | Update Server Inventory          | 2022-10-12T11:14:31.116Z  | COMPLETED  | 00:00:00  | State synchronized.           | 
| 6346a198696f6e2d30f938e2  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:14:32.052Z  | COMPLETED  | 00:00:00  |                               | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+-------------------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 6346a191696f6e2d30f9388b
- Name: Shut Down OS
- Status: COMPLETED
- Create Time: 2022-10-12T11:14:25.865Z
- Start Time: 2022-10-12T11:14:26.017Z
- End Time: 2022-10-12T11:14:32.244Z
- Duration: 00:00:06


+---------------------------+----------------------------------+---------------------------+------------+-----------+-------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                       |
+---------------------------+----------------------------------+---------------------------+------------+-----------+-------------------------------+
| 6346a192696f6e2d30f93899  | workflow.StartWorkflowTask       | 2022-10-12T11:14:26.313Z  | COMPLETED  | 00:00:00  |                               | 
| 6346a192696f6e2d30f938a2  | Invoke Server Shutdown           | 2022-10-12T11:14:26.557Z  | COMPLETED  | 00:00:02  | Server shutdown is initiated  | 
| 6346a195696f6e2d30f938ac  | Invoke the Server Shutdown       | 2022-10-12T11:14:29.221Z  | NO_OP      | 00:00:01  |                               | 
| 6346a196696f6e2d30f938c4  | Update Server Inventory          | 2022-10-12T11:14:30.745Z  | COMPLETED  | 00:00:01  | State synchronized.           | 
| 6346a197696f6e2d30f938d8  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:14:31.917Z  | COMPLETED  | 00:00:00  |                               | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+-------------------------------+
```

## Servers State

Before task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W9   | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W44  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
| P-HRS W10  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS W45  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
# iserver set power shut --group self-test-power --no-confirm

Developer output

{
    "duration": 15410,
    "isctl": {
        "read": true,
        "calls": 12,
        "success": 12,
        "failed": 0,
        "total_time": 10315
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

2022-10-12 13:14:21.223880	True	1784	isctl get compute rackunit  -o json --top 100
2022-10-12 13:14:21.659573	True	434	isctl get compute blade  -o json --top 100
2022-10-12 13:14:22.356562	True	694	isctl get compute serversetting  -o json --top 100
2022-10-12 13:14:23.094487	True	734	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:14:22.000Z" -o json --top 100
2022-10-12 13:14:23.581533	True	487	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:14:24.929687	True	1329	isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6 --AdminPowerState Shutdown -o json
2022-10-12 13:14:25.939302	True	1010	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState Shutdown -o json
2022-10-12 13:14:26.810203	True	866	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:14:25.000Z" -o json --top 100
2022-10-12 13:14:27.609540	True	794	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:14:26.000Z" -o json --top 100
2022-10-12 13:14:33.841362	True	1221	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:14:32.000Z" -o json --top 100
2022-10-12 13:14:34.198001	True	354	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a190696f6e2d30f9386f'" -o json --top 100
2022-10-12 13:14:34.807568	True	608	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a191696f6e2d30f9388b'" -o json --top 100
```