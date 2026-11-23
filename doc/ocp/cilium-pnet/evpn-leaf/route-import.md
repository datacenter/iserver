# Cilium BGP route import feature

[[Back]](./README.md)

Server needs to learn routing to:
- routing loopbacks to establish BGP control plane for evpn af with spines (100.64.10.0/24)
- vtep loopbacks for data plane vxlan encapsulation (100.64.20.0/24)

`CiliumConfiguration` must have route import enabled

```yaml
spec:
  enterprise:
    bgpControlPlane:
      routeImport:
        enabled: true
```

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

Underlay bgp peering as defined in `IsovalentBGPPeerConfig` refers to `IsovalentBGPPolicy`

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: underlay
spec:
  families:
    - afi: ipv4
      safi: unicast
      importPolicyRef:
        name: fabric-loopbacks
```

Example ipv4 routes advertised by leaf

```
$ cilium bgp routes available ipv4 unicast -n cilium
Node    VRouter   Prefix             NextHop                     Age         Attrs
bm1-1   666       100.64.10.201/32   fe80::23a:9cff:fe24:5db2    24h15m48s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::23a:9cff:fe24:5db2, NLRIs: [100.64.10.201/32]}}]    
        666       10.64.10.1/32      0.0.0.0                     18h3m8s     [{Origin: i} {Nexthop: 0.0.0.0}]                                                                                       
        666       100.64.10.202/32   fe80::a2b4:39ff:fec7:8812   24h14m47s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::a2b4:39ff:fec7:8812, NLRIs: [100.64.10.202/32]}}]   
        666       100.64.20.201/32   fe80::23a:9cff:fe24:5db2    24h15m48s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::23a:9cff:fe24:5db2, NLRIs: [100.64.20.201/32]}}]    
        666       100.64.20.202/32   fe80::a2b4:39ff:fec7:8812   24h14m47s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::a2b4:39ff:fec7:8812, NLRIs: [100.64.20.202/32]}}]   
bm1-2   666       100.64.10.201/32   fe80::23a:9cff:fe24:5db3    24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::23a:9cff:fe24:5db3, NLRIs: [100.64.10.201/32]}}]    
        666       10.64.10.2/32      0.0.0.0                     24h34m12s   [{Origin: i} {Nexthop: 0.0.0.0}]                                                                                       
        666       100.64.10.202/32   fe80::a2b4:39ff:fec7:8813   24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::a2b4:39ff:fec7:8813, NLRIs: [100.64.10.202/32]}}]   
        666       100.64.20.201/32   fe80::23a:9cff:fe24:5db3    24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::23a:9cff:fe24:5db3, NLRIs: [100.64.20.201/32]}}]    
        666       100.64.20.202/32   fe80::a2b4:39ff:fec7:8813   24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::a2b4:39ff:fec7:8813, NLRIs: [100.64.20.202/32]}}]   
bm1-3   666       100.64.10.201/32   fe80::23a:9cff:fe24:5db4    24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::23a:9cff:fe24:5db4, NLRIs: [100.64.10.201/32]}}]    
        666       10.64.10.3/32      0.0.0.0                     24h34m24s   [{Origin: i} {Nexthop: 0.0.0.0}]                                                                                       
        666       100.64.10.202/32   fe80::a2b4:39ff:fec7:8814   24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::a2b4:39ff:fec7:8814, NLRIs: [100.64.10.202/32]}}]   
        666       100.64.20.201/32   fe80::23a:9cff:fe24:5db4    24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::23a:9cff:fe24:5db4, NLRIs: [100.64.20.201/32]}}]    
        666       100.64.20.202/32   fe80::a2b4:39ff:fec7:8814   24h19m33s   [{Origin: i} {AsPath: 64385} {MpReach(ipv4-unicast): {Nexthop: fe80::a2b4:39ff:fec7:8814, NLRIs: [100.64.20.202/32]}}]
```

populated ebpf map for route reconciliation

```
$ oc exec -it -n cilium cilium-887vp -- cilium-dbg shell db/show desired-routes
Owner          Table        Prefix             Priority   AD    Selected   Nexthop                          Src       Device     MultiPath   MTU    Scope      Type      Status
bgp-underlay   main (254)   100.64.10.201/32   none       150   true       fe80::23a:9cff:fe24:5db2%eno6    none      eno6 (3)   none        none   universe   unicast   Done (17.0m ago)
bgp-underlay   main (254)   100.64.10.202/32   none       150   true       fe80::a2b4:39ff:fec7:8812%eno5   none      eno5 (2)   none        none   universe   unicast   Done (15.9m ago)
bgp-underlay   main (254)   100.64.20.201/32   none       150   true       fe80::23a:9cff:fe24:5db2%eno6    none      eno6 (3)   none        none   universe   unicast   Done (17.0m ago)
bgp-underlay   main (254)   100.64.20.202/32   none       150   true       fe80::a2b4:39ff:fec7:8812%eno5   none      eno5 (2)   none        none   universe   unicast   Done (15.9m ago)
proxy          2004         0.0.0.0/0          none       100   true       none                             0.0.0.0   lo (1)     none        none   universe   local     Done (4.3m ago)
```

expected entries in ip route table for leaf vteps incl. control plane and data plane loopbacks

```
$ ip route
100.64.10.201 via inet6 fe80::23a:9cff:fe24:5db2 dev eno6 proto kernel <<< leaf1 routing lb >>>
100.64.10.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno5 proto kernel <<< leaf2 routing lb >>>
100.64.20.201 via inet6 fe80::23a:9cff:fe24:5db2 dev eno6 proto kernel <<< leaf1 vtep lb >>>
100.64.20.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno5 proto kernel <<< leaf2 vtep lb >>>
```

[[Back]](./README.md)