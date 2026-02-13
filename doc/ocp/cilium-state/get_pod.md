# Cilium - Get pod

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


OpenShift Workflow - Cilium - Get pods
======================================

OpenShift Cluster: bm1

Cilium PODs
-----------

+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| ID | Pod                                      | Ready | Label   | Annotation         | Node  | IP           | Svc | Age    |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 1  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-1 | 10.10.10.10  | 1   | 58d    | 
|    | cilium-envoy-lj6v9                       |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 2  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-2 | 10.10.10.11  | 1   | 58d    |
|    | cilium-envoy-rng8f                       |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 3  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-3 | 10.10.10.12  | 1   | 58d    |
|    | cilium-envoy-vmjrl                       |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 4  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-1 | 10.10.10.10  | 2   | 1h14m  |
|    | cilium-jgbrt                             |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 5  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-3 | 10.10.10.12  | 2   | 1h14m  |
|    | cilium-nkpqx                             |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 6  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-3 | 10.10.10.12  | 1   | 16h26m |
|    | cilium-operator-587d69cfcd-47lqb         |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 7  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-2 | 10.10.10.11  | 1   | 16h26m |
|    | cilium-operator-587d69cfcd-wq9b2         |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 8  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-2 | 10.10.10.11  | 2   | 1h13m  | 
|    | cilium-xc9fs                             |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 9  | cilium                                   | 1/1   | Running | Initialized: V     | bm1-1 | 10.10.10.10  | 1   | 8d     |
|    | clife-controller-manager-9cb9d46d5-5c964 |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 10 | cilium                                   | 2/2   | Running | Initialized: V     | bm1-1 | 10.128.2.47  | 2   | 8d     |
|    | clustermesh-apiserver-6dfbc87f48-k2m9j   |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
| 11 | cilium                                   | 2/2   | Running | Initialized: V     | bm1-3 | 10.128.4.146 | 2   | 8d     |
|    | hubble-timescape-0                       |       |         | PodScheduled: V    |       |              |     |        |
|    |                                          |       |         | ContainersReady: V |       |              |     |        |
|    |                                          |       |         | Ready: V           |       |              |     |        |
+----+------------------------------------------+-------+---------+--------------------+-------+--------------+-----+--------+
```



[[Back]](./README.md)