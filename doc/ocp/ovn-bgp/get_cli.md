# OVNKubernetes BGP - Get FRR CLI access command

[[Back]](./README.md)

```
# iserver get ocp ovn-bgp --cluster bm1 -v cli

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------------------------+-------+----------------------------------------------------------------+
| ID | Host  | Pod                             | Ready | FRR cli                                                        |
+----+-------+---------------------------------+-------+----------------------------------------------------------------+
| 1  | bm1-1 | openshift-frr-k8s/frr-k8s-9stm4 | 7/7   | oc exec -it -n openshift-frr-k8s frr-k8s-9stm4 -c frr -- vtysh |
| 2  | bm1-2 | openshift-frr-k8s/frr-k8s-gjx7q | 7/7   | oc exec -it -n openshift-frr-k8s frr-k8s-gjx7q -c frr -- vtysh |
| 3  | bm1-3 | openshift-frr-k8s/frr-k8s-tgtgv | 7/7   | oc exec -it -n openshift-frr-k8s frr-k8s-tgtgv -c frr -- vtysh |
+----+-------+---------------------------------+-------+----------------------------------------------------------------+
```

[[Back]](./README.md)