# BGP Community

[[Back]](./README.md) 

## ipv4/unicast underlay

```
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  name: underlay-loopback-advertisement
  labels:
    advertise: underlay
spec:
  advertisements:
    - advertisementType: "Interface"
      attributes:
        communities:
          standard:
          - "666:666"
          wellKnown:
          - "internet"
      interface:
        name: lo
```

```
BGP routing table information for VRF default, address family IPv4 Unicast
BGP routing table entry for 10.64.10.1/32, version 378
Paths: (1 available, best #1)
Flags: (0x00001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

  Advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop, in rib
  AS-Path: 666 , path sourced external to AS
    fe80::200d:c753:4467:28a7 (metric 0) from fe80::200d:c753:4467:28a7 (66.66.66.1)
      Origin IGP, MED not set, localpref 100, weight 0
      Community: internet 666:666
      Extcommunity: PCTAG:0:0:0
```

## l2vpn/evpn overlay

```
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  name: evpn
  labels:
    advertise: evpn
spec:
  advertisements:
    - advertisementType: PrivateNetwork
      attributes:
        communities:
          standard:
          - "666:999"
          wellKnown:
          - "planned-shut"
```

```
BGP routing table entry for [5]:[0]:[0]:[32]:[10.0.100.12]/224, version 2916
Paths: (1 available, best #1)
Flags: (0x000002) (high32 00000000) on xmit-list, is not in l2rib/evpn, is not in HW
Multipath: iBGP

  Advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop, gshut path
             Imported from 66.66.66.1:1:[5]:[0]:[0]:[32]:[10.0.100.12]/224
  Gateway IP: 0.0.0.0
  AS-Path: 666 , path sourced external to AS
    10.64.10.2 (metric 0) from 10.64.10.2 (66.66.66.2)
      Origin incomplete, MED not set, localpref 100, weight 0
      Received label 60000
      Community: 666:999 graceful-shutdown
      Extcommunity: RT:64000:50000 ENCAP:8 PCTAG:0:80:100 Router MAC:aaaa.aaaa.aaaa
```

[[Back]](./README.md) 