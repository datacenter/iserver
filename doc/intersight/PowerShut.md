# OS Shutdown

```
# iserver set server power shut --help

Usage: iserver.py set server power shut [OPTIONS]

  Power shut

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --serial TEXT    Serial numbers
  --group TEXT     Select by group name
  --name TEXT      Name loose match
  --ip TEXT        Management IP address or subnet filter
  --confirm        Confirmation mode
  --no-wait        Wait mode
  --dry-run        Dry run
  --verbose        Verbose output
  --devel          Developer output
  --help           Show this message and exit.

Info: finished in 37 ms and logs saved in /tmp/iserver\91d7c49bd4f0
```

## Basic execution

```
# iserver set server power shut --group self-test-power

Server Summary [#2]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Collect workflow information...
OS Shutdown request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Shut Down OS  | 00:00:04 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Shut Down OS  | 00:00:04 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
```

## Verbose output

```
# iserver set server power shut --group self-test-power

Server Summary [#2]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

isctl create compute updatecomputeserversetting moid <moid>
	--AdminPowerState Shutdown
isctl create compute updatecomputeserversetting moid <moid>
	--AdminPowerState Shutdown
Collect workflow information...
OS Shutdown request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Shut Down OS  | 00:00:04 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Shut Down OS  | 00:00:04 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+

Server
- Name: Server100
- Model: UCSC-C220-M5SX
- Serial: Serial-100
- IP: 10.10.10.10


Workflow
- Workflow ID: Workflow-id
- Name: Shut Down OS
- Status: COMPLETED
- Create Time: 2024-05-24T16:19:34.023Z
- Start Time: 2024-05-24T16:19:34.05Z
- End Time: 2024-05-24T16:19:38.278Z
- Duration: 00:00:04


+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                             | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask              | 2024-05-24T16:19:34.124Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type              | 2024-05-24T16:19:34.201Z | COMPLETED | 00:00:00 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type | 2024-05-24T16:19:34.391Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Invoke Server Shutdown                  | 2024-05-24T16:19:34.558Z | COMPLETED | 00:00:03 | Server shutdown is initiated                                                 |
| Task-id                  | Invoke the Server Shutdown              | 2024-05-24T16:19:37.784Z | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                 | 2024-05-24T16:19:37.953Z | COMPLETED | 00:00:01 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask         | 2024-05-24T16:19:38.223Z | COMPLETED | 00:00:00 |                                                                              |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+

Server
- Name: Server101
- Model: UCSC-C220-M5SX
- Serial: Serial-101
- IP: 10.10.10.20


Workflow
- Workflow ID: Workflow-id
- Name: Shut Down OS
- Status: COMPLETED
- Create Time: 2024-05-24T16:19:35.798Z
- Start Time: 2024-05-24T16:19:35.826Z
- End Time: 2024-05-24T16:19:39.687Z
- Duration: 00:00:04


+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                             | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask              | 2024-05-24T16:19:35.892Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type              | 2024-05-24T16:19:35.981Z | COMPLETED | 00:00:01 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type | 2024-05-24T16:19:36.171Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Invoke Server Shutdown                  | 2024-05-24T16:19:36.333Z | COMPLETED | 00:00:03 | Server shutdown is initiated                                                 |
| Task-id                  | Invoke the Server Shutdown              | 2024-05-24T16:19:39.171Z | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                 | 2024-05-24T16:19:39.321Z | COMPLETED | 00:00:00 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask         | 2024-05-24T16:19:39.633Z | COMPLETED | 00:00:00 |                                                                              |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
```

## Servers State

Before task

```
# iserver get server --serial Serial-100,Serial-101

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Server Summary [#2]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

After task

```
# iserver get server --serial Serial-100,Serial-101

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Server Summary [#2]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P- H | cRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P- H | cRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```
