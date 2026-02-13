# Cilium Operator - Get pods

## Workflow

- get pods in `cilium` namespace
- select pods with label app.kubernetes.io/name = cilium-operator
- add leader flag based on cilium-operator-resource-lock lease

## Requirements

None

## Configurable options

```
# iserver get ocp cilium operator
  --cluster TEXT   Cluster Name
  -v, --view TEXT  [pod|config|logs]  [default: pod]
```

## Example

```
# iserver get ocp cilium operator --cluster bm1 -v pod

OpenShift Workflow - Cilium - Get operator
==========================================

OpenShift Cluster: bm1

+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
| ID | Pod                              | Leader | Ready | Label   | Annotation         | Node  | IP          | Age |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
| 1  | cilium                           | V      | 1/1   | Running | Initialized: V     | bm1-1 | 10.10.10.10 | 7d  |
|    | cilium-operator-5dcc9dbf6f-7pnmc |        |       |         | PodScheduled: V    |       |             |     |
|    |                                  |        |       |         | ContainersReady: V |       |             |     |
|    |                                  |        |       |         | Ready: V           |       |             |     |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
| 2  | cilium                           |        | 1/1   | Running | Initialized: V     | bm1-3 | 10.10.10.11 | 7d  |
|    | cilium-operator-5dcc9dbf6f-7pw2r |        |       |         | PodScheduled: V    |       |             |     |
|    |                                  |        |       |         | ContainersReady: V |       |             |     |
|    |                                  |        |       |         | Ready: V           |       |             |     |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
```

[[Back]](./README.md)