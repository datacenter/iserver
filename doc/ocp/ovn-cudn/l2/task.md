# CUDN w/L2 Topology - Task

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
                    "namespace": "island-v1",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "v"
                    }
                },
                {
                    "__type__": "namespace",
                    "namespace": "island-v2",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "v"
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
                            "tenant:v"
                        ]
                    },
                    "name": "vpl2",
                    "primary": true,
                    "topology": "l2",
                    "subnets": ["66.66.0.0/24"]
                },
                {
                    "__type__": "ovn-cudn",
                    "namespace": {
                        "label": [
                            "tenant:v"
                        ]
                    },
                    "name": "vsl2",
                    "topology": "l2",
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
                    "namespace": "island-v1",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "vsl2"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-v1",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "vsl2"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-v2",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "vsl2"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-v2",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "vsl2"
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
            "namespace": "island-v1",
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
                            "nad": "vsl2"
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
            "namespace": "island-v2",
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
                            "nad": "vsl2"
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
- name: island-v1

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: v
  name: island-v1

~~~
Namespace [island-v1] created
Wait for namespace [timeout:60]...

Check labels
- tenant:v found
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
- name: island-v2

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: v
  name: island-v2

~~~
Namespace [island-v2] created
Wait for namespace [timeout:60]...

Check labels
- tenant:v found
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
- name: vpl2

~~~
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: vpl2
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-v1
      - island-v2
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.0.0/24
    topology: Layer2

~~~
ClusterUserDefinedNetwork [vpl2] created
- wait for ClusterUserDefinedNetwork vpl2 [timeout:60s]
- wait for ClusterUserDefinedNetwork vpl2 [timeout:60s] with {"created_status": "True"}

+----+------+---+---+-----------+----------+--------------+----------------+----------+
| ID | CUDN | C | P | Namespace | Topology | Subnet       | Net Attach Def | Workload |
+----+------+---+---+-----------+----------+--------------+----------------+----------+
| 1  | vpl2 | V | V | ---       | Layer2   | 66.66.0.0/24 | ---            | ---      | 
+----+------+---+---+-----------+----------+--------------+----------------+----------+

Completed tasks
- ovn cluster user defined network created

Kubernetes Workflow - OVN Cluster User Defined Network - Create
===============================================================

OpenShift Cluster: bm1

Create ClusterUserDefinedNetwork
--------------------------------
- name: vsl2

~~~
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: vsl2
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-v1
      - island-v2
  network:
    layer2:
      role: Secondary
      subnets:
      - 66.66.1.0/24
    topology: Layer2

~~~
ClusterUserDefinedNetwork [vsl2] created
- wait for ClusterUserDefinedNetwork vsl2 [timeout:60s]
- wait for ClusterUserDefinedNetwork vsl2 [timeout:60s] with {"created_status": "True"}

+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+
| ID | CUDN | C | P | Namespace | Topology | Subnet       | Net Attach Def                             | Workload |
+----+------+---+---+-----------+----------+--------------+--------------------------------------------+----------+
| 1  | vsl2 | V |   | island-v1 | Layer2   | 66.66.1.0/24 | {                                          | ---      | 
|    |      |   |   | island-v2 |          |              |   "cniVersion": "1.0.0",                   |          | 
|    |      |   |   |           |          |              |   "name": "cluster_udn_vsl2",              |          | 
|    |      |   |   |           |          |              |   "netAttachDefName": "${NAMESPACE}/vsl2", |          | 
|    |      |   |   |           |          |              |   "role": "secondary",                     |          | 
|    |      |   |   |           |          |              |   "subnets": "66.66.1.0/24",               |          | 
|    |      |   |   |           |          |              |   "topology": "layer2",                    |          | 
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
- namespace: island-v1
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: vsl2
  name: p1-1
  namespace: island-v1
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
| 1  | island-v1 | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.62 | 3   | 0       | 1h0m | 
|    | p1-1      |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |           |       |         | ContainersReady: V |       |             |     |         |      | 
|    |           |       |         | Ready: V           |       |             |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP          |
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| 1  | island-v1 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:3e | 10.128.1.62 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:04 | 66.66.0.4   | 
|    |           |         | net1     | island-v1/vsl2 | X   | 0a:58:42:42:01:02 | 66.66.1.2   | 
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-v1
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: vsl2
  name: p1-2
  namespace: island-v1
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
| 1  | island-v1 | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.222 | 3   | 0       | 1h0m | 
|    | p1-2      |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |           |       |         | ContainersReady: V |       |              |     |         |      | 
|    |           |       |         | Ready: V           |       |              |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-v1 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:81:00:de | 10.129.0.222 | 
|    | p1-2      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:07 | 66.66.0.7    | 
|    |           |         | net1     | island-v1/vsl2 | X   | 0a:58:42:42:01:04 | 66.66.1.4    | 
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-v2
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: vsl2
  name: p1-1
  namespace: island-v2
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
| 1  | island-v2 | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.63 | 3   | 0       | 1h0m | 
|    | p1-1      |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |           |       |         | ContainersReady: V |       |             |     |         |      | 
|    |           |       |         | Ready: V           |       |             |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP          |
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+
| 1  | island-v2 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:3f | 10.128.1.63 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:09 | 66.66.0.9   | 
|    |           |         | net1     | island-v2/vsl2 | X   | 0a:58:42:42:01:07 | 66.66.1.7   | 
+----+-----------+---------+----------+----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-v2
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: vsl2
  name: p1-2
  namespace: island-v2
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
| 1  | island-v2 | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.223 | 3   | 0       | 1h0m | 
|    | p1-2      |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |           |       |         | ContainersReady: V |       |              |     |         |      | 
|    |           |       |         | Ready: V           |       |              |     |         |      | 
+----+-----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod       | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-v2 | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:81:00:df | 10.129.0.223 | 
|    | p1-2      |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:0c | 66.66.0.12   | 
|    |           |         | net1     | island-v2/vsl2 | X   | 0a:58:42:42:01:09 | 66.66.1.9    | 
+----+-----------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-v1
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
  namespace: island-v1

~~~
ConfigMap [island-v1/c8kv1-day0] created
- wait for ConfigMap island-v1/c8kv1-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-v1
- name: c8kv1

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-v1
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: island-v1
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
          networkName: island-v1/vsl2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: island-v1
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: island-v1
        name: day0

~~~
VirtualMachine [island-v1/c8kv1] created
- wait for VirtualMachine island-v1/c8kv1 [timeout:60s]
- wait for VirtualMachine island-v1/c8kv1 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-v1
- name: c8kv1-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kv1-ssh
  namespace: island-v1
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

+----+-----------+----------+----------------+--------------+-----------+-----+
| ID | Service   | Type     | IP             | Port         | Selector  | Age |
+----+-----------+----------+----------------+--------------+-----------+-----+
| 1  | island-v1 | NodePort | 172.30.170.245 | TCP/22:30759 | app:c8kv1 | 60m | 
|    | c8kv1-ssh |          |                |              |           |     | 
+----+-----------+----------+----------------+--------------+-----------+-----+

+----+-----------+----------+-------------------------------------+---------------------+---------------+
| ID | Endpoint  | Headless | Pod                                 | Address             | Port          |
+----+-----------+----------+-------------------------------------+---------------------+---------------+
| 1  | island-v1 | X        | island-v1/virt-launcher-c8kv1-kjl9m | 10.128.1.66 [bm1-1] | TCP/22 [None] | 
|    | c8kv1-ssh |          |                                     |                     |               | 
+----+-----------+----------+-------------------------------------+---------------------+---------------+

Completed tasks
- service created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-v2
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
  namespace: island-v2

~~~
ConfigMap [island-v2/c8kv2-day0] created
- wait for ConfigMap island-v2/c8kv2-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-v2
- name: c8kv2

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv2
  namespace: island-v2
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv2
      namespace: island-v2
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
          networkName: island-v2/vsl2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-2
      volumes:
      - dataVolume:
          name: c8kv2
          namespace: island-v2
        name: rootdisk
      - configMap:
          name: c8kv2-day0
          namespace: island-v2
        name: day0

~~~
VirtualMachine [island-v2/c8kv2] created
- wait for VirtualMachine island-v2/c8kv2 [timeout:60s]
- wait for VirtualMachine island-v2/c8kv2 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-v2
- name: c8kv2-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kv2-ssh
  namespace: island-v2
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
| 1  | island-v2 | NodePort | 172.30.90.232 | TCP/22:31242 | app:c8kv2 | 1h0m | 
|    | c8kv2-ssh |          |               |              |           |      | 
+----+-----------+----------+---------------+--------------+-----------+------+

+----+-----------+----------+-------------------------------------+----------------------+---------------+
| ID | Endpoint  | Headless | Pod                                 | Address              | Port          |
+----+-----------+----------+-------------------------------------+----------------------+---------------+
| 1  | island-v2 | X        | island-v2/virt-launcher-c8kv2-7mlvz | 10.129.0.226 [bm1-2] | TCP/22 [None] | 
|    | c8kv2-ssh |          |                                     |                      |               | 
+----+-----------+----------+-------------------------------------+----------------------+---------------+

Completed tasks
- service created
```

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./namespace.md)