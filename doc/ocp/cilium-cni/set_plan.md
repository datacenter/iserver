# Cilium CNI - Approve install plan

## Workflow

- check cilium subscription and install plan
- approve plan if required

## Requirements

None

## Configurable options

```
# iserver set ocp cilium plan
  --cluster TEXT   Cluster Name
```

## Example

```
# iserver set ocp cilium plan --cluster bm1

OpenShift Workflow - Approve Cilium Install Plan
================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "package": "clife"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-8rhpx
- install plan approved : ✗
- installed csv         : clife.v1.17.8-cee.1
- latest_csv            : ✗

Install plan will be approved...

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: InstallPlan
metadata:
  name: install-8rhpx
  namespace: cilium
spec:
  approved: true

~~~


Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-8rhpx [Manual]
- install plan approved : ✓
- installed csv         : clife.v1.17.8-cee.1
- latest_csv            : ✗
```

[[Back]](./README.md)