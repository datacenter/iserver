# Kubernetes BGP Control Plane

[[Back]](./README.md) [[Next]](./private-network.md) [[addressing scheme]](./address.md)

![Overview](../../images/pnet/evpn1-bgp.png)

## Table of Contents

- [Underlay peering](#underlay-peering)
- [Fabric loopbacks](#fabric-loopbacks-policy)
- [Overlay peering](#overlay-peering)
- [Private network](#private-network)

## Underlay peering

Requirements
- from every cluster node with single leaf
- ipv4 unicast address family only
- learn [fabric loopbacks](#fabric-loopbacks-policy) for bgp control plane and vxlan data plane
- nothing is expected to be advertised towards the fabric

Notes
- possible deployment option is with loopback interfaces used as control plane and data plane source. Then loopback (/32) are likely advertised
- showing `IsovalentBGPClusterConfig` for single cluster node only
- every cluster node will have different configuration since it forms bgp control plane peering via p2p interface with directly connected leaf

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: underlay
spec:
  ebgpMultihop: 5
  families:
    - afi: ipv4
      safi: unicast
      importPolicyRef:
        name: fabric-loopbacks
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: bm1-1
spec:
  nodeSelector:
    matchLabels:
      kubernetes.io/hostname: bm1-1
  bgpInstances:
    - name: instance0
      localASN: 666
      peers:
        - name: leaf
          peerASN: 64000
          peerAddress: 100.64.66.110
          peerConfigRef:
            name: underlay
```

The expected bgp state with every cluster node peering with leaf1 over p2p interface

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address    Session State   Uptime     Family         Received   Advertised
bm1-1   666        64000     100.64.66.110   established     2h31m20s   ipv4/unicast   14         0    
bm1-2   666        64000     100.64.66.120   established     2h20m0s    ipv4/unicast   14         0    
bm1-3   666        64000     100.64.66.130   established     2h20m0s    ipv4/unicast   14         0
```

## Fabric loopbacks policy

Server needs to learn routing to:
- routing loopbacks (100.64.10/24) to establish BGP control plane for evpn af with spines
- vtep loopbacks (100.64.20/24) for data plane vxlan encapsulation 

`IsovalentBGPPolicy` defines the prefixes to be accepted and installed as route table in root network namespace of the server

```yaml
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
```

The expected entries in ip route table for all vteps (leafs and spines) incl. control plane and data plane loopbacks

Example for bm1-1 node:

```
$ ip route
100.64.10.101 via 100.64.66.110 dev eno5 proto kernel 
100.64.10.102 via 100.64.66.110 dev eno5 proto kernel 
100.64.10.201 via 100.64.66.110 dev eno5 proto kernel 
100.64.10.202 via 100.64.66.110 dev eno5 proto kernel 
100.64.20.101 via 100.64.66.110 dev eno5 proto kernel 
100.64.20.102 via 100.64.66.110 dev eno5 proto kernel 
100.64.20.201 via 100.64.66.110 dev eno5 proto kernel 
100.64.20.202 via 100.64.66.110 dev eno5 proto kernel 
```

## Overlay peering

Requirements
- from every cluster node with pair of spines
- l2vpn/evpn address family only
- learn remote endpoints
- advertise local private network endpoints

Notes
- once peering is established, nothing is expected to be advertised yet. Refer to [private networks](#private-network) section for details
- underlay configuration is expected to be part of [final](#complete-configuration) `IsovalentBGPClusterConfig` definition

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: evpn
spec:
  ebgpMultihop: 5
  families:
    - afi: l2vpn
      safi: evpn
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
kind: IsovalentBGPAdvertisement
metadata:
  name: evpn
  labels:
    advertise: evpn
spec:
  advertisements:
    - advertisementType: PrivateNetwork
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: bm1-1
spec:
  nodeSelector:
    matchLabels:
      kubernetes.io/hostname: bm1-1
  bgpInstances:
    - name: instance0
      localASN: 666
      peers:
        - name: spine1
          peerASN: 64000
          peerAddress: 100.64.10.101
          peerConfigRef:
            name: evpn
        - name: spine2
          peerASN: 64000
          peerAddress: 100.64.10.102
          peerConfigRef:
            name: evpn
```

The expected bgp state

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address    Session State   Uptime     Family         Received   Advertised
bm1-1   666        64000     100.64.10.101     established     2h43m11s   l2vpn/evpn     30         0    
        666        64000     100.64.10.102     established     2h43m30s   l2vpn/evpn     30         0    
bm1-2   666        64000     100.64.10.101     established     2h31m52s   l2vpn/evpn     30         0    
        666        64000     100.64.10.102     established     2h30m29s   l2vpn/evpn     30         0    
bm1-3   666        64000     100.64.10.101     established     2h31m34s   l2vpn/evpn     30         0    
        666        64000     100.64.10.102     established     2h30m15s   l2vpn/evpn     30         0    
```

## Private network

Requirements
- the test setup has two [private network](./private-network.md) extended via vxlan/evpn fabric
- isolation on the Kubernetes layer is exposed to fabric using different exportRT per private network
- importRT define what remote endpoints are going to be reachable for applications (pod/vm) connected to private network and put into the [vrf forwarding table](./rib-list.md)

Notes:
- bgpInstances.peers section omitted for brevity
- bgp control plane advertises local endpoint (/32 or /128) addresses of the applications connected to private network and running on the node
- if there is no application connected to private network on the node, it is expected that nothing is advertised

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: bm1-1
spec:
  nodeSelector:
    matchLabels:
      kubernetes.io/hostname: bm1-1
  bgpInstances:
    - name: instance0
      localASN: 666
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

[[Back]](./README.md) [[Next]](./private-network.md) [[addressing scheme]](./address.md)