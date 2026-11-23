# CUDN w/Localnet Topology - Task

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./ovs.md)

## Goal

- two namespaces: island-y1 and island-y2
- single cudn primary network across two namespaces
- single cudn secondary network with localnet topology across two namespaces
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
                    "namespace": "island-y1",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "y"
                    }
                },
                {
                    "__type__": "namespace",
                    "namespace": "island-y2",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "y"
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
                            "tenant:y"
                        ]
                    },
                    "name": "ypl2",
                    "primary": true,
                    "topology": "l2",
                    "subnets": ["66.66.0.0/24"]
                },
                {
                    "__type__": "ovn-cudn",
                    "namespace": {
                        "label": [
                            "tenant:y"
                        ]
                    },
                    "name": "ysphy",
                    "topology": "localnet",
                    "phy": "localnet-y",
                    "subnets": ["66.66.1.0/24"]
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
                    "namespace": "island-y1",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "ysphy"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-y1",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "ysphy"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-y2",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "ysphy"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-y2",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "ysphy"
                    ]
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
            "namespace": "island-y1",
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
                            "nad": "ysphy"
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
            "namespace": "island-y2",
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
                            "nad": "ysphy"
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
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

Cluster: bm1 (type: ocp)

Kubernetes Workflow - Namespace - Create
========================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: island-y1

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: y
  name: island-y1

~~~
Namespace [island-y1] created
Wait for namespace [timeout:60]...

Check labels
- tenant:y found
- k8s.ovn.org/primary-user-defined-network: found

Check annotations
- k8s.ovn.org/multicast-enabled:true found

Completed tasks
- namespace created

Kubernetes Workflow - Namespace - Create
========================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: island-y2

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: y
  name: island-y2

~~~
Namespace [island-y2] created
Wait for namespace [timeout:60]...

Check labels
- tenant:y found
- k8s.ovn.org/primary-user-defined-network: found

Check annotations
- k8s.ovn.org/multicast-enabled:true found

Completed tasks
- namespace created

Kubernetes Workflow - OVN Cluster User Defined Network - Create
===============================================================

OpenShift Cluster: bm1

Create ClusterUserDefinedNetwork
--------------------------------
- name: ypl2

~~~
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: ypl2
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-y1
      - island-y2
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.0.0/24
    topology: Layer2

~~~
ClusterUserDefinedNetwork [ypl2] created
- wait for ClusterUserDefinedNetwork ypl2 [timeout:60s]
- wait for ClusterUserDefinedNetwork ypl2 [timeout:60s] with {"created_status": "True"}

+----+------+---+---+-----------+----------+--------------+----------------+----------+
| ID | CUDN | C | P | Namespace | Topology | Subnet       | Net Attach Def | Workload |
+----+------+---+---+-----------+----------+--------------+----------------+----------+
| 1  | ypl2 | V | V | ---       | Layer2   | 66.66.0.0/24 | ---            | ---      | 
+----+------+---+---+-----------+----------+--------------+----------------+----------+

Completed tasks
- ovn cluster user defined network created

Kubernetes Workflow - OVN Cluster User Defined Network - Create
===============================================================

OpenShift Cluster: bm1

Create ClusterUserDefinedNetwork
--------------------------------
- name: ysphy

~~~
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: ysphy
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-y1
      - island-y2
  network:
    localnet:
      physicalNetworkName: localnet-y
      role: Secondary
      subnets:
      - 66.66.1.0/24
    topology: Localnet

~~~
ClusterUserDefinedNetwork [ysphy] created
- wait for ClusterUserDefinedNetwork ysphy [timeout:60s]
- wait for ClusterUserDefinedNetwork ysphy [timeout:60s] with {"created_status": "True"}

