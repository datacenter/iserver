# VAST Operator - Create cluster via Task

## Input

```
[
    {
        "vast": {
            "cluster": [
                {
                    "filename": "/tmp/vast_cluster.yaml"
                },
                {
                    "name": "my-vast",
                    "endpoint": "my-vast.domain.com",
                    "username": "admin",
                    "password": "password",
                    "any": "value"
                }
            ]
        }
    }
]
```

`VastCluster` can be created from yaml input file or generated based on parameters
- namespace defaults to vast-csi
- name must be defined
- endpoint must be defined
- username must be defined
- password must be defined
- any other value will end up in spec of an object as-is

## Example

```
# iserver set ocp task --cluster bm1 --file C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed

OpenShift Workflow - VAST CSI Operator - Create Cluster
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
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

+----+--------------+------+-----+---------------------------------------------------+---------+
| ID | Vast Cluster | Init | Dep | Spec                                              | Storage |
+----+--------------+------+-----+---------------------------------------------------+---------+
| 1  | vast-csi     | V    | V   | {                                                 | ---     | 
|    | my-vast      |      |     |   "endpoint": "my-vast.domain.com",               |         | 
|    |              |      |     |   "password": "password",                         |         | 
|    |              |      |     |   "username": "admin"                             |         | 
|    |              |      |     | }                                                 |         | 
+----+--------------+------+-----+---------------------------------------------------+---------+

Completed tasks
- VAST cluster created
```

[Back](./create_task.md)