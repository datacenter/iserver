# Cilium - Set cilium image via Task

## Input

```
[
  {
    "cilium-image": {
      "set": {
        "url": "...."
      }
    }
  }
]
```

Notes:
- [cilium-image](./set_image.md) trigger workflow execution with image url location

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

Image changed

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Cilium - Image upgrade
===========================================

Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-v6tpt
- install plan approved : ✓
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✓



Cluster Service Version
-----------------------
- namespace   : cilium
- name        : clife.v1.17.9-cee.1
- provider    : Isovalent, part of Cisco
- description : Isovalent Networking for Kubernetes
- maturity    : stable
- version     : 1.17.9-cee.1
- image       : *******

CSV patched


Cluster Service Version
-----------------------
- namespace   : cilium
- name        : clife.v1.17.9-cee.1
- provider    : Isovalent, part of Cisco
- description : Isovalent Networking for Kubernetes
- maturity    : stable
- version     : 1.17.9-cee.1
- image       : *******


OpenShift Workflow - Cilium - Rollout restart
=============================================

Restart deployment cilium/cilium-operator
Deployment [cilium/cilium-operator] patch successful
Restart daemon set cilium/cilium
Daemon set [cilium/cilium] patch successful
Take a nap...
Wait for deployments ready (optional: False, allow zero replicas: False)...
- cilium/cilium-operator
Wait for deamon sets ready...
- cilium/cilium

Cilium PODs
-----------

+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| ID | Pod                                       | Ready | Status  | Condition          | Age  | Node  | IP          | Net | Svc | Restarts |
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 1  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m | bm3-2 | 10.10.10.11 | 0   | 2   | 0        | 
|    | cilium-745xq                              |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 2  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m | bm3-1 | 10.10.10.10 | 0   | 2   | 0        | 
|    | cilium-cdww2                              |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 3  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h5m | bm3-2 | 10.10.10.11 | 0   | 1   | 0        | 
|    | cilium-envoy-bwzml                        |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 4  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h6m | bm3-3 | 10.10.10.12 | 0   | 1   | 0        | 
|    | cilium-envoy-gm8k5                        |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 5  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h6m | bm3-1 | 10.10.10.10 | 0   | 1   | 0        | 
|    | cilium-envoy-v9jgx                        |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 6  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m | bm3-3 | 10.10.10.12 | 0   | 2   | 0        | 
|    | cilium-fz86j                              |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 7  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m | bm3-3 | 10.10.10.12 | 0   | 1   | 0        | 
|    | cilium-operator-68ffdcb688-nsskl          |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 8  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m | bm3-1 | 10.10.10.10 | 0   | 1   | 0        | 
|    | cilium-operator-68ffdcb688-xmqr7          |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| 9  | cilium                                    | 1/1   | Running | Initialized: ✓     | 1h6m | bm3-1 | 10.10.10.10 | 0   | 1   | 0        | 
|    | clife-controller-manager-6c79869f6c-gcj6l |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|    |                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|    |                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+----+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
Take a nap...

Cilium Agent Versions
---------------------
- cilium-745xq: 1.18.3-cee.pre.1
- cilium-cdww2: 1.18.3-cee.pre.1
- cilium-fz86j: 1.18.3-cee.pre.1
```

[[Back]](./README.md)