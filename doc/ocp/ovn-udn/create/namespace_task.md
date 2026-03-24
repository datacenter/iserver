# Namespace - Task

[[Back]](../README.md) [[Prev]](./namespace_crd.md) [[Next]](../get/namespace.md)

## Workflow

- namespace name restrictions: 'openshift-*'
- create namespace with label `k8s.ovn.org/primary-user-defined-network=''`
- in case of multicast requirement, add `k8s.ovn.org/multicast-enabled: "true"` annotation
- raise error if namespace already exists and is not udn-labeled

## Example 

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

[[Back]](../README.md) [[Prev]](./namespace_crd.md) [[Next]](../get/namespace.md)