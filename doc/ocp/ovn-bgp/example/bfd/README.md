# OVNKubernetes BGP - BFD

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

> [!NOTE]
> BFD is disabled by default

## FRR BFD profile

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: fabric-peering
  namespace: openshift-frr-k8s
spec:
  bgp:
    bfdProfiles:
    - name: defaultprofile
    routers:
    - asn: 64667
      neighbors:
      - address: 6.6.6.6
        asn: 64600
        ebgpMultiHop: true
        bfdProfile: defaultprofile
      - address: 6.6.6.7
        asn: 64600
        ebgpMultiHop: true
        bfdProfile: defaultprofile
```

```
spec:
  bgp:
    bfdProfiles:
    - name: simple
      echoMode: false
      passiveMode: false
```

Refer to [FRR documentation](https://docs.frrouting.org/en/latest/bfd.html#configuration) for details

## Nexus NX-OS

```
router bgp 64600
  vrf kali_test
    neighbor 66.66.66.0/24
      bfd multihop
```

## BFD state

[FRR CLI](../../kb/frr_cli.md)

```
bm1-1# show bfd peers
BFD Peers:
        peer 6.6.6.6 multihop local-address 66.66.66.10 vrf default
                ID: 1
                Remote ID: 2
                Active mode
                Minimum TTL: 1
                Status: up
                Uptime: 9 minute(s), 59 second(s)
                Diagnostics: ok
                Remote diagnostics: ok
                Peer Type: dynamic
                RTT min/avg/max: 0/0/0 usec
                Local timers:
                        Detect-multiplier: 3
                        Receive interval: 300ms
                        Transmission interval: 300ms
                        Echo receive interval: 50ms
                        Echo transmission interval: disabled
                Remote timers:
                        Detect-multiplier: 3
                        Receive interval: 250ms
                        Transmission interval: 250ms
                        Echo receive interval: disabled

        peer 6.6.6.7 multihop local-address 66.66.66.10 vrf default
                ID: 3
                Remote ID: 4
                Active mode
                Minimum TTL: 1
                Status: up
                Uptime: 9 minute(s), 59 second(s)
                Diagnostics: ok
                Remote diagnostics: ok
                Peer Type: dynamic
                RTT min/avg/max: 0/0/0 usec
                Local timers:
                        Detect-multiplier: 3
                        Receive interval: 300ms
                        Transmission interval: 300ms
                        Echo receive interval: 50ms
                        Echo transmission interval: disabled
                Remote timers:
                        Detect-multiplier: 3
                        Receive interval: 250ms
                        Transmission interval: 250ms
                        Echo receive interval: disabled
```

Nexus NX-OS fabric

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 vrf kali_test
BGP neighbor is 66.66.66.10, remote AS 64667, ebgp link, Peer index 5
  BFD live-detection is configured and enabled, state is Up
    Forced multihop session
```

[[Back]](../../README.md)