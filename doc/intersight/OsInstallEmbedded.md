# OS Install with static IP

```
# iserver create os-install embedded --help

Usage: iserver.py create os-install embedded [OPTIONS]

  OS installation with embedded kickstart

Options:
  --iaccount TEXT      Intersight account  [default: isctl]
  --ip TEXT            Management IP address
  --name TEXT          Name loose match filter
  --serial TEXT        Serial number
  --scu TEXT           SCU Name
  --image TEXT         OS Image Name
  --organization TEXT  Organization name
  --dry-run            Dry run  [default: False]
  --no-wait            Wait disabled  [default: False]
  --verbose            Verbose output  [default: False]
  --devel              Developer output  [default: False]
  --help               Show this message and exit.
```

## Basic execution

```
# iserver create os-install embedded
    --serial WMP24040059
    --scu "SCU 6.2.2a"
    --image "Ubuntu 22.04LTS"
    --organization EMEAR-SPDC-Specialists

Validate input parameters...
Power Cycle request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63467478696f6e2d30f8e329  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63467485696f6e2d30f8e390  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+
OS installation successful
```

## Verbose output

```
# iserver create os-install embedded
    --serial WMP24040059
    --scu "SCU 6.2.2a"
    --image "Ubuntu 22.04LTS"
    --organization EMEAR-SPDC-Specialists

Validate input parameters...
isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76
	--AdminPowerState PowerCycle
Power Cycle request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63467478696f6e2d30f8e329  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 63467478696f6e2d30f8e329
- Name: Power Cycle
- Status: COMPLETED
- Create Time: 2022-10-12T08:02:00.754Z
- Start Time: 2022-10-12T08:02:01.015Z
- End Time: 2022-10-12T08:02:07.22Z
- Duration: 00:00:06


+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| Task Moid                 | Description                                        | Create Time               | Status     | Duration  | Details                           |
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
| 63467479696f6e2d30f8e33a  | workflow.StartWorkflowTask                         | 2022-10-12T08:02:01.623Z  | COMPLETED  | 00:00:00  |                                   | 
| 63467479696f6e2d30f8e343  | Check and Execute Set One Time Boot Configuration  | 2022-10-12T08:02:01.997Z  | COMPLETED  | 00:00:01  | The task evaluated to case false  | 
| 6346747a696f6e2d30f8e355  | Invoke Server Power Cycle                          | 2022-10-12T08:02:02.515Z  | COMPLETED  | 00:00:03  | Server power cycle is initiated   | 
| 6346747d696f6e2d30f8e35f  | Invoke the Server Power Cycle                      | 2022-10-12T08:02:05.373Z  | NO_OP      | 00:00:00  |                                   | 
| 6346747d696f6e2d30f8e36c  | Invoke the Server Power Cycle                      | 2022-10-12T08:02:05.603Z  | NO_OP      | 00:00:01  |                                   | 
| 6346747e696f6e2d30f8e376  | Update Server Inventory                            | 2022-10-12T08:02:06.777Z  | COMPLETED  | 00:00:01  | State synchronized.               | 
| 6346747f696f6e2d30f8e380  | workflow.SuccessEndWorkflowTask                    | 2022-10-12T08:02:07.133Z  | COMPLETED  | 00:00:00  |                                   | 
+---------------------------+----------------------------------------------------+---------------------------+------------+-----------+-----------------------------------+
isctl create os install 
	--InstallMethod vMedia
	--Server="MoRef:ComputeRackUnitRelationship[Moid:5fdfe47f6176752d35001995]"
	--Image=MoRef[Moid:633068b96567612d304a7844]
	--OsduImage=MoRef[Moid:632c227a6567612d30187910]
	--Organization=MoRef[Moid:5dee1d736972652d321d26b5]
	--InstallTarget='{"ObjectType": "os.VirtualDrive", "Name": "main", "StorageControllerSlotId": "MRAID", "Id": "0"}'
	--Answers='{"Source": "Embedded"}'
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| 5fdfe47f6176752d35001995  | comp-3-p2b-eu-spdc-WMP24040059  | 63467485696f6e2d30f8e390  | COMPLETED        | 
+---------------------------+---------------------------------+---------------------------+------------------+

Server
- Name: comp-3-p2b-eu-spdc-WMP24040059
- Model: UCSC-C220-M5SX
- Serial: WMP24040059
- IP: 10.58.50.46


Workflow
- Workflow ID: 63467485696f6e2d30f8e390
- Name: Operating System Install
- Status: COMPLETED
- Create Time: 2022-10-12T08:02:13.966Z
- Start Time: 2022-10-12T08:02:14.469Z
- End Time: 2022-10-12T08:04:04.582Z
- Duration: 00:01:50


+---------------------------+------------------------------------------------+---------------------------+------------+-----------+-------------------------------------------------+
| Task Moid                 | Description                                    | Create Time               | Status     | Duration  | Details                                         |
+---------------------------+------------------------------------------------+---------------------------+------------+-----------+-------------------------------------------------+
| 63467486696f6e2d30f8e3b6  | StartTask                                      | 2022-10-12T08:02:14.575Z  | COMPLETED  | 00:00:00  |                                                 | 
| 63467486696f6e2d30f8e3c0  | Confirm Server Configuration for Installation  | 2022-10-12T08:02:14.656Z  | COMPLETED  | 00:00:00  |                                                 | 
| 63467486696f6e2d30f8e3cb  | Check and Proceed to Install Operating System  | 2022-10-12T08:02:14.82Z   | COMPLETED  | 00:00:00  | Condition to match when server is a standalone  | 
| 63467487696f6e2d30f8e3dd  | Install Operating System on Standalone Server  | 2022-10-12T08:02:15.024Z  | COMPLETED  | 00:00:00  |                                                 | 
| 63467487696f6e2d30f8e3f6  | Install Operating System on Standalone Server  | 2022-10-12T08:02:15.398Z  | COMPLETED  | 00:01:46  |                                                 | 
| 634674f4696f6e2d30f8e628  | Install Operating System on Standalone Server  | 2022-10-12T08:04:04.12Z   | COMPLETED  | 00:00:00  |                                                 | 
| 634674f4696f6e2d30f8e632  | SuccessEndTask                                 | 2022-10-12T08:04:04.474Z  | COMPLETED  | 00:00:00  |                                                 | 
+---------------------------+------------------------------------------------+---------------------------+------------+-----------+-------------------------------------------------+
OS installation successful
```

