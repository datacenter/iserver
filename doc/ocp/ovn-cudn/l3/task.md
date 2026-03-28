# CUDN w/L3 Topology - Task

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./namespace.md)

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
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

Kubernetes Workflow - Namespace - Create
========================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: island-w1

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: w
  name: island-w1

~~~
Namespace [island-w1] created
Wait for namespace [timeout:60]...

Check labels
- tenant:w found
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
- name: island-w2

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: w
  name: island-w2

~~~
Namespace [island-w2] created
Wait for namespace [timeout:60]...

Check labels
- tenant:w found
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
- name: wpl3

~~~
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: wpl3
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-w1
      - island-w2
  network:
    layer3:
      role: Primary
      subnets:
      - cidr: 66.66.0.0/24
        hostSubnet: 28
    topology: Layer3

~~~
ClusterUserDefinedNetwork [wpl3] created
- wait for ClusterUserDefinedNetwork wpl3 [timeout:60s]
- wait for ClusterUserDefinedNetwork wpl3 [timeout:60s] with {"created_status": "True"}
- wait for NetworkAttachmentDefinition island-w1/wpl3 [timeout:60s]
- wait for NetworkAttachmentDefinition island-w2/wpl3 [timeout:60s]

+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+
| ID | CUDN | C | P | Namespace | Topology | Subnet       | Net Attach Def                             | Workload |
+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+
| 1  | wpl3 | V | V | island-w1 | Layer3   | 66.66.0.0/24 | {                                          | ---      | 
|    |      |   |   | island-w2 |          | host /28     |   "cniVersion": "1.0.0",                   |          | 
|    |      |   |   |           |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          | 
|    |      |   |   |           |          |              |   "name": "cluster_udn_wpl3",              |          | 
|    |      |   |   |           |          |              |   "netAttachDefName": "${NAMESPACE}/wpl3", |          | 
|    |      |   |   |           |          |              |   "role": "primary",                       |          | 
|    |      |   |   |           |          |              |   "subnets": "66.66.0.0/24/28",            |          | 
|    |      |   |   |           |          |              |   "topology": "layer3",                    |          | 
|    |      |   |   |           |          |              |   "type": "ovn-k8s-cni-overlay"            |          | 
|    |      |   |   |           |          |              | }                                          |          | 
+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+

Completed tasks
- ovn cluster user defined network created

Kubernetes Workflow - OVN Cluster User Defined Network - Create
===============================================================

OpenShift Cluster: bm1

Create ClusterUserDefinedNetwork
--------------------------------
- name: wsl3

~~~
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: wsl3
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-w1
      - island-w2
  network:
    layer3:
      role: Secondary
      subnets:
      - cidr: 66.66.1.0/24
        hostSubnet: 28
    topology: Layer3

~~~
ClusterUserDefinedNetwork [wsl3] created
- wait for ClusterUserDefinedNetwork wsl3 [timeout:60s]
- wait for ClusterUserDefinedNetwork wsl3 [timeout:60s] with {"created_status": "True"}
- wait for NetworkAttachmentDefinition island-w1/wsl3 [timeout:60s]
- wait for NetworkAttachmentDefinition island-w2/wsl3 [timeout:60s]

+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+
| ID | CUDN | C | P | Namespace | Topology | Subnet       | Net Attach Def                             | Workload |
+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+
| 1  | wsl3 | V |   | island-w1 | Layer3   | 66.66.1.0/24 | {                                          | ---      | 
|    |      |   |   | island-w2 |          | host /28     |   "cniVersion": "1.0.0",                   |          | 
|    |      |   |   |           |          |              |   "name": "cluster_udn_wsl3",              |          | 
|    |      |   |   |           |          |              |   "netAttachDefName": "${NAMESPACE}/wsl3", |          | 
|    |      |   |   |           |          |              |   "role": "secondary",                     |          | 
|    |      |   |   |           |          |              |   "subnets": "66.66.1.0/24/28",            |          | 
|    |      |   |   |           |          |              |   "topology": "layer3",                    |          | 
|    |      |   |   |           |          |              |   "type": "ovn-k8s-cni-overlay"            |          | 
|    |      |   |   |           |          |              | }                                          |          | 
+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+

Completed tasks
- ovn cluster user defined network created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-w1
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: wsl3
  name: p1-1
  namespace: island-w1
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
| 1  | island-w1 | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.69 | 3   | 0       | 1h0m | 
|    | p1-1      |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |           |       |         | ContainersReady: V |       |             |     |         |      | 
|    |           |       |         | Ready: V           |       |             |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP          |
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| 1  | island-w1 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:45 | 10.128.1.69 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:04 | 66.66.0.4   | 
|    |           |         | net1     | island-w1/wsl3 | X   | 0a:58:42:42:01:14 | 66.66.1.20  | 
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-w1
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: wsl3
  name: p1-2
  namespace: island-w1
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
| 1  | island-w1 | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.227 | 3   | 0       | 1h0m | 
|    | p1-2      |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |           |       |         | ContainersReady: V |       |              |     |         |      | 
|    |           |       |         | Ready: V           |       |              |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-w1 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:81:00:e3 | 10.129.0.227 | 
|    | p1-2      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:24 | 66.66.0.36   | 
|    |           |         | net1     | island-w1/wsl3 | X   | 0a:58:42:42:01:05 | 66.66.1.5    | 
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-w2
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: wsl3
  name: p1-1
  namespace: island-w2
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
| 1  | island-w2 | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.70 | 3   | 0       | 1h0m | 
|    | p1-1      |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |           |       |         | ContainersReady: V |       |             |     |         |      | 
|    |           |       |         | Ready: V           |       |             |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP          |
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| 1  | island-w2 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:46 | 10.128.1.70 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:06 | 66.66.0.6   | 
|    |           |         | net1     | island-w2/wsl3 | X   | 0a:58:42:42:01:17 | 66.66.1.23  | 
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-w2
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: wsl3
  name: p1-2
  namespace: island-w2
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
| 1  | island-w2 | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.228 | 3   | 0       | 1h0m | 
|    | p1-2      |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |           |       |         | ContainersReady: V |       |              |     |         |      | 
|    |           |       |         | Ready: V           |       |              |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-w2 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:81:00:e4 | 10.129.0.228 | 
|    | p1-2      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:27 | 66.66.0.39   | 
|    |           |         | net1     | island-w2/wsl3 | X   | 0a:58:42:42:01:07 | 66.66.1.7    | 
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-w1
- name: c8kw1-day0

