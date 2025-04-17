# Workflow

Get workflow's detail selected by Moid in table, json or yaml formats.

```
# iserver get is workflow --help

Usage: iserver.py get is workflow [OPTIONS] WORKFLOW_ID

  Get workflow

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 61 ms and logs saved in /tmp/iserver\67a9a394d6a1
```

Default output

```
# iserver get is workflow <workflow-id>

Get server workflow info...

Server
- Name: Server123
- Model: UCSC-C220-M5SX
- Serial: Serial123
- IP: 10.10.10.10


Workflow
- Workflow ID: <workflow-id>
- Name: Turn Off Locator
- Status: COMPLETED
- Create Time: 2024-05-24T18:12:58.058Z
- Start Time: 2024-05-24T18:12:58.09Z
- End Time: 2024-05-24T18:13:00.308Z
- Duration: 00:00:02


+--------------------------+---------------------------------+--------------------------+-----------+----------+---------------------------+
| Task Moid                | Description                     | Create Time              | Status    | Duration | Details                   |
+--------------------------+---------------------------------+--------------------------+-----------+----------+---------------------------+
| Task-id                  | workflow.StartWorkflowTask      | 2024-05-24T18:12:58.169Z | COMPLETED | 00:00:00 |                           |
| Task-id                  | Turn off Locator LED            | 2024-05-24T18:12:58.228Z | COMPLETED | 00:00:01 | Locator LED is turned off |
| Task-id                  | Turn off the Locator LED        | 2024-05-24T18:12:59.713Z | NO_OP     | 00:00:00 |                           |
| Task-id                  | Turn off the Locator LED        | 2024-05-24T18:12:59.883Z | NO_OP     |          |                           |
| Task-id                  | Update Server Inventory         | 2024-05-24T18:12:59.952Z | COMPLETED | 00:00:01 | State synchronized.       |
| Task-id                  | workflow.SuccessEndWorkflowTask | 2024-05-24T18:13:00.253Z | COMPLETED | 00:00:00 |                           |
+--------------------------+---------------------------------+--------------------------+-----------+----------+---------------------------+
```
