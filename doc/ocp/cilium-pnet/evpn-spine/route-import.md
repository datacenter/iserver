# Cilium BGP route import feature

[[Back]](./README.md) [[kuberentes bgp configuration]](./server-bgp.md) [[fabric bgp configuration]](./fabric-bgp.md)

Server needs to learn routing to:
- routing loopbacks to establish BGP control plane for evpn af with spines (100.64.10.0/24)
- vtep loopbacks for data plane vxlan encapsulation (100.64.20.0/24)

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

available ipv4 routes advertised by leaf

```
$ cilium bgp routes available ipv4 unicast -n cilium
Node    VRouter   Prefix             NextHop         Age         Attrs
bm1-1   666       100.64.10.201/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 0} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.10.201/32]}}]   
        666       100.64.10.101/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 2} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.10.101/32]}}]   
        666       100.64.10.202/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 4} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.10.202/32]}}]   
        666       100.64.10.102/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 3} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.10.102/32]}}]   
        666       100.64.20.101/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 2} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.20.101/32]}}]   
        666       100.64.20.102/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 3} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.20.102/32]}}]   
        666       100.64.20.201/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 0} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.20.201/32]}}]   
        666       100.64.20.202/32   100.64.66.110   23h20m38s   [{Origin: ?} {AsPath: 64000} {Med: 4} {MpReach(ipv4-unicast): {Nexthop: 100.64.66.110, NLRIs: [100.64.20.202/32]}}]
```

populated ebpf map for route reconciliation

```
[root@bm1-1 cilium]# cilium-dbg shell db/show desired-routes
Owner           Table        Prefix             Priority   AD    Selected   Nexthop         Src       Device   MultiPath   MTU    Scope      Type      Status
bgp-instance0   main (254)   100.64.10.201/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.10.101/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.10.202/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.10.102/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.20.101/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.20.102/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.20.201/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
bgp-instance0   main (254)   100.64.20.202/32   none       150   true       100.64.66.110   none      none     none        none   universe   unicast   Done (18.4m ago)
```

The expected entries in ip route table for all vteps (leafs and spines) incl. control plane and data plane loopbacks

```
$ ip route
100.64.10.201 via 100.64.66.120 dev eno5 proto kernel 
100.64.10.101 via 100.64.66.120 dev eno5 proto kernel 
100.64.10.202 via 100.64.66.120 dev eno5 proto kernel 
100.64.10.102 via 100.64.66.120 dev eno5 proto kernel 
100.64.20.101 via 100.64.66.120 dev eno5 proto kernel 
100.64.20.102 via 100.64.66.120 dev eno5 proto kernel 
100.64.20.201 via 100.64.66.120 dev eno5 proto kernel 
100.64.20.202 via 100.64.66.120 dev eno5 proto kernel 
```

[[Back]](./README.md) [[kuberentes bgp configuration]](./server-bgp.md) [[fabric bgp configuration]](./fabric-bgp.md)