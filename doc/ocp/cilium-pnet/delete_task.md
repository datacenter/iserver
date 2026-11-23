# Cilium Cluster Private Network - Delete via Task

[[Back]](./README.md)

## Input

```
[
  {
    "cilium-pnet": {
      "feature": {},
      "webhook": {},
      "wipe": {},
      "test": {}
    }
  }
]
```

Notes:
- [wipe](./wipe.md), [webhook](./disable_webhook.md) and [feature](./disable.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored such as test
- if feature option is defined, webhook workflow does not run
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

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

- all private network resources wiped
- private network feature disabled

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Cilium - Wipe Private Network CRDs
==========================================================

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

No ClusterwidePrivateNetwork crds found
No PrivateNetworkEndpointSlice crds found
No PrivateNetworkExternalEndpoint crds found

Completed tasks
- Private Network crds deleted

OpenShift Workflow - Cilium - Disable Private Network
=====================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "wipe": false,
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
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-fdx2v
- pod: cilium-kdb8l
- pod: cilium-lxxp7
- pod: cilium-operator-6fcc595dd6-jsftn
- pod: cilium-operator-6fcc595dd6-tntn4
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- deployment: cilium-operator
- deployment: clife-controller-manager

Completed tasks
- Private Network feature disabled
```

[[Back]](./README.md)