+----+-------+---+---+-----------+----------+--------+---------------------------------------------+----------+
| ID | CUDN  | C | P | Namespace | Topology | Subnet | Net Attach Def                              | Workload |
+----+-------+---+---+-----------+----------+--------+---------------------------------------------+----------+
| 1  | ysphy | V |   | island-y1 | Localnet | ---    | {                                           | ---      | 
|    |       |   |   | island-y2 |          |        |   "cniVersion": "1.0.0",                    |          | 
|    |       |   |   |           |          |        |   "mtu": 1500,                              |          | 
|    |       |   |   |           |          |        |   "name": "cluster_udn_ysphy",              |          | 
|    |       |   |   |           |          |        |   "netAttachDefName": "${NAMESPACE}/ysphy", |          | 
|    |       |   |   |           |          |        |   "physicalNetworkName": "localnet-y",      |          | 
|    |       |   |   |           |          |        |   "role": "secondary",                      |          | 
|    |       |   |   |           |          |        |   "subnets": "66.66.1.0/24",                |          | 
|    |       |   |   |           |          |        |   "topology": "localnet",                   |          | 
|    |       |   |   |           |          |        |   "type": "ovn-k8s-cni-overlay"             |          | 
|    |       |   |   |           |          |        | }                                           |          | 
+----+-------+---+---+-----------+----------+--------+---------------------------------------------+----------+

Completed tasks
- ovn cluster user defined network created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-y1
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: ysphy
  name: p1-1
  namespace: island-y1
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      capabilities:
        add:
        - IPC_LOCK
        - SYS_RESOURCE
        - NET_RAW
      runAsUser: 0
  nodeName: bm1-1

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+
| ID | Pod       | Ready | Label   | Annotation         | Node  | IP          | Net | Restart | Age  |
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+
| 1  | island-y1 | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.47 | 3   | 0       | 1h0m | 
|    | p1-1      |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |           |       |         | ContainersReady: V |       |             |     |         |      | 
|    |           |       |         | Ready: V           |       |             |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network         | Def | MAC               | IP          |
+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
| 1  | island-y1 | X       | eth0     | ovn-kubernetes  | X   | 0a:58:0a:80:01:2f | 10.128.1.47 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes  | V   | 0a:58:42:42:00:05 | 66.66.0.5   | 
|    |           |         | net1     | island-y1/ysphy | X   | 0a:58:42:42:01:02 | 66.66.1.2   | 
+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-y1
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: ysphy
  name: p1-2
  namespace: island-y1
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      capabilities:
        add:
        - IPC_LOCK
        - SYS_RESOURCE
        - NET_RAW
      runAsUser: 0
  nodeName: bm1-2

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| ID | Pod       | Ready | Label   | Annotation         | Node  | IP           | Net | Restart | Age  |
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| 1  | island-y1 | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.217 | 3   | 0       | 1h0m | 
|    | p1-2      |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |           |       |         | ContainersReady: V |       |              |     |         |      | 
|    |           |       |         | Ready: V           |       |              |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+-----------+---------+----------+-----------------+-----+-------------------+--------------+
| ID | Pod       | HostNet | Intf     | Network         | Def | MAC               | IP           |
+----+-----------+---------+----------+-----------------+-----+-------------------+--------------+
| 1  | island-y1 | X       | eth0     | ovn-kubernetes  | X   | 0a:58:0a:81:00:d9 | 10.129.0.217 | 
|    | p1-2      |         | ovn-udn1 | ovn-kubernetes  | V   | 0a:58:42:42:00:07 | 66.66.0.7    | 
|    |           |         | net1     | island-y1/ysphy | X   | 0a:58:42:42:01:05 | 66.66.1.5    | 
+----+-----------+---------+----------+-----------------+-----+-------------------+--------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-y2
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: ysphy
  name: p1-1
  namespace: island-y2
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      capabilities:
        add:
        - IPC_LOCK
        - SYS_RESOURCE
        - NET_RAW
      runAsUser: 0
  nodeName: bm1-1

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+
| ID | Pod       | Ready | Label   | Annotation         | Node  | IP          | Net | Restart | Age  |
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+
| 1  | island-y2 | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.48 | 3   | 0       | 1h1m | 
|    | p1-1      |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |           |       |         | ContainersReady: V |       |             |     |         |      | 
|    |           |       |         | Ready: V           |       |             |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network         | Def | MAC               | IP          |
+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
| 1  | island-y2 | X       | eth0     | ovn-kubernetes  | X   | 0a:58:0a:80:01:30 | 10.128.1.48 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes  | V   | 0a:58:42:42:00:0a | 66.66.0.10  | 
|    |           |         | net1     | island-y2/ysphy | X   | 0a:58:42:42:01:07 | 66.66.1.7   | 
+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-y2
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: ysphy
  name: p1-2
  namespace: island-y2
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      capabilities:
        add:
        - IPC_LOCK
        - SYS_RESOURCE
        - NET_RAW
      runAsUser: 0
  nodeName: bm1-2

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| ID | Pod       | Ready | Label   | Annotation         | Node  | IP           | Net | Restart | Age  |
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| 1  | island-y2 | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.218 | 3   | 0       | 1h0m | 
|    | p1-2      |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |           |       |         | ContainersReady: V |       |              |     |         |      | 
|    |           |       |         | Ready: V           |       |              |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+-----------+---------+----------+-----------------+-----+-------------------+--------------+
| ID | Pod       | HostNet | Intf     | Network         | Def | MAC               | IP           |
+----+-----------+---------+----------+-----------------+-----+-------------------+--------------+
| 1  | island-y2 | X       | eth0     | ovn-kubernetes  | X   | 0a:58:0a:81:00:da | 10.129.0.218 | 
|    | p1-2      |         | ovn-udn1 | ovn-kubernetes  | V   | 0a:58:42:42:00:0c | 66.66.0.12   | 
|    |           |         | net1     | island-y2/ysphy | X   | 0a:58:42:42:01:0a | 66.66.1.10   | 
+----+-----------+---------+----------+-----------------+-----+-------------------+--------------+

