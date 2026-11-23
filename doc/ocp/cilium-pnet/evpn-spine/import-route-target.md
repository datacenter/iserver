# Cilium BGP EVPN advertisement - Import Route Target

[[Back]](./README.md)

Fabric advertises reachability information via vxlan/evpn fabric using bgp control plane. Cilium imports advertisements into private network (vrf) [route table](./rib-list.md) based on import route targets.

## Import Route Target

Import route targets are defined per vrf in `IsovalentBGPClusterConfig` definition

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
          configRef: evpn
```

Showing single prefix with formatted output

```
$ cilium bgp routes available l2vpn evpn -n cilium
Node    VRouter     Prefix                      NextHop         Age         Attrs
bm1-1   666         type:Prefix                 100.64.20.201   45h17m17s   Origin: ?
                    rd:100.64.10.201:5                                      AsPath: 64000
                    etag:0                                                  Extcomms
                    prefix:100.64.100.201/32                                    64000:66100   <<< THIS IS MATCHED WITH importRTs >>
                                                                                VXLAN
                                                                                4222124650659841
                                                                                router's mac: 64:00:00:40:64:c9
                                                                            MpReach(l2vpn-evpn)
                                                                                Nexthop: 100.64.20.201
                                                                                NLRI
                                                                                    type:Prefix
                                                                                    rd:100.64.10.201:5
                                                                                    etag:0
                                                                                    prefix:100.64.100.201/32
```

Resulting route table entry

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF     Prefix             Owner            Protocol    NextHop
*       7440    100.64.100.201/32  bgp-instance0    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac 64:00:00:40:64:c9
```

[[Back]](./README.md)