# Splunk - Delete Operator

[[Back]](./README.md)

## Workflow

- delete `splunk-operator` namespaced resources
- wait for resources deleted
- delete namespace

## Requirements

No Splunk CRD may exist
- ClusterManager
- ClusterMaster
- IndexerCluster
- LicenseManager
- LicenseMaster
- MonitoringConsole
- SearchHeadCluster
- Standalone

## Configurable options

```
# iserver delete ocp splunk --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp splunk --mode operator --cluster bm1

OpenShift Workflow - Splunk Operator - Delete Operator
======================================================

OpenShift Cluster: bm1


Splunk Custom Resources
-----------------------
- standalone          : 0
- cluster master      : 0
- cluster manager     : 0
- indexer cluster     : 0
- license manager     : 0
- license master      : 0
- monitoring console  : 0
- search head cluster : 0


Delete Deployment
-----------------
- namespace: splunk-operator
- name: splunk-operator-controller-manager
- replica set: splunk-operator-controller-manager-5679c957f
- pod: splunk-operator-controller-manager-5679c957f-tmh7g
- wait for no deployment
- wait for no replica set splunk-operator/splunk-operator-controller-manager-5679c957f
- wait for no pod: splunk-operator-controller-manager-5679c957f-tmh7g

Delete Custom Resource Definition
---------------------------------
- name: clustermanagers.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: clustermasters.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: indexerclusters.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: ingestorclusters.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: licensemanagers.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: licensemasters.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: monitoringconsoles.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: objectstorages.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: queues.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: searchheadclusters.enterprise.splunk.com
- wait for no custom resource definition

Delete Custom Resource Definition
---------------------------------
- name: standalones.enterprise.splunk.com
- wait for no custom resource definition

Delete Config Map
-----------------
- namespace: splunk-operator
- name: splunk-operator-config
- wait for no config map

Delete Config Map
-----------------
- namespace: splunk-operator
- name: splunk-operator-manager-config
- wait for no config map

Delete Config Map
-----------------
- namespace: splunk-operator
- name: splunk-operator-manager-telemetry
- wait for no config map

Delete Config Map
-----------------
- namespace: splunk-operator
- name: splunk-splunk-operator-probe-configmap
- wait for no config map

Delete Service
--------------
- namespace: splunk-operator
- name: splunk-operator-controller-manager-metrics-service
- wait for no service

Delete Service
--------------
- namespace: splunk-operator
- name: splunk-operator-controller-manager-service
- wait for no service

Delete Persistent Volume Claim
------------------------------
- namespace: splunk-operator
- name: splunk-operator-app-download
- wait for no pvc

Delete RoleBinding
------------------
- namespace: splunk-operator
- name: splunk-operator-leader-election-rolebinding
- deleted
- wait for no role binding

Delete RoleBinding
------------------
- namespace: splunk-operator
- name: system:openshift:scc:nonroot-v2
- deleted
- wait for no role binding

Delete Role
-----------
- namespace: splunk-operator
- name: splunk-operator-leader-election-role
- deleted
- wait for no role

Delete ServiceAccount
---------------------
- namespace: splunk-operator
- name: splunk-operator-controller-manager
- deleted
Wait for no ServiceAccount splunk-operator/splunk-operator-controller-manager [timeout:60s]

Delete Namespace
----------------
- name: splunk-operator

Namespace [splunk-operator] resources
- no deployments
- no daemon_sets
- no replica_sets
- no pods
- no services
- no pvcs
- no jobs
Wait for no Namespace splunk-operator [timeout:60s]

Completed tasks
- Splunk operator deleted

+----+---------+--------+-----------------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow        | Changes | Success | Duration [s] |
+----+---------+--------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | splunk | delete operator | 24      | ✓       | 114          | 
+----+---------+--------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)