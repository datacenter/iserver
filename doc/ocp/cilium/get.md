# OpenShift Operations

## Cilium CNI

### Task: get state

Workflow
- check openshift network settings
- check pods state in cilium namespace
- run 'cilium status' command 
- check ciliumconfig object
- check cilium-config config map

```
# iserver get ocp cilium --cluster my-cluster

OpenShift Network
-----------------
- Name            : cluster
- Network Type    : Cilium
- Cluster Network : 10.128.0.0/14
- Host Prefix     : 23
- Service Network : 172.30.0.0/16

Cilium PODs
-----------

+-------------------------------------------+-------+---------+--------------------+-----+---------+-------------+-----+-----+-------------+
| Pod                                       | Ready | Status  | Condition          | Age | Node    | IP          | Net | Svc | Restarts    |
+-------------------------------------------+-------+---------+--------------------+-----+---------+-------------+-----+-----+-------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 9d  | my-node | 10.10.10.10 | 0   | 2   | 0           |
| cilium-4f6rq                              |       |         | PodScheduled: ✓    |     |         |             |     |     |             |
|                                           |       |         | ContainersReady: ✓ |     |         |             |     |     |             |
|                                           |       |         | Ready: ✓           |     |         |             |     |     |             |
+-------------------------------------------+-------+---------+--------------------+-----+---------+-------------+-----+-----+-------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 9d  | my-node | 10.10.10.10 | 0   | 1   | 0           |
| cilium-envoy-2sl56                        |       |         | PodScheduled: ✓    |     |         |             |     |     |             |
|                                           |       |         | ContainersReady: ✓ |     |         |             |     |     |             | 
|                                           |       |         | Ready: ✓           |     |         |             |     |     |             |
+-------------------------------------------+-------+---------+--------------------+-----+---------+-------------+-----+-----+-------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 9d  | my-node | 10.10.10.10 | 0   | 1   | 30 (8d ago) |
| cilium-operator-996c7bdb4-bzbhx           |       |         | PodScheduled: ✓    |     |         |             |     |     |             |
|                                           |       |         | ContainersReady: ✓ |     |         |             |     |     |             |
|                                           |       |         | Ready: ✓           |     |         |             |     |     |             |
+-------------------------------------------+-------+---------+--------------------+-----+---------+-------------+-----+-----+-------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 9d  | my-node | 10.10.10.10 | 0   | 4   | 44 (8d ago) |
| clife-controller-manager-5674f55db6-brfwm |       |         | PodScheduled: ✓    |     |         |             |     |     |             |
|                                           |       |         | ContainersReady: ✓ |     |         |             |     |     |             |
|                                           |       |         | Ready: ✓           |     |         |             |     |     |             | 
+-------------------------------------------+-------+---------+--------------------+-----+---------+-------------+-----+-----+-------------+

    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet              cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment             cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 1
                       cilium-envoy             Running: 1
                       cilium-operator          Running: 1
                       clustermesh-apiserver
                       hubble-relay
Cluster Pods:          106/106 managed by Cilium

Cilium Config
-------------
Processing error: False
Values error: False

cluster:
  name: default
clusterHealthPort: 9940
...

Cilium Config Map
-----------------
agent-not-ready-taint-key: node.cilium.io/agent-not-ready
arping-refresh-period: 30s
auto-direct-node-routes: false
...
```

[[Back]](./README.md)