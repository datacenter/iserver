# Private Network - Wipe crds

## Workflow

- check cilium cni operator state
- check current cilium configuration
- delete all private network crds if any

## Requirements

No application (pod/vm) connected to private network

## Expected outcome

No Private network CRDs 
- ClusterwidePrivateNetwork
- PrivateNetworkEndpointSlice
- PrivateNetworkExternalEndpoint

## Configurable options

```
# iserver delete ocp cilium pnet --mode wipe
  --cluster TEXT     Cluster Name
  --wipe             Wipe crds
  --no-confirm       Confirmation mode
```

## Example

```
# iserver delete ocp cilium pnet --cluster bm1 --mode wipe


OpenShift Workflow - Cilium - Wipe Private Network CRDs
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "operator-name": "cilium-operator",
    "agent-name": "cilium"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-v6tpt
- install plan approved : ✓
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✓

No ClusterwidePrivateNetwork crds found
No PrivateNetworkEndpointSlice crds found
No PrivateNetworkExternalEndpoint crds found

Completed tasks
- Private Network crds deleted
```

[[Back]](./README.md)