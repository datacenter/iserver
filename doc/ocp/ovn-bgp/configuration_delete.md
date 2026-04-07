# OVNKubernetes BGP - Delete configuration

[[Back]](./README.md)

```
# iserver delete ocp ovn-bgp --mode config --config another-session      

OpenShift Workflow - OVNKubernetes - Delete frr configuration
=============================================================

OpenShift Cluster: bm1

Delete FRRConfiguration
-----------------------
- namespace: openshift-frr-k8s
- name: another-session
- deleted
- wait for no FRRConfiguration openshift-frr-k8s/another-session [timeout:60s]

Completed tasks
- OVN frr configuration deleted
```

[[Back]](./README.md)