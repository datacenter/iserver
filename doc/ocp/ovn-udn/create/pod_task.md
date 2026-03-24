# UDN and POD - Task

[[Back]](../README.md) [[Prev]](../create/pod_crd.md) [[Next]](../get/pod.md)

## Input 

```
[
    {
        "k8s": {
            "items": [
                {
                    "__type__": "ovn-udn",
                    "namespace": "island",
                    "name": "p1-l2",
                    "primary": true,
                    "topology": "l2",
                    "subnets": ["66.66.0.0/24"]
                },
                {
                    "__type__": "ovn-udn",
                    "namespace": "island",
                    "name": "s1-l2",
                    "topology": "l2",
                    "subnets": ["66.66.1.0/24"]
                },
                {
                    "__type__": "ovn-udn",
                    "namespace": "island",
                    "name": "s2-l2",
                    "topology": "l2",
                    "subnets": ["66.66.2.0/24"]
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
                    "namespace": "island",
                    "name": "p1-3",
                    "node": "bm1-3",
                    "app": "netshoot",
                    "network": [
                        "s1-l2",
                        "s2-l2"
                    ]
                }
            ]
        }
    }
]
```

## Expected Outcome

```
# iserver get k8s pod --namespace island -v net
Cluster: bm1 (type: ocp)

+----+--------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod    | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+--------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:82:00:7f | 10.130.0.127 |
|    | p1-3   |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:06 | 66.66.0.6    |
|    |        |         | net1     | island/s1-l2   | X   | 0a:58:42:42:01:03 | 66.66.1.3    |
|    |        |         | net2     | island/s2-l2   | X   | 0a:58:42:42:02:02 | 66.66.2.2    |
+----+--------+---------+----------+----------------+-----+-------------------+--------------+
```

## Task Outcome Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

Kubernetes Workflow - OVN User Defined Network - Create
=======================================================

OpenShift Cluster: bm1

Create UserDefinedNetwork
-------------------------
- namespace: island
- name: p1-l2

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: p1-l2
  namespace: island
spec:
  layer2:
    role: Primary
    subnets:
    - 66.66.0.0/24
  topology: Layer2

~~~
UserDefinedNetwork [island/p1-l2] created
- wait for UserDefinedNetwork island/p1-l2 [timeout:60s]
- wait for UserDefinedNetwork island/p1-l2 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island/p1-l2 [timeout:60s] with {"allocated_status": "True"}

+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+
| ID | UDN    | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload |
+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+
| 1  | island | V | V | V | Layer2   | 66.66.0.0/24 | {                                          | ---      | 
|    | p1-l2  |   |   |   |          |              |   "cniVersion": "1.0.0",                   |          | 
|    |        |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          | 
|    |        |   |   |   |          |              |   "name": "island_p1-l2",                  |          | 
|    |        |   |   |   |          |              |   "netAttachDefName": "island/p1-l2",      |          | 
|    |        |   |   |   |          |              |   "role": "primary",                       |          | 
|    |        |   |   |   |          |              |   "subnets": "66.66.0.0/24",               |          | 
|    |        |   |   |   |          |              |   "topology": "layer2",                    |          | 
|    |        |   |   |   |          |              |   "transitSubnet": "100.88.0.0/16",        |          | 
|    |        |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |          | 
|    |        |   |   |   |          |              | }                                          |          | 
+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+

Completed tasks
- ovn user defined network created

Kubernetes Workflow - OVN User Defined Network - Create
=======================================================

OpenShift Cluster: bm1

Create UserDefinedNetwork
-------------------------
- namespace: island
- name: s1-l2

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: s1-l2
  namespace: island
spec:
  layer2:
    role: Secondary
    subnets:
    - 66.66.1.0/24
  topology: Layer2

~~~
UserDefinedNetwork [island/s1-l2] created
- wait for UserDefinedNetwork island/s1-l2 [timeout:60s]
- wait for UserDefinedNetwork island/s1-l2 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island/s1-l2 [timeout:60s] with {"allocated_status": "True"}

