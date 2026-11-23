# OVNKubernetes BGP - Disable Route Advertisement

## Input

```
[
    {
        "ovn-bgp": {
            "ra": {}
        }
    }
]
```

Notes:
- `ra` triggers [workflow execution](./ra_disable.md)

## Example

```
# iserver delete ocp task --cluster bm1 --file C:\tmp\task.json 


OpenShift Workflow - OVNKubernetes - Disable frr-k8s route advertisement
========================================================================

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
|    |                  |               |                           |                      | route advertisement             | 
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+

Replace Network
---------------
- name: cluster

~~~
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
  resourceVersion: '1193936'
spec:
  additionalRoutingCapabilities:
    providers:
    - FRR
  clusterNetwork:
  - cidr: 10.244.0.0/14
    hostPrefix: 23
  defaultNetwork:
    ovnKubernetesConfig:
      egressIPConfig: {}
      gatewayConfig:
        ipv4: {}
        ipv6: {}
        routingViaHost: false
      genevePort: 6081
      ipsecConfig:
        mode: Disabled
      mtu: 1400
      policyAuditConfig:
        destination: 'null'
        maxFileSize: 50
        maxLogFiles: 5
        rateLimit: 20
        syslogFacility: local0
    type: OVNKubernetes
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
Network [cluster] replaced
- wait for Network cluster [timeout:120s] with {"Progressing_status": "True"}
- wait for Network cluster [timeout:360s] with {"Progressing_status": "False"}
- wait for no Pod openshift-ovn-kubernetes/ovnkube-control-plane-79745db5fb-5tn7w [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-control-plane-79745db5fb-s6vkz [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-node-bj6d6 [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-node-g2sg7 [timeout:120s]
- wait for no Pod openshift-ovn-kubernetes/ovnkube-node-wsrkc [timeout:120s]
Wait for deployment openshift-ovn-kubernetes/ovnkube-control-plane ready (optional: False, allow zero replicas: False, timout: 180s)...
Wait for daemonset ready (optional: False, timout: 180s)...

Completed tasks
- OVN frr-k8s route advertisement disabled
```

[[Back]](./README.md)