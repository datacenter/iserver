# Container Virtualization Operator - Create Instance

## Workflow

- create hyperconverged instance based on package reference or user-provided CRD
- wait for resources ready

## Requirements

- cnv operator must be [created](./create_operator.md)

## Expected Outcome

![InstanceCreate](../images/cnv/instance_create.png)

## Configurable options

```
# iserver set ocp cnv --mode instance
  --cluster TEXT                  Cluster Name
  --filename TEXT                 HyperConverged CRD
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp cnv --mode instance --cluster bm1 --no-confirm


OpenShift Workflow - Container Virtualization Operator - Create HyperConverged Instance
=======================================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "instance": null,
    "confirmation": false,
    "channel": "stable",
    "check-verbose": true,
    "namespace": "openshift-cnv",
    "name": "kubevirt-hyperconverged",
    "operator-group-name": "cnv-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Operator
--------
- subscription: openshift-cnv/kubevirt-hyperconverged
- channel: stable
- csv: kubevirt-hyperconverged-operator.v4.18.17

Cnv operator ready

Create HyperConverged Instance
------------------------------

~~~
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  annotations:
    deployOVS: 'false'
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec: {}

~~~

HyperConverged instance created

Wait for hyperconverged instance and resources...
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-cnv/cdi-apiserver
- openshift-cnv/cdi-deployment
- openshift-cnv/cdi-uploadproxy
- openshift-cnv/kubemacpool-cert-manager
- openshift-cnv/kubemacpool-mac-controller-manager
- openshift-cnv/kubevirt-apiserver-proxy
- openshift-cnv/kubevirt-console-plugin
- openshift-cnv/kubevirt-ipam-controller-manager
- openshift-cnv/virt-api
- openshift-cnv/virt-controller
- openshift-cnv/virt-exportproxy
- openshift-cnv/virt-template-validator
Wait for deamon sets ready...
- openshift-cnv/bridge-marker
- openshift-cnv/kube-cni-linux-bridge-plugin
- openshift-cnv/passt-binding-cni
- openshift-cnv/virt-handler

Completed tasks
- HyperConverged instance created and ready
```

[[Back]](./README.md)