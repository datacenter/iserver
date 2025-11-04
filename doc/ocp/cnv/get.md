# Container Virtualization Operator - Get

## Workflow

- get cnv operator state
- get hyperconverged instance state
- collect cnv related crds

## Example

```
# iserver get ocp cnv --cluster bm1

OpenShift Workflow - Container Virtualization Operator - Get Information
========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "view": [
        "state"
    ],
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
- ready

HyperConverged
--------------
- instance: kubevirt-hyperconverged
- ready


Containerized Data Importer (CDI)
---------------------------------
- Name  : cdi-kubevirt-hyperconverged
- Phase : Deployed
- Ready : ✓



Network Addons Config
---------------------
- Name  : cluster
- Ready : ✓
```

[[Back]](./README.md)