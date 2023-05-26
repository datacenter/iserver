# Virtual Routing and Forwarding (VRF)

## Verbose output

Get selected vrf details
- VRF properties
- associated EPGs
- associated bridge domains

```
# iserver get aci vrf --apic apic21 --name Infra_VRF -o verbose

Apic: apic21

+------------------+----------------+---------------+----------------+---------------+------------+--------------------+
| VRF              | PCE Preference | PCE Direction | Associated EPG | Associated BD | BD Subnets | Associated L3Out   |
+------------------+----------------+---------------+----------------+---------------+------------+--------------------+
| common/Infra_VRF | unenforced     | ingress       |                |               |            | common/Infra_L3out | 
+------------------+----------------+---------------+----------------+---------------+------------+--------------------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : no
- Endpoints Count                       : 0


Associated L3 Outs
------------------

+--------------------+------+-----+-----+------+-------+------------------+-------------+
| L3Out              | MPLS | PIM | BGP | OSPF | EIGRP | VRF              | L3 Domain   |
+--------------------+------+-----+-----+------+-------+------------------+-------------+
| common/Infra_L3out | X    | X   | V   | X    | X     | common/Infra_VRF | Infra_L3Dom | 
|                    |      |     |     |      |       |                  |             | 
+--------------------+------+-----+-----+------+-------+------------------+-------------+
```

[[Back]](./Vrf.md)