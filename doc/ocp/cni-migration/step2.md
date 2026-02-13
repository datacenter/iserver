# Cilium EE migration workflow

[[Back]](./step1.md) [[Next]](./step3.md)

## Step 2: Disable cluster network operator

- disable the management of the network operator
- scale the network-operator pods to zero, effectively disabling it
- delete the applied-cluster ConfigMap in the openshift-network-operator namespace to remove the state file created when the cluster was initially deployed
- pause Machine Config Operator

### Output

```
Step 2: Disable cluster network operator
========================================


Disable network operator management
-----------------------------------

~~~
api: config.openshift.io/v1
kind: ClusterVersion
metadata:
  name: version
spec:
  overrides:
  - group: apps
    kind: Deployment
    name: network-operator
    namespace: openshift-network-operator
    unmanaged: true

~~~
Continue [Y/N]? y
Patch successful

Network Operator
----------------

+----------------------------+-------+------------+-----------+-----+
| Deployment                 | Ready | Up-To-Date | Available | Age |
+----------------------------+-------+------------+-----------+-----+
| openshift-network-operator | 1/1   | 1          | 1         | 10d |
| network-operator           |       |            |           |     |
+----------------------------+-------+------------+-----------+-----+

+--------------------------------------------------------+---------+---------+-------+-----+
| Replica Set                                            | Desired | Current | Ready | Age |
+--------------------------------------------------------+---------+---------+-------+-----+
| openshift-network-operator/network-operator-798d48796b | 1       | 1       | 1     | 10d |
+--------------------------------------------------------+---------+---------+-------+-----+

+-----------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+----------------+
| Pod                               | Ready | Status  | Condition          | Age | Node                        | IP             | Net | Svc | Restarts       |
+-----------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+----------------+
| openshift-network-operator        | 1/1   | Running | Initialized: ✓     | 10d | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 8 (17h58m ago) |
| network-operator-798d48796b-sfkf4 |       |         | PodScheduled: ✓    |     |                             |                |     |     |                |
|                                   |       |         | ContainersReady: ✓ |     |                             |                |     |     |                |
|                                   |       |         | Ready: ✓           |     |                             |                |     |     |                |
+-----------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+----------------+

Configure deployment replicas
-----------------------------
- namespace: openshift-network-operator
- name: network-operator
- replicas: 0

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: network-operator
  namespace: openshift-network-operator
spec:
  replicas: 0

~~~
Continue [Y/N]? y
Patch successful

Wait for desired replica pods...

Delete Config Map
-----------------
- namespace: openshift-network-operator
- name: applied-cluster
- wait for no config map

Set Machine Config Pool Pause
-----------------------------
- name: master
- pause: True

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: master
spec:
  paused: true

~~~
Continue [Y/N]? y
Patch successful

Set Machine Config Pool Pause
-----------------------------
- name: worker
- pause: True

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker
spec:
  paused: true

~~~
Continue [Y/N]? y
Patch successful
```

[[Back]](./step1.md) [[Next]](./step3.md)