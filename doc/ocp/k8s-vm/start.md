# Virtual Machine - Start

## Workflow

- select virtual machines by namespace, name or all
- for every virtual machine in stopped state patch spec:runStrategy to Always <=> start virtual machine
- wait for virtual machine running

## Configurable options

```
# iserver set k8s vm start 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Virtual machine namespace
  --name TEXT       Virtual machine name
  --no-wait         No wait
  --no-confirm      Confirmation mode
```

## Example

```
# iserver set k8s vm start --cluster bm1 --namespace default --name fedora-lime-python-82

OpenShift Workflow - Virtual Machine - Start
============================================

OpenShift Cluster: bm3

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Stopped | 1h17m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
Continue [Y/N]? y

Start Virtual Machine
---------------------
- namespace: default
- name: fedora-lime-python-82
- state: Stopped
- runStrategy: Halted
- vmi not found <=> vm currently not running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: fedora-lime-python-82
  namespace: default
spec:
  runStrategy: Always

~~~

Virtual machine patched
Wait for virtual machine up

+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Running | 1h17m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |       | 
+----+-----------------------+-----+--------+---------------+----------------+---------+-------+
```

[[Back]](./README.md)