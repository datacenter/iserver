# MMState Operator - Get

[[Back]](./README.md)

## Workflow

- check nmstate operator subscription and cluster service version objects
- check nmstate instance object
- check NodeNetworkState CRD for every cluster node
- check NodeNetworkConfigurationPolicy objects
- check NodeNetworkConfigurationEnactment objects

## Requirements

None

## Configurable options

```
# iserver get ocp nmstate 
  --cluster TEXT         Cluster Name
```

## Example (view:state)

```
# iserver get ocp nmstate --cluster bm1 -v state

OpenShift Workflow - NMState Operator - Get Information
=======================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nmstate/kubernetes-nmstate-operator
- package               : openshift-marketplace/redhat-operators/kubernetes-nmstate-operator
- channel               : stable
- install plan          : openshift-nmstate/install-l2bpx
- install plan approved : ✓
- installed csv         : kubernetes-nmstate-operator.4.21.0-202609301335
- latest_csv            : ✓

Nmstate instance: nmstate (ready)

Node Network State
- bm1: found
Node network configuration policy: 0
Node network configuration enactment: 0
```

## Example (view:res)

```
# iserver get ocp nmstate --cluster bm1 -v res

OpenShift Workflow - NMState Operator - Get Information
=======================================================

OpenShift Cluster: bm1

+----+-----------------------------------+--------+--------+
| ID | Node Network Configuration Policy | Status | Reason |
+----+-----------------------------------+--------+--------+
+----+-----------------------------------+--------+--------+

+----+--------------------------------------+--------+
| ID | Node Network Configuration Enactment | Status |
+----+--------------------------------------+--------+
+----+--------------------------------------+--------+

+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+
| ID | Pod                                     | Ready | Status  | Annotation         | Node | IP           | Net | Restart | Age  |
+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+
| 1  | openshift-nmstate                       | 1/1   | Running | Initialized: ✓     | bm1  | 10.128.0.157 | 1   | 0       | 2h1m | 
|    | nmstate-console-plugin-5749566764-spffq |       |         | PodScheduled: ✓    |      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: ✓ |      |              |     |         |      | 
|    |                                         |       |         | Ready: ✓           |      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+
| 2  | openshift-nmstate                       | 1/1   | Running | Initialized: ✓     | bm1  | 10.58.29.81  | 0   | 0       | 2h1m | 
|    | nmstate-handler-n4ln6                   |       |         | PodScheduled: ✓    |      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: ✓ |      |              |     |         |      | 
|    |                                         |       |         | Ready: ✓           |      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+
| 3  | openshift-nmstate                       | 2/2   | Running | Initialized: ✓     | bm1  | 10.128.1.141 | 1   | 0       | 2h1m | 
|    | nmstate-metrics-6878cd9f58-7qf4g        |       |         | PodScheduled: ✓    |      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: ✓ |      |              |     |         |      | 
|    |                                         |       |         | Ready: ✓           |      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+
| 4  | openshift-nmstate                       | 1/1   | Running | Initialized: ✓     | bm1  | 10.128.1.169 | 1   | 0       | 2h3m | 
|    | nmstate-operator-79db9c9bb7-x9655       |       |         | PodScheduled: ✓    |      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: ✓ |      |              |     |         |      | 
|    |                                         |       |         | Ready: ✓           |      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+
| 5  | openshift-nmstate                       | 1/1   | Running | Initialized: ✓     | bm1  | 10.128.1.166 | 1   | 0       | 2h1m | 
|    | nmstate-webhook-6cffdc64b7-9ht9w        |       |         | PodScheduled: ✓    |      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: ✓ |      |              |     |         |      | 
|    |                                         |       |         | Ready: ✓           |      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+------+--------------+-----+---------+------+

+----+------------------------+-------+------------+-----------+------+
| ID | Deployment             | Ready | Up-To-Date | Available | Age  |
+----+------------------------+-------+------------+-----------+------+
| 1  | openshift-nmstate      | 1/1   | 1          | 1         | 2h1m | 
|    | nmstate-console-plugin |       |            |           |      | 
+----+------------------------+-------+------------+-----------+------+
| 2  | openshift-nmstate      | 1/1   | 1          | 1         | 2h1m | 
|    | nmstate-metrics        |       |            |           |      | 
+----+------------------------+-------+------------+-----------+------+
| 3  | openshift-nmstate      | 1/1   | 1          | 1         | 2h3m | 
|    | nmstate-operator       |       |            |           |      | 
+----+------------------------+-------+------------+-----------+------+
| 4  | openshift-nmstate      | 1/1   | 1          | 1         | 2h1m | 
|    | nmstate-webhook        |       |            |           |      | 
+----+------------------------+-------+------------+-----------+------+

+----+-----------------------------------+------------------------+---------+---------+-------+------+
| ID | Replica Set                       | Owner                  | Desired | Current | Ready | Age  |
+----+-----------------------------------+------------------------+---------+---------+-------+------+
| 1  | openshift-nmstate                 | Deployment             | 1       | 1       | 1     | 2h1m | 
|    | nmstate-console-plugin-5749566764 | nmstate-console-plugin |         |         |       |      | 
+----+-----------------------------------+------------------------+---------+---------+-------+------+
| 2  | openshift-nmstate                 | Deployment             | 1       | 1       | 1     | 2h1m | 
|    | nmstate-metrics-6878cd9f58        | nmstate-metrics        |         |         |       |      | 
+----+-----------------------------------+------------------------+---------+---------+-------+------+
| 3  | openshift-nmstate                 | Deployment             | 1       | 1       | 1     | 2h3m | 
|    | nmstate-operator-79db9c9bb7       | nmstate-operator       |         |         |       |      | 
+----+-----------------------------------+------------------------+---------+---------+-------+------+
| 4  | openshift-nmstate                 | Deployment             | 1       | 1       | 1     | 2h1m | 
|    | nmstate-webhook-6cffdc64b7        | nmstate-webhook        |         |         |       |      | 
+----+-----------------------------------+------------------------+---------+---------+-------+------+
```

[[Back]](./README.md)