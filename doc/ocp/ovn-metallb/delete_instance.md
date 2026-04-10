# MetalLB - Delete instance

[[Back]](./README.md) [[Create]](./create_instance.md)

## Workflow

- delete any `MetalLB` instance in `metallb-system` namespace
- wait for controller and speaker resources gone

## Example

```
# iserver delete ocp metallb --cluster bm1 --mode instance

OpenShift Workflow - MetalLB Operator - Delete instance
=======================================================

OpenShift Cluster: bm1


Operator
--------
- subscription          : metallb-system/metallb-operator
- package               : openshift-marketplace/redhat-operators/metallb-operator
- channel               : stable
- install plan          : metallb-system/install-hfq5s
- install plan approved : ✓
- installed csv         : metallb-operator.v4.21.0-202603300221
- latest_csv            : ✓


Delete MetalLB
--------------
- namespace: metallb-system
- name: metallb
- deleted
- wait for no MetalLB metallb-system/metallb [timeout:60s]
- wait for Deployment metallb-system/controller [timeout:180s]
- wait for ReplicaSet metallb-system/controller-5d4886b677 [timeout:180s]
- wait for Pod metallb-system/controller-5d4886b677-gfcj7 [timeout:180s]
- wait for DaemonSet metallb-system/speaker [timeout:180s]
- wait for Pod metallb-system/speaker-nvdtq [timeout:180s]
- wait for Pod metallb-system/speaker-snjcl [timeout:180s]
- wait for Pod metallb-system/speaker-w7kq5 [timeout:180s]
Subscription metallb resources gone

Completed tasks
- MetalLB instance deleted
```

[[Back]](./README.md) [[Create]](./create_instance.md)