# Bidirectional Forwarding Detection (BFD)

[[Back]](./README.md) 

## Table of Contents

- [Overview](#overview)
- [Cilium](#cilium)
- [NX-OS](#nx-os-leaf)
- [Functionality Test](#test)

## Overview

Bidirectional Forwarding Detection (BFD) is a standardized network protocol ([RFC-5880](https://datatracker.ietf.org/doc/html/rfc5880)) that provides low-overhead forwarding failure detection between two network devices. Cilium can use BFD to detect network failures between Cilium nodes and external networking devices, such as top-of-rack switches.

BFD can be enabled for **overlay bgp peering** to achieve faster peer failure detection times, which would not be possible to achieve just by tweaking BGP timers.

## Cilium

### Enable

Additional configuration on top of [base](./kube-baseline.md)

```yaml
spec:
  enterprise:
    featureGate:
      approved:
      - BFD
    bfd:
      enabled: true
```

Once enabled new CRDs are installed
- IsovalentBFDNodeConfigOverride
- IsovalentBFDNodeConfig
- IsovalentBFDProfile

Complete configuration [reference](./kube-extras.md)

### Configure

Additional configuration on top of [base](./kube-baseline.md)

```
apiVersion: isovalent.com/v1alpha1
kind: IsovalentBFDProfile
metadata:
  name: tor
spec:
  receiveIntervalMilliseconds: 300
  transmitIntervalMilliseconds: 300
  detectMultiplier: 3
  minimumTTL: 2
```

Note:
- the default minimutTTL value of 255 expects direct connection between cilium node and the peer
- keep it below 255 for multi-hop bfd sessions

Update peer config with bfd profile reference

```
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: evpn
spec:
  bfdProfileRef: tor
```

Complete configuration [reference](./kube-extras.md)

### Verify

Example output from single kube node
- expected two bfd peers with leaves (ToRs) using the same destination address as bgp peer

```
$ oc exec -it -n cilium cilium-887vp -- cilium-dbg bfd peers
PeerAddress   Interface   Discriminator   RemDiscriminator   State   LastStateChange   Multi   RemMulti   RxInt   RemRxInt   TxInt   RemTxInt   EchoRxInt   RemEchoRxInt   EchoTxInt   Diagnostic      RemDiagnostic
100.64.10.201             4133850494      1090519054         Up      31m43s            3       3          300ms   300ms      300ms   300ms      0s          0s             0s          No Diagnostic   No Diagnostic
100.64.10.202             1084740823      1090519056         Up      31m44s            3       3          300ms   300ms      300ms   300ms      0s          0s             0s          No Diagnostic   No Diagnostic
```

on tcpdump level 

```
17:12:57.073064 IP 100.64.10.201.51479 > 10.64.10.1.4784: BFDv1, Multihop, State Up, Flags: [none], length: 24
17:12:57.157089 IP 10.64.10.1.64398 > 100.64.10.201.4784: BFDv1, Multihop, State Up, Flags: [none], length: 24
```

netstat

```
$ netstat -na | grep 4784
udp        0      0 0.0.0.0:4784            0.0.0.0:*                          
```

Note: I have seen behavior where udp:4784 was not openned and bfd session was down even if it was configured. Cilium agent rollout restart did the trick.

## NX-OS Leaf

### Configure

Notes
- BFD echo interface configured to be the same as bgp source
- BFD enabled on bgp peer template used to configure overlay bgp peering with kube nodes

```
feature bfd
bfd echo-interface loopback0
bfd echo-rx-interval 300
bfd multihop interval 300 min_rx 300 multiplier 3
!
router bgp 64000
  template peer CILIUM_OVERLAY
    bfd multihop
```

### Verify

```
leaf1# show bfd neighbors

OurAddr         NeighAddr    LD/RD                 RH/RS  Holdown(mult)  State  Int  Vrf       Type  BSID
100.64.10.201   10.64.10.3   1090519052/4156455856 Up     900(3)         Up     Lo0  default   MH    N/A
100.64.10.201   10.64.10.2   1090519053/1794293876 Up     900(3)         Up     Lo0  default   MH    N/A
100.64.10.201   10.64.10.1   1090519054/4133850494 Up     900(3)         Up     Lo0  default   MH    N/A
```

## Functionality Test

### Test methodology

Starting point with both overlay bgp peers established to leaf devices

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address   Session State   Uptime      Family         Received   Advertised
bm1-1   666        64000     100.64.10.201  established     24s         l2vpn/evpn     15         2           <<< leaf1 overlay >>>
        666        64000     100.64.10.202  established     24s         l2vpn/evpn     15         2           <<< leaf2 overlay >>>
        666        64000     fe80::a2b4:39ff:fec7:8812%eno5 20s         ipv4/unicast   2          1           <<< leaf1 underlay >>>
        666        64000     fe80::200d:c753:4467:28a7%eno6 20s         ipv4/unicast   2          1           <<< leaf2 underlay >>>
```

One leaf (in the output below leaf1) selected as active vtep

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF      Prefix               Owner          Protocol    NextHop
*       35644    100.64.200.201/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35644    100.64.200.101/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35644    100.64.200.102/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.101/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.102/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.202/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.201/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
```

Check interface to active vtep

```
$ ip r
100.64.10.201 via inet6 fe80::23a:9cff:fe24:5db2 dev eno5 proto kernel 
```

Shutdown interface to active VTEP on the leaf and observe
- cilium bgp peers
- rib/list
- ping from application running on the node towards the spine's loopback

### Without BFD

Underlay session goes down immediately once physical interface shuts down. However overlay stays up until default hold timers detect session is down

```
Node    Local AS   Peer AS   Peer Address                     Session State   Uptime   Family         Received   Advertised
bm1-1   666        64000     100.64.10.201                    established     1m39s    l2vpn/evpn     15         2 <<< this one stays established until hold timer elapses >>>
        666        64000     100.64.10.202                    established     1m38s    l2vpn/evpn     15         2
        666        0         fe80::200d:c753:4467:28a7%eno5   active          0s       ipv4/unicast   0          0 <<< this is down immediately >>>
        666        64000     fe80::a2b4:39ff:fec7:8812%eno6   established     1m41s    ipv4/unicast   2          1
```

RIB remains configured with vtep that is not reachable 

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF      Prefix               Owner          Protocol    NextHop
*       35644    100.64.200.201/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35644    100.64.200.101/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35644    100.64.200.102/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.101/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.102/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.202/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.201/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
```

since underlay is down, the route to leaf1 loopbacks are gone, however bgp packets take default route entry and that is not reaching leaf device

```
$ ip r
default via 100.100.100.100 dev bond0.666 proto static <<< default kube interface >>>
100.64.10.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno6 proto kernel <<< leaf2 routing lb >>>
100.64.20.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno6 proto kernel <<< leaf2 vtep lb >>>
```

the connectivity problem will be detected after bgp hold timer elapses i.e. 90 seconds by default, then
- overlay bgp session to active vtep leaf goes down
- forwarding table updated with all route entries to other leaf
- pod connectivity works again

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF      Prefix               Owner          Protocol    NextHop
*       35644    100.64.200.201/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35644    100.64.200.101/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35644    100.64.200.102/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.101/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.102/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.202/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.201/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
```

### With BFD

Boht underlay and overlay sessions go down "immediately" once physical interface shuts down. 

```
Node    Local AS   Peer AS   Peer Address                     Session State   Uptime   Family         Received   Advertised
bm1-1   666        0         100.64.10.201                    active          0s       l2vpn/evpn     0          0 <<< this is down immediately >>>
        666        64000     100.64.10.202                    established     1m38s    l2vpn/evpn     15         2
        666        0         fe80::200d:c753:4467:28a7%eno5   active          0s       ipv4/unicast   0          0 <<< this is down immediately >>>
        666        64000     fe80::a2b4:39ff:fec7:8812%eno6   established     1m41s    ipv4/unicast   2          1
```

RIB changes to another vtep

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF      Prefix               Owner          Protocol    NextHop
*       35644    100.64.200.201/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35644    100.64.200.101/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35644    100.64.200.102/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.101/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.102/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.202/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
*       35645    100.64.100.201/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac bb:bb:bb:bb:bb:bb
```

ip route entries advertised via bgp underlay by leaf1 are deleted

```
$ ip r
default via 100.100.100.100 dev bond0.666 proto static <<< default kube interface >>>
100.64.10.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno6 proto kernel <<< leaf2 routing lb >>>
100.64.20.202 via inet6 fe80::a2b4:39ff:fec7:8812 dev eno6 proto kernel <<< leaf2 vtep lb >>>
```

no ping problem with packet sent every 1 second

[[Back]](./README.md) 