Completed tasks
- pod created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-y1
- name: c8kv1-day0

~~~
apiVersion: v1
data:
  iosxe_config.txt: |-
    hostname c8kv1
    ip domain name domain.com
    aaa new-model
    aaa authentication login default local
    aaa authorization exec default local
    username admin privilege 15 secret password
    no ip http secure-server
    crypto key generate rsa modulus 2048
    ip ssh version 2
    interface GigabitEthernet1
      ip address dhcp
      no shutdown
    interface GigabitEthernet2
      ip address dhcp
      no shutdown
    ip http secure-server
    line con 0
      length 0
    line vty 0 4
      length 0
kind: ConfigMap
metadata:
  name: c8kv1-day0
  namespace: island-y1

~~~
ConfigMap [island-y1/c8kv1-day0] created
- wait for ConfigMap island-y1/c8kv1-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-y1
- name: c8kv1

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-y1
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: island-y1
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
        storageClassName: lvms-vg1
        volumeMode: Block
      source:
        http:
          url: http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2
  runStrategy: Always
  template:
    metadata:
      labels:
        app: c8kv1
        kubevirt.io/domain: c8kv1
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          - cdrom:
              bus: sata
              readyOnly: true
            name: day0
          interfaces:
          - binding:
              name: l2bridge
            name: default
          - bridge: {}
            name: net1
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv1
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island-y1/ysphy
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: island-y1
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: island-y1
        name: day0

~~~
VirtualMachine [island-y1/c8kv1] created
- wait for VirtualMachine island-y1/c8kv1 [timeout:60s]
- wait for VirtualMachine island-y1/c8kv1 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-y1
- name: c8kv1-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kv1-ssh
  namespace: island-y1
spec:
  ports:
  - port: 22
    protocol: TCP
    targetPort: 22
  selector:
    app: c8kv1
  type: NodePort

~~~
Wait until service found [timeout:60s]...

