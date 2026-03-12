# OpenShitf Authentication (OAuth) - Restart authentication pods

[[Back]](./README.md) [[Prev]](./get.md) [[Next]](./log.md)

## Workflow

Operator (--mode operator)
- get `Deployment` in `openshift-authentication-operator` namespace with label app:authentication-operator
- scale to 0 and wait till all pods are gone
- scale to previous replicas and wait

OAuth (--mode oauth)
- get `Deployment` in `openshift-authentication` namespace with label app:oauth-openshift
- scale to 0
- wait until deployment is back ready

## Requirements

None

## Configurable options

```
# iserver set ocp oauth --mode restart
  --cluster TEXT   Cluster Name
  --cluster TEXT            Cluster Name
  --mode [log|restart]      Mode of operation
  --scope [oauth|operator]  Restart deployment  [default: oauth]
  --no-confirm              Confirmation mode
```

## Example (operator)

```
# iserver set ocp oauth --cluster bm1 --mode restart --scope operator

OpenShift Workflow - OAuth - Restart
====================================

OpenShift Cluster: bm1

+----+-----------------------------------+-------+------------+-----------+-----+
| ID | Deployment                        | Ready | Up-To-Date | Available | Age |
+----+-----------------------------------+-------+------------+-----------+-----+
| 1  | openshift-authentication-operator | 1/1   | 1          | 1         | 13d | 
|    | authentication-operator           |       |            |           |     | 
+----+-----------------------------------+-------+------------+-----------+-----+

+----+-----------------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| ID | Pod                                     | Ready | Label   | Annotation         | Node                 | IP           | Net | Restart | Age  |
+----+-----------------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| 1  | openshift-authentication-operator       | 1/1   | Running | Initialized: V     | bm1-1                | 10.128.5.115 | 1   | 0       | 1h2m | 
|    | authentication-operator-b95c6db64-cr5vb |       |         | PodScheduled: V    |                      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: V |                      |              |     |         |      | 
|    |                                         |       |         | Ready: V           |                      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+

Configure deployment replicas
-----------------------------
- namespace: openshift-authentication-operator
- name: authentication-operator
- replicas: 0

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: authentication-operator
  namespace: openshift-authentication-operator
spec:
  replicas: 0

~~~
Patch successful

Wait for desired replica pods...

Configure deployment replicas
-----------------------------
- namespace: openshift-authentication-operator
- name: authentication-operator
- replicas: 1

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: authentication-operator
  namespace: openshift-authentication-operator
spec:
  replicas: 1

~~~
Patch successful

Wait for desired replica pods...

+----+-----------------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| ID | Pod                                     | Ready | Label   | Annotation         | Node                 | IP           | Net | Restart | Age  |
+----+-----------------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| 1  | openshift-authentication-operator       | 1/1   | Running | Initialized: V     | bm1-1                | 10.128.5.197 | 1   | 0       | 1h0m | 
|    | authentication-operator-b95c6db64-nx7bs |       |         | PodScheduled: V    |                      |              |     |         |      | 
|    |                                         |       |         | ContainersReady: V |                      |              |     |         |      | 
|    |                                         |       |         | Ready: V           |                      |              |     |         |      | 
+----+-----------------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
```

## Example (oauth)

