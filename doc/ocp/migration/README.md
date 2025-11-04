# OpenShift CNI Migration: OVNKubernetes to Cilium EE

## Overview

OpenShift cluster deployed with OVNKubernetes CNI can be migrated to Cilium EE CNI using the automated workflow as explained below.

## Requirements

- cluster with ssh access and management ip node defined. Refer to [cluster access](../Access.md) for details

```
# iserver.py get ocp connector --cluster bm1

+---------+--------+------------+----------------+---------------+
| Cluster | Domain | Kubeconfig | SSH Public Key | Management IP |
+---------+--------+------------+----------------+---------------+
| bm1     | local  | ✓          | ✓              | 10.10.10.10   |
+---------+--------+------------+----------------+---------------+ 
```

- OVNKubernetes CNI

```
# iserver get k8s cni --cluster bm1

+------------------+---------------+---------------------+---------------+
| CNI Network Type | Cluster CIDR  | Cluster Host Prefix | Service CIDR  |
+------------------+---------------+---------------------+---------------+
| OVNKubernetes    | 10.128.0.0/14 | 23                  | 172.30.0.0/16 |
+------------------+---------------+---------------------+---------------+
```

- all cluster operators available

```
# iserver get k8s co --cluster bm1

+----+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+-----+
| ID | Cluster Operator                         | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since  | Age |
+----+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+-----+
| 1  | authentication                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 23h20m | 4d  |
|    |                                          |         | version        |           |             |          |             |        |     |
+----+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+-----+
| 34 | storage                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 4d     | 4d  |
|    |                                          |         | version        |           |             |          |             |        |     |
+----+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+-----+

All cluster operators available: yes
```

## Configurable options

```
# iserver set ocp cni --mode cilium
  --cluster TEXT         Cluster Name
  --cidr TEXT            Target cidr
  --host-prefix INTEGER  Target host prefix  [default: 24]
  --manifest TEXT        Manifest directory
  --start INTEGER        Starting step  [default: 1]
  --stop INTEGER         Ending step  [default: 10]
  --no-confirm           Confirmation mode
```

Notes:
- target network cidr must not overlap with the existing OVNKubernetes network (hint: use 'oc get network cluster -o yaml' to check current network)
- use --no-confirm otherwise you will have to accept every change in the cluster throughout the workflow
- Cilium EE Clife manifests supported only
- unpack Cilium EE Clife manifests into --manifest directory, do not modify them
- workflow is not designed to re-run, it should run to completion
- in case workflow breaks and you need to resume it, use --start option to start the workflow from desired step
- you can execute range of steps using --start and --stop options

## Expected Outcome

```
$ cilium status -n cilium
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
Cluster Pods:          102/104 managed by Cilium
```

## Workflow

```
# iserver set ocp cni \
  --mode cilium \
  --cluster my-cluster \
  --cidr 10.253.0.0/16 \
  --host-prefix 24 \
  --manifest absolute-dir-with-cilium-ee-manifests \
  --no-confirm
```

Full output: [SNO](./output-sno.md), [3 node](./output-3node.md)

Step | Intent | Link
-- | -- | --
1 | Check cluster state and input parameters | [Link](./step1.md)
2 | Disable cluster network operator | [Link](./step2.md)
3 | Change default CNI | [Link](./step3.md)
4 | Deploy Cilium | [Link](./step4.md)
5 | Re-enable OpenShift operator management | [Link](./step5.md)
6 | Restart cluster | [Link](./step6.md)
7 | Wait cluster ready | [Link](./step7.md)
8 | Post migration | [Link](./step8.md)
9 | Cluster restart | [Link](./step9.md)

Note: check for possibility of manual node reboot in [step6](./step6.md)

[[Back]](../Operations.md)