# OVNKubernetes BGP - Enable

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
- `feature` triggers [workflow execution](./feature_enable.md)

## Example

```
# iserver set ocp task --cluster bm1 --file C:\tmp\task.json 

Cluster: bm1 (type: ocp)

OpenShift Workflow - OVNKubernetes - Enable frr-k8s
===================================================

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
Network [cluster] patched
- wait for Network cluster [timeout:120s] with {"Progressing_status": "True"}
- wait for Network cluster [timeout:360s] with {"Progressing_status": "False"}

Completed tasks
- OVN frr-k8s enabled
```

[[Back]](./README.md)