```
# iserver set ocp oauth --cluster bm1 --mode restart --scope oauth


OpenShift Workflow - OAuth - Restart
====================================

OpenShift Cluster: bm1

+----+--------------------------+-------+------------+-----------+-----+
| ID | Deployment               | Ready | Up-To-Date | Available | Age |
+----+--------------------------+-------+------------+-----------+-----+
| 1  | openshift-authentication | 3/3   | 3          | 3         | 13d | 
|    | oauth-openshift          |       |            |           |     | 
+----+--------------------------+-------+------------+-----------+-----+

+----+----------------------------------+-------+---------+--------------------+----------------------+-------------+-----+---------+------+
| ID | Pod                              | Ready | Label   | Annotation         | Node                 | IP          | Net | Restart | Age  |
+----+----------------------------------+-------+---------+--------------------+----------------------+-------------+-----+---------+------+
| 1  | openshift-authentication         | 1/1   | Running | Initialized: V     | bm1-3                | 10.128.3.40 | 1   | 0       | 1h1m | 
|    | oauth-openshift-55f74b6ccd-k2kjj |       |         | PodScheduled: V    |                      |             |     |         |      | 
|    |                                  |       |         | ContainersReady: V |                      |             |     |         |      | 
|    |                                  |       |         | Ready: V           |                      |             |     |         |      | 
+----+----------------------------------+-------+---------+--------------------+----------------------+-------------+-----+---------+------+
| 2  | openshift-authentication         | 1/1   | Running | Initialized: V     | bm1-2                | 10.128.0.5  | 1   | 0       | 1h1m | 
|    | oauth-openshift-55f74b6ccd-lkw8x |       |         | PodScheduled: V    |                      |             |     |         |      | 
|    |                                  |       |         | ContainersReady: V |                      |             |     |         |      | 
|    |                                  |       |         | Ready: V           |                      |             |     |         |      | 
+----+----------------------------------+-------+---------+--------------------+----------------------+-------------+-----+---------+------+
| 3  | openshift-authentication         | 1/1   | Running | Initialized: V     | bm1-1                | 10.128.4.28 | 1   | 0       | 1h1m | 
|    | oauth-openshift-55f74b6ccd-zl7h8 |       |         | PodScheduled: V    |                      |             |     |         |      | 
|    |                                  |       |         | ContainersReady: V |                      |             |     |         |      | 
|    |                                  |       |         | Ready: V           |                      |             |     |         |      | 
+----+----------------------------------+-------+---------+--------------------+----------------------+-------------+-----+---------+------+

Configure deployment replicas
-----------------------------
- namespace: openshift-authentication
- name: oauth-openshift
- replicas: 0

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: oauth-openshift
  namespace: openshift-authentication
spec:
  replicas: 0

~~~
Patch successful
Take a nap...
Wait for deployment openshift-authentication/oauth-openshift [timeout:600s]

+----+----------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| ID | Pod                              | Ready | Label   | Annotation         | Node                 | IP           | Net | Restart | Age  |
+----+----------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| 1  | openshift-authentication         | 1/1   | Running | Initialized: V     | bm1-2                | 10.128.1.11  | 1   | 0       | 1h0m | 
|    | oauth-openshift-55f74b6ccd-bj9sv |       |         | PodScheduled: V    |                      |              |     |         |      | 
|    |                                  |       |         | ContainersReady: V |                      |              |     |         |      | 
|    |                                  |       |         | Ready: V           |                      |              |     |         |      | 
+----+----------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| 2  | openshift-authentication         | 1/1   | Running | Initialized: V     | bm1-3                | 10.128.3.108 | 1   | 0       | 1h0m | 
|    | oauth-openshift-55f74b6ccd-dsdds |       |         | PodScheduled: V    |                      |              |     |         |      | 
|    |                                  |       |         | ContainersReady: V |                      |              |     |         |      | 
|    |                                  |       |         | Ready: V           |                      |              |     |         |      | 
+----+----------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
| 3  | openshift-authentication         | 1/1   | Running | Initialized: V     | bm1-1                | 10.128.4.133 | 1   | 0       | 1h0m | 
|    | oauth-openshift-55f74b6ccd-glst7 |       |         | PodScheduled: V    |                      |              |     |         |      | 
|    |                                  |       |         | ContainersReady: V |                      |              |     |         |      | 
|    |                                  |       |         | Ready: V           |                      |              |     |         |      | 
+----+----------------------------------+-------+---------+--------------------+----------------------+--------------+-----+---------+------+
```

[[Back]](./README.md) [[Prev]](./get.md) [[Next]](./log.md)