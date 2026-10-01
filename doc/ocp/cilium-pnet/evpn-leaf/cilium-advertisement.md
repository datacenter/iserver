# Cilium BGP EVPN advertisement

[[Back]](./README.md)

![Overview](../../images/pnet/evpn2-bgp.png)

## Cilium perspective

Notes
- every cilium node peers with pair of leafs (ToRs) for both underlay (ipv4/unicast) and overlay (l2vpn/evpn)
- bgp unnumbered session for underlay where node loopback is advertised and leaves' loopbacks are received
- application (pod or kubevirt vm) ip address (/32 or /128) connected to private network advertised using route type 5 with overlay bgp session 
- cilium nodes receive reachability information in overlay bgp session of remote prefixes and that information is used to built [forwarding table](./rib-list.md)

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address                     Session State   Uptime     Family         Received   Advertised
bm1-1   666        64000     100.64.10.201                    established     12m34s     l2vpn/evpn     15         2    
        666        64000     100.64.10.202                    established     12m34s     l2vpn/evpn     15         2    
        666        64000     fe80::23a:9cff:fe24:5db2%eno6    established     6h25m16s   ipv4/unicast   2          1    
        666        64000     fe80::a2b4:39ff:fec7:8812%eno5   established     6h24m15s   ipv4/unicast   2          1    
bm1-2   666        64000     100.64.10.201                    established     6h18m48s   l2vpn/evpn     15         2    
        666        64000     100.64.10.202                    established     6h18m53s   l2vpn/evpn     15         2    
        666        64000     fe80::23a:9cff:fe24:5db3%eno5    established     6h29m1s    ipv4/unicast   2          1    
        666        64000     fe80::a2b4:39ff:fec7:8813%eno6   established     6h29m1s    ipv4/unicast   2          1    
bm1-3   666        64000     100.64.10.201                    established     6h18m47s   l2vpn/evpn     15         2    
        666        64000     100.64.10.202                    established     6h18m52s   l2vpn/evpn     15         2    
        666        64000     fe80::23a:9cff:fe24:5db4%eno5    established     6h29m0s    ipv4/unicast   2          1    
        666        64000     fe80::a2b4:39ff:fec7:8814%eno6   established     6h29m0s    ipv4/unicast   2          1
```

Example type 5 route for r1 pod advertised to Leaf1 with "nexthop self"
- router's mac is set to cilium_evpn interface mac on the node
- extended communities controlled with [export route target](./export-route-target.md)

```
$ cilium bgp routes advertised l2vpn evpn -n cilium
Node    VRouter   Peer          Prefix                  NextHop         Age      Attrs
bm1-1   666       100.64.10.201 [type:Prefix]           100.64.10.1     23m10s   Origin: ?
                                [rd:100.66.66.1:1]                               AsPath: 666
                                [etag:0]                                         MpReach(l2vpn-evpn):   
                                [prefix:10.0.100.11/32]                             Nexthop: 100.64.10.1
                                                                                    NLRIs: 
                                                                                        [type:Prefix]
                                                                                        [rd:100.66.66.1:1]
                                                                                        [etag:0]
                                                                                        [prefix:10.0.100.11/32]
                                                                                    Extcomms: 
                                                                                        [VXLAN]
                                                                                        [666:66100]
                                                                                        [router's mac: 66:66:66:11:11:11]
```

[[Back]](./README.md)