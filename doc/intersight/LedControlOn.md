# Locator LED On

## Help output

```
# iserver set server locator on --help

Usage: iserver.py set server locator on [OPTIONS]

  Locator on

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

Info: finished in 29 ms and logs saved in /tmp/iserver\ca56ca548348
```

## Default output

```
# iserver set server locator on --group self-test-locator

Server Summary [#1]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL-123  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Collect workflow information...
Turn On Locator request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+--------------------------+--------------------------------+--------------------------+-----------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name   | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+-----------------+----------+-----------+
| Moid-value               | Server123                      | Workflow-id-value        | Turn On Locator | 00:00:06 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+-----------------+----------+-----------+
```

Server state

```
# iserver get server --group self-test-locator

iaccount isctl (cache: off)
Select servers...
Selected servers: 1
Collect server api objects...


Server Summary [#1]
-------------------

+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | CRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL-123  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Dry run

```
# iserver set server locator on --group self-test-locator --dry-run

Server Summary [#1]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL-123  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

isctl create compute updatecomputeserversetting moid <moid>
	--AdminLocatorLedState On
```

## Verbose

```
# iserver set server locator on --group self-test-locator

Server Summary [#1]
-------------------

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | cRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL-123  | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

isctl create compute updatecomputeserversetting moid <moid>
	--AdminLocatorLedState On
Collect workflow information...
Turn On Locator request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+--------------------------+--------------------------------+--------------------------+-----------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name   | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+-----------------+----------+-----------+
| Moid-value               | Server123                      | Workflow-id-value        | Turn On Locator | 00:00:06 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+-----------------+----------+-----------+
```
