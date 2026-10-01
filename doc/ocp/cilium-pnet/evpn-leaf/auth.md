# BGP Authentication

[[Back]](./README.md) 

## Table of Contents

>[!NOTE]
>Tested with bgp l2vpn/evpn overlay session. Underaly with IPv6 link-local requires Cilium 1.20 with goBGP fix related to TCP MD5.

- [Cilium](#cilium)
- [NX-OS](#nx-os-leaf)
- [Functionality Test](#test)

## Cilium

Secret from other namespace than default `kube-system`

```
spec:
  enterprise:
    bfd:
      enabled: true
    bgpControlPlane:
      enabled: true
      secretsNamespace:
        name: cilium
        create: false
      routeImport:
        enabled: true
```

Create secret

```
$ kubectl create secret generic -n cilium --type=string bgpsecret --from-literal=password=cisco123
secret/bgpsecret create
```

Configure bgp peer authentication with secret reference

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: evpn
spec:
  authSecretRef: bgpsecret
```

## NX-OS

```
router bgp 64000
  template peer CILIUM_OVERLAY
    password 3 a667d47acc18ea6b
```

## Functionality Test

```
BGP neighbor is 10.64.10.1, remote AS 666, ebgp link, Peer index 7
  Inherits peer configuration from peer-template CILIUM_OVERLAY
  Inherits session configuration from session-template CILIUM_OVERLAY
  BGP version 4, remote router ID 66.66.66.1
  Neighbor previous state = OpenConfirm
  BGP state = Established, up for 00:05:21
  Neighbor vrf: default
  Using loopback0 as update source for this peer
  Using iod 14 (loopback0) as update source
  Enable logging neighbor events
  BFD live-detection is configured and enabled, state is Invalid
    Forced multihop session
  External BGP peer might be up to 5 hops away
  TCP MD5 authentication is set (enabled) <<< confirmation >>>
```

[[Back]](./README.md) 