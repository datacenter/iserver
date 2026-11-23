# OVNKubernetes BGP - Add route advertisement

[[Back]](./README.md)

```
# iserver set ocp ovn-bgp --cluster bm1 --mode ra-config --config .\tasks\bgp\cudn.yaml

OpenShift Workflow - OVNKubernetes - Create route advertisement
===============================================================

OpenShift Cluster: bm7

Create RouteAdvertisements
--------------------------
- name: cudn

~~~
apiVersion: k8s.ovn.org/v1
kind: RouteAdvertisements
metadata:
  name: cudn
spec:
  advertisements:
  - PodNetwork
  frrConfigurationSelector:
    matchLabels:
      fabric: nxos
  networkSelectors:
  - clusterUserDefinedNetworkSelector:
      networkSelector:
        matchLabels:
          bgp: enabled
    networkSelectionType: ClusterUserDefinedNetworks
  nodeSelector: {}

~~~
Continue [Y/N]? y
RouteAdvertisements [cudn] created
- wait for RouteAdvertisement cudn [timeout:60s]

Completed tasks
- OVN route advertisement created
```

[[Back]](./README.md)