# Observability Dashboards - Create

## Task

```
[
    {
        "grafana": {
            "operator": {},
            "mon": {},
            "instance": [
                {
                    "instance": "tetragon",
                    "username": "user",
                    "password": "pass",
                    "prometheus": true,
                    "datasource": "k8s",
                    "crd": [
                      "crd-filename-or-directory"
                    ],
                    "fixup": true
                }
            ]
        }
    },
    {
        "tetragon": {
            "operator": {
                "image": "image-name-as-provided-by-isovalent"
            },
            "prometheus": {},
            "wipe": {},
            "crd": {
                "crd": [
                  "crd-filename-or-directory"
                ]
            }
        }
    }
]
```

## Example

```
# iserver set ocp task --filename absolute-filename --cluster bm1 --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Grafana Operator - Create Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "channel": "__default__",
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
Install plan: install-8xjw5
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
    "instance": "tetragon",
    "username": "user",
    "password": "pass",
    "prometheus": true,
    "datasource": "k8s",
    "crd": "user-defined",
    "fixup": true,
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


Create Grafana Instance
-----------------------

~~~
apiVersion: grafana.integreatly.org/v1beta1
kind: Grafana
metadata:
  labels:
    dashboards: tetragon
    folders: tetragon
  name: tetragon
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
- grafana-operator/tetragon-deployment
Wait for service account...
Grafana instance route [tetragon-route-grafana-operator.apps.bm1.domain.com]

Check User Workload Monitoring
------------------------------
- config map namespace: openshift-monitoring
- config map name: cluster-monitoring-config
- enableUserWorkload enabled

Cluster Role Binding
--------------------
Service Account [tetragon-sa] is not yet associated with role [cluster-monitoring-view]
Cluster role binding created: tetragon-sa-view

Create Grafana Datasource
-------------------------
- instance: tetragon
- get service account token for grafana instance

~~~
apiVersion: grafana.integreatly.org/v1beta1
kind: GrafanaDatasource
metadata:
  name: tetragon-thanos
  namespace: grafana-operator
spec:
  datasource:
    access: proxy
    editable: true
    isDefault: true
    jsonData:
      httpHeaderName1: Authorization
      timeInterval: 5s
      tlsSkipVerify: true
    name: k8s
    secureJsonData:
      httpHeaderValue1: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlJHN1lTcTVuMTlIVElkb3FGMWR6OWtvbU81bEN5ZmJXeGhoYU5XLVlORXMifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjIl0sImV4cCI6NjA1NTI0MjgxNywiaWF0IjoxNzYwMjc1NTIxLCJpc3MiOiJodHRwczovL2t1YmVybmV0ZXMuZGVmYXVsdC5zdmMiLCJqdGkiOiJhZDQ1YzdhYy1lYWU2LTRkMmItYjE4Yi04MWU4MzExMTg4NTkiLCJrdWJlcm5ldGVzLmlvIjp7Im5hbWVzcGFjZSI6ImdyYWZhbmEtb3BlcmF0b3IiLCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoidGV0cmFnb24tc2EiLCJ1aWQiOiIxNDI1NjMyOS1jNjkyLTRjM2ItOWFmOC0xOTg3NjBhMDRmNmIifX0sIm5iZiI6MTc2MDI3NTUyMSwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmdyYWZhbmEtb3BlcmF0b3I6dGV0cmFnb24tc2EifQ.VXFggIuDbTyw3FKcykgC79fZR0xCv3Kz4Gr0BPqo2P2Vn9xbcjOMqUO0Qnhl--qdj_ipgO3mbY6-ApXjXNmA-IA4XnKbqjnhvIiTscVp41qRH9Lwb4N4zRch8tXfGD4rdwLFZ0t-FcMXzgAJsZzX-H3lCX22g3LiHeOtZx8AlH5te3p6VaIyvrrnuhf9AhNc9xImiCbkE16lOiQQS4gqgn1dQvxdIWbvVWFCMCNLNl7gL_J4oGNdOhgL3g9RFytcHEFK1k3FCbvyHs8mENiwdaPDyn-H7CGl6NX-GFB6ibXue0-gwL5T9IemoCYjur4_CC8wTTyfyeBN5kIT1l8lv78HU2pf0RnqHuPFPCMGBJ4v3gQCUXAiDWnc25QH_GNoczzlmauGMLTr0OiicLgGuAnghB0A5W9JJpQYBukO8FqEoK0J3obVlMyMHxMPSHaBZCWoUrRoCoHvneaIrr3cd4araXXEdtTrP_HxYDpGATRAx3jlgG6OelTAdFzl9R5535myUvZcasvB30sTG_bOvrMnVD2s5j7KekJ80f4BfUrwQS8VJX1iBiME32oUKmVDP8aPROPUHNZyNwVDhu9E7vOtuwgkk7L4lxD5IVWQUl3Ym2XqLiex1UyPEcj-ejatIsK5CLexf46Ap1ijDSAYww8_LNgeEbBchoLTYPLJWiI
    type: prometheus
    url: https://thanos-querier.openshift-monitoring.svc.cluster.local:9091
  instanceSelector:
    matchLabels:
      dashboards: tetragon

~~~
Wait until grafana found [timeout:60s]...

Grafana datasource created
- grafana-operator/tetragon-thanos
- type: prometheus
- name: k8s
- token: service account [grafana-operator/tetragon-sa]
- dashboards: tetragon

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...

Create Grafana Dashboard from YAML (with fixup)
-----------------------------------------------
- spec:json found
- ${PROMETHEUS} replaced with k8s
- dashboard created
- wait until grafana dashboard found [timeout:60s]...


Completed tasks
---------------
- Grafana instance defined
- Prometheus data source created
- CRDs added

OpenShift Workflow - Tetragon Operator - Create Operator
========================================================

Workflow Parameters
-------------------
{
    "image": "user-defined",
    "cluster": "bm1",
    "confirmation": false,
    "channel": "__default__",
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Namespace
----------------
- name: tetragon
- labels
	openshift.io/user-monitoring:true

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/user-monitoring: 'true'
  name: tetragon

~~~

Namespace created

Wait for namespace [timeout:60]...

Check labels
- openshift.io/user-monitoring:true

Create Operator Group
---------------------
Operator group: tetragon/tetragon

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: tetragon
  namespace: tetragon
spec:
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Catalog Source
---------------------
- namespace: tetragon
- name: tetragon-catalog
- source: grpc

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: tetragon-catalog
  namespace: tetragon
spec:
  image: user-provided
  sourceType: grpc

~~~

Catalog source created

Wait for catalog source [timeout:60]...
Wait for tetragon package...

Create Subscription
-------------------
Subscription: tetragon/tetragon-operator
Source: tetragon/tetragon-catalog/tetragon-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: v1.17
- CSV [tetragon-operator.v1.17.0]
- CSV Display name [Tetragon Operator]
- CVS Version [1.17.0]
- CSV Provider [{'name': 'Isovalent', 'url': 'https://isovalent.com'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/tetragon-operator.tetragon: ''
  name: tetragon-operator
  namespace: tetragon
spec:
  channel: v1.17
  installPlanApproval: Automatic
  name: tetragon-operator
  source: tetragon-catalog
  sourceNamespace: tetragon

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-ggdgz
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- tetragon/tetragon-operator

Completed tasks
- Namespace created
- Operator Group created
- Tetragon Operator installed

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
- enableUserWorkload already enabled

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

OpenShift Workflow - Tetragon Operator - Enable Prometheus Service Monitor
==========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Config map [tetragon/tetragon-operator-config] found
agentDaemonSet found in config map data
serviceMonitorEnabled will be set to true
Config map patched
Deployment [tetragon/tetragon-operator] restarted
Config map patched
Deployment [tetragon/tetragon-operator] restarted
Wait for service monitors...
- tetragon/tetragon

Completed tasks
- Tetragon service monitors enabled

OpenShift Workflow - Tetragon Operator - Wipe Resources
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Alert Rule
----------
- no resources found

Sandbox Policy
--------------
- no resources found

Sandbox Policy Namespaced
-------------------------
- no resources found

Tetragon Network Policy
-----------------------
- no resources found

Tetragon Network Policy Namespaced
----------------------------------
- no resources found

Tracing Policy
--------------
- no resources found

Tracing Policy Namespaced
-------------------------
- no resources found

Completed tasks
- Tetragon resources deleted

OpenShift Workflow - Tetragon Operator - Create Policy
======================================================

Workflow Parameters
-------------------
{
    "crd": "user-defined",
    "cluster": "bm1",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Tracing Policy
---------------------
- name: upper-layers

Tracing policy created

Wait for tracing policy [timeout:60]...

Completed tasks
- CRDs applied
```

[[Back]](./README.md)