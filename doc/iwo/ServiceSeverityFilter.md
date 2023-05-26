# Intersight Workload Optimizer

## Filter by severity

```
# iserver get iwo service --critical

Summary
-------
- Active   : 83/83
- Severity : 83/0/0/0
- Current  : 83/83


+--------+----------+-----------+---------+---------------------------+-------------------------------------------------------------------------------------+
| State  | Severity | Staleness | Actions | Cluster                   | Service Name                                                                        |
+--------+----------+-----------+---------+---------------------------+-------------------------------------------------------------------------------------+
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-calico-apiserver/calico-api                                                 | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-calico-system/calico-kube-controllers-metrics                               | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-calico-system/calico-typha                                                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-default/my-twamp                                                            | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-default/my-twamp-insecure                                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-apiserver-operator/metrics                                        | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-apiserver/api                                                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-apiserver/check-endpoints                                         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-authentication-operator/metrics                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-authentication/oauth-openshift                                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cloud-credential-operator/cco-metrics                             | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-csi-drivers/vmware-vsphere-csi-driver-controller-metrics  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-csi-drivers/vmware-vsphere-csi-driver-operator-metrics    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-csi-drivers/vmware-vsphere-csi-driver-webhook-svc         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-machine-approver/machine-approver                         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-node-tuning-operator/node-tuning-operator                 | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-node-tuning-operator/performance-addon-operator-service   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-samples-operator/metrics                                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-storage-operator/cluster-storage-operator-metrics         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-storage-operator/csi-snapshot-controller-operator-metrics | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-storage-operator/csi-snapshot-webhook                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-storage-operator/vsphere-problem-detector-metrics         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-cluster-version/cluster-version-operator                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-config-operator/metrics                                           | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-console-operator/metrics                                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-console/console                                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-console/downloads                                                 | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-controller-manager-operator/metrics                               | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-controller-manager/controller-manager                             | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-dns-operator/metrics                                              | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-dns/dns-default                                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-etcd-operator/metrics                                             | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-etcd/etcd                                                         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-image-registry/image-registry-operator                            | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-ingress-canary/ingress-canary                                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-ingress-operator/metrics                                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-ingress/router-internal-default                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-insights/metrics                                                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-apiserver-operator/metrics                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-apiserver/apiserver                                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-controller-manager-operator/metrics                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-controller-manager/kube-controller-manager                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-proxy/openshift-kube-proxy                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-scheduler-operator/metrics                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-scheduler/scheduler                                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-kube-storage-version-migrator-operator/metrics                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-api/cluster-autoscaler-operator                           | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-api/cluster-baremetal-operator-service                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-api/cluster-baremetal-webhook-service                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-api/machine-api-controllers                               | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-api/machine-api-operator                                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-api/machine-api-operator-webhook                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-config-operator/machine-config-controller                 | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-machine-config-operator/machine-config-daemon                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/certified-operators                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/community-operators                                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/marketplace-operator-metrics                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-marketplace                                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-marketplace/redhat-operators                                      | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/alertmanager-main                                      | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/alertmanager-operated                                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/cluster-monitoring-operator                            | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/kube-state-metrics                                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/node-exporter                                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/openshift-state-metrics                                | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/prometheus-adapter                                     | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/prometheus-k8s                                         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/prometheus-k8s-thanos-sidecar                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/prometheus-operated                                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/prometheus-operator                                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/prometheus-operator-admission-webhook                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/telemeter-client                                       | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-monitoring/thanos-querier                                         | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-multus/multus-admission-controller                                | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-multus/network-metrics-service                                    | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-network-diagnostics/network-check-source                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-network-diagnostics/network-check-target                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-network-operator/metrics                                          | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-oauth-apiserver/api                                               | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-operator-lifecycle-manager/catalog-operator-metrics               | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-operator-lifecycle-manager/olm-operator-metrics                   | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-operator-lifecycle-manager/packageserver-service                  | 
| ACTIVE | Critical | CURRENT   | -       | Kubernetes-my-k8s-cluster | Service-openshift-service-ca-operator/metrics                                       | 
+--------+----------+-----------+---------+---------------------------+-------------------------------------------------------------------------------------+
```
