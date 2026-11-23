# CUDN - Delete Task

[[Back]](./overview.md)

## Goal

- two namespaces: island-v1 and island-v2
- single cudn primary network w/l2 topology across two namespaces
- single cudn secondary network w/l2 topology across two namespaces
- 2x netshoot pods per namespace connecting to both cudn
- 2x c8kv vms per namespace connecting to both cuds, no connection to pod cidr 

## Input

```
[
    {
        "k8s": {
            "__enabled__": true,
            "description": "namespaces",
            "items": [
                {
                    "__type__": "namespace",
                    "namespace": "island-w1",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "w"
                    }
                },
                {
                    "__type__": "namespace",
                    "namespace": "island-w2",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "w"
                    }
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "description": "cudn",
            "items": [
                {
                    "__type__": "ovn-cudn",
                    "namespace": {
                        "label": [
                            "tenant:w"
                        ]
                    },
                    "name": "wpl3",
                    "primary": true,
                    "topology": "l3",
                    "subnets": [
                        {
                            "cidr": "66.66.0.0/24",
                            "host": 28
                        }
                    ]
                },
                {
                    "__type__": "ovn-cudn",
                    "namespace": {
                        "label": [
                            "tenant:w"
                        ]
                    },
                    "name": "wsl3",
                    "topology": "l3",
                    "subnets": [
                        {
                            "cidr": "66.66.1.0/24",
                            "host": 28
                        }
                    ]
                }
            ]
        }
    },
    {
        "k8s": {
            "description": "pod",
            "items": [
                {
                    "__type__": "pod",
                    "namespace": "island-w1",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "wsl3"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-w1",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "wsl3"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-w2",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "wsl3"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-w2",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "wsl3"
                    ]
                }

            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "__variables__": {
                "NAME": "c8kw1",
                "NODE": "bm1-1"
            },
            "namespace": "island-w1",
            "items": [
                {
                    "__type__": "config-map",
                    "name": "${NAME}-day0",
                    "content": {
                        "iosxe_config.txt": {
                            "file": "C:\\tmp\\c8kv-2intf-dhcp.txt",
                            "vars": {
                                "HOSTNAME": "${NAME}",
                                "DOMAIN": "domain.com",
                                "USERNAME": "admin",
                                "PASSWORD": "password"
                            }
                        }
                    }
                },
                {
                    "__type__": "virtual-machine",
                    "name": "${NAME}",
                    "template": "c8kv",
                    "url": "http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2",
                    "pvc": "default/c8kv-17.06.05",
                    "day0": "${NAME}-day0",
                    "interface": [
                        {
                            "name": "default",
                            "type": "udn-l3-primary"
                        },
                        {
                            "name": "net1",
                            "type": "bridge",
                            "nad": "wsl3"
                        }
                    ],
                    "node": "${NODE}",
                    "stop-on-delete": true,
                    "sleep-on-delete": 60
                },
                {
                    "__type__": "service",
                    "name": "${NAME}-ssh",
                    "type": "NodePort",
                    "port": [
                        {
                            "port": 22,
                            "protocol": "TCP",
                            "targetPort": 22
                        }
                    ],
                    "selector": {
                        "app": "${NAME}"
                    }
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "__variables__": {
                "NAME": "c8kw2",
                "NODE": "bm1-2"
            },
            "namespace": "island-w2",
            "items": [
                {
                    "__type__": "config-map",
                    "name": "${NAME}-day0",
                    "content": {
                        "iosxe_config.txt": {
                            "file": "C:\\tmp\\c8kv-2intf-dhcp.txt",
                            "vars": {
                                "HOSTNAME": "${NAME}",
                                "DOMAIN": "domain.com",
                                "USERNAME": "admin",
                                "PASSWORD": "password"
                            }
                        }
                    }
                },
                {
                    "__type__": "virtual-machine",
                    "name": "${NAME}",
                    "template": "c8kv",
                    "url": "http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2",
                    "pvc": "default/c8kv-17.06.05",
                    "day0": "${NAME}-day0",
                    "interface": [
                        {
                            "name": "default",
                            "type": "udn-l3-primary"
                        },
                        {
                            "name": "net1",
                            "type": "bridge",
                            "nad": "wsl3"
                        }
                    ],
                    "node": "${NODE}",
                    "stop-on-delete": true,
                    "sleep-on-delete": 60
                },
                {
                    "__type__": "service",
                    "name": "${NAME}-ssh",
                    "type": "NodePort",
                    "port": [
                        {
                            "port": 22,
                            "protocol": "TCP",
                            "targetPort": 22
                        }
                    ],
                    "selector": {
                        "app": "${NAME}"
                    }
                }
            ]
        }
    }
]
```