~~~
apiVersion: v1
data:
  iosxe_config.txt: |-
    hostname c8kw1
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
  name: c8kw1-day0
  namespace: island-w1

~~~
ConfigMap [island-w1/c8kw1-day0] created
- wait for ConfigMap island-w1/c8kw1-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-w1
- name: c8kw1

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kw1
  namespace: island-w1
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kw1
      namespace: island-w1
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
        app: c8kw1
        kubevirt.io/domain: c8kw1
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
      hostname: c8kw1
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island-w1/wsl3
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kw1
          namespace: island-w1
        name: rootdisk
      - configMap:
          name: c8kw1-day0
          namespace: island-w1
        name: day0

~~~
VirtualMachine [island-w1/c8kw1] created
- wait for VirtualMachine island-w1/c8kw1 [timeout:60s]
- wait for VirtualMachine island-w1/c8kw1 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-w1
- name: c8kw1-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kw1-ssh
  namespace: island-w1
spec:
  ports:
  - port: 22
    protocol: TCP
    targetPort: 22
  selector:
    app: c8kw1
  type: NodePort

~~~
Wait until service found [timeout:60s]...

+----+-----------+----------+---------------+--------------+-----------+-----+
| ID | Service   | Type     | IP            | Port         | Selector  | Age |
+----+-----------+----------+---------------+--------------+-----------+-----+
| 1  | island-w1 | NodePort | 172.30.183.39 | TCP/22:32422 | app:c8kw1 | 60m | 
|    | c8kw1-ssh |          |               |              |           |     | 
+----+-----------+----------+---------------+--------------+-----------+-----+

+----+-----------+----------+-------------------------------------+---------------------+---------------+
| ID | Endpoint  | Headless | Pod                                 | Address             | Port          |
+----+-----------+----------+-------------------------------------+---------------------+---------------+
| 1  | island-w1 | X        | island-w1/virt-launcher-c8kw1-7fhfn | 10.128.1.73 [bm1-1] | TCP/22 [None] | 
|    | c8kw1-ssh |          |                                     |                     |               | 
+----+-----------+----------+-------------------------------------+---------------------+---------------+

Completed tasks
- service created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-w2
- name: c8kw2-day0

~~~
apiVersion: v1
data:
  iosxe_config.txt: |-
    hostname c8kw2
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
  name: c8kw2-day0
  namespace: island-w2

~~~
ConfigMap [island-w2/c8kw2-day0] created
- wait for ConfigMap island-w2/c8kw2-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-w2
- name: c8kw2

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kw2
  namespace: island-w2
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kw2
      namespace: island-w2
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
        app: c8kw2
        kubevirt.io/domain: c8kw2
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
      hostname: c8kw2
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island-w2/wsl3
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-2
      volumes:
      - dataVolume:
          name: c8kw2
          namespace: island-w2
        name: rootdisk
      - configMap:
          name: c8kw2-day0
          namespace: island-w2
        name: day0

~~~
VirtualMachine [island-w2/c8kw2] created
- wait for VirtualMachine island-w2/c8kw2 [timeout:60s]
- wait for VirtualMachine island-w2/c8kw2 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-w2
- name: c8kw2-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kw2-ssh
  namespace: island-w2
spec:
  ports:
  - port: 22
    protocol: TCP
    targetPort: 22
  selector:
    app: c8kw2
  type: NodePort

~~~
Wait until service found [timeout:60s]...

+----+-----------+----------+--------------+--------------+-----------+-----+
| ID | Service   | Type     | IP           | Port         | Selector  | Age |
+----+-----------+----------+--------------+--------------+-----------+-----+
| 1  | island-w2 | NodePort | 172.30.85.17 | TCP/22:30648 | app:c8kw2 | 60m | 
|    | c8kw2-ssh |          |              |              |           |     | 
+----+-----------+----------+--------------+--------------+-----------+-----+

+----+-----------+----------+-------------------------------------+----------------------+---------------+
| ID | Endpoint  | Headless | Pod                                 | Address              | Port          |
+----+-----------+----------+-------------------------------------+----------------------+---------------+
| 1  | island-w2 | X        | island-w2/virt-launcher-c8kw2-vfmns | 10.129.0.231 [bm1-2] | TCP/22 [None] | 
|    | c8kw2-ssh |          |                                     |                      |               | 
+----+-----------+----------+-------------------------------------+----------------------+---------------+

Completed tasks
- service created
```

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./namespace.md)