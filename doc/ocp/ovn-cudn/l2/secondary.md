# Secondary l2 cluster user-defined networks

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
  - [ospf](#ospf)
  - [fhrp](#fhrp)

## key highlights

Application
- ipam enabled by default and can be disabled
- pod annotation selecting cudn network attachment definition as secondary interface
- vm definition selecting cudn network attachment definition as secondary interface

Forwarding
- default routing via primary interface incl. east-west services and north-south egress
- configured secondary subnet only via secondary interface
  - ip and mac security enforced
  - l2 bridging between the applications deployed on the cluster nodes
- both primary and secondary network inter-node traffic takes Kubernetes interface e.g., `br-ex` with Geneve encapsulation

Differences from [primary](./primary.md)
- no vrf or dedicated ovn instance created on the host
- no support for service
- no north-south (egress) 
- `NetworkAttachmentDefinition` without `tunnel-keys`

Limitations for ipam enabled
- ip and mac security cannot be disabled and that breaks virtual source mac techniques such as [hsrp](../evpn/cudn-l2-v2.md#hsrp), [vrrp](../evpn/cudn-l2-v2.md#vrrp), [glbp](../evpn/cudn-l2-v2.md#glbp)
- static ip address configuration not supported
- mac address must be auto-generated, static mac address configuration breaks ip dhcp
- no policy can be configured i.e. `NetworkPolicy` and `MultinetworkPolicy` unsupported

## namespace

- add optional label used by [cudn](#cluster-user-defined-network) to select the namespaces by label where cudn is operational
- add optional annotation `k8s.ovn.org/multicast-enabled: 'true'` to enable multicast forwarding

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    tenant: l2
  name: l2
```

## cluster user defined network

Definition
- cluster user defined network selects namespace by label or name
- [namespace](#namespace) must not be primary-enabled
- `ipam.mode` can be `Disabled` with the default `Enabled`
- IPv4 and/or IPv6 subnets mandatory if ipam is enabled, with max one subnet per address family

What it triggers
- `NetworkAttachmentDefinition` created in every selected namespace however, without tunnel-keys defined like in [primary](./primary.md)

Note: no vrf or ovn instance created

### namespace selected by label

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: my-cudn
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "l2"
  network:
    topology: Layer2
    layer2:
      role: Secondary
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
      role: Secondary
      subnets:
      - 66.66.66.0/24
```

### ipam disabled

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: my-cudn
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "l2"
  network:
    topology: Layer2
    layer2:
      role: Secondary
      ipam:
        mode: Disabled
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

### network attachment definition with ipam enabled

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "4"
    k8s.ovn.org/network-name: cluster_udn_my-cudn
    k8s.ovn.org/tunnel-keys: '[]'
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
      "name":"cluster_udn_my-cudn",
      "netAttachDefName":"l2/my-cudn",
      "role":"secondary",
      "subnets":"66.66.66.0/24",
      "topology":"layer2",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

### network attachment definition with ipam disabled

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "5"
    k8s.ovn.org/network-name: cluster_udn_my-cudn
    k8s.ovn.org/tunnel-keys: '[]'
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
      "name":"cluster_udn_my-cudn",
      "netAttachDefName":"l2/my-cudn",
      "role":"secondary",
      "topology":"layer2",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

## ipam

IP Address Management (IPAM) is optional in case of L2 secondary network and controlled with `spec.network.layer2.ipam.mode` set to `Enabled` by default.

### enabled

IPAM feature not only assigns IP address from `spec.network.layer2.subnets` but also enables
- mac address allocation
- network policy
- service
- IP port security

DHCP-based allocation for [pod](#pod-with-ipam-enabled) and [virtual machine](#example-cat8kv-with-ipam-enabled) is **mandatory**. Static IP allocation is not supported and tracked in [feature request](https://access.redhat.com/solutions/7135572)

### disabled

Since IPAM feature is disabled, you can assign any IP address for [pod](#pod-with-ipam-disabled) and [virtual machine](#example-cat8kv-with-ipam-disabled)

As the consoquence, IP port security is disabled, while mac address security is still enforced. That alone allows hsrp with use-bia to work.

## pod 

### pod with ipam enabled

Pod definition must select [network attachment definition](#network-attachment-definition) created by [cudn](#cluster-user-defined-network)

```yaml
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: my-cudn
```

Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: t11
  namespace: l2
  annotations:
    k8s.v1.cni.cncf.io/networks: my-cudn
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

Example outcome, not that ovn-k\eth0 interface is annotated as default one

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
                            "10.128.0.134"
                        ],
                        "mac": "0a:58:0a:80:00:86",
                        "default": true,
                        "dns": {}
                    },{
                        "name": "l2/my-cudn",
                        "interface": "net1",
                        "ips": [
                            "66.66.66.1"
                        ],
                        "mac": "0a:58:42:42:42:01",
                        "dns": {}
                    }]
```

`eth0` interface remains the main/default way in-and-out (routing-wise) for east-west, service and north-south,  `net1` interface connects the pod to configured l2 cudn subnet. `net1` is veth interface type that connects to `ovs-system` when in host network namespace

```
$ oc exec -it -n l2 t11 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if173: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400
    link/ether 0a:58:0a:80:00:86 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.0.134/23 brd 10.128.1.255 scope global eth0
3: net1@if174: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400
    link/ether 0a:58:42:42:42:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.66.1/24 brd 66.66.66.255 scope global net1
```

```
$ oc exec -it -n l2 t11 -- ip r
default via 10.128.0.1 dev eth0 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.0.134 
10.128.0.0/14 via 10.128.0.1 dev eth0 
66.66.66.0/24 dev net1 proto kernel scope link src 66.66.66.1 
100.64.0.0/16 via 10.128.0.1 dev eth0 
169.254.0.5 via 10.128.0.1 dev eth0 
172.30.0.0/16 via 10.128.0.1 dev eth0 
```

```
$ ip a l if174
174: 271aea4d203b2_3@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue master ovs-system state UP group default 
    link/ether ae:c4:b5:10:ca:de brd ff:ff:ff:ff:ff:ff link-netns d9686336-524b-4590-9c1b-c6a974ab1e08
```

### pod with ipam disabled

Pod definition must select [network attachment definition](#network-attachment-definition) created by [cudn](#cluster-user-defined-network) **and** define ip address

```yaml
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: '[ { "name": "my-cudn", "ips": [ "66.66.66.1/24" ] } ]'
```

Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: t11
  namespace: l2
  annotations:
    k8s.v1.cni.cncf.io/networks: '[ { "name": "my-cudn", "ips": [ "66.66.66.1/24" ] } ]'
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

Example outcome, not that ovn-k\eth0 interface is annotated as default one

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
                            "10.128.0.215"
                        ],
                        "mac": "0a:58:0a:80:00:d7",
                        "default": true,
                        "dns": {}
                    },{
                        "name": "l2/my-cudn",
                        "interface": "net1",
                        "ips": [
                            "66.66.66.1"
                        ],
                        "mac": "0a:58:42:42:42:01",
                        "dns": {}
                    }]
                  k8s.v1.cni.cncf.io/networks: [ { "name": "my-cudn", "ips": [ "66.66.66.1/24" ] } ]
```

`eth0` interface remains the main/default way in-and-out (routing-wise) for east-west, service and north-south,  `net1` interface connects the pod to configured l2 cudn subnet with manually configured ip address. `net1` is veth interface type that connects to `ovs-system` when in host network namespace

```
$ oc exec -it -n l2 t11 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if217: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default qlen 1000
    link/ether 0a:58:0a:80:00:d7 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.0.215/23 brd 10.128.1.255 scope global eth0
3: net1@if218: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default qlen 1000
    link/ether 0a:58:42:42:42:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.66.1/24 brd 66.66.66.255 scope global net1
```

```
$ oc exec -it -n l2 t11 -- ip r
default via 10.128.0.1 dev eth0 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.0.215 
10.128.0.0/14 via 10.128.0.1 dev eth0 
66.66.66.0/24 dev net1 proto kernel scope link src 66.66.66.1 
100.64.0.0/16 via 10.128.0.1 dev eth0 
169.254.0.5 via 10.128.0.1 dev eth0 
172.30.0.0/16 via 10.128.0.1 dev eth0 
```

```
$ ip a l if218
218: d17ff8530aa63_3@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue master ovs-system state UP group default 
    link/ether 7e:1c:6d:d0:d1:cb brd ff:ff:ff:ff:ff:ff link-netns 2584dadc-8344-4a4b-8921-c49f9938a68f
```

## vm

### Overview

Requirements
- storage e.g., [lvm](../../lvm/README.md), [odf](../../odf/README.md)
- [cnv operator](../../cnv/README.md)

Virtual Machine can connect to cudn as secondary interface via Multus network using [nad](#network-attachment-definition) reference

```yaml
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: net1
      networks:
      - multus:
          networkName: l2/my-cudn
        name: net1
```

Virtual machine gets IP address and MAC address allocated dynamically based on [ipam](#ipam) settings. 

Static configuration of ip/mac is supported if ipam is disabled.

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

### Example: cat8kv with ipam enabled

cat8kv instance is configured with dhcp on both interface
- primary that connects to pod network in masquerade mode
- secondary that connects to l2 cudn

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
    interface GigabitEthernet2
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
          - name: default
            masquerade: {}
          - name: net1
            bridge: {}
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv1
      networks:
      - name: default
        pod: {}
      - name: net1
        multus:
          networkName: l2/my-cudn
      nodeSelector:
        kubernetes.io/hostname: bm1-1
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

Virtlauncher pod shows the allocated ip address for both interfaces

```
$ oc describe pod -n l2 virt-launcher-c8kv1-crts2
Name:              virt-launcher-c8kv1-crts2
Namespace:         l2
Annotations:       k8s.v1.cni.cncf.io/network-status:
                     [{
                         "name": "ovn-kubernetes",
                         "interface": "eth0",
                         "ips": [
                             "10.128.0.140"
                         ],
                         "mac": "0a:58:0a:80:00:8c",
                         "default": true,
                         "dns": {}
                     },{
                         "name": "l2/my-cudn",
                         "interface": "pod6c270ef2f25",
                         "ips": [
                             "66.66.66.7"
                         ],
                         "mac": "02:9a:2a:20:c8:6c",
                         "dns": {}
                     }]
```

The same state is "inside the vm"

```
c8kv1#show int gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up 
  Hardware is vNIC, address is 029a.2a20.c86b (bia 029a.2a20.c86b)
  Internet address is 10.0.2.2/24

c8kv1#show int gigabitEthernet 2
GigabitEthernet2 is up, line protocol is up 
  Hardware is vNIC, address is 029a.2a20.c86c (bia 029a.2a20.c86c)
  Internet address is 66.66.66.7/24
```

Routing table has default with ovn-k interface and connected subnet via multus interface

```
c8kv1#show ip route
Gateway of last resort is 10.0.2.1 to network 0.0.0.0

S*    0.0.0.0/0 [254/0] via 10.0.2.1
      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        10.0.2.0/24 is directly connected, GigabitEthernet1
L        10.0.2.2/32 is directly connected, GigabitEthernet1
      66.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        66.66.66.0/24 is directly connected, GigabitEthernet2
L        66.66.66.7/32 is directly connected, GigabitEthernet2
```

DHCP on-the-wire captured on veth interface paired with `net1`

```
13:26:49.846443 02:9a:2a:20:c8:6c > ff:ff:ff:ff:ff:ff, ethertype IPv4 (0x0800), length 358: (tos 0x0, ttl 255, id 19, offset 0, flags [none], proto UDP (17), length 344)
    0.0.0.0.68 > 255.255.255.255.67: BOOTP/DHCP, Request from 02:9a:2a:20:c8:6c, length 316, xid 0xf84, secs 3, Flags [Broadcast]
          Client-Ethernet-Address 02:9a:2a:20:c8:6c
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: Discover
            MSZ (57), length 2: 1200
            Client-ID (61), length 25: "cisco-029a.2a20.c86c-Gi2"
            Hostname (12), length 5: "c8kv1"
            Parameter-Request (55), length 8: 
              Subnet-Mask (1), Domain-Name-Server (6), Domain-Name (15), Netbios-Name-Server (44)
              Default-Gateway (3), Static-Route (33), TFTP-Server-Address (150), Vendor-Option (43)
            Vendor-Class (60), length 8: "ciscopnp"
            Unknown (124), length 12: 9,117850936,808464470
13:26:49.846627 be:9d:43:3e:a5:9b > ff:ff:ff:ff:ff:ff, ethertype IPv4 (0x0800), length 444: (tos 0x0, ttl 64, id 40815, offset 0, flags [DF], proto UDP (17), length 430)
    169.254.75.11.67 > 255.255.255.255.68: BOOTP/DHCP, Reply, length 402, xid 0xf84, Flags [Broadcast]
          Your-IP 66.66.66.7
          Client-Ethernet-Address 02:9a:2a:20:c8:6c
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: Offer
            Server-ID (54), length 4: 169.254.75.11
            Lease-Time (51), length 4: 86313600
            Unknown (119), length 94: 620,12803,29558,25351,25452,30067,29797,29189,27759,25441,27648,883,30307,1891,27765,29556,25970,1388,28515,24940,7,25452,30067,29797,29189,27759,25441,27648,866,27959,879,25456,1893,28005,24877,29552,1379,26995,25455,867,28525,5,25449,29539,28419,25455,27904
            Hostname (12), length 5: "c8kv1"
            Domain-Name (15), length 25: "bm1.ocp.domain.com"
            Domain-Name-Server (6), length 4: 172.30.0.10
            MTU (26), length 2: 1400
            Subnet-Mask (1), length 4: 255.255.255.0
13:26:49.847243 02:9a:2a:20:c8:6c > ff:ff:ff:ff:ff:ff, ethertype IPv4 (0x0800), length 376: (tos 0x0, ttl 255, id 20, offset 0, flags [none], proto UDP (17), length 362)
    0.0.0.0.68 > 255.255.255.255.67: BOOTP/DHCP, Request from 02:9a:2a:20:c8:6c, length 334, xid 0xf84, Flags [Broadcast]
          Client-Ethernet-Address 02:9a:2a:20:c8:6c
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: Request
            MSZ (57), length 2: 1200
            Client-ID (61), length 25: "cisco-029a.2a20.c86c-Gi2"
            Server-ID (54), length 4: 169.254.75.11
            Requested-IP (50), length 4: 66.66.66.7
            Lease-Time (51), length 4: 86313600
            Hostname (12), length 5: "c8kv1"
            Parameter-Request (55), length 8: 
              Subnet-Mask (1), Domain-Name-Server (6), Domain-Name (15), Netbios-Name-Server (44)
              Default-Gateway (3), Static-Route (33), TFTP-Server-Address (150), Vendor-Option (43)
            Vendor-Class (60), length 8: "ciscopnp"
            Unknown (124), length 12: 9,117850936,808464470
13:26:49.847359 be:9d:43:3e:a5:9b > ff:ff:ff:ff:ff:ff, ethertype IPv4 (0x0800), length 444: (tos 0x0, ttl 64, id 40816, offset 0, flags [DF], proto UDP (17), length 430)
    169.254.75.11.67 > 255.255.255.255.68: BOOTP/DHCP, Reply, length 402, xid 0xf84, Flags [Broadcast]
          Your-IP 66.66.66.7
          Client-Ethernet-Address 02:9a:2a:20:c8:6c
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message (53), length 1: ACK
            Server-ID (54), length 4: 169.254.75.11
            Lease-Time (51), length 4: 86313600
            Unknown (119), length 94: 620,12803,29558,25351,25452,30067,29797,29189,27759,25441,27648,883,30307,1891,27765,29556,25970,1388,28515,24940,7,25452,30067,29797,29189,27759,25441,27648,866,27959,879,25456,1893,28005,24877,29552,1379,26995,25455,867,28525,5,25449,29539,28419,25455,27904
            Hostname (12), length 5: "c8kv1"
            Domain-Name (15), length 25: "bm1.ocp.domain.com"
            Domain-Name-Server (6), length 4: 172.30.0.10
            MTU (26), length 2: 1400
            Subnet-Mask (1), length 4: 255.255.255.0
13:26:49.847550 02:9a:2a:20:c8:6c > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Reply 66.66.66.7 is-at 02:9a:2a:20:c8:6c, length 46
13:26:52.850460 02:9a:2a:20:c8:6c > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Ethernet (len 6), IPv4 (len 4), Reply 66.66.66.7 is-at 02:9a:2a:20:c8:6c, length 46
```

### Example: cat8kv with ipam disabled

cat8kv instance is configured with dhcp on primary interface and static ip address on secondary interace via day0 configuraiton i.e. **not** via `VirtualMachine`
- primary that connects to pod network in masquerade mode
- secondary that connects to l2 cudn

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
    interface GigabitEthernet2
      ip address 66.66.66.10 255.255.255.0
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
          - name: default
            masquerade: {}
          - name: net1
            bridge: {}
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv1
      networks:
      - name: default
        pod: {}
      - name: net1
        multus:
          networkName: l2/my-cudn
      nodeSelector:
        kubernetes.io/hostname: bm1-1
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

Virtlauncher pod shows the allocated ip address for primary interfaces only

```
$ oc describe pod -n l2 virt-launcher-c8kv1-crts2
Name:              virt-launcher-c8kv1-crts2
Namespace:         l2
Annotations:       k8s.v1.cni.cncf.io/network-status:
                   k8s.v1.cni.cncf.io/network-status:
                     [{
                         "name": "ovn-kubernetes",
                         "interface": "eth0",
                         "ips": [
                             "10.128.0.219"
                         ],
                         "mac": "0a:58:0a:80:00:db",
                         "default": true,
                         "dns": {}
                     },{
                         "name": "l2/my-cudn",
                         "interface": "pod6c270ef2f25",
                         "mac": "02:9a:2a:06:dd:f1",
                         "dns": {}
                     }]
```

The state is "inside the vm" is reflecting the combination of dhcp and static ip address assignment

```
c8kv1#show int gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up 
  Hardware is vNIC, address is 029a.2a06.ddf0 (bia 029a.2a06.ddf0)
  Internet address is 10.0.2.2/24

c8kv1#show int gigabitEthernet 2
GigabitEthernet2 is up, line protocol is up 
  Hardware is vNIC, address is 029a.2a06.ddf1 (bia 029a.2a06.ddf1)
  Internet address is 66.66.66.10/24
```

Routing table has default with ovn-k interface and connected subnet via multus interface

```
c8kv1#show ip route
Gateway of last resort is 10.0.2.1 to network 0.0.0.0

S*    0.0.0.0/0 [254/0] via 10.0.2.1
      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        10.0.2.0/24 is directly connected, GigabitEthernet1
L        10.0.2.2/32 is directly connected, GigabitEthernet1
      66.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        66.66.66.0/24 is directly connected, GigabitEthernet2
L        66.66.66.10/32 is directly connected, GigabitEthernet2
```

## arp resolution

In order to verify arp resolution, ping test from vm deployed on `bm1-1` node to pod deployed on another node

Initial arp table state

```
c8kv1>show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.0.2.1               18   0200.0000.0000  ARPA   GigabitEthernet1
Internet  10.0.2.2                -   029a.2a20.c86b  ARPA   GigabitEthernet1
Internet  66.66.66.7              -   029a.2a20.c86c  ARPA   GigabitEthernet
```

Connection test

```
c8kv1>ping 66.66.66.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 66.66.66.2, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/4 ms
```

Checking `net1` interface, arp request is sent and responded to

```
13:41:24.185968 02:9a:2a:20:c8:6c > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806)
  Request who-has 66.66.66.2 tell 66.66.66.7, length 46

13:41:24.186368 0a:58:42:42:42:02 > 02:9a:2a:20:c8:6c, ethertype ARP (0x0806)
  Reply 66.66.66.2 is-at 0a:58:42:42:42:02, length 46
```

However, this arp request it **not** sent over the wire and clearly (tcpdump as an evidence) does not reach the destination pod. Since OpenShift is aware of all ip/mac allocations, it is likely responded locally.

The first ping may time-out due to the behavior on the receiving side, that sends arp request upon receiving the first echo request e.g.,

```
13:41:26.186736 02:9a:2a:20:c8:6c > 0a:58:42:42:42:02, ethertype IPv4 (0x0800)
  66.66.66.7 > 66.66.66.2: ICMP echo request, id 1, seq 1, length 80

13:41:26.186764 0a:58:42:42:42:02 > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806)
  Request who-has 66.66.66.7 tell 66.66.66.2, length 28

13:41:26.187092 02:9a:2a:20:c8:6c > 0a:58:42:42:42:02, ethertype ARP (0x0806)
  Reply 66.66.66.7 is-at 02:9a:2a:20:c8:6c, length 28

13:41:26.187100 0a:58:42:42:42:02 > 02:9a:2a:20:c8:6c, ethertype IPv4 (0x0800)
  66.66.66.2 > 66.66.66.7: ICMP echo reply, id 1, seq 1, length 80
```

Similarly to arp request sent by cat8kv, the arp request sent by pod is **not** sent over the wire and does not reach cat8kv instance.

## east west unicast

Following [arp resolution](#arp-resolution) test setup and successful ping between two applications deployed on different cluster nodes, tcpdump confirms that communication between the cudn members is using Kubernetes standard interfaces, `br-ex` in this case, with Geneve encapsulation, using likely the specific `vni` value, however, it is **not** as defined in [network attachment definition](#network-attachment-definition) `tunnel-keys` property, like in the case of [primary cudn](./primary.md)

```
10.10.10.210.51915 > 10.10.10.211.6081: Geneve, Flags [C], vni 0xff0007
  02:9a:2a:20:c8:6c > 0a:58:42:42:42:02, ethertype IPv4 (0x0800)
    66.66.66.7 > 66.66.66.2: ICMP echo request, id 2, seq 0, length 80

10.10.10.211.43538 > 10.10.10.210.6081: Geneve, Flags [C], vni 0xff0007
  0a:58:42:42:42:02 > 02:9a:2a:20:c8:6c, ethertype IPv4 (0x0800)
    66.66.66.2 > 66.66.66.7: ICMP echo reply, id 2, seq 0, length 80
```

## ospf

>[!NOTE]
>Requires [namespace](#namespace) multicast annotation

>[!CAUTION]
>Link local multicast (224.0.0.x) works within namespace only, not across namespaces

VM | Node | IP | MAC
--- | --- | --- | --- 
c8kv1 | bm1-1 | 66.66.66.7/24 | 029a.2a20.c86c
c8kv2 | bm1-2 | 66.66.66.10/24 | 029a.2a20.c86e

Configuration c8kv1

```
interface GigabitEthernet2
 ip address dhcp
 negotiation auto
!
router ospf 1
 network 66.66.66.0 0.0.0.255 area 0
```

Configuration c8kv2

```
interface GigabitEthernet2
 ip address dhcp
 negotiation auto
!
router ospf 1
 network 66.66.66.0 0.0.0.255 area 0
```

OSPF neighborship is formed correctly on the secondary interface

```
c8kv1#sho ip ospf nei

Neighbor ID     Pri   State           Dead Time   Address         Interface
66.66.66.10       1   FULL/BDR        00:00:39    66.66.66.10     GigabitEthernet2
```

Hello sent by `c8kv1` on-the-wire interface `br-ex` on node `bm1-1`

```
10.10.10.210.53854 > 10.10.10.211.6081: Geneve, Flags [C], vni 0xff0007
  02:9a:2a:20:c8:6c > 01:00:5e:00:00:05, ethertype IPv4 (0x0800), proto OSPF (89)
    66.66.66.7 > 224.0.0.5: OSPFv2, Hello, length 80 [len 48]
        Router-ID 66.66.66.7, Backbone Area, Authentication Type: none (0)
        Options [External, LLS]
          Hello Timer 10s, Dead Timer 40s, Mask 255.255.255.0, Priority 1
          Designated Router 66.66.66.7, Backup Designated Router 66.66.66.10
          Neighbor List:
            66.66.66.10
          LLS: checksum: 0x7fbe, length: 8
            Extended Options (1), length: 4
              Options: 0x00000001 [LSDB resync]
            Unknown TLV (18), length: 4
            Unknown TLV (32768), length: 8
```

# fhrp

First hop redundancy protocol such as [hsrp](../evpn/cudn-l2-v2.md#hsrp), [vrrp](../evpn/cudn-l2-v2.md#vrrp), [glbp](../evpn/cudn-l2-v2.md#glbp) are broken.

However, if ipam is disabled, then hsrp with use-bia should work. This is due to the fact that ip security checks are relaxed, while mac address checks are still enforced and continue blocking vrrp and glbp.

Example c8kv1

```
interface GigabitEthernet2
 ip address 66.66.66.10 255.255.255.0
 standby use-bia scope interface
 standby 1 ip 66.66.66.250
 negotiation auto
```

```
c8kv1#show standby 
GigabitEthernet2 - Group 1
  State is Active
    2 state changes, last state change 00:03:57
  Virtual IP address is 66.66.66.250
  Active virtual MAC address is 029a.2a06.ddf1 (MAC In Use)
    Local virtual MAC address is 029a.2a06.ddf1 (bia)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 1.632 secs
  Preemption disabled
  Active router is local
  Standby router is 66.66.66.11, priority 100 (expires in 10.288 sec)
  Priority 100 (default 100)
  Group name is "hsrp-Gi2-1" (default)
  FLAGS: 0/1
```

Example c8kv2

```
interface GigabitEthernet2
 ip address 66.66.66.11 255.255.255.0
 standby use-bia scope interface
 standby 1 ip 66.66.66.250
 negotiation auto
```

```
c8kv2#show standby
GigabitEthernet2 - Group 1
  State is Standby
    1 state change, last state change 00:02:59
  Virtual IP address is 66.66.66.250
  Active virtual MAC address is 029a.2a06.ddf1 (MAC Not In Use)
    Local virtual MAC address is 029a.2a06.ddf3 (bia)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 1.920 secs
  Preemption disabled
  Active router is 66.66.66.10, priority 100 (expires in 10.096 sec)
  Standby router is local
  Priority 100 (default 100)
  Group name is "hsrp-Gi2-1" (default)
  FLAGS: 0/1
```

Test from the pod connected to the same secondary cudn

```
$ oc exec -it -n l2 t11 -- ping 66.66.66.250 -c 1
PING 66.66.66.250 (66.66.66.250) 56(84) bytes of data.
64 bytes from 66.66.66.250: icmp_seq=1 ttl=255 time=3.26 ms

--- 66.66.66.250 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 3.260/3.260/3.260/0.000 ms
```

```
$ oc exec -it -n l2 t11 -- arp -n
? (66.66.66.250) at 02:9a:2a:06:dd:f1 [ether]  on net1
```

[[Back]](../README.md)