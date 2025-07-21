# Tasks

General notes:
- tasks are optional
- tasks run only after successful installation of bare metal cluster
- use --mode tasks flag during command execution to run tasks only
- it should be safe to re-run the tasks however this is in general designed to run only once
- by default, the tasks will run to completion even if some tasks fail
- add 'break-on-error:flag' property per task if you want workflow to stop when task fails
- tasks can be defined in tasks.json file or 'tasks' diction in the main cluster.json file

Input format

```
    "tasks": [
        {
            "task-name": {
                task-parameters
            }
        }
    ]
```

Supported tasks:
- [cli](./input_data_task_cli.md)
- [cni](./input_data_task_cni.md)
- [identity](./input_data_task_identity.md)
- [nfd](./input_data_task_nfd.md)
- [nmstate](./input_data_task_nmstate.md)
- [sriov](./input_data_task_sriov.md)
- [ssh](./input_data_task_ssh.md)

[Back](../BareMetalCluster.md)
