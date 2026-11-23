# Virtual Machine - Memory Configuration

## Overview

![Change](../images/cnv/cpu_memory_change.png)

Triggers the following PATCH

~~~
[
  {
    "op":"replace",
    "path":"/spec/template/spec/domain/memory/guest",
    "value":"4Gi"
  }
]
~~~

Changes may require virtual machine restart 

![Pending](../images/cnv/cpu_memory_pending_changes.png)

Memory change may be rejected if it is lower than minimum e.g.

![MemoryTooLow](../images/cnv/memory_too_low.png)

## Workflow

- select virtual machines by namespace, name or all
- for every virtual machine change memory
- check restart required condition 
- restart virtual machine

Note:
- when virtual machine changes to 'Running', the actual OS may still be booting

## Configurable options

```
# iserver set k8s vm memory 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Virtual machine namespace
  --name TEXT       Virtual machine name
  --size INTEGER    Memory size in Gi 
  --restart         Restart if required
  --no-confirm      Confirmation mode
```

Notes:
- size is in range <1, 32>

## Example

```
# iserver set k8s vm memory --cluster bm1 --namespace default --name fedora-lime-python-82 --size 4 --restart --no-confirm


OpenShift Workflow - Virtual Machine - Memory Configuration
===========================================================

OpenShift Cluster: bm3

+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Restart Reqd | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+-------+
| 1  | default               | 1   | 2Gi    | rootdisk      | default (masq) | Running | X            | 9h11m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |              |       |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+-------+

Virtual Machine Memory Change
-----------------------------
- namespace: default
- name: fedora-lime-python-82
- current memory: 2Gi
- requested memory: 4Gi
- vm currenty running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: fedora-lime-python-82
  namespace: default
spec:
  template:
    spec:
      domain:
        memory:
          guest: 4Gi

~~~

Virtual machine patched
Wait for virtual machine restart required condition check...
Restart required
Restart virtual machine...
Wait for virtual machine up

+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+-------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Restart Reqd | Age   |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+-------+
| 1  | default               | 1   | 4Gi    | rootdisk      | default (masq) | Running | X            | 9h11m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |              |       |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+-------+
```

[[Back]](./README.md)