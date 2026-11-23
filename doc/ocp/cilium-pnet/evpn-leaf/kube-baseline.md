# Complete Kubernetes configuration reference

[[Back]](./README.md) 

## Table of Contents

- [Cilium configuration](#cilium)
- [Loopback interfaces](#loopback-interfaces)
- [p2p interfaces](#p2p-interfaces)
- [bgp](#bgp)
- [private network](#private-network)
- [application](#application)

## Cilium 

```yaml
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  name: ciliumconfig
spec:
  cluster:
    name: default
  clusterHealthPort: 9940
  cni:
    binPath: /var/lib/cni/bin
    chainingMode: portmap
    confPath: /var/run/multus/cni/net.d
    exclusive: false
  enterprise:
    featureGate:
      approved:
      - CNIChainingMode
      - BGPControlPlane
      - BGPRouteImport
      - EVPN
      - EnterpriseBGPControlPlane
      - MultiNetwork
      - VTEPIntegration
      - PrivateNetworks
      strict: false
    bgpControlPlane:
      enabled: true
      routeImport:
        enabled: true
    evpn:
      enabled: true
    privateNetworks:
      enabled: true
  hubble:
    enabled: true
  ipam:
    mode: cluster-pool
    operator:
      clusterPoolIPv4MaskSize: 23
      clusterPoolIPv4PodCIDRList:
      - 10.128.0.0/14
  kubeProxyReplacement: false
  operator:
    prometheus:
      enabled: true
      serviceMonitor:
        enabled: true
  prometheus:
    enabled: true
    serviceMonitor:
      enabled: true
  securityContext:
    privileged: true
  sessionAffinity: true
  tunnelPort: 4790
```

## loopback interfaces

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bm1-1-lo
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 100.64.10.1
          prefix-length: 32
        dhcp: false
        enabled: true
      name: lo
      state: up
      type: loopback
  nodeSelector:
    kubernetes.io/hostname: bm1-1
---
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bm1-2-lo
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 100.64.10.2
          prefix-length: 32
        dhcp: false
        enabled: true
      name: lo
      state: up
      type: loopback
  nodeSelector:
    kubernetes.io/hostname: bm1-2
---
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bm1-3-lo
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 100.64.10.3
          prefix-length: 32
        dhcp: false
        enabled: true
      name: lo
      state: up
      type: loopback
  nodeSelector:
    kubernetes.io/hostname: bm1-3
```

## p2p interfaces

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: eno5-unnumbered
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno5
      state: up
      type: ethernet
---
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: eno5-unnumbered
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno6
      state: up
      type: ethernet
```

## BGP

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  name: underlay-loopbacks
  labels:
    advertise: underlay-loopbacks
spec:
  advertisements:
    - advertisementType: "Interface"
      interface:
        name: lo
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPPolicy
metadata:
  name: fabric-loopbacks
spec:
  import:
    statements:
      - conditions:
          prefixesV4:
            matchType: Or
            matches:
              - prefix: 100.64.10.0/24
                minLen: 24
                maxLen: 32
              - prefix: 100.64.20.0/24
                minLen: 24
                maxLen: 32
        actions:
          routeAction: Accept
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: underlay
spec:
  ebgpMultihop: 5
  families:
    - afi: ipv4
      safi: unicast
      advertisements:
        matchLabels:
          advertise: underlay-loopbacks
      importPolicyRef:
        name: fabric-loopbacks
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: evpn
spec:
  ebgpMultihop: 5
  families:
    - afi: l2vpn
      safi: evpn
  transport:
    sourceInterface: lo 
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  name: evpn
  labels:
    advertise: evpn
spec:
  advertisements:
    - advertisementType: PrivateNetwork
---
apiVersion: isovalent.com/v1alpha1
kind: IsovalentBGPVRFConfig
metadata:
  name: evpn
spec:
  families:
    - afi: ipv4
      safi: unicast
      advertisements:
        matchLabels:
          advertise: evpn
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: nxos
spec:
  bgpInstances:
    - name: underlay
      localASN: 666
      peers:
        - name: leaf1
          autoDiscovery:
            mode: Unnumbered
            unnumbered:
              interface: eno5
          peerConfigRef:
            name: underlay
        - name: leaf2
          autoDiscovery:
            mode: Unnumbered
            unnumbered:
              interface: eno6
          peerConfigRef:
            name: underlay
    - name: overlay
      localASN: 666
      peers:
        - name: leaf1
          peerASN: 64000
          peerAddress: 100.64.10.201
          peerConfigRef:
            name: evpn
        - name: leaf2
          peerASN: 64000
          peerAddress: 100.64.10.202
          peerConfigRef:
            name: evpn
      vrfs:
        - privateNetworkRef:
            name: red
          rd: 100.66.66.1:1
          importRTs:
            - "64000:66100"
          exportRTs:
            - "666:66100"
          configRef: evpn
        - privateNetworkRef:
            name: blue
          rd: 100.66.66.1:1
          importRTs:
            - "64000:66200"
          exportRTs:
            - "666:66200"
          configRef: evpn
```

## Private Network

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: red
spec:
  vni: 66100
  subnets:
    - name: subnet0
      cidrv4: 10.0.100.0/24
      routes:
        - destination: 0.0.0.0/0
          gateway: EVPN
---
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: blue
spec:
  vni: 66200
  subnets:
    - name: subnet0
      cidrv4: 10.0.200.0/24
      routes:
        - destination: 0.0.0.0/0
          gateway: EVPN
```

## Application

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: r1
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "red",
        "ipv4": "10.0.100.11"
      }
spec:
  nodeName: bm1-1
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
---
apiVersion: v1
kind: Pod
metadata:
  name: r2
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "red",
        "ipv4": "10.0.100.12"
      }
spec:
  nodeName: bm1-2
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
---
apiVersion: v1
kind: Pod
metadata:
  name: r3
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "red",
        "ipv4": "10.0.100.13"
      }
spec:
  nodeName: bm1-3
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
---
apiVersion: v1
kind: Pod
metadata:
  name: b1
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "blue",
        "ipv4": "10.0.200.11"
      }
spec:
  nodeName: bm1-1
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
---
apiVersion: v1
kind: Pod
metadata:
  name: b2
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "blue",
        "ipv4": "10.0.200.12"
      }
spec:
  nodeName: bm1-2
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
---
apiVersion: v1
kind: Pod
metadata:
  name: b3
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "blue",
        "ipv4": "10.0.200.13"
      }
spec:
  nodeName: bm1-3
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
```

[[Back]](./README.md)