# Locator LED Off

## Help output

```
# iserver set server locator off --help

Usage: iserver.py set server locator off [OPTIONS]

  Locator off

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

Info: finished in 30 ms and logs saved in /tmp/iserver\694f2d38d73f
```

## Default output

```
# iserver set server locator off --group self-test-locator

Server Summary [#1]
-------------------

+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | cRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL00001 | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Collect workflow information...
Turn Off Locator request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+--------------------------+--------------------------------+--------------------------+------------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name    | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+------------------+----------+-----------+
| Moid-value               | Server123                      | Workflow-id-value        | Turn Off Locator | 00:00:03 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+------------------+----------+-----------+
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

+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL00001 | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Dry run

```
# iserver set server locator off --group self-test-locator --dry-run

Server Summary [#1]
-------------------

+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | cRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL00001 | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

isctl create compute updatecomputeserversetting moid <moid>
	--AdminLocatorLedState Off
```

## Verbose

```
# iserver set server locator off --group self-test-locator

Server Summary [#1]
-------------------

+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | Name                           | Moid                     | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | cRi | Server123                      | Moid-value               | ---        | (R) UCSC-C220-M5SX | SERIAL00001 | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+--------+-----+--------------------------------+--------------------------+------------+--------------------+-------------+-------------+------------+-----------+

isctl create compute updatecomputeserversetting moid <moid>
	--AdminLocatorLedState Off
Collect workflow information...
Turn Off Locator request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+--------------------------+--------------------------------+--------------------------+------------------+----------+-----------+
| Server Moid              | Server Name                    | Workflow ID              | Workflow Name    | Duration | Status    |
+--------------------------+--------------------------------+--------------------------+------------------+----------+-----------+
| Moid-value               | Server123                      | Workflow-id-value        | Turn Off Locator | 00:00:03 | COMPLETED |
+--------------------------+--------------------------------+--------------------------+------------------+----------+-----------+
```
