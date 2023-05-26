# Intersight Workload Optimizer

## Multiple filtering rules

```
# iserver get iwo service
    --cluster my-k8s
    --critical
    --app registry-server
    --name redhat

Summary
-------
- Active   : 2/2
- Severity : 2/0/0/0
- Current  : 2/2


+--------+----------+-----------+---------+---------------------------+--------------------------------------------------+----------------------+--------------------------------------------------------------------+
| State  | Severity | Staleness | Actions | Cluster                   | Service Name                                     | Application Severity | Application                                                        |
+--------+----------+-----------+---------+---------------------------+--------------------------------------------------+----------------------+--------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-marketplace | 0/0/0/1              | App-openshift-marketplace/redhat-marketplace-7ft9l/registry-server | 
+--------+----------+-----------+---------+---------------------------+--------------------------------------------------+----------------------+--------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-operators   | 0/0/0/1              | App-openshift-marketplace/redhat-operators-zfmpd/registry-server   | 
+--------+----------+-----------+---------+---------------------------+--------------------------------------------------+----------------------+--------------------------------------------------------------------+
```
