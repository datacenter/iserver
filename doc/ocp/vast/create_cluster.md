# VAST CSI - Create Cluster

[[Back]](./README.md) [[kb]](./kb/cluster.md)

## HowTo

```
# iserver set ocp vast --cluster bm1 --mode cluster --filename C:\tmp\cluster.yaml --no-confirm

# iserver set ocp vast --mode cluster
  --cluster TEXT            Cluster Name
  --filename TEXT           VAST CSI CRD
  --no-confirm              Confirmation mode
```

## Workflow

- check vast csi [operator](./create_operator.md)
- create `VastCluster` resource
- wait for initiatlization and deployed status

## Example

```
# iserver set ocp vast --cluster bm1 --mode cluster --filename C:\tmp\cluster.yaml --no-confirm

OpenShift Workflow - VAST CSI Operator - Create Cluster
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Create VastCluster
------------------
- namespace: vast-csi
- name: my-vast

~~~
apiVersion: storage.vastdata.com/v1
kind: VastCluster
metadata:
  name: my-vast
  namespace: vast-csi
spec:
  endpoint: my-vast.domain.com
  password: password
  username: admin
~~~
VastCluster [vast-csi/my-vast] created
- wait for VastCluster vast-csi/my-vast [timeout:60s]
- wait for VastCluster vast-csi/my-vast [timeout:360s] with {"initialized_status": "True"}
- wait for VastCluster vast-csi/my-vast [timeout:360s] with {"deployed_status": "True"}

+----+--------------+------+-----+---------------------------------------------------+
| ID | Vast Cluster | Init | Dep | Spec                                              |
+----+--------------+------+-----+---------------------------------------------------+
| 1  | vast-csi     | V    | V   | {                                                 | 
|    | my-vast      |      |     |   "endpoint": "my-vast.domain.com",               | 
|    |              |      |     |   "password": "password",                         | 
|    |              |      |     |   "username": "admin"                             | 
|    |              |      |     | }                                                 | 
+----+--------------+------+-----+---------------------------------------------------+

Completed tasks
- VAST cluster created

+----+------------+-------+----------------+---------+---------+--------------+
| ID | Target     | Scope | Workflow       | Changes | Success | Duration [s] |
+----+------------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1    | vast  | create cluster | 1       | V       | 46           | 
+----+------------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/cluster.md)