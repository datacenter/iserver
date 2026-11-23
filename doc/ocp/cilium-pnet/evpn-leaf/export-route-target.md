# Cilium BGP EVPN advertisement - Export Route Target

[[Back]](./README.md)

Cilium advertises application (pod or kubevirt vm) ip address connected to private network via bgp control plane

## Export Route Target

Export route targets are defined per vrf in `IsovalentBGPClusterConfig` definition

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
          exportRTs:
            - "666:66100"
          configRef: evpn
```

Example type 5 route for r1 pod advertised to Leaf1
- "nexthop self"
- rd and community controlled with `IsovalentBGPClusterConfig`

```
$ cilium bgp routes advertised l2vpn evpn -n cilium
Node    VRouter   Peer          Prefix                  NextHop         Age      Attrs
bm1-1   666       100.64.10.201 [type:Prefix]           100.64.10.1     23m10s   Origin: ?
                                [rd:100.66.66.1:1]                               AsPath: 666
                                [etag:0]                                         MpReach(l2vpn-evpn):   
                                [prefix:10.0.100.11/32]                             Nexthop: 100.64.10.1
                                                                                    NLRIs: 
                                                                                        [type:Prefix]
                                                                                        [rd:100.66.66.1:1] <<< THIS IS CONTROLLED WITH rd >>>
                                                                                        [etag:0]
                                                                                        [prefix:10.0.100.11/32]
                                                                                    Extcomms: 
                                                                                        [VXLAN]
                                                                                        [666:66100] <<< THIS IS CONTROLLED WITH exportRTs >>>
                                                                                        [router's mac: 66:66:66:11:11:11]
```

## Fabric perspective

### Leaf1

```
Leaf1# show bgp l2vpn evpn rd 66.66.66.1:1 <<< rd of bm1-1 >>>
Paths: (3 available, best #3)
Flags: (0x000002) (high32 00000000) on xmit-list, is not in l2rib/evpn, is not in HW
Multipath: iBGP

  Path type: internal, path is valid, not best reason: Neighbor Address, no labeled nexthop
  Gateway IP: 0.0.0.0
  AS-Path: 666 , path sourced external to AS
    100.64.20.202 (metric 4) from 100.64.10.102 (100.64.10.102) <<< leaf2 vtep from spine2>>>
      Origin incomplete, MED not set, localpref 100, weight 0
      Received label 66100
      Received path-id 1
      Extcommunity: RT:64000:66100 ENCAP:8 Router MAC:aaaa.aaaa.aaaa
      Originator: 100.64.10.202 Cluster list: 0.0.251.129 <<< from leaf2 >>>

  Advertised path-id 2
  Path type: internal, path is valid, not best reason: Internal path, no labeled nexthop
  Gateway IP: 0.0.0.0
  AS-Path: 666 , path sourced external to AS
    100.64.20.102 (metric 4) from 100.64.10.101 (100.64.10.101) <<< spine2 vtep from spine1 >>>
      Origin incomplete, MED not set, localpref 100, weight 0
      Received label 66100
      Received path-id 2
      Extcommunity: RT:64000:66100 ENCAP:8 Router MAC:aaaa.aaaa.aaaa
      Originator: 100.64.10.202 Cluster list: 0.0.251.129 <<< from leaf2 >>>

  Advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop
             Imported to 2 destination(s)
             Imported paths list: infra L3-66100
  Gateway IP: 0.0.0.0
  AS-Path: 666 , path sourced external to AS <<< k8s bgp >>>
    10.64.10.1 (metric 0) from 10.64.10.1 (66.66.66.1) <<< bm1-1 loopback >>>
      Origin incomplete, MED not set, localpref 100, weight 0
      Received label 66100
      Extcommunity: 
        RT:64000:66100 <<< exportRT as defined in IsovalentBGPClusterConfig >>>
        ENCAP:8 <<< VXLAN encap >>>
        Router MAC:aaaa.aaaa.aaaa <<< bm1-1 cilium_evpn intf mac >>>

  Path-id 1 advertised to peers:
    100.64.10.101 <<< spine1 >>>
    100.64.10.102 <<< spine2 >>>

  Path-id 2 not advertised to any peer
```

[[Back]](./README.md)