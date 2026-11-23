# Virtual Machine - Stop

## Workflow

- select virtual machines by namespace, name or all
- for every virtual machine in running state patch spec:runStrategy to Halted <=> stop virtual machine
- wait for virtual machine down

## Configurable options

```
# iserver set k8s vm stop 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Virtual machine namespace
  --name TEXT       Virtual machine name
  --no-wait         No wait
  --no-confirm      Confirmation mode
```

## Example

```
# iserver set k8s vm stop --cluster bm1 --namespace default --name fedora-lime-python-82

OpenShift Workflow - Virtual Machine - Stop
===========================================

OpenShift Cluster: bm1

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Running | 1h13m | 
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       | 
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
Continue [Y/N]? y

Stop Virtual Machine
--------------------
- namespace: default
- name: fedora-lime-python-82
- state: Running
- runStrategy: RerunOnFailure
- vmi found <=> vm currently running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: fedora-lime-python-82
  namespace: default
spec:
  runStrategy: Halted

~~~

Virtual machine patched
Wait for virtual machine down
Wait for no virtual machine instance

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Stopped | 1h13m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
```

[[Back]](./README.md)