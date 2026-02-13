# Cilium Agent - Get pods

## Workflow

- get pods in `cilium` namespace
- select pods with label app.kubernetes.io/name = cilium-agent

## Requirements

None

## Configurable options

```
# iserver get ocp cilium agent
  --cluster TEXT   Cluster Name
  -v, --view TEXT  [pod|logs]  [default: pod]
```

## Example

```
# iserver get ocp cilium agent --cluster bm1 -v pod

OpenShift Workflow - Cilium - Get agent
=======================================

OpenShift Cluster: bm3

+----+--------------+-------+---------+--------------------+-------+-------------+-------+
| ID | Pod          | Ready | Label   | Annotation         | Node  | IP          | Age   |
+----+--------------+-------+---------+--------------------+-------+-------------+-------+
| 1  | cilium       | 1/1   | Running | Initialized: ✓     | bm3-3 | 10.58.24.99 | 10h8m |
|    | cilium-4ccpl |       |         | PodScheduled: ✓    |       |             |       |
|    |              |       |         | ContainersReady: ✓ |       |             |       |
|    |              |       |         | Ready: ✓           |       |             |       | 
+----+--------------+-------+---------+--------------------+-------+-------------+-------+
| 2  | cilium       | 1/1   | Running | Initialized: ✓     | bm3-2 | 10.58.24.98 | 10h7m |
|    | cilium-fk4t6 |       |         | PodScheduled: ✓    |       |             |       |
|    |              |       |         | ContainersReady: ✓ |       |             |       |
|    |              |       |         | Ready: ✓           |       |             |       |
+----+--------------+-------+---------+--------------------+-------+-------------+-------+
| 3  | cilium       | 1/1   | Running | Initialized: ✓     | bm3-1 | 10.58.24.97 | 10h8m |
|    | cilium-n444l |       |         | PodScheduled: ✓    |       |             |       |
|    |              |       |         | ContainersReady: ✓ |       |             |       |
|    |              |       |         | Ready: ✓           |       |             |       |
+----+--------------+-------+---------+--------------------+-------+-------------+-------+
```

[[Back]](./README.md)