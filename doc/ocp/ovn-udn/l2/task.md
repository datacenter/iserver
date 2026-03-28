# UDN w/L2 Topology - Task

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./udn.md)

## Goal

- namespaces: island-p
- single udn primary network w/l2 topology
- single udn secondary network w/l2 topology
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
                    "namespace": "island-p",
                    "ovn-udn": true,
                    "ovn-multicast": true
                },
                {
                    "__type__": "ovn-udn",
                    "namespace": "island-p",
                    "name": "pl2",
                    "primary": true,
                    "topology": "l2",
                    "subnets": ["66.66.0.0/24"]
                },
                {
                    "__type__": "ovn-udn",
                    "namespace": "island-p",
                    "name": "sl2",
                    "topology": "l2",
                    "subnets": ["66.66.1.0/24"]
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
                    "namespace": "island-p",
                    "name": "p1-1",
                    "node": "bm1-1",
                    "app": "netshoot",
                    "network": [
                        "sl2"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-p",
                    "name": "p1-2",
                    "node": "bm1-2",
                    "app": "netshoot",
                    "network": [
                        "sl2"
                    ]
                },
                {
                    "__type__": "pod",
                    "namespace": "island-p",
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
                    "namespace": "island-p",
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
            "namespace": "island-p",
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
                            "nad": "sl2"
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
            "namespace": "island-p",
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
                            "nad": "sl2"
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
- name: island-p

~~~
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
  name: island-p

~~~
Namespace [island-p] created
Wait for namespace [timeout:60]...

Check labels
- k8s.ovn.org/primary-user-defined-network: found

Check annotations
- k8s.ovn.org/multicast-enabled:true found

Completed tasks
- namespace created

Kubernetes Workflow - OVN User Defined Network - Create
=======================================================

OpenShift Cluster: bm1

Create UserDefinedNetwork
-------------------------
- namespace: island-p
- name: pl2

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: pl2
  namespace: island-p
spec:
  layer2:
    role: Primary
    subnets:
    - 66.66.0.0/24
  topology: Layer2

~~~
UserDefinedNetwork [island-p/pl2] created
- wait for UserDefinedNetwork island-p/pl2 [timeout:60s]
- wait for UserDefinedNetwork island-p/pl2 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island-p/pl2 [timeout:60s] with {"allocated_status": "True"}

+----+----------+---+---+---+----------+--------------+--------------------------------------------+----------+
| ID | UDN      | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload |
+----+----------+---+---+---+----------+--------------+--------------------------------------------+----------+
| 1  | island-p | V | V | V | Layer2   | 66.66.0.0/24 | {                                          | ---      | 
|    | pl2      |   |   |   |          |              |   "cniVersion": "1.0.0",                   |          | 
|    |          |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          | 
|    |          |   |   |   |          |              |   "name": "island-p_pl2",                  |          | 
|    |          |   |   |   |          |              |   "netAttachDefName": "island-p/pl2",      |          | 
|    |          |   |   |   |          |              |   "role": "primary",                       |          | 
|    |          |   |   |   |          |              |   "subnets": "66.66.0.0/24",               |          | 
|    |          |   |   |   |          |              |   "topology": "layer2",                    |          | 
|    |          |   |   |   |          |              |   "transitSubnet": "100.88.0.0/16",        |          | 
|    |          |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |          | 
|    |          |   |   |   |          |              | }                                          |          | 
+----+----------+---+---+---+----------+--------------+--------------------------------------------+----------+

Completed tasks
- ovn user defined network created

Kubernetes Workflow - OVN User Defined Network - Create
=======================================================

OpenShift Cluster: bm1

Create UserDefinedNetwork
-------------------------
- namespace: island-p
- name: sl2

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: sl2
  namespace: island-p
spec:
  layer2:
    role: Secondary
    subnets:
    - 66.66.1.0/24
  topology: Layer2

~~~
UserDefinedNetwork [island-p/sl2] created
- wait for UserDefinedNetwork island-p/sl2 [timeout:60s]
- wait for UserDefinedNetwork island-p/sl2 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island-p/sl2 [timeout:60s] with {"allocated_status": "True"}

+----+----------+---+---+---+----------+--------------+---------------------------------------+----------+
| ID | UDN      | C | A | P | Topology | Subnet       | Net Attach Def                        | Workload |
+----+----------+---+---+---+----------+--------------+---------------------------------------+----------+
| 1  | island-p | V | V |   | Layer2   | 66.66.1.0/24 | {                                     | ---      | 
|    | sl2      |   |   |   |          |              |   "cniVersion": "1.0.0",              |          | 
|    |          |   |   |   |          |              |   "name": "island-p_sl2",             |          | 
|    |          |   |   |   |          |              |   "netAttachDefName": "island-p/sl2", |          | 
|    |          |   |   |   |          |              |   "role": "secondary",                |          | 
|    |          |   |   |   |          |              |   "subnets": "66.66.1.0/24",          |          | 
|    |          |   |   |   |          |              |   "topology": "layer2",               |          | 
|    |          |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"       |          | 
|    |          |   |   |   |          |              | }                                     |          | 
+----+----------+---+---+---+----------+--------------+---------------------------------------+----------+

Completed tasks
- ovn user defined network created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-p
- name: p1-1

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: sl2
  name: p1-1
  namespace: island-p
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

+----+----------+-------+---------+--------------------+-------+-------------+-----+---------+------+
| ID | Pod      | Ready | Label   | Annotation         | Node  | IP          | Net | Restart | Age  |
+----+----------+-------+---------+--------------------+-------+-------------+-----+---------+------+
| 1  | island-p | 1/1   | Running | Initialized: V     | bm1-1 | 10.128.1.74 | 3   | 0       | 1h0m | 
|    | p1-1     |       |         | PodScheduled: V    |       |             |     |         |      | 
|    |          |       |         | ContainersReady: V |       |             |     |         |      | 
|    |          |       |         | Ready: V           |       |             |     |         |      | 
+----+----------+-------+---------+--------------------+-------+-------------+-----+---------+------+

+----+----------+---------+----------+----------------+-----+-------------------+-------------+
| ID | Pod      | HostNet | Intf     | Network        | Def | MAC               | IP          |
+----+----------+---------+----------+----------------+-----+-------------------+-------------+
| 1  | island-p | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:4a | 10.128.1.74 | 
|    | p1-1     |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:04 | 66.66.0.4   | 
|    |          |         | net1     | island-p/sl2   | X   | 0a:58:42:42:01:03 | 66.66.1.3   | 
+----+----------+---------+----------+----------------+-----+-------------------+-------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-p
- name: p1-2

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: sl2
  name: p1-2
  namespace: island-p
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

+----+----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| ID | Pod      | Ready | Label   | Annotation         | Node  | IP           | Net | Restart | Age  |
+----+----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| 1  | island-p | 1/1   | Running | Initialized: V     | bm1-2 | 10.129.0.232 | 3   | 0       | 1h0m | 
|    | p1-2     |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |          |       |         | ContainersReady: V |       |              |     |         |      | 
|    |          |       |         | Ready: V           |       |              |     |         |      | 
+----+----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod      | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-p | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:81:00:e8 | 10.129.0.232 | 
|    | p1-2     |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:08 | 66.66.0.8    | 
|    |          |         | net1     | island-p/sl2   | X   | 0a:58:42:42:01:06 | 66.66.1.6    | 
+----+----------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island-p
- name: nginx3

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.ovn.org/open-default-ports: '[{"protocol": "tcp", "port": 8080}]'
  labels:
    app: nginx3
  name: nginx3
  namespace: island-p
spec:
  containers:
  - image: nginxinc/nginx-unprivileged
    name: nginx
  nodeName: bm1-3

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| ID | Pod      | Ready | Label   | Annotation         | Node  | IP           | Net | Restart | Age  |
+----+----------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| 1  | island-p | 1/1   | Running | Initialized: V     | bm1-3 | 10.130.0.226 | 2   | 0       | 1h0m | 
|    | nginx3   |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |          |       |         | ContainersReady: V |       |              |     |         |      | 
|    |          |       |         | Ready: V           |       |              |     |         |      | 
+----+----------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod      | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-p | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:82:00:e2 | 10.130.0.226 | 
|    | nginx3   |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:0a | 66.66.0.10   | 
+----+----------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-p
- name: nginx3

~~~
apiVersion: v1
kind: Service
metadata:
  name: nginx3
  namespace: island-p
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 8080
  selector:
    app: nginx3
  type: NodePort

~~~
Wait until service found [timeout:60s]...

+----+----------+----------+----------------+--------------+------------+-----+
| ID | Service  | Type     | IP             | Port         | Selector   | Age |
+----+----------+----------+----------------+--------------+------------+-----+
| 1  | island-p | NodePort | 172.30.195.101 | TCP/80:31166 | app:nginx3 | 60m | 
|    | nginx3   |          |                |              |            |     | 
+----+----------+----------+----------------+--------------+------------+-----+

+----+----------+----------+-----------------+----------------------+-----------------+
| ID | Endpoint | Headless | Pod             | Address              | Port            |
+----+----------+----------+-----------------+----------------------+-----------------+
| 1  | island-p | X        | island-p/nginx3 | 10.130.0.226 [bm1-3] | TCP/8080 [None] | 
|    | nginx3   |          |                 |                      |                 | 
+----+----------+----------+-----------------+----------------------+-----------------+

Completed tasks
- service created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: default
- name: tool

~~~
apiVersion: v1
kind: Pod
metadata:
  name: tool
  namespace: default
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

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+---------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| ID | Pod     | Ready | Label   | Annotation         | Node  | IP           | Net | Restart | Age  |
+----+---------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| 1  | default | 1/1   | Running | Initialized: V     | bm1-3 | 10.130.0.227 | 1   | 0       | 1h0m | 
|    | tool    |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |         |       |         | ContainersReady: V |       |              |     |         |      | 
|    |         |       |         | Ready: V           |       |              |     |         |      | 
+----+---------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+---------+---------+------+----------------+-----+-------------------+--------------+
| ID | Pod     | HostNet | Intf | Network        | Def | MAC               | IP           |
+----+---------+---------+------+----------------+-----+-------------------+--------------+
| 1  | default | X       | eth0 | ovn-kubernetes | V   | 0a:58:0a:82:00:e3 | 10.130.0.227 | 
|    | tool    |         |      |                |     |                   |              | 
+----+---------+---------+------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-p
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
  namespace: island-p

~~~
ConfigMap [island-p/c8kv1-day0] created
- wait for ConfigMap island-p/c8kv1-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-p
- name: c8kv1

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-p
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: island-p
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
          networkName: island-p/sl2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: island-p
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: island-p
        name: day0

~~~
VirtualMachine [island-p/c8kv1] created
- wait for VirtualMachine island-p/c8kv1 [timeout:60s]
- wait for VirtualMachine island-p/c8kv1 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-p
- name: c8kv1-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kv1-ssh
  namespace: island-p
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
| 1  | island-p  | NodePort | 172.30.214.71 | TCP/22:30999 | app:c8kv1 | 60m | 
|    | c8kv1-ssh |          |               |              |           |     | 
+----+-----------+----------+---------------+--------------+-----------+-----+

+----+-----------+----------+------------------------------------+---------------------+---------------+
| ID | Endpoint  | Headless | Pod                                | Address             | Port          |
+----+-----------+----------+------------------------------------+---------------------+---------------+
| 1  | island-p  | X        | island-p/virt-launcher-c8kv1-qz8bf | 10.128.1.77 [bm1-1] | TCP/22 [None] | 
|    | c8kv1-ssh |          |                                    |                     |               | 
+----+-----------+----------+------------------------------------+---------------------+---------------+

Completed tasks
- service created

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island-p
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
  namespace: island-p

~~~
ConfigMap [island-p/c8kv2-day0] created
- wait for ConfigMap island-p/c8kv2-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island-p
- name: c8kv2

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv2
  namespace: island-p
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv2
      namespace: island-p
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
          networkName: island-p/sl2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-2
      volumes:
      - dataVolume:
          name: c8kv2
          namespace: island-p
        name: rootdisk
      - configMap:
          name: c8kv2-day0
          namespace: island-p
        name: day0

~~~
VirtualMachine [island-p/c8kv2] created
- wait for VirtualMachine island-p/c8kv2 [timeout:60s]
- wait for VirtualMachine island-p/c8kv2 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created

OpenShift Workflow - Service - Create
=====================================

OpenShift Cluster: bm1

Create Service
--------------
- namespace: island-p
- name: c8kv2-ssh

~~~
apiVersion: v1
kind: Service
metadata:
  name: c8kv2-ssh
  namespace: island-p
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

+----+-----------+----------+----------------+--------------+-----------+-----+
| ID | Service   | Type     | IP             | Port         | Selector  | Age |
+----+-----------+----------+----------------+--------------+-----------+-----+
| 1  | island-p  | NodePort | 172.30.121.170 | TCP/22:30406 | app:c8kv2 | 60m | 
|    | c8kv2-ssh |          |                |              |           |     | 
+----+-----------+----------+----------------+--------------+-----------+-----+

+----+-----------+----------+------------------------------------+----------------------+---------------+
| ID | Endpoint  | Headless | Pod                                | Address              | Port          |
+----+-----------+----------+------------------------------------+----------------------+---------------+
| 1  | island-p  | X        | island-p/virt-launcher-c8kv2-mchtj | 10.129.0.235 [bm1-2] | TCP/22 [None] | 
|    | c8kv2-ssh |          |                                    |                      |               | 
+----+-----------+----------+------------------------------------+----------------------+---------------+

Completed tasks
- service created
```

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./namespace.md)