## Outcome

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm


OpenShift Workflow - Service - Delete
=====================================

OpenShift Cluster: bm1

Delete Service
--------------
- namespace: island-w2
- name: c8kw2-ssh
- wait for no service

Completed tasks
- service deleted

Kubernetes Workflow - Virtual Machine - Delete
==============================================

OpenShift Cluster: bm1

Stop Virtual Machine
--------------------
- namespace: island-w2
- name: c8kw2
- state: Running
- runStrategy: Always
- vmi found <=> vm currently running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kw2
  namespace: island-w2
spec:
  runStrategy: Halted

~~~

Virtual machine patched
Wait for virtual machine down
Wait for no virtual machine instance

Delete Virtual Machine
----------------------
- namespace: island-w2
- name: c8kw2
- state: Stopped
- vmi not found <=> vm stopped

Virtual machine deleted
Wait for virtual machine gone

Sleep on delete for 60 seconds

Completed tasks
- virtual machine deleted

Kubernetes Workflow - Config Map - Delete
=========================================

OpenShift Cluster: bm1

Delete Config Map
-----------------
- namespace: island-w2
- name: c8kw2-day0
- wait for no config map

Completed tasks
- config map deleted

OpenShift Workflow - Service - Delete
=====================================

OpenShift Cluster: bm1

Delete Service
--------------
- namespace: island-w1
- name: c8kw1-ssh
- wait for no service

Completed tasks
- service deleted

Kubernetes Workflow - Virtual Machine - Delete
==============================================

OpenShift Cluster: bm1

Stop Virtual Machine
--------------------
- namespace: island-w1
- name: c8kw1
- state: Running
- runStrategy: Always
- vmi found <=> vm currently running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kw1
  namespace: island-w1
spec:
  runStrategy: Halted

~~~

Virtual machine patched
Wait for virtual machine down
Wait for no virtual machine instance

Delete Virtual Machine
----------------------
- namespace: island-w1
- name: c8kw1
- state: Stopped
- vmi not found <=> vm stopped

Virtual machine deleted
Wait for virtual machine gone

Sleep on delete for 60 seconds

Completed tasks
- virtual machine deleted

Kubernetes Workflow - Config Map - Delete
=========================================

OpenShift Cluster: bm1

Delete Config Map
-----------------
- namespace: island-w1
- name: c8kw1-day0
- wait for no config map

Completed tasks
- config map deleted

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-w2
- name: p1-2
- wait for no pod

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-w2
- name: p1-1
- wait for no pod

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-w1
- name: p1-2
- wait for no pod

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-w1
- name: p1-1
- wait for no pod

Kubernetes Workflow - OVN Cluster User Defined Network - Delete
===============================================================

OpenShift Cluster: bm1

Delete ClusterUserDefinedNetwork
--------------------------------
- name: wsl3
- deleted
- wait for no ClusterUserDefinedNetwork wsl3 [timeout:60s]

Completed tasks
- ovn cluster user defined network deleted

Kubernetes Workflow - OVN Cluster User Defined Network - Delete
===============================================================

OpenShift Cluster: bm1

Delete ClusterUserDefinedNetwork
--------------------------------
- name: wpl3
- deleted
- wait for no ClusterUserDefinedNetwork wpl3 [timeout:60s]

Completed tasks
- ovn cluster user defined network deleted

Kubernetes Workflow - Namespace - Delete
========================================

OpenShift Cluster: bm1

Delete Namespace
----------------
- name: island-w2

Namespace [island-w2] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks
- wait for no namespace

Completed tasks
- namespace deleted

Kubernetes Workflow - Namespace - Delete
========================================

OpenShift Cluster: bm1

Delete Namespace
----------------
- name: island-w1

Namespace [island-w1] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks
- wait for no namespace

Completed tasks
- namespace deleted
```

[[Back]](./overview.md)