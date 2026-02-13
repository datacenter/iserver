# Virtual Machine - CPU Topology

## Overview

![Change](../images/cnv/cpu_topology.png)

Triggers the following PATCH

~~~
[
  {
    "op":"replace",
    "path":"/spec/template/spec/domain/cpu",
    "value":{
      "cores":2,
      "sockets":3,
      "threads":4
    }
  }
]
~~~

Changes may require virtual machine restart 

![Pending](../images/cnv/cpu_pending_changes.png)

## Workflow

- select virtual machines by namespace, name or all
- for every virtual machine change cpu topology
- check restart required condition 
- restart virtual machine

## Configurable options

```
# iserver set k8s vm cpu 
  --cluster TEXT     Cluster Name
  --namespace TEXT   Virtual machine namespace
  --name TEXT        Virtual machine name
  --sockets INTEGER  Socket count
  --cores INTEGER    Cores count
  --threads INTEGER  Threads count
  --restart          Restart if required
  --no-confirm       Confirmation mode
```

## Example (sockets only - no restart required)

```
# iserver set k8s vm start --cluster bm1 --namespace default --name fedora-lime-python-82 --sockets 2 --no-confirm

OpenShift Workflow - Virtual Machine - CPU Topology Configuration
=================================================================

OpenShift Cluster: bm3

+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Restart Reqd | Age    |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| 1  | default               | 1   | 4Gi    | rootdisk      | default (masq) | Running | X            | 10h53m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |              |        |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+

Virtual Machine CPU Change
--------------------------
- namespace: default
- name: fedora-lime-python-82
- current sockets/cores/threads: 1/1/1
- requested CPU topology: 2/1/1
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
        cpu:
          cores: 1
          sockets: 2
          threads: 1

~~~

Virtual machine patched
Wait for virtual machine restart required condition check...
Restart not required

+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Restart Reqd | Age    |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| 1  | default               | 2   | 4Gi    | rootdisk      | default (masq) | Running | X            | 10h53m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |              |        |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
```

## Example (full topology - restart required)

```
# iserver set k8s vm start --cluster bm1 --namespace default --name fedora-lime-python-82 --sockets 1 --cores 2 --threads 2 --restart --no-confirm


OpenShift Workflow - Virtual Machine - CPU Topology Configuration
=================================================================

OpenShift Cluster: bm3

+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Restart Reqd | Age    |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| 1  | default               | 2   | 4Gi    | rootdisk      | default (masq) | Running | X            | 10h55m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |              |        |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+

Virtual Machine CPU Change
--------------------------
- namespace: default
- name: fedora-lime-python-82
- current sockets/cores/threads: 2/1/1
- requested CPU topology: 1/2/2
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
        cpu:
          cores: 2
          sockets: 1
          threads: 2

~~~

Virtual machine patched
Wait for virtual machine restart required condition check...
Restart required
Restart virtual machine...
Wait for virtual machine up

+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| ID | Virtual Machine       | CPU | Memory | Disk          | Interface      | Status  | Restart Reqd | Age    |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
| 1  | default               | 4   | 4Gi    | rootdisk      | default (masq) | Running | X            | 10h55m |
|    | fedora-lime-python-82 |     |        | cloudinitdisk |                |         |              |        |
+----+-----------------------+-----+--------+---------------+----------------+---------+--------------+--------+
```

[[Back]](./README.md)