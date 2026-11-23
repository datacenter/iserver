# Container Virtualization Operator - Delete Instance

## Workflow

- delete hyperconverged instance
- wait for resources gone

## Requirements

- no data volume can have associated pvc

## Configurable options

```
# iserver delete ocp cnv --mode instance
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp cnv --cluster bm1 --mode instance

OpenShift Workflow - Container Virtualization Operator - Delete HyperConverged Instance
=======================================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-cnv/kubevirt-hyperconverged
- package               : openshift-marketplace/redhat-operators/kubevirt-hyperconverged
- channel               : stable
- install plan          : openshift-cnv/install-lnx26
- install plan approved : V
- installed csv         : kubevirt-hyperconverged-operator.v4.21.3
- latest_csv            : V

No ready data volumes found <=> virtualization subsystem is not using storage

Delete HyperConverged Instance
------------------------------
- namespace: openshift-cnv
- name: kubevirt-hyperconverged
- wait for no hyperconverged instance and resources
- wait for no Deployment openshift-cnv/cdi-apiserver [timeout:180s]
- wait for no Deployment openshift-cnv/cdi-deployment [timeout:180s]
- wait for no Deployment openshift-cnv/cdi-uploadproxy [timeout:180s]
- wait for no Deployment openshift-cnv/kubemacpool-cert-manager [timeout:180s]
- wait for no Deployment openshift-cnv/kubemacpool-mac-controller-manager [timeout:180s]
- wait for no Deployment openshift-cnv/kubevirt-apiserver-proxy [timeout:180s]
- wait for no Deployment openshift-cnv/kubevirt-console-plugin [timeout:180s]
- wait for no Deployment openshift-cnv/kubevirt-ipam-controller-manager [timeout:180s]
- wait for no Deployment openshift-cnv/virt-api [timeout:180s]
- wait for no Deployment openshift-cnv/virt-controller [timeout:180s]
- wait for no Deployment openshift-cnv/virt-exportproxy [timeout:180s]
- wait for no Deployment openshift-cnv/virt-template-validator [timeout:180s]
- wait for no DaemonSet openshift-cnv/bridge-marker [timeout:180s]
- wait for no DaemonSet openshift-cnv/kube-cni-linux-bridge-plugin [timeout:180s]
- wait for no DaemonSet openshift-cnv/passt-binding-cni [timeout:180s]
- wait for no DaemonSet openshift-cnv/virt-handler [timeout:180s]
Subscription cnv resources gone

Completed tasks
- Hyperconverged instance deleted

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cnv   | delete instance | 1       | V       | 71           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)