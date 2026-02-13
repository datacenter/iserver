# Cilium Operator - Restart

## Workflow

- get pods in `cilium` namespace
- select pods with label app.kubernetes.io/name = cilium-operator
- show the pods
- rollout restart of deployment `cilium-operator` in `cilium` namespace
- wait until deployment restarted successfully
- show the operator pods

## Requirements

None

## Configurable options

```
# iserver set ocp cilium restart 
  --cluster TEXT               Cluster Name
  --mode [operator|agent|all]  Mode of operation  [default: all]
  --no-wait                    Wait mode
```

## Example

```
# iserver set ocp cilium restart --cluster bm1 --mode operator

OpenShift Workflow - Cilium - Rollout restart
=============================================

OpenShift Cluster: bm1

+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
| ID | Pod                              | Leader | Ready | Label   | Annotation         | Node  | IP          | Age |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
| 1  | cilium                           | V      | 1/1   | Running | Initialized: V     | bm1-1 | 10.10.10.10 | 7d  |
|    | cilium-operator-5dcc9dbf6f-7pnmc |        |       |         | PodScheduled: V    |       |             |     |
|    |                                  |        |       |         | ContainersReady: V |       |             |     |
|    |                                  |        |       |         | Ready: V           |       |             |     |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
| 2  | cilium                           |        | 1/1   | Running | Initialized: V     | bm1-3 | 10.10.10.12 | 7d  |
|    | cilium-operator-5dcc9dbf6f-7pw2r |        |       |         | PodScheduled: V    |       |             |     |
|    |                                  |        |       |         | ContainersReady: V |       |             |     |
|    |                                  |        |       |         | Ready: V           |       |             |     |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+-----+
Restart deployment cilium/cilium-operator
Deployment [cilium/cilium-operator] patch successful
Take a nap...
Wait for deployments ready (optional: False, allow zero replicas: False)...
- cilium/cilium-operator

+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+------+
| ID | Pod                              | Leader | Ready | Label   | Annotation         | Node  | IP          | Age  |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+------+
| 1  | cilium                           |        | 1/1   | Running | Initialized: V     | bm1-3 | 10.10.10.12 | 1h0m |
|    | cilium-operator-587d69cfcd-47lqb |        |       |         | PodScheduled: V    |       |             |      |
|    |                                  |        |       |         | ContainersReady: V |       |             |      |
|    |                                  |        |       |         | Ready: V           |       |             |      |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+------+
| 2  | cilium                           | V      | 1/1   | Running | Initialized: V     | bm1-2 | 10.10.10.11 | 1h0m |
|    | cilium-operator-587d69cfcd-wq9b2 |        |       |         | PodScheduled: V    |       |             |      |
|    |                                  |        |       |         | ContainersReady: V |       |             |      |
|    |                                  |        |       |         | Ready: V           |       |             |      |
+----+----------------------------------+--------+-------+---------+--------------------+-------+-------------+------+
```

[[Back]](./README.md)