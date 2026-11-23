# Leaf p2p connection with server

[[Back]](./README.md) [[Next]](./fabric-bgp.md) [[addressing scheme]](./address.md)

Interface | IP address | Server
--- | --- | --- 
Ethernet1/11 | 100.64.66.110/31 | bm1-1
Ethernet1/12 | 100.64.66.120/31 | bm1-2
Ethernet1/13 | 100.64.66.130/31 | bm1-3

>[!NOTE]
>p2p links are ospf advertised to underlay

```
!
interface Ethernet1/11
  ttag
  ttag-strip
  no switchport
  description bm1-1 eno5
  ip address 100.64.66.110/31
  ip router ospf UNDERLAY area 0.0.0.0
  mtu 9216
  fec fc-fec
  no shutdown
!
interface Ethernet1/12
  ttag
  ttag-strip
  no switchport
  description bm1-2 eno5
  ip address 100.64.66.120/31
  ip router ospf UNDERLAY area 0.0.0.0
  mtu 9216
  fec fc-fec
  no shutdown
!
interface Ethernet1/13
  ttag
  ttag-strip
  no switchport
  description bm1-3 eno5
  ip address 100.64.66.130/31
  ip router ospf UNDERLAY area 0.0.0.0
  mtu 9216
  fec fc-fec
  no shutdown
!
```

[[Back]](./README.md) [[Next]](./fabric-bgp.md) [[addressing scheme]](./address.md)