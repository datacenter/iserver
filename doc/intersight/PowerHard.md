# Hard Reset

```
# iserver set server power hard --help

Usage: iserver.py set server power hard [OPTIONS]

  Power hard

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

Info: finished in 22 ms and logs saved in /tmp/iserver\9b82e5102a5e
```

## Basic execution

```
# iserver set server power hard --group self-test-power

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
Hard Reset request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Hard Reset    | 00:00:22 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Hard Reset    | 00:00:23 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
```

## Verbose output

```
# iserver set server power hard --group self-test-power

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
	--AdminPowerState HardReset
isctl create compute updatecomputeserversetting moid <moid>
	--AdminPowerState HardReset
Collect workflow information...
Hard Reset request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Hard Reset    | 00:00:22 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Hard Reset    | 00:00:23 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+

Server
- Name: Server100
- Model: UCSC-C220-M5SX
- Serial: Serial-100
- IP: 10.10.10.10


Workflow
- Workflow ID: Workflow-id
- Name: Hard Reset
- Status: COMPLETED
- Create Time: 2024-05-24T16:10:41.125Z
- Start Time: 2024-05-24T16:10:41.162Z
- End Time: 2024-05-24T16:11:03.399Z
- Duration: 00:00:22


+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                             | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask              | 2024-05-24T16:10:41.244Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type              | 2024-05-24T16:10:41.322Z | COMPLETED | 00:00:00 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type | 2024-05-24T16:10:41.55Z  | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Invoke Server Hard Reset                | 2024-05-24T16:10:41.727Z | COMPLETED | 00:00:21 | Server hard reset is initiated                                               |
| Task-id                  | Invoke the Server Hard Reset            | 2024-05-24T16:11:02.885Z | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                 | 2024-05-24T16:11:03.061Z | COMPLETED | 00:00:00 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask         | 2024-05-24T16:11:03.33Z  | COMPLETED | 00:00:00 |                                                                              |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+

Server
- Name: Server101
- Model: UCSC-C220-M5SX
- Serial: Serial-101
- IP: 10.10.10.20


Workflow
- Workflow ID: Workflow-id
- Name: Hard Reset
- Status: COMPLETED
- Create Time: 2024-05-24T16:10:42.73Z
- Start Time: 2024-05-24T16:10:42.76Z
- End Time: 2024-05-24T16:11:05.281Z
- Duration: 00:00:23


+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                             | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask              | 2024-05-24T16:10:42.839Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type              | 2024-05-24T16:10:42.943Z | COMPLETED | 00:00:01 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type | 2024-05-24T16:10:43.208Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Invoke Server Hard Reset                | 2024-05-24T16:10:43.538Z | COMPLETED | 00:00:21 | Server hard reset is initiated                                               |
| Task-id                  | Invoke the Server Hard Reset            | 2024-05-24T16:11:04.76Z  | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                 | 2024-05-24T16:11:04.926Z | COMPLETED | 00:00:01 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask         | 2024-05-24T16:11:05.215Z | COMPLETED | 00:00:00 |                                                                              |
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
| P+ H | CRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
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
| P+ H | CRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```
