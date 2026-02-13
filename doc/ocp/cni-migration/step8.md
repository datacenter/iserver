# Cilium EE migration workflow

[[Back]](./step7.md) [[Next]](./step9.md)

## Step 8: Post migration


- remove devices setting from CiliumConfig
- restart cilium agents and wait till running
- approve cilium installplan
- remove openshift-ovn-kubernetes namespace
- install cilium cli on the selected node of the cluster aka management node
- run cilium health checks

### Output

```
Step 8: Post migration
======================

Remove device from cilium config
- patched
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-jf7wg
- pod: cilium-operator-6ffffff74-hdjmj
- pod: cilium-s42mz
- pod: clife-controller-manager-5c5ccd57bc-2p7ln
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+------+
| Deployment               | Ready | Up-To-Date | Available | Age  |
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 7h4m | 
| cilium-operator          |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 7h4m | 
| clife-controller-manager |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+

+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+---------------+
| Pod                                       | Ready | Status  | Condition          | Age  | Node                        | IP             | Net | Svc | Restarts      |
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 7h4m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 1 (6h28m ago) | 
| cilium-envoy-jf7wg                        |       |         | PodScheduled: ✓    |      |                             |                |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |      |                             |                |     |     |               | 
|                                           |       |         | Ready: ✓           |      |                             |                |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0             | 
| cilium-operator-6ffffff74-hdjmj           |       |         | PodScheduled: ✓    |      |                             |                |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |      |                             |                |     |     |               | 
|                                           |       |         | Ready: ✓           |      |                             |                |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0             | 
| cilium-s42mz                              |       |         | PodScheduled: ✓    |      |                             |                |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |      |                             |                |     |     |               | 
|                                           |       |         | Ready: ✓           |      |                             |                |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 7h4m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 4 (4h45m ago) | 
| clife-controller-manager-5c5ccd57bc-2p7ln |       |         | PodScheduled: ✓    |      |                             |                |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |      |                             |                |     |     |               | 
|                                           |       |         | Ready: ✓           |      |                             |                |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+---------------+

Approve cilium install plan
- installplan cilium/install-mklwg will be approved
- patched (approved)

Remove ovn-kubernetes namespace

Namespace [openshift-ovn-kubernetes] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs

Namespace deleted 

OpenShift Workflow - Install cilium cli
=======================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
    "url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz",
    "check-verbose": false
}

Downloading cilium binary from https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz
Uploading cilium binary to cluster management node
Unpack
Change file flags
Cilium binary ready to be used
cilium-cli: v0.18.6 compiled with go1.24.5 on linux/amd64
cilium image (default): v1.18.0
cilium image (stable): v1.18.2

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

[[Back]](./step7.md) [[Next]](./step9.md)