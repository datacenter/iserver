# Virtual Machine - Pause

## Workflow

- select virtual machines by namespace, name or all
- for every virtual machine in running state execute 'virtctl pause vm'
- wait for virtual machine paused

Notes:
- requires [cluster management server](../ManagementServer.md) defined and [virtctl cli](../cli/virtctl.md)

## Configurable options

```
# iserver set k8s vm pause 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Virtual machine namespace
  --name TEXT       Virtual machine name
  --no-wait         No wait
  --no-confirm      Confirmation mode
```

## Example

```
# iserver set k8s vm pause --cluster bm1 --namespace default --name fedora-lime-python-82

OpenShift Workflow - Virtual Machine - Pause
============================================

OpenShift Cluster: bm3

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Running | 1h20m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
Continue [Y/N]? y

Pause Virtual Machine
---------------------
- namespace: default
- name: fedora-lime-python-82
- state: Running
Wait for virtual machine paused

+----+-----------------------+-----+--------+---------------+----------------+--------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status | Age   |
+----+-----------------------+-----+--------+---------------+----------------+--------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Paused | 1h31m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |        |       |
+----+-----------------------+-----+--------+---------------+----------------+--------+-------+
```

[[Back]](./README.md)