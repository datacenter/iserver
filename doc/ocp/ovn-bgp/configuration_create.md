# OVNKubernetes BGP - Add configuration

[[Back]](./README.md)

```
# iserver set ocp ovn-bgp --cluster bm1 --mode config --config .\tasks\bgp\config1.yaml

OpenShift Workflow - OVNKubernetes - Create frr configuration
=============================================================

OpenShift Cluster: bm1

Create FRRConfiguration
-----------------------
- namespace: openshift-frr-k8s
- name: another-session

~~~
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  labels:
    fabric: nxos
  name: another-session
  namespace: openshift-frr-k8s
spec:
  bgp:
    routers:
    - asn: 64667
      neighbors:
      - address: 8.8.8.8
        asn: 64668

~~~
Continue [Y/N]? y
FRRConfiguration [openshift-frr-k8s/another-session] created
- wait for FRRConfiguration openshift-frr-k8s/another-session [timeout:60s]

Completed tasks
- OVN frr configuration created
```

[[Back]](./README.md)