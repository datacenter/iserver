# OVNKubernetes BGP - Get route advertisement configuration object

[[Back]](./README.md)

```
# iserver get ocp ovn-bgp --cluster bm1 -v ra

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-----------+----------+------------------------------------------------------------+
| ID | Route Adv | Accepted | Config                                                     |
+----+-----------+----------+------------------------------------------------------------+
| 1  | cudn      | V        | {                                                          |
|    |           |          |   "advertisements": [                                      |
|    |           |          |     "PodNetwork"                                           |
|    |           |          |   ],                                                       |
|    |           |          |   "frrConfigurationSelector": {                            |
|    |           |          |     "matchLabels": {                                       |
|    |           |          |       "fabric": "nxos"                                     |
|    |           |          |     }                                                      |
|    |           |          |   },                                                       |
|    |           |          |   "networkSelectors": [                                    |
|    |           |          |     {                                                      |
|    |           |          |       "clusterUserDefinedNetworkSelector": {               |
|    |           |          |         "networkSelector": {                               | 
|    |           |          |           "matchLabels": {                                 |
|    |           |          |             "bgp": "enabled"                               |
|    |           |          |           }                                                |
|    |           |          |         }                                                  |
|    |           |          |       },                                                   |
|    |           |          |       "networkSelectionType": "ClusterUserDefinedNetworks" |
|    |           |          |     }                                                      | 
|    |           |          |   ],                                                       |
|    |           |          |   "nodeSelector": {}                                       |
|    |           |          | }                                                          |
+----+-----------+----------+------------------------------------------------------------+
```

[[Back]](./README.md)