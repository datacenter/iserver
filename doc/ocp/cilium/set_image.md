# Cilium CNI - Set cilium image

## Workflow

- check cilium subscription and install plan
- check cilium cluster service version
- patch image to the location provided in --url option
- restart operator and agent pods
- wait until all are up
- print cilium agents version

## Requirements

None

## Configurable options

```
# iserver set ocp cilium image
  --cluster TEXT  Cluster Name
  --url TEXT      Image url
```

## Example

```
# iserver set ocp cilium image --cluster bm1 --url image-location

OpenShift Workflow - Cilium - Image upgrade
===========================================

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
- image       : current-image

CSV patched


Cluster Service Version
-----------------------
- namespace   : cilium
- name        : clife.v1.17.9-cee.1
- provider    : Isovalent, part of Cisco
- description : Isovalent Networking for Kubernetes
- maturity    : stable
- version     : 1.17.9-cee.1
- image       : new-image


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

+-------------------------------------------+-------+---------+--------------------+-------+------+-------------+-----+-----+----------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node | IP          | Net | Svc | Restarts |
+-------------------------------------------+-------+---------+--------------------+-------+------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1h31m | bm1  | 10.10.10.10 | 0   | 1   | 0        |
| cilium-envoy-4wxls                        |       |         | PodScheduled: ✓    |       |      |             |     |     |          |
|                                           |       |         | ContainersReady: ✓ |       |      |             |     |     |          |
|                                           |       |         | Ready: ✓           |       |      |             |     |     |          |
+-------------------------------------------+-------+---------+--------------------+-------+------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m  | bm1  | 10.10.10.10 | 0   | 1   | 0        |
| cilium-operator-6694cd7dd4-m4xg8          |       |         | PodScheduled: ✓    |       |      |             |     |     |          |
|                                           |       |         | ContainersReady: ✓ |       |      |             |     |     |          |
|                                           |       |         | Ready: ✓           |       |      |             |     |     |          |
+-------------------------------------------+-------+---------+--------------------+-------+------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1h0m  | bm1  | 10.10.10.10 | 0   | 2   | 0        |
| cilium-tkxbr                              |       |         | PodScheduled: ✓    |       |      |             |     |     |          |
|                                           |       |         | ContainersReady: ✓ |       |      |             |     |     |          |
|                                           |       |         | Ready: ✓           |       |      |             |     |     |          |
+-------------------------------------------+-------+---------+--------------------+-------+------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1h33m | bm1  | 10.10.10.10 | 0   | 1   | 0        |
| clife-controller-manager-6d479996fd-t96hm |       |         | PodScheduled: ✓    |       |      |             |     |     |          |
|                                           |       |         | ContainersReady: ✓ |       |      |             |     |     |          |
|                                           |       |         | Ready: ✓           |       |      |             |     |     |          |
+-------------------------------------------+-------+---------+--------------------+-------+------+-------------+-----+-----+----------+

Cilium Agent Versions
---------------------
- cilium-tkxbr: 1.18.1-cee.beta.3
```

[[Back]](./README.md)