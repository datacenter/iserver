# Power Off

```
# iserver set server power off --help

Usage: iserver.py set server power off [OPTIONS]

  Power off

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

Info: finished in 28 ms and logs saved in /tmp/iserver\0330342f603b
```

## Basic execution

```
# iserver set server power off --group self-test-power

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
Power Off request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Power Off     | 00:00:04 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Power Off     | 00:00:05 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
```

## Verbose output

```
# iserver set server power off --group self-test-power

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
	--AdminPowerState PowerOff
isctl create compute updatecomputeserversetting moid <moid>
	--AdminPowerState PowerOff
Collect workflow information...
Power Off request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Power Off     | 00:00:04 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Power Off     | 00:00:05 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+---------------+----------+-----------+

Server
- Name: Server100
- Model: UCSC-C220-M5SX
- Serial: Serial-100
- IP: 10.10.10.10


Workflow
- Workflow ID: Workflow-id
- Name: Power Off
- Status: COMPLETED
- Create Time: 2024-05-24T16:06:34.759Z
- Start Time: 2024-05-24T16:06:34.8Z
- End Time: 2024-05-24T16:06:38.518Z
- Duration: 00:00:04


+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                             | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask              | 2024-05-24T16:06:34.899Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type              | 2024-05-24T16:06:35.026Z | COMPLETED | 00:00:00 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type | 2024-05-24T16:06:35.227Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Invoke Server Power Off                 | 2024-05-24T16:06:35.42Z  | COMPLETED | 00:00:02 | Server power off is initiated                                                |
| Task-id                  | Invoke the Server Power Off             | 2024-05-24T16:06:37.987Z | NO_OP     | 00:00:01 |                                                                              |
| Task-id                  | Update Server Inventory                 | 2024-05-24T16:06:38.147Z | COMPLETED | 00:00:00 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask         | 2024-05-24T16:06:38.426Z | COMPLETED | 00:00:00 |                                                                              |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+

Server
- Name: Server101
- Model: UCSC-C220-M5SX
- Serial: Serial-101
- IP: 10.10.10.20


Workflow
- Workflow ID: <workflow-id>
- Name: Power Off
- Status: COMPLETED
- Create Time: 2024-05-24T16:06:36.802Z
- Start Time: 2024-05-24T16:06:36.83Z
- End Time: 2024-05-24T16:06:41.256Z
- Duration: 00:00:05


+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                             | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+-----------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask              | 2024-05-24T16:06:36.913Z | COMPLETED | 00:00:00 |                                                                              |
| Task-id                  | Validate the platform type              | 2024-05-24T16:06:36.985Z | COMPLETED | 00:00:01 | Physical Summary for Server Moid Moid-value found successfully               |
| Task-id                  | Invoke tasks based on the platform type | 2024-05-24T16:06:37.211Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             |
| Task-id                  | Invoke Server Power Off                 | 2024-05-24T16:06:37.424Z | COMPLETED | 00:00:03 | Server power off is initiated                                                |
| Task-id                  | Invoke the Server Power Off             | 2024-05-24T16:06:40.764Z | NO_OP     | 00:00:00 |                                                                              |
| Task-id                  | Update Server Inventory                 | 2024-05-24T16:06:40.919Z | COMPLETED | 00:00:01 | State synchronized.                                                          |
| Task-id                  | workflow.SuccessEndWorkflowTask         | 2024-05-24T16:06:41.19Z  | COMPLETED | 00:00:00 |                                                                              |
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
| P- H | CRi | Server100                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-100  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P- H | CRi | Server101                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | Serial-101  | 10.10.10.20 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```
