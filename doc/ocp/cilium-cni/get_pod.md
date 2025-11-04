# Cilium CNI - Get pod

## Workflow

- check pods state in cilium namespace

## Requirements

None

## Configurable options

```
# iserver get ocp cilium pod
  --cluster TEXT   Cluster Name
```

## Example: 

```
# iserver get ocp cilium pod --cluster bm1

OpenShift Workflow - Get Cilium CNI Pod
=======================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok

Cilium PODs
-----------

+-------------------------------------------+-------+---------+--------------------+-----+------+-------------+-----+-----+-----------------+
| Pod                                       | Ready | Status  | Condition          | Age | Node | IP          | Net | Svc | Restarts        |
+-------------------------------------------+-------+---------+--------------------+-----+------+-------------+-----+-----+-----------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1d  | bm1  | 10.10.10.10 | 0   | 1   | 0               |
| cilium-envoy-vw2rh                        |       |         | PodScheduled: ✓    |     |      |             |     |     |                 |
|                                           |       |         | ContainersReady: ✓ |     |      |             |     |     |                 |
|                                           |       |         | Ready: ✓           |     |      |             |     |     |                 |
+-------------------------------------------+-------+---------+--------------------+-----+------+-------------+-----+-----+-----------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1d  | bm1  | 10.10.10.10 | 0   | 1   | 11 (22h54m ago) |
| cilium-operator-996c7bdb4-vl57m           |       |         | PodScheduled: ✓    |     |      |             |     |     |                 |
|                                           |       |         | ContainersReady: ✓ |     |      |             |     |     |                 |
|                                           |       |         | Ready: ✓           |     |      |             |     |     |                 |
+-------------------------------------------+-------+---------+--------------------+-----+------+-------------+-----+-----+-----------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1d  | bm1  | 10.10.10.10 | 0   | 2   | 0               |
| cilium-wb7ws                              |       |         | PodScheduled: ✓    |     |      |             |     |     |                 |
|                                           |       |         | ContainersReady: ✓ |     |      |             |     |     |                 |
|                                           |       |         | Ready: ✓           |     |      |             |     |     |                 |
+-------------------------------------------+-------+---------+--------------------+-----+------+-------------+-----+-----+-----------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 1d  | bm1  | 10.10.10.10 | 0   | 1   | 21 (22h53m ago) |
| clife-controller-manager-5674f55db6-9hsss |       |         | PodScheduled: ✓    |     |      |             |     |     |                 | 
|                                           |       |         | ContainersReady: ✓ |     |      |             |     |     |                 |
|                                           |       |         | Ready: ✓           |     |      |             |     |     |                 |
+-------------------------------------------+-------+---------+--------------------+-----+------+-------------+-----+-----+-----------------+
```



[[Back]](./README.md)