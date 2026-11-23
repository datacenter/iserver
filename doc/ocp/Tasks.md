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
    }
]
```

## Example

Scope | Link
--- | ---
Access | [Link](./task/access.json)
AI | [Link](./task/ai.json)
Monitoring | [Link](./task/monitoring.json)
Network | [Link](./task/network.json)
Storage | [Link](./task/storage.json)

## Supported tasks

Feature | Create | Delete
--- | --- | ---
Cilium Image | [Link](./cilium-cni/set_image_task.md) | ---
Cilium BGP | [Link](./cilium-bgp/create_task.md) | [Link](./cilium-bgp/delete_task.md)
Cilium Mesh | [Link](./cilium-mesh/create_task.md) | [Link](./cilium-mesh/delete_task.md)
Cilium Private Network | [Link](./cilium-pnet/create_task.md) | [Link](./cilium-pnet/delete_task.md)
Cilium Timescape | [Link](./cilium-timescape/create_task.md) | [Link](./cilium-timescape/delete_task.md)
CLI tools | [Link](./cli/create_task.md) | ---
Container virtualization (cnv) | [Link](./cnv/create_task.md) | [Link](./cnv/delete_task.md)
GPU | [Link](./gpu/create_task.md) | [Link](./gpu/delete_task.md)
Grafana | [Link](./grafana/create_task.md) | [Link](./grafana/delete_task.md)
HTPasswd Identity Provider | [Link](./htpasswd/create_task.md) | [Link](./htpasswd/delete_task.md)
Intersight Open Telemetry | [Link](./iotel/create_task.md) | [Link](./iotel/delete_task.md)
Intersight Server Discovery | [Link](./imm/create_task.md) | [Link](./imm/delete_task.md)
Isovalent Network Bridge | [Link](./inb/create_task.md) | [Link](./inb/delete_task.md)
Local Storage | [Link](./lso/create_task.md) | [Link](./lso/delete_task.md)
LVM Storage | [Link](./lvm/create_task.md) | [Link](./lvm/delete_task.md)
MinIO AIStor | [Link](./minio/create_task.md) | [Link](./minio/delete_task.md)
Node Feature Discovery (nfd) | [Link](./nfd/create_task.md) | [Link](./nfd/delete_task.md)
NMstate | [Link](./nmstate/create_task.md) | [Link](./nmstate/delete_task.md)
NVIDIA NIM | [Link](./nim/create_task.md) | [Link](./nim/delete_task.md)
OpenShift Data Foundation (odf) | [Link](./odf/create_task.md) | [Link](./odf/delete_task.md)
Portworx | [Link](./portworx/create_task.md) | [Link](./portworx/delete_task.md)
Red Hat OpenShift AI | [Link](./ai/create_task.md) | [Link](./ai/delete_task.md)
Serverless | [Link](./serverless/create_task.md) | [Link](./serverless/delete_task.md)
Service Mesh | [Link](./service-mesh/create_task.md) | [Link](./service-mesh/delete_task.md)
SR-IOV | [Link](./sriov/create_task.md) | [Link](./sriov/delete_task.md)
SSH | [Link](./ssh/create_task.md) | [Link](./ssh/delete_task.md)
Tetragon | [Link](./tetragon/create_task.md) | [Link](./tetragon/delete_task.md)
Trident | [Link](./trident/create_task.md) | [Link](./trident/delete_task.md)
Web Terminal | [Link](./web-terminal/create_task.md) | ---

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