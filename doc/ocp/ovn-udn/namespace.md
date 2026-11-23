# User Defined Network (UDN) - Namespace

[[Back]](./README.md)

User Defined Network (UDN) is namespace-scope object. [Primary](./primary.md) udn requires `k8s.ovn.org/primary-user-defined-network` namespace label. [Secondary](./secondary.md) udn has no such requirement.

> [!NOTE]
> namespace udn-label patch not supported by OpenShift

## CRD

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
  name: island
```

## State

```
# iserver get k8s ns -v udn --cluster bm1
Cluster: bm1 (type: ocp)
|
+----+-----------+--------+-------+
| ID | Namespace | Status | Age   |
+----+-----------+--------+-------+
| 1  | island    | Active | 4h19m |
| 2  | island-a  | Active | 2d    |
| 3  | island-b  | Active | 5h1m  |
| 4  | island-c  | Active | 4h55m |
+----+-----------+--------+-------+

Filter: name
View:   state (def), udn
```

## Task

```
[
    {
        "k8s": {
            "items": [
                {
                    "__type__": "namespace",
                    "namespace": "island",
                    "ovn-udn": true,
                    "ovn-multicast": true
                }
            ]
        }
    }
]
```

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

Cluster: bm1 (type: ocp)

Kubernetes Workflow - Namespace - Create
========================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: island

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: "true"
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
  name: island

~~~
Namespace [island] created
Wait for namespace [timeout:60]...

Check labels
- k8s.ovn.org/primary-user-defined-network: found

Completed tasks
- namespace created
```

[[Back]](./README.md)