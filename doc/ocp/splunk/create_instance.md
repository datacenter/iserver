# Splunk - Create Standalone Instance

[[Back]](./README.md)

## Workflow

- create standalone splunk instance
- create route
- wait for instance resources ready

## Configurable options

```
# iserver set ocp splunk --mode instance
  --cluster TEXT          Cluster name
  --name TEXT             Standalone instance name
  --etc-size TEXT         etc volume size  [default: 10Gi]
  --etc-sc TEXT           etc storage class
  --var-size TEXT         var volume size  [default: 100Gi]
  --var-sc TEXT           var storage class
  --sa TEXT               service account  [default: default]
  --no-route              Instance route
  --no-confirm            Confirmation mode
```

## Expected outcome

```
$ oc get standalones.enterprise.splunk.com -A
NAMESPACE         NAME    PHASE   DESIRED   READY   AGE     MESSAGE
splunk-operator   inst1   Ready   1         1       2m44s
```

## Example

```
# iserver set ocp splunk --mode instance --cluster bm1 --name inst1 --etc-size 20Gi --var-size 50Gi --no-confirm

OpenShift Workflow - Splunk Operator - Create Instance
======================================================

OpenShift Cluster: bm1

Replace RoleBinding
-------------------
- namespace: splunk-operator
- name: system:openshift:scc:nonroot-v2

~~~
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: system:openshift:scc:nonroot-v2
  namespace: splunk-operator
  resource_version: '853136'
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:openshift:scc:nonroot-v2
subjects:
- kind: ServiceAccount
  name: splunk-operator-controller-manager
  namespace: splunk-operator
- kind: ServiceAccount
  name: default
  namespace: splunk-operator
~~~
RoleBinding [splunk-operator/system:openshift:scc:nonroot-v2] replaced

Create Standalone
-----------------
- namespace: splunk-operator
- name: inst1

~~~
apiVersion: enterprise.splunk.com/v4
kind: Standalone
metadata:
  finalizers:
  - enterprise.splunk.com/delete-pvc
  name: inst1
  namespace: splunk-operator
spec:
  etcVolumeStorageConfig:
    storageCapacity: 20Gi
    storageClassName: lvms-vg1
  varVolumeStorageConfig:
    storageCapacity: 50Gi
    storageClassName: lvms-vg1
~~~
Standalone [splunk-operator/inst1] created
Wait until pod splunk-operator/splunk-inst1-standalone-0 is running [timeout:1800s]...
Wait for Standalone splunk-operator/inst1 [timeout:600s] with {"ready": true}

Create splunk instance route
----------------------------
- instance namespace: splunk-operator
- instance name: inst1
- service namespace: splunk-operator
- service name: splunk-inst1-standalone-service
- service found
- route namespace: splunk-operator
- route name: splunk-inst1-standalone-service

~~~
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  labels:
    app.kubernetes.io/component: standalone
    app.kubernetes.io/instance: splunk-inst1-standalone
    app.kubernetes.io/managed-by: splunk-operator
    app.kubernetes.io/name: standalone
    app.kubernetes.io/part-of: splunk-inst1-standalone
  name: splunk-inst1-standalone-service
  namespace: splunk-operator
spec:
  host: splunk-inst1-standalone-service-splunk-operator.apps.bm1.domain.com
  port:
    targetPort: http-splunkweb
  to:
    kind: Service
    name: splunk-inst1-standalone-service
    weight: 100
  wildcardPolicy: null
~~~

Route created
Wait for Route splunk-operator/splunk-inst1-standalone-service [timeout:120s] with {"ready": true}

+----+-----------------+-------+-----+-----+---------+-------+-----------------------------------------------------------------------------+
| ID | Standalone      | Ready | Pod | PVC | Service | Route | URL                                                                         |
+----+-----------------+-------+-----+-----+---------+-------+-----------------------------------------------------------------------------+
| 1  | splunk-operator | ✓     | ✓   | 2/2 | ✓       | 1/1   | http://splunk-inst1-standalone-service-splunk-operator.apps.bm1.domain.com | 
|    | inst1           |       |     |     |         |       | (admin, 1BEluK4lz9A4l9XX1WqMr5bG)                                           | 
|    |                 |       |     |     |         |       | hec_token:1F2B0614-5FE6-B0EC-C7AE-38794FA15AF3                              | 
|    |                 |       |     |     |         |       | idxc_secret:Z23S01LDCrWs0BecsHoE6lk0                                        | 
|    |                 |       |     |     |         |       | pass4SymmKey:sHKmgVN2qokWi46ahtJSRLIC                                       | 
|    |                 |       |     |     |         |       | shc_secret:ib4j7Gy2qjfcSXEvUVsc0pdw                                         | 
+----+-----------------+-------+-----+-----+---------+-------+-----------------------------------------------------------------------------+

Completed tasks
- Standalone instance created
- Route configured

+----+---------+--------+-----------------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow        | Changes | Success | Duration [s] |
+----+---------+--------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | splunk | create instance | 3       | ✓       | 75           | 
+----+---------+--------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)