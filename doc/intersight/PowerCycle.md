# Power Cycle

```
# iserver set server power cycle --help

Usage: iserver.py set server power cycle [OPTIONS]

  Power cycle

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

Info: finished in 23 ms and logs saved in /tmp/iserver\4217acdbb3ad
```

## Basic execution

```
# iserver set server power cycle --group self-test-power

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
Power Cycle request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Power Cycle   | 00:00:05 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Power Cycle   | 00:00:04 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
```

## Verbose output

```
# iserver set server power cycle --group self-test-power

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
	--AdminPowerState PowerCycle
isctl create compute updatecomputeserversetting moid <moid>
	--AdminPowerState PowerCycle
Collect workflow information...
Power Cycle request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Power Cycle   | 00:00:05 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Power Cycle   | 00:00:04 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+

Server
- Name: Server100
- Model: UCSC-C220-M5SX
- Serial: Serial-100
- IP: 10.10.10.10


Workflow
- Workflow ID: Worklof-id
- Name: Power Cycle
- Status: COMPLETED
- Create Time: 2024-05-24T16:15:01.621Z
- Start Time: 2024-05-24T16:15:01.671Z
- End Time: 2024-05-24T16:15:06.118Z
- Duration: 00:00:05


+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                                       | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask                        | 2024-05-24T16:15:01.739Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type                        | 2024-05-24T16:15:01.845Z | COMPLETED | 00:00:00 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type           | 2024-05-24T16:15:02.044Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Check and Execute Set One Time Boot Configuration | 2024-05-24T16:15:02.227Z | COMPLETED | 00:00:00 | The task evaluated to case false                                             |
| Task-id                  | Invoke Server Power Cycle                         | 2024-05-24T16:15:02.434Z | COMPLETED | 00:00:03 | Server power cycle is initiated                                              |
| Task-id                  | Invoke the Server Power Cycle                     | 2024-05-24T16:15:05.528Z | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                           | 2024-05-24T16:15:05.721Z | COMPLETED | 00:00:00 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask                   | 2024-05-24T16:15:06.035Z | COMPLETED | 00:00:00 |                                                                              |
+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+

Server
- Name: Server101
- Model: UCSC-C220-M5SX
- Serial: Serial-101
- IP: 10.10.10.20


Workflow
- Workflow ID: Worklof-id
- Name: Power Cycle
- Status: COMPLETED
- Create Time: 2024-05-24T16:15:03.279Z
- Start Time: 2024-05-24T16:15:03.309Z
- End Time: 2024-05-24T16:15:07.816Z
- Duration: 00:00:04


+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                                       | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask                        | 2024-05-24T16:15:03.405Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type                        | 2024-05-24T16:15:03.478Z | COMPLETED | 00:00:00 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type           | 2024-05-24T16:15:03.651Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Check and Execute Set One Time Boot Configuration | 2024-05-24T16:15:03.815Z | COMPLETED | 00:00:00 | The task evaluated to case false                                             |
| Task-id                  | Invoke Server Power Cycle                         | 2024-05-24T16:15:04.02Z  | COMPLETED | 00:00:03 | Server power cycle is initiated                                              |
| Task-id                  | Invoke the Server Power Cycle                     | 2024-05-24T16:15:07.253Z | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                           | 2024-05-24T16:15:07.424Z | COMPLETED | 00:00:00 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask                   | 2024-05-24T16:15:07.726Z | COMPLETED | 00:00:00 |                                                                              |
+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
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
