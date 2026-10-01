# Primary l2 cluster user-defined networks

[[Back]](../README.md)

## Table of content

- [key highlights](#summary)
- OpenShift setup
  - [namespace](#namespace)
  - [cluster user defined network](#cluster-user-defined-network)
  - [ipam](#ipam)
- Application deployment
  - [pod](#pod)
  - [virtual machine](#vm)
- Data Plane
  - [arp resolution](#arp-resolution)
  - [east-west unicast](#east-west-unicast)
  - [cluster ip service](#east-west-cluster-ip-service)
  - [microsegmentation](#east-west-microsegmentation)
  - [north-south](#north-south)
  - [ospf](#ospf)
  - [fhrp](#fhrp)

## key highlights

Application
- ipam enabled and cannot be disabled
- no extra annotation or label required for [pod](#pod), as long as pod deployed in "cudn namespace", it will be connected to it
- [vm](#vm) needs to be deployed in "cudn namespace" and requires `l2bridge` binding value 

Forwarding
- ip and mac security enforced
- l2 bridging between the applications deployed on the cluster nodes
- east-west service i.e. [cluster ip](#east-west-cluster-ip-service) supported
- [microsegmentation](#east-west-microsegmentation) supported
- [north-south](#north-south) supported
- traffic takes Kubernetes interface e.g., `br-ex` with Geneve encapsulation for e/w and node masquerade for n/s directions

Limitations
- ip and mac security cannot be disabled and that breaks virtual source mac techniques such as [hsrp](../evpn/cudn-l2-v2.md#hsrp), [vrrp](../evpn/cudn-l2-v2.md#vrrp), [glbp](../evpn/cudn-l2-v2.md#glbp)
- static ip address configuration not supported
- mac address must be auto-generated, static mac address configuration breaks ip dhcp

## namespace

- label namespace with `metadata.labels.k8s.ovn.org/primary-user-defined-network = ''`
- add optional label used by [cudn](#cluster-user-defined-network) to select the namespaces by label where cudn is operational
- add optional annotation `k8s.ovn.org/multicast-enabled: 'true'` to enable multicast forwarding

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: l2a
  name: l2
```

## cluster user defined network

Definition
- cluster user defined network selects namespace by label or name
- [namespace](#namespace) is required to be primary-enabled
- `ipam.mode` must be `Enabled` or unset
- IPv4 and/or IPv6 subnets mandatory with max one subnet per address family

What it triggers
- `NetworkAttachmentDefinition` created in every selected namespace
- vrf and ovn instance created on every cluster host

### namespace selected by label

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: my-cudn
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "l2a"
  network:
    topology: Layer2
    layer2:
      role: Primary
      subnets:
      - 66.66.66.0/24
```

### namespace selected by name

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: my-cudn
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - l2
  network:
    topology: Layer2
    layer2:
      role: Primary
      subnets:
      - 66.66.66.0/24
```

### expected status

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-08-11T08:48:40Z"
    message: 'NetworkAttachmentDefinition has been created in following namespaces:
      [l2]'
    reason: NetworkAttachmentDefinitionCreated
    status: "True"
    type: NetworkCreated
  - lastTransitionTime: "2026-08-11T08:48:40Z"
    message: Network allocation succeeded for all synced nodes.
    reason: NetworkAllocationSucceeded
    status: "True"
    type: NetworkAllocationSucceeded
```

### network attachment definition

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "3"
    k8s.ovn.org/network-name: cluster_udn_my-cudn
    k8s.ovn.org/tunnel-keys: '[16711686,16715781]'
  labels:
    k8s.ovn.org/user-defined-network: ""
  name: my-cudn
  namespace: l2
  ownerReferences:
  - apiVersion: k8s.ovn.org/v1
    blockOwnerDeletion: true
    controller: true
    kind: ClusterUserDefinedNetwork
    name: my-cudn
spec:
  config: '
    {
        "cniVersion":"1.1.0",
        "joinSubnet":"100.65.0.0/16,fd99::/64",
        "name":"cluster_udn_my-cudn",
        "netAttachDefName":"l2/my-cudn",
        "role":"primary",
        "subnets":"66.66.66.0/24",
        "topology":"layer2",
        "transitSubnet":"100.88.0.0/16",
        "type":"ovn-k8s-cni-overlay"
    }
  '
```

### vrf

```
[core@bm1-1 l2]$ ip vrf show
Name              Table
-----------------------
my-cudn           1161
```

```
$ ip route show vrf my-cudn
default via 10.10.10.222 dev br-ex mtu 1400 
unreachable default metric 4278198272 
66.66.66.0/24 dev ovn-k8s-mp3 proto kernel scope link src 66.66.66.2 
169.254.0.3 via 66.66.66.1 dev ovn-k8s-mp3 
169.254.0.16 dev ovn-k8s-mp3 mtu 1400 
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

```
162: my-cudn: <NOARP,MASTER,UP,LOWER_UP> mtu 65575 qdisc noqueue state UP group default 
    link/ether 86:a5:3a:cb:91:4f brd ff:ff:ff:ff:ff:ff
```

### ovn

Note: ovn index based on nad `k8s.ovn.org/network-id` annotation

```
$ ip a show vrf my-cudn
161: ovn-k8s-mp3: <BROADCAST,MULTICAST,PROMISC,UP,LOWER_UP> mtu 1400
    link/ether 0a:58:42:42:42:02 brd ff:ff:ff:ff:ff:ff
    inet 66.66.66.2/24 brd 66.66.66.255 scope global ovn-k8s-mp3
```

## ipam

IP Address Management (IPAM) is optional in case of L2 secondary network **only**. As such in the context of primary l2 cluster used-defined network is mandatory with `spec.network.layer2.ipam.mode` set to `Enabled` by default.

IPAM feature not only assigns IP address from `spec.network.layer2.subnets` but also enables
- mac address allocation
- network policy
- service
- IP port security

DHCP-based allocation for [pod](#pod) and [virtual machine](#vm) is **mandatory**. Static IP allocation is not supported and tracked in [feature request](https://access.redhat.com/solutions/7135572)

## pod

There is no need for extra label or annotation, pod can be defined in a usual way. As long as it is deployed in the [namespace](#namespace) labeled as cudn primary and the [cudn](#cluster-user-defined-network) is defined, pod will get its main connection via cudn.

Pod gets IP address and MAC address allocated dynamically based on [ipam](#ipam) settings. Static configuration of ip/mac is not supported.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: t11
  namespace: l2
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
```

Example outcome

```
$ oc describe pod -n l2 t11
Name:             t11
Namespace:        l2
Node:             bm1-1/...
Annotations:      k8s.v1.cni.cncf.io/network-status:
                    [{
                        "name": "ovn-kubernetes",
                        "interface": "eth0",
                        "ips": [
                            "10.128.0.126"
                        ],
                        "mac": "0a:58:0a:80:00:7e",
                        "dns": {}
                    },{
                        "name": "ovn-kubernetes",
                        "interface": "ovn-udn1",
                        "ips": [
                            "66.66.66.6"
                        ],
                        "mac": "0a:58:42:42:42:06",
                        "default": true,
                        "dns": {}
                    }]
```

`ovn-udn1` interface
- the only way in-and-out (routing-wise) for east-west, service and north-south
- veth interface that connects to `ovs-system` when in host network namespace

```
$ oc exec -it -n l2 t11 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP>
2: eth0@if163: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400
    link/ether 0a:58:0a:80:00:7e brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.0.126/23 brd 10.128.1.255 scope global eth0
3: ovn-udn1@if164: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400
    link/ether 0a:58:42:42:42:06 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.66.6/24 brd 66.66.66.255 scope global ovn-udn1
```

```
$ oc exec -it -n l2 t11 -- ip r
default via 66.66.66.1 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.0.126 
10.128.0.0/14 via 10.128.0.1 dev eth0 
66.66.66.0/24 dev ovn-udn1 proto kernel scope link src 66.66.66.6 
100.64.0.0/16 via 10.128.0.1 dev eth0 
100.65.0.0/16 via 66.66.66.1 dev ovn-udn1 
172.30.0.0/16 via 66.66.66.1 dev ovn-udn1 
```

```
$ ip a l if164
164: 2cce5da8de106_3@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue master ovs-system state UP group default 
    link/ether 1a:13:a8:64:99:c8 brd ff:ff:ff:ff:ff:ff link-netns 6bfe97de-97b6-4c1c-8dd7-ce873b4adb24
```

## vm

### Overview

Requirements
- storage e.g., [lvm](../../lvm/README.md), [odf](../../odf/README.md)
- [cnv operator](../../cnv/README.md)

Virtual Machine can connect to cudn as primary interface, the cudn/nad name is not explicitly defined, `l2bridge` binding value is used instead

```yaml
  template:
    spec:
      domain:
        devices:
          interfaces:
          - binding:
              name: l2bridge
            name: default
      networks:
      - name: default
        pod: {}
```

Virtual machine gets IP address and MAC address allocated dynamically based on [ipam](#ipam) settings. Static configuration of ip/mac is not supported.

Even if technicaly speaking, mac address can be defined e.g.

```yaml
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
          - name: default
            macAddress: '02:85:38:00:00:0b'
```

then ip address allocation fails, probably since internal dhcp server is not configured with lease for manually defined mac address

```
c8kv3#show interfaces gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up
  Hardware is vNIC, address is 0285.3800.000b (bia 0285.3800.000b)
  Internet address will be negotiated using DHCP  <<< and it's not >>>
```

If data volume source is in another namespace, then clone operation must be allowed from source namespace e.g., `default` to target cudn namespace e.g., `l2`

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: datavolume-cloner
rules:
- apiGroups: ["cdi.kubevirt.io"]
  resources: ["datavolumes/source"]
  verbs: ["*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: my-cudn-cloner
  namespace: default
subjects:
- kind: ServiceAccount
  name: default
  namespace: l2
roleRef:
  kind: ClusterRole
  name: datavolume-cloner 
  apiGroup: rbac.authorization.k8s.io
```

### Example: cat8kv

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: c8kv1-day0
  namespace: l2
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
    ip http secure-server
    line con 0
      length 0
    line vty 0 4
      length 0
---
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: l2
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: l2
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
        pvc:
          namespace: default
          name: c8kv
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
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv1
      networks:
      - name: default
        pod: {}
      nodeSelector:
        kubernetes.io/hostname: bm1-2
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: l2
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: l2
        name: day0
```

Virtlauncher pod shows the allocated ip address for `ovn-udn1` interface that is also provided to virtual machine **using dhcp**

```
$ oc describe pod -n l2 virt-launcher-c8kv1-lzbm4
Name:              virt-launcher-c8kv1-lzbm4
Namespace:         l2
Annotations:       k8s.v1.cni.cncf.io/network-status:
                     [{
                         "name": "ovn-kubernetes",
                         "interface": "eth0",
                         "ips": [
                             "10.128.0.131"
                         ],
                         "mac": "0a:58:0a:80:00:83",
                         "dns": {}
                     },{
                         "name": "ovn-kubernetes",
                         "interface": "ovn-udn1",
                         "ips": [
                             "66.66.66.10"
                         ],
                         "mac": "0a:58:42:42:42:0a",
                         "default": true,
                         "dns": {}
                     }]
```

State of the configured interface, note that vm has the same mac and ip on its primary interface as seen on the virt-launcher pod level due to `l2bridge` connectivity mode.

```
c8kv1#show int gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up 
  Hardware is vNIC, address is 0a58.4242.420a (bia 0a58.4242.420a)
  Internet address is 66.66.66.10/24
```

DHCP on-the-wire captured on veth interface paired with `ovn-udn1`

```
09:33:58.564931 0a:58:42:42:42:0a > ff:ff:ff:ff:ff:ff, ethertype IPv4 (0x0800), length 358: (tos 0x0, ttl 255, id 62, offset 0, flags [none], proto UDP (17), length 344)
    0.0.0.0.68 > 255.255.255.255.67: BOOTP/DHCP, Request from 0a:58:42:42:42:0a, length 316, xid 0x1e9e, secs 3, Flags [Broadcast]
          Client-Ethernet-Address 0a:58:42:42:42:0a
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: Discover
            MSZ (57), length 2: 1200
            Client-ID (61), length 25: "cisco-0a58.4242.420a-Gi1"
            Hostname (12), length 5: "c8kv1"
            Parameter-Request (55), length 8: 
              Subnet-Mask (1), Domain-Name-Server (6), Domain-Name (15), Netbios-Name-Server (44)
              Default-Gateway (3), Static-Route (33), TFTP-Server-Address (150), Vendor-Option (43)
            Vendor-Class (60), length 8: "ciscopnp"
            Unknown (124), length 12: 9,117850936,808464470
09:33:58.567452 0a:58:a9:fe:01:01 > 0a:58:42:42:42:0a, ethertype IPv4 (0x0800), length 335: (tos 0x0, ttl 255, id 62, offset 0, flags [none], proto UDP (17), length 321)
    169.254.1.1.67 > 255.255.255.255.68: BOOTP/DHCP, Reply, length 293, xid 0x1e9e, secs 3, Flags [Broadcast]
          Your-IP 66.66.66.10
          Client-Ethernet-Address 0a:58:42:42:42:0a
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: Offer
            Domain-Name-Server (6), length 4: 172.30.0.10
            Hostname (12), length 5: "c8kv1"
            Lease-Time (51), length 4: 3500
            MTU (26), length 2: 1400
            Subnet-Mask (1), length 4: 255.255.255.0
            Default-Gateway (3), length 4: 66.66.66.1
            Server-ID (54), length 4: 169.254.1.1
09:33:58.568092 0a:58:42:42:42:0a > ff:ff:ff:ff:ff:ff, ethertype IPv4 (0x0800), length 376: (tos 0x0, ttl 255, id 63, offset 0, flags [none], proto UDP (17), length 362)
    0.0.0.0.68 > 255.255.255.255.67: BOOTP/DHCP, Request from 0a:58:42:42:42:0a, length 334, xid 0x1e9e, Flags [Broadcast]
          Client-Ethernet-Address 0a:58:42:42:42:0a
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: Request
            MSZ (57), length 2: 1200
            Client-ID (61), length 25: "cisco-0a58.4242.420a-Gi1"
            Server-ID (54), length 4: 169.254.1.1
            Requested-IP (50), length 4: 66.66.66.10
            Lease-Time (51), length 4: 3500
            Hostname (12), length 5: "c8kv1"
            Parameter-Request (55), length 8: 
              Subnet-Mask (1), Domain-Name-Server (6), Domain-Name (15), Netbios-Name-Server (44)
              Default-Gateway (3), Static-Route (33), TFTP-Server-Address (150), Vendor-Option (43)
            Vendor-Class (60), length 8: "ciscopnp"
            Unknown (124), length 12: 9,117850936,808464470
09:33:58.568331 0a:58:a9:fe:01:01 > 0a:58:42:42:42:0a, ethertype IPv4 (0x0800), length 335: (tos 0x0, ttl 255, id 63, offset 0, flags [none], proto UDP (17), length 321)
    169.254.1.1.67 > 255.255.255.255.68: BOOTP/DHCP, Reply, length 293, xid 0x1e9e, Flags [Broadcast]
          Your-IP 66.66.66.10
          Client-Ethernet-Address 0a:58:42:42:42:0a
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: ACK
            Domain-Name-Server (6), length 4: 172.30.0.10
            Hostname (12), length 5: "c8kv1"
            Lease-Time (51), length 4: 3500
            MTU (26), length 2: 1400
            Subnet-Mask (1), length 4: 255.255.255.0
            Default-Gateway (3), length 4: 66.66.66.1
            Server-ID (54), length 4: 169.254.1.1
09:33:58.568611 0a:58:42:42:42:0a > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Reply 66.66.66.10 is-at 0a:58:42:42:42:0a, length 46
09:34:01.570972 0a:58:42:42:42:0a > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Reply 66.66.66.10 is-at 0a:58:42:42:42:0a, length 46
09:34:01.574157 0a:58:42:42:42:0a > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Request who-has 66.66.66.1 tell 66.66.66.10, length 46
09:34:01.575619 0a:58:42:42:42:01 > 0a:58:42:42:42:0a, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Reply 66.66.66.1 is-at 0a:58:42:42:42:01, length 46
```

## arp resolution

In order to verify arp resolution, ping test from vm deployed on `bm1-1` node to pod deployed on another node

Initial arp table state

```
c8kv1#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  66.66.66.1              2   0a58.4242.4201  ARPA   GigabitEthernet1
Internet  66.66.66.10             -   0a58.4242.420a  ARPA   GigabitEthernet1
```

Connection test

```
c8kv1#ping 66.66.66.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 66.66.66.8, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/2/5 ms
```

Checking `ovn-udn1` interface, arp request is sent and responded to

```
09:37:50.876869 0a:58:42:42:42:0a > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Request who-has 66.66.66.8 tell 66.66.66.10, length 46
09:37:50.878669 0a:58:42:42:42:08 > 0a:58:42:42:42:0a, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Reply 66.66.66.8 is-at 0a:58:42:42:42:08, length 46
```

However, this arp request it **not** sent over the wire and clearly (tcpdump as an evidence) does not reach the destination pod. Since OpenShift is aware of all ip/mac allocations, it is likely responded locally (timestamp confirms that behavior too i.e. too quick).

## east west unicast

Following [arp resolution](#arp-resolution) test setup and successful ping between two applications deployed on different cluster nodes, tcpdump confirms that communication between the cudn members is using Kubernetes standard interfaces, `br-ex` in this case, with Geneve encapsulation, using the `vni` value as defined in [network attachment definition](#network-attachment-definition) `tunnel-keys` property

```
10.10.10.210.20043 > 10.10.10.212.6081: Geneve, Flags [C], vni 0xff0006
  0a:58:42:42:42:0a > 0a:58:42:42:42:08, ethertype IPv4 (0x0800)
    66.66.66.10 > 66.66.66.8: ICMP echo request, id 13, seq 7236, length 80

10.10.10.212.14070 > 10.10.10.210.6081: Geneve, Flags [C], vni 0xff0006
  0a:58:42:42:42:08 > 0a:58:42:42:42:0a, ethertype IPv4 (0x0800)
    66.66.66.8 > 66.66.66.10: ICMP echo reply, id 13, seq 7236, length 80
```

## east-west cluster ip service

east-west connectivity test in [previous step](#east-west-unicast) was performed using pod ip address directly, let's check the service

New nginx pod deployed on node bm1-3 with associated service

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: l2
  labels:
    app: nginx
spec:
  nodeName: bm1-3
  containers:
  - name: nginx
    image: nginxinc/nginx-unprivileged
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: l2
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - name: http
    port: 80
    targetPort: 8080
```

Outcome

Name | Node | IP | MAC
--- | --- | --- | --- 
t11 | bm1-1 | 66.66.66.6/24 | 0a:58:42:42:42:06
nginx | bm1-3 | 66.66.66.13/24 | 0a:58:42:42:42:0d

```
$ oc get service -n l2 -o wide
NAME    TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE    SELECTOR
nginx   NodePort   172.30.142.21   <none>        80:30540/TCP   2m3s   app=nginx
```

```
$ oc get ep -n l2
NAME    ENDPOINTS           AGE
nginx   10.129.0.168:8080   2m20s
```

Functional test
- source `t11` with 66.66.66.6
- destination cluster ip service 172.30.142.21 
- `nginx` pod with 66.66.66.13 as service endpoint

```
$ oc exec -it -n l2 t11 -- curl 172.30.142.21
<!DOCTYPE html>
<html>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

Originating pod route table has route entry to service cidr via `ovn-udn1` interface as such traffic takes "cudn tranport" path

```
$ oc exec -it -n l2 t11 -- ip r
default via 66.66.66.1 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.0.126 
10.128.0.0/14 via 10.128.0.1 dev eth0 
66.66.66.0/24 dev ovn-udn1 proto kernel scope link src 66.66.66.6 
100.64.0.0/16 via 10.128.0.1 dev eth0 
100.65.0.0/16 via 66.66.66.1 dev ovn-udn1 
172.30.0.0/16 via 66.66.66.1 dev ovn-udn1 <<< that's the one >>>
```

### ovn-udn1 interface i.e. inside originating pod

Service ip seen in both direections

```
$ oc exec -it -n l2 t11 -- tcpdump -i ovn-udn1 -n -nn
11:26:27.582303 IP 66.66.66.6.60302 > 172.30.142.21.80: Flags [S], seq 3531475941
11:26:27.586829 IP 172.30.142.21.80 > 66.66.66.6.60302: Flags [S.], seq 3035541414, ack 3531475942
```

### on-the-wire

Service ip is resolved to endpoint ip address before packets hits the `br-ex` wire so the communication is like in [east west connectivity](#east-west-unicast) analysis.

```
10.10.10.210.8172 > 10.10.10.212.6081: Geneve, Flags [C], vni 0xff0006
  0a:58:42:42:42:01 > 0a:58:42:42:42:0d, ethertype IPv4 (0x0800)
    66.66.66.6.36338 > 66.66.66.13.8080: Flags [S], cksum 0xb340 (correct), seq 3186827363
```

Note: Geneve encapsulated Ethernet frame has source mac of anycast gateway

## east-west microsegmentation

Following the previous [cluster ip service](#east-west-cluster-ip-service) test, let's add the rule that only `t12` pod should be able to reach `nginx` either directly using pod ip address or via cluster ip (service), even if all pods are in the same cudn and should be able to talk to each other.

Initial state

```
$ oc get pod -n l2 -o wide
NAME               READY   STATUS    RESTARTS   AGE    IP             NODEGATES
nginx              1/1     Running   0          12m    10.129.0.168   bm7-3
t11                1/1     Running   0          148m   10.128.0.126   bm7-1
t12                1/1     Running   0          148m   10.130.0.118   bm7-2
t13                1/1     Running   0          148m   10.129.0.162   bm7-3
```

```
$ oc get service -n l2 -o wide
NAME    TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE    SELECTOR
nginx   NodePort   172.30.142.21   <none>        80:30540/TCP   2m3s   app=nginx
```

```
$ oc get ep -n l2
NAME    ENDPOINTS           AGE
nginx   10.129.0.168:8080   2m20s
```

Pod `t12` is labeled with `nginx=enabled`

```
$ oc label pod -n l2 t12 nginx=enabled
pod/t12 labeled
```

`nginx` pod is already labeled with `app=ginx` for service selector.

New `NetworkPolicy` object implemeting the desired microsegmentation scenario

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-t12
  namespace: l2
spec:
  podSelector:
    matchLabels:
      app: nginx
  ingress:
  - from:
    - podSelector:
        matchLabels:
          nginx: enabled
    ports:
    - protocol: TCP
      port: 8080
```

Pod `t12` is allowed to reach `nginx` application directly or via service

```
$ oc exec -it -n l2 t12 -- curl -v 172.30.142.21
*   Trying 172.30.142.21:80...
* Established connection to 172.30.142.21 (172.30.142.21 port 80) from 66.66.66.7 port 5162

$ oc exec -it -n l2 t12 -- curl -v 66.66.66.13:8080
*   Trying 66.66.66.13:8080...
* Established connection to 66.66.66.13 (66.66.66.13 port 8080) from 66.66.66.7 port 41978
```

Any other pod in the same cudn times out on such connection

```
$ oc exec -it -n l2 t11 -- curl -v 172.30.142.21
*   Trying 172.30.142.21:80...

$ oc exec -it -n l2 t11 -- curl -v 66.66.66.13:8080
*   Trying 66.66.66.13:8080...
```

## north-south

Any connection that leaves the cluster i.e. north-south, follows standard source ip masqeurade operation with the cluster node ip address e.g.,

```
$ oc exec -it -n l2 t11 -- ssh cisco@20.20.20.207
cisco@20.20.20.207's password: 
```

On the ssh server

```
$ netstat -na | grep ESTABL
tcp        0      0 20.20.20.207:22         10.10.10.210:59322      ESTABLISHED
```

# ospf

>[!NOTE]
>Requires [namespace](#namespace) multicast annotation

>[!CAUTION]
>Link local multicast (224.0.0.x) works within namespace only, not across namespaces

VM | Node | IP | MAC
--- | --- | --- | --- 
c8kv1 | bm1-1 | 66.66.66.10/24 | 0a:58:42:42:42:0a
c8kv2 | bm1-2 | 66.66.66.11/24 | 0a:58:42:42:42:0b

Configuration c8kv1

```
interface GigabitEthernet1
 ip address dhcp
 negotiation auto
!
router ospf 1
 network 66.66.66.0 0.0.0.255 area 0
```

Configuration c8kv2

```
interface GigabitEthernet1
 ip address dhcp
 negotiation auto
!
router ospf 1
 network 66.66.66.0 0.0.0.255 area 0
```

OSPF neighborship is formed correctly

```
c8kv1#show ip ospf nei

Neighbor ID     Pri   State           Dead Time   Address         Interface
66.66.66.11       1   FULL/DR         00:00:31    66.66.66.11     GigabitEthernet1
```

Hello sent by `c8kv1` on-the-wire interface `br-ex` on node `bm1-1`

```
10.10.10.210.5779 > 10.10.10.211.6081: Geneve, Flags [C], vni 0xff0006
  0a:58:42:42:42:0a > 01:00:5e:00:00:05, ethertype IPv4 (0x0800), proto OSPF (89)
    66.66.66.10 > 224.0.0.5: OSPFv2, Hello, length 80 [len 48]
      Router-ID 66.66.66.10, Backbone Area, Authentication Type: none (0)
      Options [External, LLS]
        Hello Timer 10s, Dead Timer 40s, Mask 255.255.255.0, Priority 1
        Designated Router 66.66.66.11, Backup Designated Router 66.66.66.10
        Neighbor List:
          66.66.66.11
        LLS: checksum: 0x7fc0, length: 8
          Extended Options (1), length: 4
            Options: 0x00000001 [LSDB resync]
          Unknown TLV (18), length: 4
          Unknown TLV (32768), length: 8
```

# fhrp

First hop redundancy protocol such as [hsrp](../evpn/cudn-l2-v2.md#hsrp), [vrrp](../evpn/cudn-l2-v2.md#vrrp), [glbp](../evpn/cudn-l2-v2.md#glbp) are broken.

[[Back]](../README.md)