+----+--------+---+---+---+----------+--------------+---------------------------------------+----------+
| ID | UDN    | C | A | P | Topology | Subnet       | Net Attach Def                        | Workload |
+----+--------+---+---+---+----------+--------------+---------------------------------------+----------+
| 1  | island | V | V |   | Layer2   | 66.66.1.0/24 | {                                     | ---      | 
|    | s1-l2  |   |   |   |          |              |   "cniVersion": "1.0.0",              |          | 
|    |        |   |   |   |          |              |   "name": "island_s1-l2",             |          | 
|    |        |   |   |   |          |              |   "netAttachDefName": "island/s1-l2", |          | 
|    |        |   |   |   |          |              |   "role": "secondary",                |          | 
|    |        |   |   |   |          |              |   "subnets": "66.66.1.0/24",          |          | 
|    |        |   |   |   |          |              |   "topology": "layer2",               |          | 
|    |        |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"       |          | 
|    |        |   |   |   |          |              | }                                     |          | 
+----+--------+---+---+---+----------+--------------+---------------------------------------+----------+

Completed tasks
- ovn user defined network created

Kubernetes Workflow - OVN User Defined Network - Create
=======================================================

OpenShift Cluster: bm1

Create UserDefinedNetwork
-------------------------
- namespace: island
- name: s2-l2

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: s2-l2
  namespace: island
spec:
  layer2:
    role: Secondary
    subnets:
    - 66.66.2.0/24
  topology: Layer2

~~~
UserDefinedNetwork [island/s2-l2] created
- wait for UserDefinedNetwork island/s2-l2 [timeout:60s]
- wait for UserDefinedNetwork island/s2-l2 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island/s2-l2 [timeout:60s] with {"allocated_status": "True"}

+----+--------+---+---+---+----------+--------------+---------------------------------------+----------+
| ID | UDN    | C | A | P | Topology | Subnet       | Net Attach Def                        | Workload |
+----+--------+---+---+---+----------+--------------+---------------------------------------+----------+
| 1  | island | V | V |   | Layer2   | 66.66.2.0/24 | {                                     | ---      | 
|    | s2-l2  |   |   |   |          |              |   "cniVersion": "1.0.0",              |          | 
|    |        |   |   |   |          |              |   "name": "island_s2-l2",             |          | 
|    |        |   |   |   |          |              |   "netAttachDefName": "island/s2-l2", |          | 
|    |        |   |   |   |          |              |   "role": "secondary",                |          | 
|    |        |   |   |   |          |              |   "subnets": "66.66.2.0/24",          |          | 
|    |        |   |   |   |          |              |   "topology": "layer2",               |          | 
|    |        |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"       |          | 
|    |        |   |   |   |          |              | }                                     |          | 
+----+--------+---+---+---+----------+--------------+---------------------------------------+----------+

Completed tasks
- ovn user defined network created

OpenShift Workflow - Pod - Create
=================================

OpenShift Cluster: bm1

Create Pod
----------
- namespace: island
- name: p1-3

~~~
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: s1-l2,s2-l2
  name: p1-3
  namespace: island
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
  nodeName: bm1-3

~~~
Create pod rest api successful
Wait until pod running [timeout:600s]...

+----+--------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| ID | Pod    | Ready | Label   | Annotation         | Node  | IP           | Net | Restart | Age  |
+----+--------+-------+---------+--------------------+-------+--------------+-----+---------+------+
| 1  | island | 1/1   | Running | Initialized: V     | bm1-3 | 10.130.0.127 | 4   | 0       | 1h0m | 
|    | p1-3   |       |         | PodScheduled: V    |       |              |     |         |      | 
|    |        |       |         | ContainersReady: V |       |              |     |         |      | 
|    |        |       |         | Ready: V           |       |              |     |         |      | 
+----+--------+-------+---------+--------------------+-------+--------------+-----+---------+------+

+----+--------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod    | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+--------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:82:00:7f | 10.130.0.127 | 
|    | p1-3   |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:06 | 66.66.0.6    | 
|    |        |         | net1     | island/s1-l2   | X   | 0a:58:42:42:01:03 | 66.66.1.3    | 
|    |        |         | net2     | island/s2-l2   | X   | 0a:58:42:42:02:02 | 66.66.2.2    | 
+----+--------+---------+----------+----------------+-----+-------------------+--------------+

Completed tasks
- pod created
```

[[Back]](../README.md) [[Prev]](../create/pod_crd.md) [[Next]](../get/pod.md)