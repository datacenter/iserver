# Node Protocol - BGP

## Filter BGP neighbors by source interface

Use --output parameter to select neighborship attributes template
- [summary](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

```
# iserver get aci proto bgp --apic apic11 --node any --intf lo9 -o trans

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| Node                | VRF                      | Neighbor Address | Router Id  | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP    |
+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 172.24.3.1 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 172.24.3.2 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
```

[[Back]](./ProtocolBgp.md)