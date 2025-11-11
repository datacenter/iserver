# Cilium Timescape - Disable feature

## Workflow

- check cilium cni operator state
- check current cilium configuration
- delete spec:hubble configuration section
- restart cilium operators and agents
- wait for timescape resources to be deleted
- delete timescape ui route

## Requirements

None

## Expected outcome

- timescape disabled
- timescape resources deleted
- timescape ui route deleted

## Configurable options

```
# iserver delete ocp cilium timescape --mode feature
  --cluster TEXT     Cluster Name
  --no-confirm       Confirmation mode
```

## Example

```
# iserver delete ocp cilium timescape --cluster bm1 

OpenShift Workflow - Cilium - Disable Timescape
===============================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
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


Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Automatic pods rollout detected

Wait for Cilium resources
-------------------------
- pod: cilium-86gsb
- pod: cilium-envoy-bwzml
- pod: cilium-envoy-gm8k5
- pod: cilium-envoy-v9jgx
- pod: cilium-operator-85c8cf7cf6-2gx6x
- pod: cilium-operator-85c8cf7cf6-fm8k9
- pod: cilium-pscgc
- pod: cilium-r59c2
- pod: clife-controller-manager-6c79869f6c-gcj6l
- pod: clustermesh-apiserver-5fbcd5b558-gws27
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver
Wait for no timescape pods...
Wait for no timescape endpoints...

Delete cilium timescape route
-----------------------------
- route namespace: cilium
- route name: hubble-timescape

Route deleted

Completed tasks
- Timescape feature disabled
- Route deleted
```

[[Back]](./README.md)