+----+-----------+----------+---------------+--------------+-----------+-----+
| ID | Service   | Type     | IP            | Port         | Selector  | Age |
+----+-----------+----------+---------------+--------------+-----------+-----+
| 1  | island-y1 | NodePort | 172.30.39.213 | TCP/22:30106 | app:c8kv1 | 60m | 
|    | c8kv1-ssh |          |               |              |           |     | 
+----+-----------+----------+---------------+--------------+-----------+-----+

+----+-----------+----------+-------------------------------------+---------------------+---------------+
| ID | Endpoint  | Headless | Pod                                 | Address             | Port          |
+----+-----------+----------+-------------------------------------+---------------------+---------------+
| 1  | island-y1 | X        | island-y1/virt-launcher-c8kv1-n5z4p | 10.128.1.51 [bm1-1] | TCP/22 [None] | 
|    | c8kv1-ssh |          |                                     |                     |               | 
+----+-----------+----------+-------------------------------------+---------------------+---------------+

Completed tasks
- service created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-y2
- name: c8kv2-day0

~~~
apiVersion: v1
data:
  iosxe_config.txt: |-
    hostname c8kv2
    ip domain name domain.com
    aaa new-model
    aaa authentication login default local
    aaa authorization exec default local
    username admin privilege 15 secret password
    no ip http secure-server
    crypto key generate rsa modulus 2048
    ip ssh version 2
    interface GigabitEthernet1
      ip address dhcp
      no shutdown
    interface GigabitEthernet2
      ip address dhcp
      no shutdown
    ip http secure-server
    line con 0
      length 0
    line vty 0 4
      length 0
kind: ConfigMap
metadata:
  name: c8kv2-day0
  namespace: island-y2

~~~
ConfigMap [island-y2/c8kv2-day0] created
- wait for ConfigMap island-y2/c8kv2-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-y2
- name: c8kv2

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv2
  namespace: island-y2
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv2
      namespace: island-y2
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
        storageClassName: lvms-vg1
        volumeMode: Block
      source:
        http:
          url: http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2
  runStrategy: Always
  template:
    metadata:
      labels:
        app: c8kv2
        kubevirt.io/domain: c8kv2
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          - cdrom:
              bus: sata
              readyOnly: true
            name: day0
          interfaces:
          - binding:
              name: l2bridge
            name: default
          - bridge: {}
            name: net1
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv2
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island-y2/ysphy
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-2
      volumes:
      - dataVolume:
          name: c8kv2
          namespace: island-y2
        name: rootdisk
      - configMap:
          name: c8kv2-day0
          namespace: island-y2
        name: day0

~~~
VirtualMachine [island-y2/c8kv2] created
- wait for VirtualMachine island-y2/c8kv2 [timeout:60s]
- wait for VirtualMachine island-y2/c8kv2 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-y2
- name: c8kv2-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kv2-ssh
  namespace: island-y2
spec:
  ports:
  - port: 22
    protocol: TCP
    targetPort: 22
  selector:
    app: c8kv2
  type: NodePort

~~~
Wait until service found [timeout:60s]...

+----+-----------+----------+---------------+--------------+-----------+------+
| ID | Service   | Type     | IP            | Port         | Selector  | Age  |
+----+-----------+----------+---------------+--------------+-----------+------+
| 1  | island-y2 | NodePort | 172.30.100.59 | TCP/22:31707 | app:c8kv2 | 1h0m | 
|    | c8kv2-ssh |          |               |              |           |      | 
+----+-----------+----------+---------------+--------------+-----------+------+

+----+-----------+----------+-------------------------------------+----------------------+---------------+
| ID | Endpoint  | Headless | Pod                                 | Address              | Port          |
+----+-----------+----------+-------------------------------------+----------------------+---------------+
| 1  | island-y2 | X        | island-y2/virt-launcher-c8kv2-8qk22 | 10.129.0.221 [bm1-2] | TCP/22 [None] | 
|    | c8kv2-ssh |          |                                     |                      |               | 
+----+-----------+----------+-------------------------------------+----------------------+---------------+

Completed tasks
- service created
```

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./ovs.md)