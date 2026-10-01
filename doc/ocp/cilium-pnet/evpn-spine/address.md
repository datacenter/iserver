# Addressing scheme

[[Back]](./README.md)

BGP | Description
--- | ---
666 | kube asn
64000 | fabric asn

Kube | Description
--- | ---
100.66.66.1-3 | node ip

Private network | Description
--- | ---
10.0.100.0/24 | private network red
10.0.100.11-13 | pod ips in red
66100 | red vni
10.0.200.0/24 | private network blue
10.0.200.11-13 | pod ips in blue
66200 | blue vni

Fabric Routing Loopbacks | Description
--- | ---
100.64.10.0/24 | routing loopbacks (BGP EVPN peering)
100.64.10.101 | spine1
100.64.10.102 | spine2
100.64.10.201 | leaf1
100.64.10.202 | leaf2

Fabric VTEP Loopbacks | Description
--- | ---
100.64.20.0/24 | VTEP loopbacks (VXLAN data plane)
100.64.20.101 | spine1
100.64.20.102 | spine2
100.64.20.201 | leaf1
100.64.20.202 | leaf2

Fabric Test Loopbacks | Description
--- | ---
100.64.100.0/24 | Test loopbacks vrf red
100.64.100.101/32 | spine1
100.64.100.102/32 | spine2
100.64.100.201/32 | leaf1
100.64.100.202/32 | leaf2
100.64.200.0/24 | Test loopbacks vrf blue
100.64.200.101/32 | spine1
100.64.200.102/32 | spine2
100.64.200.201/32 | leaf1
100.64.200.202/32 | leaf1

Kube2Fabric p2p links | Description
--- | ---
100.64.66.0/24 | p2p links between kube nodes and leaf
100.64.66.110/31 | **leaf1** - bm1-1
100.64.66.111/31 | leaf1 - **bm1-1**
100.64.66.120/31 | **leaf1** - bm1-2
100.64.66.121/31 | leaf1 - **bm1-2**
100.64.66.130/31 | **leaf1** - bm1-3
100.64.66.131/31 | leaf1 - **bm1-2**

[[Back]](./README.md)