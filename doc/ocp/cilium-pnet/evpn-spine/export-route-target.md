# Cilium BGP EVPN advertisement - Export Route Target

[[Back]](./README.md)

Cilium advertises application (pod or kubevirt vm) ip address connected to private network via bgp control plane

## Export Route Target

Export route targets are defined per vrf in `IsovalentBGPClusterConfig` definition

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
          exportRTs:
            - "666:66100"
          configRef: evpn
```

Showing r1 pod only with formatted output

```
$ cilium bgp routes advertised l2vpn evpn peer 100.64.10.101 -n cilium
Node    VRouter   Peer          Prefix                  NextHop         Age      Attrs
bm1-1   666       100.64.10.101   [type:Prefix]           100.64.66.111   42m19s   Origin: ?
                                [rd:100.66.66.1:1]                               AsPath: 666
                                [etag:0]                                         MpReach(l2vpn-evpn):   
                                [prefix:10.0.100.11/32]                             Nexthop: 100.64.66.111
                                                                                    NLRIs: 
                                                                                        [type:Prefix]
                                                                                        [rd:100.66.66.1:1]  <<< THIS IS CONTROLLED WITH rd >>>
                                                                                        [etag:0]
                                                                                        [prefix:10.0.100.11/32]
                                                                                    Extcomms: 
                                                                                        [VXLAN]
                                                                                        [666:66100]  <<< THIS IS CONTROLLED WITH exportRTs >>>
                                                                                        [router's mac: 66:66:66:11:11:11]
```

## Fabric perspective

The extended community shown below is RT:64000:66100 due to rewrite-evpn-rt-asn feature enabled in [data center fabric](./fabric-bgp.md#overlay-vrf)

```
spine1# show bgp l2vpn evpn rd 66.66.66.1:1
BGP routing table information for VRF default, address family L2VPN EVPN
Route Distinguisher: 66.66.66.1:1
BGP routing table entry for [5]:[0]:[0]:[32]:[10.0.100.11]/224, version 555
Paths: (2 available, best #2)
Flags: (0x000002) (high32 00000000) on xmit-list, is not in l2rib/evpn, is not in HW

  Path type: internal, path is valid, not best reason: Internal path, no labeled nexthop
  Gateway IP: 0.0.0.0
  AS-Path: 666 , path sourced external to AS
    100.64.66.111 (metric 2) from 100.64.10.102 (100.64.10.102)
      Origin incomplete, MED not set, localpref 100, weight 0
      Received label 66100
      Extcommunity: RT:64000:66100 ENCAP:8 Router MAC:6666.6611.1111

  Advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop
             Imported to 2 destination(s)
             Imported paths list: infra L3-66100
  Gateway IP: 0.0.0.0
  AS-Path: 666 , path sourced external to AS
    100.64.66.111 (metric 2) from 100.64.66.111 (66.66.66.1)
      Origin incomplete, MED not set, localpref 100, weight 0
      Received label 66100
      Extcommunity: RT:64000:66100 ENCAP:8 Router MAC:6666.6611.1111

  Path-id 1 advertised to peers:
    100.64.10.201        100.64.10.202        100.64.10.102
```

[[Back]](./README.md)