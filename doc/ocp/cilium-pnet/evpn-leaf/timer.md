# BGP Timers

[[Back]](./README.md) 

## Table of Contents

- [Cilium](#cilium)
- [NX-OS](#nx-os-leaf)
- [Functionality Test](#test)

## Cilium

The `IsovalentBGPPeerConfig` resource contains peer-specific BGP peering configuration such as timers

Name | Field | Default
--- | --- | ---
ConnectRetryTimer | connectRetryTimeSeconds | 120
HoldTimer | holdTimeSeconds | 90
KeepaliveTimer | keepAliveTimeSeconds | 30

```yaml
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  timers:
    connectRetryTimeSeconds: 5
    holdTimeSeconds: 9
    keepAliveTimeSeconds: 3
```

## NX-OS

```
router bgp 64000
  neighbor Ethernet1/11
    timers 3 9
```

## Functionality Test

```
leaf1# show bgp ipv4 unicast neighbors ethernet 1/11
BGP neighbor is fe80::200d:c753:4467:28a7, remote AS 666, ebgp link, Peer index 9
  Peer is an instance of interface peering Ethernet1/11
  BGP version 4, remote router ID 66.66.66.1
  Neighbor previous state = OpenConfirm
  BGP state = Established, up for 00:00:06
  Neighbor vrf: default
  Using iod 28 (Ethernet1/11) as update source
  Peer is directly attached, interface Ethernet1/11
  Enable logging neighbor events
  Last read 0.935211, hold time = 9, keepalive interval is 3 seconds  <<< as configured in IsovalentBGPPeerConfig and NX-OS >>>
  Last written 0.093340, keepalive timer expiry due 00:00:02
```

[[Back]](./README.md) 