# Node Protocol - BGP

## Filter BGP neighbors by neighbor IP Address

Use --output parameter to select neighborship attributes template
- [summary](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: IP address

```
# iserver get aci proto bgp --apic apic11 --node rl --nbr-ip 172.24.3.3

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                      | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
```

Example: IP subnet

```
# iserver get aci proto bgp --apic apic11 --node rl --nbr-subnet 15.0.0.0/8

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF       | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+-----------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.1        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.5        | established | 64001 | ebgp | 1   | 0               | 
+---------------------+-----------+------------------+-------------+-------+------+-----+-----------------+
```

[[Back]](./ProtocolBgp.md)