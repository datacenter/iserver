# VAST Cluster

## Get state

```
# iserver get k8s vastc --cluster bm1
Cluster: bm1 (type: ocp)

+----+--------------+------+-----+---------------------------------------------------+------------+
| ID | Vast Cluster | Init | Dep | Spec                                              | Storage    |
+----+--------------+------+-----+---------------------------------------------------+------------+
| 1  | vast-csi     | V    | V   | {                                                 | vast-block |
|    | my-vast      |      |     |   "endpoint": "my-vast.domain.com", | vast-nfs    |
|    |              |      |     |   "password": "password",                         |            |
|    |              |      |     |   "username": "admin"                             |            |
|    |              |      |     | }                                                 |            |
+----+--------------+------+-----+---------------------------------------------------+------------+

Filter: namespace, name
View:   state (def), manifest
```

## Get release manifest

```
# iserver get k8s vastc --cluster bm1 -v manifest
Cluster: bm1 (type: ocp)

Vast Cluster Manifest [vast-csi/cluster]
----------------------------------------
~~~
---
# Source: vastcluster/templates/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: cluster
  namespace: "vast-csi"
  labels:
    used-by: vast-csi-driver-operator
    helm.sh/chart: vastcluster-v2.6.4
    app.kubernetes.io/name: vastcluster
    app.kubernetes.io/instance: cluster
    app.kubernetes.io/managed-by: Helm
type: Opaque
data:
  endpoint: ...
  username: ...
  password: ...

~~~

Filter: namespace, name
View:   state (def), manifest
```

[[Back]](./README.md)