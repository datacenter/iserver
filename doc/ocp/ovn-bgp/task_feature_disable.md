# OVNKubernetes BGP - Disable

## Input

```
[
    {
        "ovn-bgp": {
            "feature": {}
        }
    }
]
```

Notes:
- `feature` triggers [workflow execution](./feature_disable.md)

## Example

```
# iserver delete ocp task --cluster bm1 --file C:\tmp\task.json 

OpenShift Workflow - OVNKubernetes - Disable frr-k8s
====================================================

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

Replace Network
---------------
- name: cluster

~~~
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
  resourceVersion: '1188270'
spec:
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
- wait for no Pod openshift-frr-k8s/frr-k8s-dlp9f [timeout:120s]
- wait for no Pod openshift-frr-k8s/frr-k8s-m8l44 [timeout:120s]
- wait for no Pod openshift-frr-k8s/frr-k8s-nkc5m [timeout:120s]
- wait for no Pod openshift-frr-k8s/frr-k8s-statuscleaner-6c46867584-wb54f [timeout:120s]

Namespace [openshift-frr-k8s] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: openshift-frr-k8s
- wait for no namespace

Completed tasks
- OVN frr-k8s disabled
```

[[Back]](./README.md)