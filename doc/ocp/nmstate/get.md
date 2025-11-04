# MMState Operator - Get

## Workflow

- check nmstate operator subscription and cluster service version objects
- check nmstate instance object
- check NodeNetworkState CRD for every cluster node
- check NodeNetworkConfigurationPolicy objects
- check NodeNetworkConfigurationEnactment objects

## Requirements

None

## Configurable options

```
# iserver get ocp nmstate 
  --cluster TEXT         Cluster Name
```

## Example

```
python.exe .\iserver.py get ocp nmstate                

OpenShift Workflow - NMState Operator - Get Information
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-nmstate",
    "name": "kubernetes-nmstate-operator",
    "operator-group-name": "nmstate-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Operator
--------
- subscription: openshift-nmstate/kubernetes-nmstate-operator
- channel: stable
- csv: kubernetes-nmstate-operator.4.18.0-202509241752
- instance: nmstate

Operator functional readiness
-----------------------------
ready

Node Network State
------------------
- ocp-bm1: found

Node Network Configuration Policy [#1]
--------------------------------------

+--------+-----------+------------------------+
| Name   | Status    | Reason                 |
+--------+-----------+------------------------+
| policy | Available | SuccessfullyConfigured |
+--------+-----------+------------------------+

Node Network Configuration Enactment [#1]
-----------------------------------------

+----------------+-----------+
| Name           | Status    |
+----------------+-----------+
| my-node.policy | Available |
+----------------+-----------+
```

[[Back]](./README.md)