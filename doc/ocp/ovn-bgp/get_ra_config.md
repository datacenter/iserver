# OVNKubernetes BGP - Get route advertisement configuration object with generated frr configs

[[Back]](./README.md)

```
# iserver get ocp ovn-bgp --cluster bm1 -v ra-config

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-----------+----------+------------------------------------------------------------+------------------------------------------------+
| ID | Route Adv | Accepted | Config                                                     | FRR                                            |
+----+-----------+----------+------------------------------------------------------------+------------------------------------------------+
| 1  | cudn      | V        | {                                                          | {                                              | 
|    |           |          |   "advertisements": [                                      |   "test @bm1-1": {                             | 
|    |           |          |     "PodNetwork"                                           |     "bgp": {                                   | 
|    |           |          |   ],                                                       |       "routers": [                             | 
|    |           |          |   "frrConfigurationSelector": {                            |         {                                      | 
|    |           |          |     "matchLabels": {                                       |           "asn": 64667,                        | 
|    |           |          |       "fabric": "nxos"                                     |           "imports": [                         | 
|    |           |          |     }                                                      |             {                                  | 
|    |           |          |   },                                                       |               "vrf": "tenant-blue"             | 
|    |           |          |   "networkSelectors": [                                    |             },                                 | 
|    |           |          |     {                                                      |             {                                  | 
|    |           |          |       "clusterUserDefinedNetworkSelector": {               |               "vrf": "tenant-red"              | 
|    |           |          |         "networkSelector": {                               |             }                                  | 
|    |           |          |           "matchLabels": {                                 |           ],                                   | 
|    |           |          |             "bgp": "enabled"                               |           "neighbors": [                       | 
|    |           |          |           }                                                |             {                                  | 
|    |           |          |         }                                                  |               "address": "6.6.6.6",            | 
|    |           |          |       },                                                   |               "asn": 64701,                    | 
|    |           |          |       "networkSelectionType": "ClusterUserDefinedNetworks" |               "disableMP": true,               | 
|    |           |          |     }                                                      |               "dualStackAddressFamily": false, | 
|    |           |          |   ],                                                       |               "ebgpMultiHop": true,            | 
|    |           |          |   "nodeSelector": {}                                       |               "passwordSecret": {},            | 
|    |           |          | }                                                          |               "toAdvertise": {                 | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered",          | 
|    |           |          |                                                            |                   "prefixes": [                | 
|    |           |          |                                                            |                     "69.69.100.16/28",         | 
|    |           |          |                                                            |                     "69.69.200.0/28"           | 
|    |           |          |                                                            |                   ]                            | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               },                               | 
|    |           |          |                                                            |               "toReceive": {                   | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered"           | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               }                                | 
|    |           |          |                                                            |             },                                 | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "address": "6.6.6.7",            | 
|    |           |          |                                                            |               "asn": 64701,                    | 
|    |           |          |                                                            |               "disableMP": true,               | 
|    |           |          |                                                            |               "dualStackAddressFamily": false, | 
|    |           |          |                                                            |               "ebgpMultiHop": true,            | 
|    |           |          |                                                            |               "passwordSecret": {},            | 
|    |           |          |                                                            |               "toAdvertise": {                 | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered",          | 
|    |           |          |                                                            |                   "prefixes": [                | 
|    |           |          |                                                            |                     "69.69.100.16/28",         | 
|    |           |          |                                                            |                     "69.69.200.0/28"           | 
|    |           |          |                                                            |                   ]                            | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               },                               | 
|    |           |          |                                                            |               "toReceive": {                   | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered"           | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               }                                | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "prefixes": [                        | 
|    |           |          |                                                            |             "69.69.100.16/28",                 | 
|    |           |          |                                                            |             "69.69.200.0/28"                   | 
|    |           |          |                                                            |           ]                                    | 
|    |           |          |                                                            |         },                                     | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "default"                 | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "vrf": "tenant-blue"                 | 
|    |           |          |                                                            |         },                                     | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "default"                 | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "vrf": "tenant-red"                  | 
|    |           |          |                                                            |         }                                      | 
|    |           |          |                                                            |       ]                                        | 
|    |           |          |                                                            |     },                                         | 
|    |           |          |                                                            |     "nodeSelector": {                          | 
|    |           |          |                                                            |       "matchLabels": {                         | 
|    |           |          |                                                            |         "kubernetes.io/hostname": "bm1-1"      | 
|    |           |          |                                                            |       }                                        | 
|    |           |          |                                                            |     },                                         | 
|    |           |          |                                                            |     "raw": {}                                  | 
|    |           |          |                                                            |   },                                           | 
|    |           |          |                                                            |   "test @bm1-2": {                             | 
|    |           |          |                                                            |     "bgp": {                                   | 
|    |           |          |                                                            |       "routers": [                             | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "tenant-blue"             | 
|    |           |          |                                                            |             },                                 | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "tenant-red"              | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "neighbors": [                       | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "address": "6.6.6.6",            | 
|    |           |          |                                                            |               "asn": 64701,                    | 
|    |           |          |                                                            |               "disableMP": true,               | 
|    |           |          |                                                            |               "dualStackAddressFamily": false, | 
|    |           |          |                                                            |               "ebgpMultiHop": true,            | 
|    |           |          |                                                            |               "passwordSecret": {},            | 
|    |           |          |                                                            |               "toAdvertise": {                 | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered",          | 
|    |           |          |                                                            |                   "prefixes": [                | 
|    |           |          |                                                            |                     "69.69.100.32/28",         | 
|    |           |          |                                                            |                     "69.69.200.16/28"          | 
|    |           |          |                                                            |                   ]                            | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               },                               | 
|    |           |          |                                                            |               "toReceive": {                   | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered"           | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               }                                | 
|    |           |          |                                                            |             },                                 | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "address": "6.6.6.7",            | 
|    |           |          |                                                            |               "asn": 64701,                    | 
|    |           |          |                                                            |               "disableMP": true,               | 
|    |           |          |                                                            |               "dualStackAddressFamily": false, | 
|    |           |          |                                                            |               "ebgpMultiHop": true,            | 
|    |           |          |                                                            |               "passwordSecret": {},            | 
|    |           |          |                                                            |               "toAdvertise": {                 | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered",          | 
|    |           |          |                                                            |                   "prefixes": [                | 
|    |           |          |                                                            |                     "69.69.100.32/28",         | 
|    |           |          |                                                            |                     "69.69.200.16/28"          | 
|    |           |          |                                                            |                   ]                            | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               },                               | 
|    |           |          |                                                            |               "toReceive": {                   | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered"           | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               }                                | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "prefixes": [                        | 
|    |           |          |                                                            |             "69.69.100.32/28",                 | 
|    |           |          |                                                            |             "69.69.200.16/28"                  | 
|    |           |          |                                                            |           ]                                    | 
|    |           |          |                                                            |         },                                     | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "default"                 | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "vrf": "tenant-blue"                 | 
|    |           |          |                                                            |         },                                     | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "default"                 | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "vrf": "tenant-red"                  | 
|    |           |          |                                                            |         }                                      | 
|    |           |          |                                                            |       ]                                        | 
|    |           |          |                                                            |     },                                         | 
|    |           |          |                                                            |     "nodeSelector": {                          | 
|    |           |          |                                                            |       "matchLabels": {                         | 
|    |           |          |                                                            |         "kubernetes.io/hostname": "bm1-2"      | 
|    |           |          |                                                            |       }                                        | 
|    |           |          |                                                            |     },                                         | 
|    |           |          |                                                            |     "raw": {}                                  | 
|    |           |          |                                                            |   },                                           | 
|    |           |          |                                                            |   "test @bm1-3": {                             | 
|    |           |          |                                                            |     "bgp": {                                   | 
|    |           |          |                                                            |       "routers": [                             | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "tenant-blue"             | 
|    |           |          |                                                            |             },                                 | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "tenant-red"              | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "neighbors": [                       | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "address": "6.6.6.6",            | 
|    |           |          |                                                            |               "asn": 64701,                    | 
|    |           |          |                                                            |               "disableMP": true,               | 
|    |           |          |                                                            |               "dualStackAddressFamily": false, | 
|    |           |          |                                                            |               "ebgpMultiHop": true,            | 
|    |           |          |                                                            |               "passwordSecret": {},            | 
|    |           |          |                                                            |               "toAdvertise": {                 | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered",          | 
|    |           |          |                                                            |                   "prefixes": [                | 
|    |           |          |                                                            |                     "69.69.100.0/28",          | 
|    |           |          |                                                            |                     "69.69.200.32/28"          | 
|    |           |          |                                                            |                   ]                            | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               },                               | 
|    |           |          |                                                            |               "toReceive": {                   | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered"           | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               }                                | 
|    |           |          |                                                            |             },                                 | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "address": "6.6.6.7",            | 
|    |           |          |                                                            |               "asn": 64701,                    | 
|    |           |          |                                                            |               "disableMP": true,               | 
|    |           |          |                                                            |               "dualStackAddressFamily": false, | 
|    |           |          |                                                            |               "ebgpMultiHop": true,            | 
|    |           |          |                                                            |               "passwordSecret": {},            | 
|    |           |          |                                                            |               "toAdvertise": {                 | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered",          | 
|    |           |          |                                                            |                   "prefixes": [                | 
|    |           |          |                                                            |                     "69.69.100.0/28",          | 
|    |           |          |                                                            |                     "69.69.200.32/28"          | 
|    |           |          |                                                            |                   ]                            | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               },                               | 
|    |           |          |                                                            |               "toReceive": {                   | 
|    |           |          |                                                            |                 "allowed": {                   | 
|    |           |          |                                                            |                   "mode": "filtered"           | 
|    |           |          |                                                            |                 }                              | 
|    |           |          |                                                            |               }                                | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "prefixes": [                        | 
|    |           |          |                                                            |             "69.69.100.0/28",                  | 
|    |           |          |                                                            |             "69.69.200.32/28"                  | 
|    |           |          |                                                            |           ]                                    | 
|    |           |          |                                                            |         },                                     | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "default"                 | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "vrf": "tenant-blue"                 | 
|    |           |          |                                                            |         },                                     | 
|    |           |          |                                                            |         {                                      | 
|    |           |          |                                                            |           "asn": 64667,                        | 
|    |           |          |                                                            |           "imports": [                         | 
|    |           |          |                                                            |             {                                  | 
|    |           |          |                                                            |               "vrf": "default"                 | 
|    |           |          |                                                            |             }                                  | 
|    |           |          |                                                            |           ],                                   | 
|    |           |          |                                                            |           "vrf": "tenant-red"                  | 
|    |           |          |                                                            |         }                                      | 
|    |           |          |                                                            |       ]                                        | 
|    |           |          |                                                            |     },                                         | 
|    |           |          |                                                            |     "nodeSelector": {                          | 
|    |           |          |                                                            |       "matchLabels": {                         | 
|    |           |          |                                                            |         "kubernetes.io/hostname": "bm1-3"      | 
|    |           |          |                                                            |       }                                        | 
|    |           |          |                                                            |     },                                         | 
|    |           |          |                                                            |     "raw": {}                                  | 
|    |           |          |                                                            |   }                                            | 
|    |           |          |                                                            | }                                              | 
+----+-----------+----------+------------------------------------------------------------+------------------------------------------------+

View: state (def), cli, config, exec, frr, ra, ra-config, session, all
```

[[Back]](./README.md)