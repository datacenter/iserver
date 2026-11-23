# Workflows

Get selected workflows' information in table, json or yaml formats.

Use command options for workflows' filtering.

```
# iserver get is workflows --help

Usage: iserver.py get is workflows [OPTIONS]

  Get workflows

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  --ip TEXT                       Select by IP or subnet
  --name TEXT                     Select by name
  --serial TEXT                   Select by serial
  --model TEXT                    Select by model
  --type [any|blade|rack]         Select by type  [default: any]
  --group TEXT                    Select by group name
  --failed                        Filter failed
  --completed                     Filter completed
  --power                         Filter power related
  --os                            Filter OS related
  --fw                            Filter firmware related
  --count INTEGER                 Last <n> count  [default: -1]
  --days INTEGER                  Last <n> days
  --ttl TEXT                      Cache TTL
  --order [server|workflow|date]  [default: date]
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 58 ms and logs saved in /tmp/iserver\7382c02f356a
```

## Example: failed workflows

```
# iserver get is workflows
    --group mygroup
    --failed
    --days 7
    --count 5
    --order workflow

Get servers info...

No workflows found
```

## Example: power related in last 7 days

```
# iserver get is workflows
    --group mygroup
    --power
    --order workflow
    --days 7
    --count 5

Get servers info...

+---------+--------------------------------+-------------+-------------+--------------------------+--------------+--------------------------+----------+-----------+
| SF      | Server Name                    | Server IP   | Serial      | Workflow ID              | Name         | Create Time              | Duration | Status    |
+---------+--------------------------------+-------------+-------------+--------------------------+--------------+--------------------------+----------+-----------+
| P+ H    | Server123                      | 10.10.10.10 | Serial123   | Workflow-id              | Power Cycle  | 2024-05-24T16:15:03.279Z | 00:00:04 | COMPLETED |
| P+ H    | Server666                      | 10.10.10.66 | Serial666   | Workflow-id              | Power Cycle  | 2024-05-24T16:15:01.621Z | 00:00:05 | COMPLETED |
+---------+--------------------------------+-------------+-------------+--------------------------+--------------+--------------------------+----------+-----------+
```
