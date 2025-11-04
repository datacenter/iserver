# Grafana Operator - Create All

## Workflow

Workflows deployed in sequence
- [create operator](./create_operator.md)
- [enable monitoring](./enable_monitoring.md) if prometheus enabled for instance
- [enable instance](./delete_wipe.md) if instance defined

## Requirements

None

## Configurable options

```
# iserver set ocp grafana --mode all
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --instance TEXT                 Grafana instance name
  --username TEXT                 Grafana instance admin username
  --password TEXT                 Grafana instance admin password
  --prometheus                    Enable prometheus data source
  --datasource TEXT               Prometheus data source name  [default: my-prometheus]
  --no-confirm                    Confirmation mode
```

## Expected Outcome

- grafana operator installed
- user-workload monitoring enabled (optional)
- grafana instances created with prometheus datasource (optional)

## Example

```
# iserver set ocp grafana --mode all --cluster bm1 --instance test --username user --password pass --prometheus --datasource k8s --no-confirm

OpenShift Workflow - Grafana Operator - Create Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "channel": "__default__",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "grafana-operator",
    "name": "grafana-operator",
    "operator-group-name": "grafana-operator-group",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Namespace
----------------
- name: grafana-operator

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: grafana-operator

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: grafana-operator/grafana-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: grafana-operator-group
  namespace: grafana-operator
spec:
  targetNamespaces:
  - grafana-operator
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: grafana-operator/grafana-operator
Source: openshift-marketplace/community-operators/grafana-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: v5
- CSV [grafana-operator.v5.19.4]
- CSV Display name [Grafana Operator]
- CVS Version [5.19.4]
- CSV Provider [{'name': 'Grafana Labs', 'url': 'https://grafana.com'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: grafana-operator
  namespace: grafana-operator
spec:
  channel: v5
  installPlanApproval: Automatic
  name: grafana-operator
  source: community-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-gwpmd
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- grafana-operator/grafana-operator-controller-manager-v5


Completed tasks
---------------
- Namespace created
- Operator Group created
- Grafana Operator installed

OpenShift Workflow - Grafana Operator - Enable user-workload monitoring
=======================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "grafana-operator",
    "name": "grafana-operator",
    "operator-group-name": "grafana-operator-group",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Config Map
----------
- namespace: openshift-monitoring
- name: cluster-monitoring-config
- found and will be checked
- enableUserWorkload value will be changed in config map
Config map udpated

Check for resources
-------------------
Wait for deployments ready (optional: False, allow zero replicas: False)...
- openshift-user-workload-monitoring/prometheus-operator
Wait for stateful sets ready...
- openshift-user-workload-monitoring/prometheus-user-workload
- openshift-user-workload-monitoring/thanos-ruler-user-workload


Completed tasks
---------------
- User workload monitoring enabled

OpenShift Workflow - Grafana Operator - Create Instance
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "instance": "test",
    "username": "user",
    "password": "pass",
    "prometheus": true,
    "datasource": "k8s",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "grafana-operator",
    "name": "grafana-operator",
    "operator-group-name": "grafana-operator-group",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Check User Workload Monitoring
------------------------------
- config map namespace: openshift-monitoring
- config map name: cluster-monitoring-config
- enableUserWorkload enabled

Create Grafana Instance
-----------------------

~~~
apiVersion: grafana.integreatly.org/v1beta1
kind: Grafana
metadata:
  labels:
    dashboards: test
    folders: test
  name: test
  namespace: grafana-operator
spec:
  config:
    auth:
      disable_login_form: 'false'
    log:
      mode: console
    security:
      admin_password: pass
      admin_user: user
  route:
    spec: {}

~~~
Wait until grafana found [timeout:60s]...
Wait until grafana resources [timeout:60s]...
Wait for deployments ready (optional: False, allow zero replicas: False)...
- grafana-operator/test-deployment
Wait for service account...
Grafana instance route [test-route-grafana-operator.apps.bm1.domain.com]

Cluster Role Binding
--------------------
Service Account [test-sa] already associated with role [cluster-monitoring-view] in ClusterRoleBinding CR [test-sa-view]

Grafana Data Source
-------------------
Grafana datasource created
- grafana-operator/prometheus-test
- type: prometheus
- name: k8s
- token: service account [grafana-operator/test-sa]
- dashboards: test


Completed tasks
---------------
- Grafana instance created
- Prometheus data source created
```

[[Back]](./README.md)