# OpenShift Operations Automation via Tasks

## Overview 

- tasks allow to define the execution of several workflows in batch
- each workflow is defined by task-name followed with task-parameters that are specific to the workflow
- check details of the operations features and search for task-way documentation to understand the syntax
- tasks can be passed to create or delete workflow

## Input file structure

Input json file defines the list of dictionaries, where each dictionary has single item with the task name followed with task parameters, check supported tasks table below for quick links to task parameters

```
[
    {
        "task-name": {
            task-parameters
        }
    },
    {
        "task-name": {
            task-parameters
        }
    }
]
```

Example:

```
[
    {
        "lvm": {
            "operator": {},
            "cluster": {
                "device": [
                  "sda",
                  "sdb"
                ]
            }
        }
    },
    {
        "grafana": {
            "operator": {},
            "mon": {},
            "instance": [
                {
                    "instance": "testa",
                    "username": "usera",
                    "password": "pass",
                    "prometheus": true,
                    "datasource": "k8s",
                    "crd": [
                      "file-or-directory"
                    ],
                    "fixup": true
                },
                {
                    "instance": "testb",
                    "username": "userb",
                    "password": "pass",
                    "prometheus": true,
                    "datasource": "k8s"
                }
            ]
        }
    }
]
```

## Supported tasks

Feature | Create | Delete
--- | --- | ---
Container virtualization (cnv) | [Link](./cnv/create_task.md) | [Link](./cnv/delete_task.md)
GPU | [Link](./gpu/create_task.md) | [Link](./gpu/delete_task.md)
Grafana | [Link](./grafana/create_task.md) | [Link](./grafana/delete_task.md)
HTPasswd Identity Provider | [Link](./htpasswd/create_task.md) | [Link](./htpasswd/delete_task.md)
Local Storage | [Link](./lso/create_task.md) | [Link](./lso/delete_task.md)
LVM Storage | [Link](./lvm/create_task.md) | [Link](./lvm/delete_task.md)
Node Feature Discovery (nfd) | [Link](./nfd/create_task.md) | [Link](./nfd/delete_task.md)
NMstate | [Link](./nmstate/create_task.md) | [Link](./nmstate/delete_task.md)
OpenShift Data Foundation (odf) | [Link](./odf/create_task.md) | [Link](./odf/delete_task.md)
SR-IOV | [Link](./sriov/create_task.md) | [Link](./sriov/delete_task.md)
SSH | [Link](./ssh/create_task.md) | [Link](./ssh/delete_task.md)
Tetragon | [Link](./tetragon/create_task.md) | [Link](./tetragon/delete_task.md)
Trident | [Link](./trident/create_task.md) | [Link](./trident/delete_task.md)

## Create tasks

```
# iserver set ocp task --cluster cluster-name --filename task-filename
```

```
# iserver set ocp task --help
Options:
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
  --help           Show this message and exit
```

## Delete tasks

```
# iserver delete ocp task --cluster cluster-name --filename task-filename
```

```
# iserver delete ocp task --help
Options:
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
  --help           Show this message and exit
```

[[Back]](./Operations.md)