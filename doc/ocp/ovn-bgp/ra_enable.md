# OVNKubernetes BGP - Enable Route Advertisement

[[Back]](./README.md)

## Workflow

- checks
    - ovn-k cni
    - frr-k8s enabled
    - cluster network operator not progressing
- patch cluster network operator spec with route advertisement enabled
- wait for condition progressing:true
- wait for condition progressing:false
- check openshift-ovn-kubernetes resources have been updated

## Output

```
# iserver delete ocp ovn-bgp --cluster bm1 --mode ra

OpenShift Workflow - OVNKubernetes - Enable frr-k8s route advertisement
=======================================================================

OpenShift Cluster: bm1

+----+------------------+---------------+---------------------------+----------------------+---------------------------------+
| ID | Network Operator | CNI           | Condition                 | CIDR                 | Settings                        |
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+
| 1  | cluster 4.21.4   | OVNKubernetes | V Available               | Pod 10.244.0.0/14/23 | deployKubeProxy:False           | 
|    |                  |               | X Degraded                | Svc 172.244.0.0/16   | disableMultiNetwork:False       | 
|    |                  |               | X ManagementStateDegraded |                      | disableNetworkDiagnostics:False | 
|    |                  |               | X Progressing             |                      | logLevel:Normal                 | 
|    |                  |               | V Upgradeable             |                      | managementState:Managed         | 
|    |                  |               |                           |                      | operatorLogLevel:Normal         | 
|    |                  |               |                           |                      | ---                             | 
|    |                  |               |                           |                      | frr-k8s                         | 
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+

Patch Network
-------------
- name: cluster

~~~
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalRoutingCapabilities:
    providers:
    - FRR
  clusterNetwork:
  - cidr: 10.244.0.0/14
    hostPrefix: 23
  defaultNetwork:
    ovnKubernetesConfig:
      routeAdvertisements: Enabled
  deployKubeProxy: false
  disableMultiNetwork: false
  disableNetworkDiagnostics: false
  logLevel: Normal
  managementState: Managed
  operatorLogLevel: Normal
  serviceNetwork:
  - 172.244.0.0/16
  useMultiNetworkPolicy: false

~~~
Network [cluster] patched
- wait for Network cluster [timeout:120s] with {"Progressing_status": "True"}
- wait for Network cluster [timeout:360s] with {"Progressing_status": "False"}
- wait for no Pod openshift-ovn-kubernetes/ovnkube-control-plane-958fd69c7-6djz6 [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-control-plane-958fd69c7-cvxtt [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-node-7mrlm [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-node-dl5np [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-node-lcdv2 [timeout:120s]
Wait for deployment openshift-ovn-kubernetes/ovnkube-control-plane ready (optional: False, allow zero replicas: False, timout: 180s)...
Wait for daemonset ready (optional: False, timout: 180s)...

Completed tasks
- OVN frr-k8s route advertisement enabled
```

[[Back]](./README.md)