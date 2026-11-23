# Observability Dashboards - Delete Setup

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
# iserver delete ocp task --filename absolute-filename --cluster bm1 --no-confirm

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Grafana Operator - Delete instance
=======================================================

Workflow Parameters
-------------------
{
    "instance": "tetragon",
    "cluster": "bm1",
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


Grafana Data Source
-------------------
- delete tetragon-thanos

Cluster Role Binding
--------------------
Service Account [tetragon-sa] associated with role [cluster-monitoring-view] in ClusterRoleBinding CR [tetragon-sa-view]
Delete ClusterRoleBinding CR [tetragon-sa-view]

Delete Grafana Instance
-----------------------
- namespace: grafana-operator
- name: grafana-operator
Wait until grafana gone [timeout:60s]...
Wait until grafana resources are gone [timeout:60s]...
Wait for deployments deleted (optional: False)...
- grafana-operator/tetragon-deployment
Wait for no service account...


Completed tasks
---------------
- Grafana instance deleted

OpenShift Workflow - Grafana Operator - Wipe Resources
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
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


Grafana
-------
- no resources found

GrafanaAlertRuleGroup
---------------------
- no resources found

GrafanaContactPoint
-------------------
- no resources found

GrafanaDashboard
----------------
- grafana-operator/tetragon-dns
- grafana-operator/tetragon-http-golden-signals-pod-pod
- grafana-operator/tetragon-http-golden-signals-socket
- grafana-operator/tetragon-network-interface
- grafana-operator/tetragon-tcp-throughput-socket
- grafana-operator/tetragon-tcp-throughput-sockets-host-binaries
- grafana-operator/tetragon-udp-throughput-socket
- grafana-operator/tetragonm-multicast
- grafana-operator/tetragonm-tcp-latency-socket
- grafana-operator/tetragonm-tcp-throughput-pod-pod

GrafanaDatasource
-----------------
- no resources found

GrafanaFolder
-------------
- no resources found

GrafanaLibraryPanel
-------------------
- no resources found

GrafanaMuteTiming
-----------------
- no resources found

GrafanaNotificationPolicy
-------------------------
- no resources found

GrafanaNotificationPolicyRoute
------------------------------
- no resources found

GrafanaNotificationTemplate
---------------------------
- no resources found

Completed tasks
- Grafana resources deleted

OpenShift Workflow - Grafana Operator - Disable user-workload monitoring
========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
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

Check for resources gone
------------------------
Wait for deployments deleted (optional: False)...
- openshift-user-workload-monitoring/prometheus-operator
Wait for stateful sets deleted (optional: False)...
- openshift-user-workload-monitoring/prometheus-user-workload
- openshift-user-workload-monitoring/thanos-ruler-user-workload


Completed tasks
---------------
- User workload monitoring disabled

OpenShift Workflow - Grafana Operator - Delete Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
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


Check Grafana resource
----------------------
- Grafana
- GrafanaAlertRuleGroup
- GrafanaContactPoint
- GrafanaDashboard
- GrafanaDatasource
- GrafanaFolder
- GrafanaLibraryPanel
- GrafanaMuteTiming
- GrafanaNotificationPolicy
- GrafanaNotificationPolicyRoute
- GrafanaNotificationTemplate

Delete Subscription
-------------------
- subscription: grafana-operator/grafana-operator
- checking cluster service version...
- csv found and will be deleted: grafana-operator/grafana-operator.v5.19.4
- wait for no subscription
- check cluster service version: grafana-operator/grafana-operator.v5.19.4
- wait for no csv
Wait for deployments deleted (optional: False)...
- grafana-operator/grafana-operator-controller-manager-v5

Delete Operator Group
---------------------
- namespace: grafana-operator
- name: grafana-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: grafana-operator

Namespace [grafana-operator] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Grafana Operator deleted
- Operator group deleted
- Namespace deleted

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
- upper-layers

Tracing Policy Namespaced
-------------------------
- no resources found

Completed tasks
- Tetragon resources deleted

OpenShift Workflow - Tetragon Operator - Delete Operator
========================================================

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
- no resources found

Delete Subscription
-------------------
- subscription: tetragon/tetragon-operator
- checking cluster service version...
- csv found and will be deleted: tetragon/tetragon-operator.v1.17.0
- wait for no subscription
- check cluster service version: tetragon/tetragon-operator.v1.17.0
- wait for no csv
Wait for deployments deleted (optional: True)...
- tetragon/tetragon-operator

Delete Catalog Source
---------------------
- namespace: tetragon
- name: tetragon-catalog
- wait for no catalog source
- wait for no catalog source pod

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-config
- wait for no config map

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-operator-config
- wait for no config map

Delete Service Monitor
----------------------
- namespace: tetragon
- name: tetragon
- wait for no service monitor

Delete Service
--------------
- namespace: tetragon
- name: tetragon
- wait for no service

Delete Operator Group
---------------------
- namespace: tetragon
- name: tetragon-operator
- already deleted

Delete Namespace
----------------
- name: tetragon

Namespace [tetragon] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace
```

[[Back]](./README.md)