## Dry Run

```
# iserver create os-install embedded
    --serial WMP24040059
    --scu "SCU 6.2.2a"
    --image "Ubuntu 22.04LTS"
    --organization EMEAR-SPDC-Specialists
    --dry-run

Validate input parameters...
isctl create os install 
	--InstallMethod vMedia
	--Server="MoRef:ComputeRackUnitRelationship[Moid:5fdfe47f6176752d35001995]"
	--Image=MoRef[Moid:633068b96567612d304a7844]
	--OsduImage=MoRef[Moid:632c227a6567612d30187910]
	--Organization=MoRef[Moid:5dee1d736972652d321d26b5]
	--InstallTarget='{"ObjectType": "os.VirtualDrive", "Name": "main", "StorageControllerSlotId": "MRAID", "Id": "0"}'
	--Answers='{"Source": "Embedded"}'
```

## Developers output

```
# iserver create os-install embedded
    --serial WMP24040059
    --scu "SCU 6.2.2a"
    --image "Ubuntu 22.04LTS"
    --organization EMEAR-SPDC-Specialists

Developer output

{
    "duration": 141505,
    "isctl": {
        "read": true,
        "calls": 40,
        "success": 40,
        "failed": 0,
        "total_time": 46176
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

2022-10-12 10:01:49.399273	True	714	isctl get organization organization name "EMEAR-SPDC-Specialists" -o json
2022-10-12 10:01:51.400123	True	1966	isctl get compute rackunit  -o json --top 100
2022-10-12 10:01:52.017393	True	616	isctl get compute blade  -o json --top 100
2022-10-12 10:01:53.424463	True	1403	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:01:52.000Z" -o json --top 100
2022-10-12 10:01:54.685751	True	1244	isctl get compute serversetting  -o json --top 100
2022-10-12 10:01:55.015479	True	330	isctl get storage controller --filter "Parent/Moid eq '61dc833176752d3139cba603'" -o json --top 100
2022-10-12 10:01:55.560879	True	545	isctl get storage physicaldisk --filter "RegisteredDevice/Moid eq '5fdfe4666f72612d30130510'" -o json --top 100
2022-10-12 10:01:56.074572	True	513	isctl get storage virtualdrive --filter "RegisteredDevice/Moid eq '5fdfe4666f72612d30130510'" -o json --top 100
2022-10-12 10:01:57.021203	True	946	isctl get firmware serverconfigurationutilitydistributable name "SCU 6.2.2a" -o json
2022-10-12 10:01:57.878350	True	857	isctl get softwarerepository operatingsystemfile name "Ubuntu 22.04LTS" -o json
2022-10-12 10:01:58.354533	True	475	isctl get hcl operatingsystemvendor name "Ubuntu" -o json
2022-10-12 10:01:58.919053	True	562	isctl get hcl operatingsystem  -o json --top 100
2022-10-12 10:01:59.839430	True	919	isctl get hcl operatingsystem  -o json --top 100 --skip 100
2022-10-12 10:02:01.117223	True	1274	isctl create compute updatecomputeserversetting moid 5fdfe47f6573732d3006dc76 --AdminPowerState PowerCycle -o json
2022-10-12 10:02:02.203718	True	1081	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:01.000Z" -o json --top 100
2022-10-12 10:02:03.334771	True	1126	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:02.000Z" -o json --top 100
2022-10-12 10:02:09.652086	True	1307	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:08.000Z" -o json --top 100
2022-10-12 10:02:10.318083	True	663	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63467478696f6e2d30f8e329'" -o json --top 100
2022-10-12 10:02:13.125123	True	2804	isctl create os install  --InstallMethod vMedia --Server="MoRef:ComputeRackUnitRelationship[Moid:5fdfe47f6176752d35001995]" --Image=MoRef[Moid:633068b96567612d304a7844] --OsduImage=MoRef[Moid:632c227a6567612d30187910] --Organization=MoRef[Moid:5dee1d736972652d321d26b5] --InstallTarget='{"ObjectType": "os.VirtualDrive", "Name": "main", "StorageControllerSlotId": "MRAID", "Id": "0"}' --Answers='{"Source": "Embedded"}' -o json
2022-10-12 10:02:14.463200	True	1331	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:13.000Z" -o json --top 100
2022-10-12 10:02:20.818487	True	1345	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:19.000Z" -o json --top 100
2022-10-12 10:02:21.788618	True	963	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:20.000Z" -o json --top 100
2022-10-12 10:02:27.822882	True	1023	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:26.000Z" -o json --top 100
2022-10-12 10:02:34.178356	True	1344	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:32.000Z" -o json --top 100
2022-10-12 10:02:40.535547	True	1345	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:39.000Z" -o json --top 100
2022-10-12 10:02:46.950850	True	1404	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:45.000Z" -o json --top 100
2022-10-12 10:02:53.336870	True	1374	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:51.000Z" -o json --top 100
2022-10-12 10:02:59.547870	True	1200	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:02:58.000Z" -o json --top 100
2022-10-12 10:03:05.943576	True	1384	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:04.000Z" -o json --top 100
2022-10-12 10:03:12.316277	True	1361	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:10.000Z" -o json --top 100
2022-10-12 10:03:18.643310	True	1316	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:17.000Z" -o json --top 100
2022-10-12 10:03:25.032109	True	1377	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:23.000Z" -o json --top 100
2022-10-12 10:03:30.998600	True	955	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:30.000Z" -o json --top 100
2022-10-12 10:03:37.350185	True	1340	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:36.000Z" -o json --top 100
2022-10-12 10:03:43.993608	True	1632	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:42.000Z" -o json --top 100
2022-10-12 10:03:50.215794	True	1210	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:49.000Z" -o json --top 100
2022-10-12 10:03:56.639843	True	1412	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:03:55.000Z" -o json --top 100
2022-10-12 10:04:03.034974	True	1384	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:04:01.000Z" -o json --top 100
2022-10-12 10:04:09.468243	True	1421	isctl get workflow workflowinfo --filter "CreateTime gt 2022-10-11T10:04:08.000Z" -o json --top 100
2022-10-12 10:04:10.181437	True	710	isctl get workflow taskinfo --filter "WorkflowInfo/Moid eq '63467485696f6e2d30f8e390'" -o json --top 100
```