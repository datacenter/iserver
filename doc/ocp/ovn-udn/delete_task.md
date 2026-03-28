# UDN w/L3 Topology - Delete Task

[[Back]](./README.md)

## Goal

- namespaces: island-p
- single udn primary network w/l3 topology
- single udn secondary network w/l3 topology
- 2x netshoot pods connecting to both udn, deployed on different nodes
- 1x nginx pod connected to primary udn only
- 2x c8kv vms to both udns, no connection to pod cidr, deployed on different nodes

## Input

```
[
    {
        "k8s": {
            "description": "udn setup",
            "items": [
                {
                    "__type__": "namespace",
                    "namespace": "island-q",
                    "ovn-udn": true,
                    "ovn-multicast": true
                },
                {
                    "__type__": "ovn-udn",
                    "namespace": "island-q",
                    "name": "pl3",
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
                    "__type__": "ovn-udn",
                    "namespace": "island-q",
                    "name": "sl3",
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
            "description": "udn pods",
            "items": [
                {
                    "__type__": "pod",
                    "namespace": "island-q",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "sl3"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-q",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "sl3"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-q",
                    "name": "nginx3",
                    "node": "bm1-3",
                    "app": "nginx",
                    "udn-port": [
                        "tcp/8080"
                    ],
                    "label": {
                        "app": "nginx3"
                    }
                },
                {
                    "__type__": "service",
                    "namespace": "island-q",
                    "name": "nginx3",
                    "type": "NodePort",
                    "port": [
                        {
                            "port": 80,
                            "protocol": "TCP",
                            "targetPort": 8080
                        }
                    ],
                    "selector": {
                        "app": "nginx3"
                    }
                },
                {
                    "__type__": "pod",
                    "namespace": "default",
                    "name": "tool",
                    "app": "netshoot"
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "__variables__": {
                "NAME": "c8kv1",
                "NODE": "bm1-1"
            },
            "namespace": "island-q",
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
                            "type": "udn-l2-primary"
                        },
                        {
                            "name": "net1",
                            "type": "bridge",
                            "nad": "sl3"
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
                "NAME": "c8kv2",
                "NODE": "bm1-2"
            },
            "namespace": "island-q",
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
                            "type": "udn-l2-primary"
                        },
                        {
                            "name": "net1",
                            "type": "bridge",
                            "nad": "sl3"
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
- namespace: island-q
- name: c8kv2-ssh
- wait for no service

Completed tasks
- service deleted

Kubernetes Workflow - Virtual Machine - Delete
==============================================

OpenShift Cluster: bm1

Stop Virtual Machine
--------------------
- namespace: island-q
- name: c8kv2
- state: Running
- runStrategy: Always
- vmi found <=> vm currently running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv2
  namespace: island-q
spec:
  runStrategy: Halted

~~~

Virtual machine patched
Wait for virtual machine down
Wait for no virtual machine instance

Delete Virtual Machine
----------------------
- namespace: island-q
- name: c8kv2
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
- namespace: island-q
- name: c8kv2-day0
- wait for no config map

Completed tasks
- config map deleted

OpenShift Workflow - Service - Delete
=====================================

OpenShift Cluster: bm1

Delete Service
--------------
- namespace: island-q
- name: c8kv1-ssh
- wait for no service

Completed tasks
- service deleted

Kubernetes Workflow - Virtual Machine - Delete
==============================================

OpenShift Cluster: bm1

Stop Virtual Machine
--------------------
- namespace: island-q
- name: c8kv1
- state: Running
- runStrategy: Always
- vmi found <=> vm currently running

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-q
spec:
  runStrategy: Halted

~~~

Virtual machine patched
Wait for virtual machine down
Wait for no virtual machine instance

Delete Virtual Machine
----------------------
- namespace: island-q
- name: c8kv1
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
- namespace: island-q
- name: c8kv1-day0
- wait for no config map

Completed tasks
- config map deleted

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: default
- name: tool
- wait for no pod

OpenShift Workflow - Service - Delete
=====================================

OpenShift Cluster: bm1

Delete Service
--------------
- namespace: island-q
- name: nginx3
- wait for no service

Completed tasks
- service deleted

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-q
- name: nginx3
- wait for no pod

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-q
- name: p1-2
- wait for no pod

OpenShift Workflow - Pod - Delete
=================================

OpenShift Cluster: bm1

Delete Pod
----------
- namespace: island-q
- name: p1-1
- wait for no pod

Kubernetes Workflow - OVN User Defined Network - Delete
=======================================================

OpenShift Cluster: bm1

Delete UserDefinedNetwork
-------------------------
- namespace: island-q
- name: sl3
- deleted
- wait for no UserDefinedNetwork island-q/sl3 [timeout:60s]

Completed tasks
- ovn user defined network deleted

Kubernetes Workflow - OVN User Defined Network - Delete
=======================================================

OpenShift Cluster: bm1

Delete UserDefinedNetwork
-------------------------
- namespace: island-q
- name: pl3
- deleted
- wait for no UserDefinedNetwork island-q/pl3 [timeout:60s]

Completed tasks
- ovn user defined network deleted

Kubernetes Workflow - Namespace - Delete
========================================

OpenShift Cluster: bm1

Delete Namespace
----------------
- name: island-q

Namespace [island-q] resources
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

[[Back]](./README.md)