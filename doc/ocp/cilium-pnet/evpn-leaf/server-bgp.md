# Kubernetes BGP Control Plane

[[Back]](./README.md) [[Next]](./private-network.md)

![Overview](../../images/pnet/evpn2-bgp.png)

## Table of Contents

- [Underlay peering](#underlay-peering)
- [Fabric loopbacks](#fabric-loopbacks-policy)
- [Overlay peering](#overlay-peering)
- [Private network](#private-network)

## Underlay peering

Requirements
- from every cluster node with pair of leaf (ToR) switches
- physical interface IP unnumbered i.e. only v6 link-local address
- learn [fabric loopbacks](#fabric-loopbacks-policy) for bgp control plane and vxlan data plane
- advertise node's loopback ip address towards the fabric that will be used as bgp router-id and vtep source

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  name: underlay-loopback-advertisement
  labels:
    advertise: k8s-loopbacks
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
          advertise: k8s-loopbacks
      importPolicyRef:
        name: fabric-loopbacks
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
```

The expected bgp state with every cluster node peering with pair of leafs over p2p unnumbered interface
- loopback address advertised
- leaf loopbacks received

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address                     Session State   Uptime     Family         Received   Advertised
bm1-1   666        64385     fe80::23a:9cff:fe24:5db2%eno6    established     2h35m8s    ipv4/unicast   2          1    
        666        64385     fe80::a2b4:39ff:fec7:8812%eno5   established     2h34m7s    ipv4/unicast   2          1    
bm1-2   666        64385     fe80::23a:9cff:fe24:5db3%eno5    established     2h38m53s   ipv4/unicast   2          1    
        666        64385     fe80::a2b4:39ff:fec7:8813%eno6   established     2h38m53s   ipv4/unicast   2          1    
bm1-3   666        64385     fe80::23a:9cff:fe24:5db4%eno5    established     2h38m52s   ipv4/unicast   2          1    
        666        64385     fe80::a2b4:39ff:fec7:8814%eno6   established     2h38m52s   ipv4/unicast   2          1  
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

>[!NOTE]
>In this design, leaves are hiding the fabric details. Refer to [fabric bgp configuration](./fabric-bgp.md)

The expected entries in ip route table for **directly connected leafs only** incl. control plane and data plane loopbacks

Example for bm1-1 node:

```
$ ip route
100.64.10.201 via inet6 fe80::23a:9cff:fe24:5db2 dev eno5 proto kernel 
100.64.20.201 via inet6 fe80::23a:9cff:fe24:5db2 dev eno5 proto kernel 
100.64.10.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno6 proto kernel 
100.64.20.201 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno6 proto kernel
```

## Overlay peering

Requirements
- from every cluster node with pair of leaf (ToR) switches
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
  transport:
    sourceInterface: lo
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
```

The expected bgp state with every cluster node peering with pair of leafs

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address    Session State   Uptime     Family         Received   Advertised
bm1-1   666        64000     100.64.10.201   established     2h43m11s   l2vpn/evpn     15         0    
        666        64000     100.64.10.202   established     2h43m30s   l2vpn/evpn     15         0    
bm1-2   666        64000     100.64.10.201   established     2h31m52s   l2vpn/evpn     15         0    
        666        64000     100.64.10.202   established     2h30m29s   l2vpn/evpn     15         0    
bm1-3   666        64000     100.64.10.201   established     2h31m34s   l2vpn/evpn     15         0    
        666        64000     100.64.10.202   established     2h30m15s   l2vpn/evpn     15         0    
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
  name: nxos
spec:
  bgpInstances:
    - name: overlay
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

[[Back]](./README.md) [[Next]](./private-network.md)