# Virtual Machine - Restart

## Workflow

- select virtual machines by namespace, name or all
- for every virtual machine with VirtualMachineInstance CRD, delete vmi
- wait for virtual machine running

## Configurable options

```
# iserver set k8s vm restart 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Virtual machine namespace
  --name TEXT       Virtual machine name
  --no-wait         No wait
  --no-confirm      Confirmation mode
```

## Example

```
# iserver set k8s vm restart --cluster bm1 --namespace default --name fedora-lime-python-82


OpenShift Workflow - Virtual Machine - Restart
==============================================

OpenShift Cluster: bm3

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Running | 1h37m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       | 
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
Continue [Y/N]? y

Restart Virtual Machine
-----------------------
- namespace: default
- name: fedora-lime-python-82
- state: Running
- runStrategy: Always
- vmi found <=> vm currently running
- vmi deletetd
Wait for virtual machine up

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Running | 1h37m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
```

[[Back]](./README.md)