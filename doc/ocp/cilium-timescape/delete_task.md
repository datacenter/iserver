# Cilium Timescape - Delete via Task

## Input

```
[
  {
    "cilium-timescape": {
      "feature": {}
    }
  }
]
```

Notes:
- [feature](./enable.md) trigger workflow execution with optional input parameters

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

- timescape disabled
- timescape resources deleted
- timescape ui route deleted

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


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
- pod: cilium-9rht4
- pod: cilium-envoy-bwzml
- pod: cilium-envoy-gm8k5
- pod: cilium-envoy-v9jgx
- pod: cilium-k5jt8
- pod: cilium-kmd7d
- pod: cilium-operator-85c8cf7cf6-2gx6x
- pod: cilium-operator-85c8cf7cf6-fm8k9
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