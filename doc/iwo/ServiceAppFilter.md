# Intersight Workload Optimizer

## Filter by service application name

```
# iserver get iwo service --app registry-server

Summary
-------
- Active   : 4/4
- Severity : 4/0/0/0
- Current  : 4/4


+--------+----------+-----------+---------+---------------------------+---------------------------------------------------+----------------------+---------------------------------------------------------------------+
| State  | Severity | Staleness | Actions | Cluster                   | Service Name                                      | Application Severity | Application                                                         |
+--------+----------+-----------+---------+---------------------------+---------------------------------------------------+----------------------+---------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/certified-operators | 0/0/0/1              | App-openshift-marketplace/certified-operators-7hbwj/registry-server | 
+--------+----------+-----------+---------+---------------------------+---------------------------------------------------+----------------------+---------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/community-operators | 0/0/0/1              | App-openshift-marketplace/community-operators-lk6qp/registry-server | 
+--------+----------+-----------+---------+---------------------------+---------------------------------------------------+----------------------+---------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-marketplace  | 0/0/0/1              | App-openshift-marketplace/redhat-marketplace-7ft9l/registry-server  | 
+--------+----------+-----------+---------+---------------------------+---------------------------------------------------+----------------------+---------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-operators    | 0/0/0/1              | App-openshift-marketplace/redhat-operators-zfmpd/registry-server    | 
+--------+----------+-----------+---------+---------------------------+---------------------------------------------------+----------------------+---------------------------------------------------------------------+
```
