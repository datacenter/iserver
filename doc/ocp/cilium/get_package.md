# Cilium CNI - Get package

## Workflow

- get cilium operator package and subscription details

## Requirements

None

## Configurable options

```
# iserver get ocp cilium package
  --cluster TEXT   Cluster Name
```

## Example

```
# iserver get ocp cilium package --cluster bm1


OpenShift Workflow - Get Cilium CNI Package
===========================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : install-9xjnm [Manual]
- install plan approved : ✗
- installed csv         : ---
- latest_csv            : ✗
```

[[Back]](./README.md)