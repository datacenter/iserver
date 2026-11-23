# Private Network - east-west connectivity test

[[Back]](./README.md) [[Next]](./blue.md) [[Prev]](./setup.md)

![Overview](../../images/pnet/ew.png)

## Namespace 

>[!CAUTION]
>Kubevirt autoconfiguration of interface mac address **must be disabled**

```shell
iserver create k8s ns --name a --kubemacpool
iserver create k8s ns --name a --label mutatevirtualmachines.kubemacpool.io=ignore
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    mutatevirtualmachines.kubemacpool.io: ignore
  name: a
```

## Example

```
# iserver create k8s ns --name a --kubemacpool --no-confirm

Kubernetes Workflow - Namespace - Create
========================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: a

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    mutatevirtualmachines.kubemacpool.io: ignore
  name: a
~~~
Namespace [a] created
Wait for namespace [timeout:60]...

Check labels
- mutatevirtualmachines.kubemacpool.io:ignore found

Completed tasks
- namespace created

+----+---------+-------+-----------+---------+---------+--------------+
| ID | Target  | Scope | Workflow  | Changes | Success | Duration [s] |
+----+---------+-------+-----------+---------+---------+--------------+
| 1  | ocp:bm1 | k8s   | create ns | 1       | ✓       | 6            | 
+----+---------+-------+-----------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./blue.md) [[Prev]](./setup.md)