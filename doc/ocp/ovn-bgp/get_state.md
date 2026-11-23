# OVNKubernetes BGP - Get state summary

[[Back]](./README.md)

```
# iserver get ocp ovn-bgp --cluster bm1 -v state
get ocp ovn-bgp 

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+------------------+---------------+---------------------------+----------------------+---------------------------------+
| ID | Network Operator | CNI           | Condition                 | CIDR                 | Settings                        |
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+
| 1  | cluster 4.21.4   | OVNKubernetes | V Available               | Pod 10.128.0.0/14/23 | deployKubeProxy:False           |
|    |                  |               | X Degraded                | Svc 172.30.0.0/16    | disableMultiNetwork:False       |
|    |                  |               | X ManagementStateDegraded |                      | disableNetworkDiagnostics:False |
|    |                  |               | X Progressing             |                      | logLevel:Normal                 |
|    |                  |               | V Upgradeable             |                      | managementState:Managed         |
|    |                  |               |                           |                      | operatorLogLevel:Normal         |
|    |                  |               |                           |                      | ---                             |
|    |                  |               |                           |                      | frr-k8s                         |
|    |                  |               |                           |                      | route advertisement             | 
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+

Feature
- frr-k8s:  enabled
- route advertisement: enabled
Configuration
- frr: 4 incl. 3 ra-generated
- route advertisement: 1/1
- node bm1-1: converted, reloaded
- node bm1-2: converted, reloaded
- node bm1-3: converted, reloaded
BGP sessions
- configured nodes: 3/3
- bm1-1: 2/2
- bm1-2: 2/2
- bm1-3: 2/2

View: state (def), cli, config, exec, frr, ra, ra-config, session, all
```

[[Back]](./README.md)