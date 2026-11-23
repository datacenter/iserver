# Cilium EE migration workflow

[[Back]](./step8.md) [[Next]](./README.md)

## Step 9: Cluster restart

- restart nodes
- wait till all nodes ready
- wait till all machine config pools updated
- wait till all cluster operators available
- wait till cilium pods and deployments are ready 

### Output

```
Step 9: Cluster Restart
=======================


Reload nodes
- openshift.public.domain.com

Wait for no kubernetes api [1hr]...
Wait for kubernetes api [30min]...
Wait nodes ready [30min]...

+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+
| Node                        | Ready | Memory | Disk | PID | CNV | MCP | Role   | IP                   | Age |
+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+
| openshift.public.domain.com | ✓     | ✓      | ✓    | ✓   | ✓   | ✓   | Master | 166.11.170.180 (int) | 10d | 
|                             |       |        |      |     |     |     | Worker |                      |     | 
+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+

Wait machine config pool ready [1hr]...

+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| Machine Config Pool | Config                                           | Updated | Updating | Degraded | Machines | Ready | Updated | Degraded | Unavail | Machine Config                  | Age |
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| master              | rendered-master-457a635dc59d9952e43ba0aa5441936e | ✓       | ✗        | ✗        | 1        | 1     | 1       | 0        | 0       | 00-master                       | 10d | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-container-runtime     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-kubelet               |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-master-dnsmasq-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-masters-chrony-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-master-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-master-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-generated-registries  |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-ssh                   |     | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| worker              | rendered-worker-975ce5252c6b5da7f2935fbfb9f481af | ✓       | ✗        | ✗        | 0        | 0     | 0       | 0        | 0       | 00-worker                       | 10d | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-container-runtime     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-kubelet               |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-workers-chrony-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-worker-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-worker-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-generated-registries  |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-ssh                   |     | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+

Wait Cluster Operators
- wait for authentication available
- wait for baremetal available
- wait for cloud-controller-manager available
- wait for cloud-credential available
- wait for cluster-autoscaler available
- wait for config-operator available
- wait for console available
- wait for control-plane-machine-set available
- wait for csi-snapshot-controller available
- wait for dns available
- wait for etcd available
- wait for image-registry available
- wait for ingress available
- wait for insights available
- wait for kube-apiserver available
- wait for kube-controller-manager available
- wait for kube-scheduler available
- wait for kube-storage-version-migrator available
- wait for machine-api available
- wait for machine-approver available
- wait for machine-config available
- wait for marketplace available
- wait for monitoring available
- wait for network available
- wait for node-tuning available
- wait for olm available
- wait for openshift-apiserver available
- wait for openshift-controller-manager available
- wait for openshift-samples available
- wait for operator-lifecycle-manager available
- wait for operator-lifecycle-manager-catalog available
- wait for operator-lifecycle-manager-packageserver available
- wait for service-ca available
- wait for storage available

Check Cluster Operators
-----------------------

+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| Cluster Operator                         | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since | Age |
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| authentication                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 4h55m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| baremetal                                | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cloud-controller-manager                 | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cloud-credential                         | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cluster-autoscaler                       | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| config-operator                          | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| console                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 4h55m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| control-plane-machine-set                | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| csi-snapshot-controller                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| dns                                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h0m  | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| etcd                                     | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| image-registry                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| ingress                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 5h37m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| insights                                 | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-apiserver                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-controller-manager                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-scheduler                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-storage-version-migrator            | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-api                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-approver                         | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-config                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| marketplace                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| monitoring                               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| network                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| node-tuning                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| olm                                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-apiserver                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 7h24m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-controller-manager             | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-samples                        | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager-catalog       | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager-packageserver | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h13m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| service-ca                               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| storage                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-jf7wg
- pod: cilium-operator-6ffffff74-hdjmj
- pod: cilium-s42mz
- pod: clife-controller-manager-5755b9f7f5-8mcn2
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 7h55m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 7h55m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node                        | IP             | Net | Svc | Restarts     |
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 7h55m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 3 (2h3m ago) | 
| cilium-envoy-jf7wg                        |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h51m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 2 (2h3m ago) | 
| cilium-operator-6ffffff74-hdjmj           |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h51m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 2 (2h3m ago) | 
| cilium-s42mz                              |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h35m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 4 (2h2m ago) | 
| clife-controller-manager-5755b9f7f5-8mcn2 |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+

~~~
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
~~~
```

[[Back]](./step8.md) [[Next]](./README.md)