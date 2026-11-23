# CIMC Reboot

```
# iserver set server power reboot --help

Usage: iserver.py set server power reboot [OPTIONS]

  Power reboot

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

Info: finished in 32 ms and logs saved in /tmp/iserver\55d042008222
```

## Basic execution

```
# iserver set server power reboot --group self-test-power

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
Reboot Management Controller request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+------------------------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name                | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+------------------------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Reboot Management Controller | 00:00:11 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Reboot Management Controller | 00:00:10 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+------------------------------+----------+-----------+
```

## Verbose output

```
# iserver set server power reboot --group self-test-power

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
	--AdminPowerState Reboot
isctl create compute updatecomputeserversetting moid <moid>
	--AdminPowerState Reboot
Collect workflow information...
Reboot Management Controller request: [#######################] 2/2
Workflows started: [#######################] 2/2
Workflows finished: [#######################] 2/2

+--------------------------+--------------------------------+--------------------------+------------------------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name                | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+------------------------------+----------+-----------+
| Moid-value               | Server100                      | Workflow-id              | Reboot Management Controller | 00:00:11 | COMPLETED |
| Moid-value               | Server101                      | Workflow-id              | Reboot Management Controller | 00:00:10 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+------------------------------+----------+-----------+

Server
- Name: Server100
- Model: UCSC-C220-M5SX
- Serial: Serial-100
- IP: 10.10.10.10


Workflow
- Workflow ID: Workflow-id
- Name: Reboot Management Controller
- Status: COMPLETED
- Create Time: 2024-05-24T16:24:08.213Z
- Start Time: 2024-05-24T16:24:08.244Z
- End Time: 2024-05-24T16:24:19.013Z
- Duration: 00:00:11


+--------------------------+-------------------------------------+--------------------------+-----------+----------+-------------------------------------------------+
| Task Moid                | Description                         | Create Time              | Status    | Duration | Details                                         |
+--------------------------+-------------------------------------+--------------------------+-----------+----------+-------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask          | 2024-05-24T16:24:08.309Z | COMPLETED | 00:00:00 |                                                 |
| Task-id                  | Invoke Management Controller Reboot | 2024-05-24T16:24:08.385Z | COMPLETED | 00:00:10 | Cisco Management Controller reboot is initiated |
| Task-id                  | Invoke Management Controller Reboot | 2024-05-24T16:24:18.57Z  | NO_OP     | 00:00:00 |                                                 |
| Task-id                  | Invoke Management Controller Reboot | 2024-05-24T16:24:18.816Z | NO_OP     |          |                                                 |
| Task-id                  | Update Server Inventory             | 2024-05-24T16:24:18.868Z | NO_OP     | 00:00:00 | Skipped                                         |
| Task-id                  | workflow.SuccessEndWorkflowTask     | 2024-05-24T16:24:18.962Z | COMPLETED | 00:00:00 |                                                 |
+--------------------------+-------------------------------------+--------------------------+-----------+----------+-------------------------------------------------+

Server
- Name: Server101
- Model: UCSC-C220-M5SX
- Serial: Serial-101
- IP: 10.10.10.20


Workflow
- Workflow ID: Workflow-id
- Name: Reboot Management Controller
- Status: COMPLETED
- Create Time: 2024-05-24T16:24:09.997Z
- Start Time: 2024-05-24T16:24:10.027Z
- End Time: 2024-05-24T16:24:20.714Z
- Duration: 00:00:10


+--------------------------+-------------------------------------+--------------------------+-----------+----------+-------------------------------------------------+
| Task Moid                | Description                         | Create Time              | Status    | Duration | Details                                         |
+--------------------------+-------------------------------------+--------------------------+-----------+----------+-------------------------------------------------+
| Task-id                  | workflow.StartWorkflowTask          | 2024-05-24T16:24:10.107Z | COMPLETED | 00:00:00 |                                                 |
| Task-id                  | Invoke Management Controller Reboot | 2024-05-24T16:24:10.16Z  | COMPLETED | 00:00:10 | Cisco Management Controller reboot is initiated |
| Task-id                  | Invoke Management Controller Reboot | 2024-05-24T16:24:20.339Z | NO_OP     | 00:00:00 |                                                 |
| Task-id                  | Invoke Management Controller Reboot | 2024-05-24T16:24:20.51Z  | NO_OP     |          |                                                 |
| Task-id                  | Update Server Inventory             | 2024-05-24T16:24:20.565Z | NO_OP     | 00:00:00 | Skipped                                         |
| Task-id                  | workflow.SuccessEndWorkflowTask     | 2024-05-24T16:24:20.66Z  | COMPLETED | 00:00:00 |                                                 |
+--------------------------+-------------------------------------+--------------------------+-----------+----------+-------------------------------------------------+
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
