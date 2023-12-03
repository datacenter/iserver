# CIMC Reboot

```
# iserver set power reboot --help

Usage: iserver.py set power reboot [OPTIONS]

  CIMC reboot

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
# iserver set power reboot --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W11  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W46  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
CIMC Reboot request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a23c696f6e2d30f93ad5  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a23c696f6e2d30f93af4  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
```

## Verbose output

```
# iserver set power reboot --group self-test-power --no-confirm

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W11  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W46  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
Auto confirmation: Y
isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6
	--AdminPowerState Reboot
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState Reboot
CIMC Reboot request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfa1806176752d35e678c2  | comp-1-p2b-eu-spdc-WMP240400FM  | 6346a23c696f6e2d30f93ad5  | COMPLETED        | 
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 6346a23c696f6e2d30f93af4  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 6346a23c696f6e2d30f93ad5
- Name: Reboot IMC
- Status: COMPLETED
- Create Time: 2022-10-12T11:17:16.245Z
- Start Time: 2022-10-12T11:17:16.286Z
- End Time: 2022-10-12T11:17:27.422Z
- Duration: 00:00:11


+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                        |
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| 6346a23c696f6e2d30f93ae6  | workflow.StartWorkflowTask       | 2022-10-12T11:17:16.398Z  | COMPLETED  | 00:00:00  |                                | 
| 6346a23c696f6e2d30f93aef  | Invoke IMC Reboot                | 2022-10-12T11:17:16.476Z  | COMPLETED  | 00:00:10  | Cisco IMC reboot is initiated  | 
| 6346a246696f6e2d30f93b17  | Invoke the IMC Reboot            | 2022-10-12T11:17:26.713Z  | NO_OP      | 00:00:00  |                                | 
| 6346a246696f6e2d30f93b24  | Invoke IMC Reboot                | 2022-10-12T11:17:26.935Z  | NO_OP      | 00:00:01  |                                | 
| 6346a247696f6e2d30f93b2f  | Update Server Inventory          | 2022-10-12T11:17:27.18Z   | NO_OP      | 00:00:00  | Skipped                        | 
| 6346a247696f6e2d30f93b42  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:17:27.346Z  | COMPLETED  | 00:00:00  |                                | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 6346a23c696f6e2d30f93af4
- Name: Reboot IMC
- Status: COMPLETED
- Create Time: 2022-10-12T11:17:16.837Z
- Start Time: 2022-10-12T11:17:16.867Z
- End Time: 2022-10-12T11:17:27.936Z
- Duration: 00:00:11


+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                        |
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| 6346a23c696f6e2d30f93b04  | workflow.StartWorkflowTask       | 2022-10-12T11:17:16.975Z  | COMPLETED  | 00:00:00  |                                | 
| 6346a23d696f6e2d30f93b0d  | Invoke IMC Reboot                | 2022-10-12T11:17:17.048Z  | COMPLETED  | 00:00:10  | Cisco IMC reboot is initiated  | 
| 6346a247696f6e2d30f93b3c  | Invoke the IMC Reboot            | 2022-10-12T11:17:27.298Z  | NO_OP      | 00:00:00  |                                | 
| 6346a247696f6e2d30f93b5a  | Invoke IMC Reboot                | 2022-10-12T11:17:27.5Z    | NO_OP      | 00:00:00  |                                | 
| 6346a247696f6e2d30f93b64  | Update Server Inventory          | 2022-10-12T11:17:27.727Z  | NO_OP      | 00:00:00  | Skipped                        | 
| 6346a247696f6e2d30f93b6e  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:17:27.869Z  | COMPLETED  | 00:00:00  |                                | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
```

## Servers State

Before task

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRS W11  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W46  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
| P+HRS W12  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W47  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
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
# iserver set power reboot --group self-test-power --no-confirm

Developer output

{
    "duration": 20939,
    "isctl": {
        "read": true,
        "calls": 13,
        "success": 13,
        "failed": 0,
        "total_time": 10833
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

2022-10-12 13:17:13.084889	True	1468	isctl get compute rackunit  -o json --top 100
2022-10-12 13:17:13.518593	True	432	isctl get compute blade  -o json --top 100
2022-10-12 13:17:14.134415	True	613	isctl get compute serversetting  -o json --top 100
2022-10-12 13:17:15.299610	True	1161	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:17:14.000Z" -o json --top 100
2022-10-12 13:17:15.632713	True	333	isctl get equipment locatorled --filter "OperState eq 'on'" -o json --top 100
2022-10-12 13:17:16.294282	True	641	isctl create compute updatecomputeserversetting moid 5fdfa1806573732d30fe43d6 --AdminPowerState Reboot -o json
2022-10-12 13:17:17.043598	True	749	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState Reboot -o json
2022-10-12 13:17:18.209861	True	1160	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:17:17.000Z" -o json --top 100
2022-10-12 13:17:19.046420	True	831	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:17:18.000Z" -o json --top 100
2022-10-12 13:17:25.060938	True	1004	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:17:24.000Z" -o json --top 100
2022-10-12 13:17:31.245945	True	1173	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T13:17:30.000Z" -o json --top 100
2022-10-12 13:17:31.864204	True	615	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a23c696f6e2d30f93ad5'" -o json --top 100
2022-10-12 13:17:32.518569	True	653	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '6346a23c696f6e2d30f93af4'" -o json --top 100
```