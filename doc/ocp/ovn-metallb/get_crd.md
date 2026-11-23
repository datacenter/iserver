# MetalLB - Get crds command

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)

```
# iserver get ocp metallb --cluster bm1 -v crd


OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1
Operator metallb-operator found
Metallb instance in l3 mode

+----+-----------------+-------------------------+-------------------------+
| ID | IP Address Pool | Address                 | Status                  |
+----+-----------------+-------------------------+-------------------------+
| 1  | metallb-system  | 69.69.69.1-69.69.69.254 | {                       | 
|    | pool1           |                         |   "assignedIPv4": 1,    | 
|    |                 |                         |   "assignedIPv6": 0,    | 
|    |                 |                         |   "availableIPv4": 253, | 
|    |                 |                         |   "availableIPv6": 0    | 
|    |                 |                         | }                       | 
+----+-----------------+-------------------------+-------------------------+

+----+----------------+------------------------------------+
| ID | BGP Peer       | Spec                               |
+----+----------------+------------------------------------+
| 1  | metallb-system | {                                  | 
|    | leaf1          |   "disableMP": false,              | 
|    |                |   "dualStackAddressFamily": false, | 
|    |                |   "ebgpMultiHop": true,            | 
|    |                |   "myASN": 64667,                  | 
|    |                |   "peerASN": 64600,                | 
|    |                |   "peerAddress": "6.6.6.6",        | 
|    |                |   "peerPort": 179                  | 
|    |                | }                                  | 
+----+----------------+------------------------------------+

+----+----------+------+
| ID | BGP Peer | Spec |
+----+----------+------+
+----+----------+------+

+----+-------------------+------+
| ID | BGP Advertisement | Spec |
+----+-------------------+------+
| 1  | metallb-system    | {}   | 
|    | basic             |      | 
+----+-------------------+------+

+----+-----------+------+
| ID | Community | Spec |
+----+-----------+------+
+----+-----------+------+

+----+-------------------+-----------+----------------------------------------------+
| ID | Config            | Route Adv | Body                                         |
+----+-------------------+-----------+----------------------------------------------+
| 1  | openshift-frr-k8s | ---       | {                                            | 
|    | another-session2  |           |   "bgp": {                                   | 
|    |                   |           |     "routers": [                             | 
|    |                   |           |       {                                      | 
|    |                   |           |         "asn": 64667,                        | 
|    |                   |           |         "neighbors": [                       | 
|    |                   |           |           {                                  | 
|    |                   |           |             "address": "8.8.8.8",            | 
|    |                   |           |             "asn": 64669,                    | 
|    |                   |           |             "disableMP": false,              | 
|    |                   |           |             "dualStackAddressFamily": false  | 
|    |                   |           |           }                                  | 
|    |                   |           |         ]                                    | 
|    |                   |           |       }                                      | 
|    |                   |           |     ]                                        | 
|    |                   |           |   }                                          | 
|    |                   |           | }                                            | 
+----+-------------------+-----------+----------------------------------------------+
| 2  | openshift-frr-k8s | ---       | {                                            | 
|    | metallb-bm1-1     |           |   "bgp": {                                   | 
|    |                   |           |     "routers": [                             | 
|    |                   |           |       {                                      | 
|    |                   |           |         "asn": 64667,                        | 
|    |                   |           |         "neighbors": [                       | 
|    |                   |           |           {                                  | 
|    |                   |           |             "address": "6.6.6.6",            | 
|    |                   |           |             "asn": 64600,                    | 
|    |                   |           |             "disableMP": false,              | 
|    |                   |           |             "dualStackAddressFamily": false, | 
|    |                   |           |             "ebgpMultiHop": true,            | 
|    |                   |           |             "passwordSecret": {},            | 
|    |                   |           |             "port": 179,                     | 
|    |                   |           |             "toAdvertise": {                 | 
|    |                   |           |               "allowed": {                   | 
|    |                   |           |                 "mode": "filtered",          | 
|    |                   |           |                 "prefixes": [                | 
|    |                   |           |                   "69.69.69.1/32"            | 
|    |                   |           |                 ]                            | 
|    |                   |           |               }                              | 
|    |                   |           |             },                               | 
|    |                   |           |             "toReceive": {                   | 
|    |                   |           |               "allowed": {                   | 
|    |                   |           |                 "mode": "filtered"           | 
|    |                   |           |               }                              | 
|    |                   |           |             }                                | 
|    |                   |           |           }                                  | 
|    |                   |           |         ],                                   | 
|    |                   |           |         "prefixes": [                        | 
|    |                   |           |           "69.69.69.1/32"                    | 
|    |                   |           |         ]                                    | 
|    |                   |           |       }                                      | 
|    |                   |           |     ]                                        | 
|    |                   |           |   },                                         | 
|    |                   |           |   "nodeSelector": {                          | 
|    |                   |           |     "matchLabels": {                         | 
|    |                   |           |       "kubernetes.io/hostname": "bm1-1"      | 
|    |                   |           |     }                                        | 
|    |                   |           |   },                                         | 
|    |                   |           |   "raw": {}                                  | 
|    |                   |           | }                                            | 
+----+-------------------+-----------+----------------------------------------------+
| 3  | openshift-frr-k8s | ---       | {                                            | 
|    | metallb-bm1-2     |           |   "bgp": {                                   | 
|    |                   |           |     "routers": [                             | 
|    |                   |           |       {                                      | 
|    |                   |           |         "asn": 64667,                        | 
|    |                   |           |         "neighbors": [                       | 
|    |                   |           |           {                                  | 
|    |                   |           |             "address": "6.6.6.6",            | 
|    |                   |           |             "asn": 64600,                    | 
|    |                   |           |             "disableMP": false,              | 
|    |                   |           |             "dualStackAddressFamily": false, | 
|    |                   |           |             "ebgpMultiHop": true,            | 
|    |                   |           |             "passwordSecret": {},            | 
|    |                   |           |             "port": 179,                     | 
|    |                   |           |             "toAdvertise": {                 | 
|    |                   |           |               "allowed": {                   | 
|    |                   |           |                 "mode": "filtered",          | 
|    |                   |           |                 "prefixes": [                | 
|    |                   |           |                   "69.69.69.1/32"            | 
|    |                   |           |                 ]                            | 
|    |                   |           |               }                              | 
|    |                   |           |             },                               | 
|    |                   |           |             "toReceive": {                   | 
|    |                   |           |               "allowed": {                   | 
|    |                   |           |                 "mode": "filtered"           | 
|    |                   |           |               }                              | 
|    |                   |           |             }                                | 
|    |                   |           |           }                                  | 
|    |                   |           |         ],                                   | 
|    |                   |           |         "prefixes": [                        | 
|    |                   |           |           "69.69.69.1/32"                    | 
|    |                   |           |         ]                                    | 
|    |                   |           |       }                                      | 
|    |                   |           |     ]                                        | 
|    |                   |           |   },                                         | 
|    |                   |           |   "nodeSelector": {                          | 
|    |                   |           |     "matchLabels": {                         | 
|    |                   |           |       "kubernetes.io/hostname": "bm1-2"      | 
|    |                   |           |     }                                        | 
|    |                   |           |   },                                         | 
|    |                   |           |   "raw": {}                                  | 
|    |                   |           | }                                            | 
+----+-------------------+-----------+----------------------------------------------+
| 4  | openshift-frr-k8s | ---       | {                                            | 
|    | metallb-bm1-3     |           |   "bgp": {                                   | 
|    |                   |           |     "routers": [                             | 
|    |                   |           |       {                                      | 
|    |                   |           |         "asn": 64667,                        | 
|    |                   |           |         "neighbors": [                       | 
|    |                   |           |           {                                  | 
|    |                   |           |             "address": "6.6.6.6",            | 
|    |                   |           |             "asn": 64600,                    | 
|    |                   |           |             "disableMP": false,              | 
|    |                   |           |             "dualStackAddressFamily": false, | 
|    |                   |           |             "ebgpMultiHop": true,            | 
|    |                   |           |             "passwordSecret": {},            | 
|    |                   |           |             "port": 179,                     | 
|    |                   |           |             "toAdvertise": {                 | 
|    |                   |           |               "allowed": {                   | 
|    |                   |           |                 "mode": "filtered",          | 
|    |                   |           |                 "prefixes": [                | 
|    |                   |           |                   "69.69.69.1/32"            | 
|    |                   |           |                 ]                            | 
|    |                   |           |               }                              | 
|    |                   |           |             },                               | 
|    |                   |           |             "toReceive": {                   | 
|    |                   |           |               "allowed": {                   | 
|    |                   |           |                 "mode": "filtered"           | 
|    |                   |           |               }                              | 
|    |                   |           |             }                                | 
|    |                   |           |           }                                  | 
|    |                   |           |         ],                                   | 
|    |                   |           |         "prefixes": [                        | 
|    |                   |           |           "69.69.69.1/32"                    | 
|    |                   |           |         ]                                    | 
|    |                   |           |       }                                      | 
|    |                   |           |     ]                                        | 
|    |                   |           |   },                                         | 
|    |                   |           |   "nodeSelector": {                          | 
|    |                   |           |     "matchLabels": {                         | 
|    |                   |           |       "kubernetes.io/hostname": "bm1-3"      | 
|    |                   |           |     }                                        | 
|    |                   |           |   },                                         | 
|    |                   |           |   "raw": {}                                  | 
|    |                   |           | }                                            | 
+----+-------------------+-----------+----------------------------------------------+

View: state (def), cli, crd, exec, frr, all
```

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)