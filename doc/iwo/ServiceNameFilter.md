# Intersight Workload Optimizer

## Filter by service name

```
# iserver get iwo service --name marketplace

Summary
-------
- Active   : 5/5
- Severity : 5/0/0/0
- Current  : 5/5


+--------+----------+-----------+---------+---------------------------+------------------------------------------------------------+
| State  | Severity | Staleness | Actions | Cluster                   | Service Name                                               |
+--------+----------+-----------+---------+---------------------------+------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/certified-operators          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/community-operators          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/marketplace-operator-metrics | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-marketplace           | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-operators             | 
+--------+----------+-----------+---------+---------------------------+------------------------------------------------------------+
```
