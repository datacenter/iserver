# Cilium BGP EVPN advertisement - Import Route Target

[[Back]](./README.md)

Fabric advertises reachability information via vxlan/evpn fabric using bgp control plane. Cilium imports advertisements into private network (vrf) [route table](./rib-list.md) based on import route targets.

## Import Route Target

Import route targets are defined per vrf in `IsovalentBGPClusterConfig` definition

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
          configRef: evpn
```

Example with spine1 loopback interface in vrf:red `100.64.100.101/32` received by bm1-1 from leaf1

```
Node    VRouter     Prefix                      NextHop         Age           Attrs
bm1-1   666         [type:Prefix]               100.64.20.201   19h57m56s   	Origin: ?
                    [rd:100.64.10.101:4]						                          AsPath: 64000
                    [etag:0]							                                    Extcomms
                    [prefix:100.64.100.101/32]						                      64000:66100
                                                                                VXLAN
                                                                                4222124650659841
                                                                                router's mac: aa:aa:aa:aa:aa:aa <<< leaf1 mac address>>>
                                                                              MpReach(l2vpn-evpn)
                                                                                Nexthop: 100.64.20.201 <<< leaf1 vtep >>>
                                                                                NLRIs
                                                                                  [type:Prefix]
                                                                                  [rd:100.64.10.101:4] <<< spine1 routing lb >>>
                                                                                  [etag:0]
                                                                                  [prefix:100.64.100.101/32]
```

Resulting route table entry

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF      Prefix               Owner          Protocol    NextHop
*       35645    100.64.100.101/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
```


[[Back]](./README.md)