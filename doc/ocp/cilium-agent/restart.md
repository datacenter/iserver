# Cilium Agent - Restart

## Workflow

- get pods in `cilium` namespace
- select pods with label app.kubernetes.io/name = cilium-agent
- show the pods
- rollout restart of daemon set `cilium` in `cilium` namespace
- wait until daemon set restarted successfully
- show the agent pods

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
# iserver set ocp cilium restart --cluster bm1 --mode agent

OpenShift Workflow - Cilium - Rollout restart
=============================================

OpenShift Cluster: bm1

+----+--------------+-------+---------+--------------------+-------+-------------+--------+
| ID | Pod          | Ready | Label   | Annotation         | Node  | IP          | Age    |
+----+--------------+-------+---------+--------------------+-------+-------------+--------+
| 1  | cilium       | 1/1   | Running | Initialized: ✓     | bm1-3 | 10.10.10.12 | 10h17m |
|    | cilium-4ccpl |       |         | PodScheduled: ✓    |       |             |        |
|    |              |       |         | ContainersReady: ✓ |       |             |        |
|    |              |       |         | Ready: ✓           |       |             |        |
+----+--------------+-------+---------+--------------------+-------+-------------+--------+
| 2  | cilium       | 1/1   | Running | Initialized: ✓     | bm1-2 | 10.10.10.11 | 10h17m | 
|    | cilium-fk4t6 |       |         | PodScheduled: ✓    |       |             |        |
|    |              |       |         | ContainersReady: ✓ |       |             |        |
|    |              |       |         | Ready: ✓           |       |             |        |
+----+--------------+-------+---------+--------------------+-------+-------------+--------+
| 3  | cilium       | 1/1   | Running | Initialized: ✓     | bm1-1 | 10.10.10.10 | 10h17m |
|    | cilium-n444l |       |         | PodScheduled: ✓    |       |             |        |
|    |              |       |         | ContainersReady: ✓ |       |             |        |
|    |              |       |         | Ready: ✓           |       |             |        |
+----+--------------+-------+---------+--------------------+-------+-------------+--------+
Restart daemon set cilium/cilium
Daemon set [cilium/cilium] patch successful
Take a nap...
Wait for deamon sets ready...
- cilium/cilium

+----+--------------+-------+---------+--------------------+-------+-------------+------+
| ID | Pod          | Ready | Label   | Annotation         | Node  | IP          | Age  |
+----+--------------+-------+---------+--------------------+-------+-------------+------+
| 1  | cilium       | 1/1   | Running | Initialized: ✓     | bm1-2 | 10.10.10.11 | 1h0m |
|    | cilium-hrwfw |       |         | PodScheduled: ✓    |       |             |      |
|    |              |       |         | ContainersReady: ✓ |       |             |      |
|    |              |       |         | Ready: ✓           |       |             |      |
+----+--------------+-------+---------+--------------------+-------+-------------+------+
| 2  | cilium       | 1/1   | Running | Initialized: ✓     | bm1-3 | 10.10.10.12 | 1h0m |
|    | cilium-wd27b |       |         | PodScheduled: ✓    |       |             |      |
|    |              |       |         | ContainersReady: ✓ |       |             |      |
|    |              |       |         | Ready: ✓           |       |             |      |
+----+--------------+-------+---------+--------------------+-------+-------------+------+
| 3  | cilium       | 1/1   | Running | Initialized: ✓     | bm1-1 | 10.10.10.10 | 1h0m |
|    | cilium-xbqkc |       |         | PodScheduled: ✓    |       |             |      |
|    |              |       |         | ContainersReady: ✓ |       |             |      |
|    |              |       |         | Ready: ✓           |       |             |      |
+----+--------------+-------+---------+--------------------+-------+-------------+------+
```

[[Back]](./README.md)