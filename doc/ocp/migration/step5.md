# Cilium EE migration workflow

[[Back]](./step4.md) [[Next]](./step6.md)

## Step 5: Re-enable OpenShift operator management

- restart the OpenShift API server
- restart Machine Config Operator pods
- scale the Cluster Network Operator up to start managing the network
- configure the Cluster Version Operator to once again manage the Network Operator

### Output

```
Step 5: Re-enable OpenShift operator management
===============================================


Delete kube API server pods
---------------------------

+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+-----------------+
| Pod                                        | Ready | Status  | Condition          | Age | Node                        | IP             | Net | Svc | Restarts        |
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+-----------------+
| openshift-kube-apiserver                   | 5/5   | Running | Initialized: ✓     | 9d  | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 25 (18h40m ago) | 
| kube-apiserver-openshift.public.domain.com |       |         | PodScheduled: ✓    |     |                             |                |     |     |                 | 
|                                            |       |         | ContainersReady: ✓ |     |                             |                |     |     |                 | 
|                                            |       |         | Ready: ✓           |     |                             |                |     |     |                 | 
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+-----------------+

Delete
- kube-apiserver-openshift.public.domain.com

Delete machine config deployments
---------------------------------

+-----------------------------------+-------+------------+-----------+-----+
| Deployment                        | Ready | Up-To-Date | Available | Age |
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-controller         |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-operator           |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+

+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+-----------------+
| Pod                                        | Ready | Status  | Condition          | Age | Node                        | IP          | Net | Svc | Restarts        |
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+-----------------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 10d | openshift.public.domain.com | 10.128.0.34 | 0   | --  | 15 (18h37m ago) | 
| machine-config-controller-594f4479f5-54zn5 |       |         | PodScheduled: ✓    |     |                             |             |     |     |                 | 
|                                            |       |         | ContainersReady: ✓ |     |                             |             |     |     |                 | 
|                                            |       |         | Ready: ✓           |     |                             |             |     |     |                 | 
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+-----------------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 10d | openshift.public.domain.com | 10.128.0.10 | 0   | --  | 15 (18h35m ago) | 
| machine-config-operator-847bd8d8b8-4d2pb   |       |         | PodScheduled: ✓    |     |                             |             |     |     |                 | 
|                                            |       |         | ContainersReady: ✓ |     |                             |             |     |     |                 | 
|                                            |       |         | Ready: ✓           |     |                             |             |     |     |                 | 
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+-----------------+

Rollout restart

Take a nap...


Wait for deployment ready

+-----------------------------------+-------+------------+-----------+-----+
| Deployment                        | Ready | Up-To-Date | Available | Age |
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-controller         |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-operator           |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+

+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+
| Pod                                       | Ready | Status  | Condition          | Age  | Node                        | IP           | Net | Svc | Restarts |
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+
| openshift-machine-config-operator         | 2/2   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 10.128.0.138 | 0   | --  | 0        | 
| machine-config-controller-cc9c5bfb9-vmbnp |       |         | PodScheduled: ✓    |      |                             |              |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |                             |              |     |     |          | 
|                                           |       |         | Ready: ✓           |      |                             |              |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+
| openshift-machine-config-operator         | 2/2   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 10.128.0.139 | 0   | --  | 0        | 
| machine-config-operator-8684b89d95-mwkzc  |       |         | PodScheduled: ✓    |      |                             |              |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |                             |              |     |     |          | 
|                                           |       |         | Ready: ✓           |      |                             |              |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+

Network Operator
----------------

+----------------------------+-------+------------+-----------+-----+
| Deployment                 | Ready | Up-To-Date | Available | Age |
+----------------------------+-------+------------+-----------+-----+
| openshift-network-operator | 0/0   | None       | None      | 10d | 
| network-operator           |       |            |           |     | 
+----------------------------+-------+------------+-----------+-----+

Configure deployment replicas
-----------------------------
- namespace: openshift-network-operator
- name: network-operator
- replicas: 1

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: network-operator
  namespace: openshift-network-operator
spec:
  replicas: 1

~~~
Patch successful

Wait for desired replica pods...

+--------------------------------------------------------+---------+---------+-------+-----+
| Replica Set                                            | Desired | Current | Ready | Age |
+--------------------------------------------------------+---------+---------+-------+-----+
| openshift-network-operator/network-operator-798d48796b | 1       | 1       | 1     | 10d | 
+--------------------------------------------------------+---------+---------+-------+-----+

+-----------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| Pod                               | Ready | Status  | Condition          | Age  | Node                        | IP             | Net | Svc | Restarts |
+-----------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| openshift-network-operator        | 1/1   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| network-operator-798d48796b-l8bfg |       |         | PodScheduled: ✓    |      |                             |                |     |     |          | 
|                                   |       |         | ContainersReady: ✓ |      |                             |                |     |     |          | 
|                                   |       |         | Ready: ✓           |      |                             |                |     |     |          | 
+-----------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+

Enable network operator management
----------------------------------

~~~
api: config.openshift.io/v1
kind: ClusterVersion
metadata:
  name: version
spec:
  overrides: null

~~~
Patch successful
```

[[Back]](./step4.md) [[Next]](./step6.md)