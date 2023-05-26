get_aci_bd# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated L3Out name

```
# iserver get aci vrf --apic apic21 --l3out mgmt/*

Apic: apic21

+----------+----------------+---------------+----------------+---------------+------------+------------------+
| VRF      | PCE Preference | PCE Direction | Associated EPG | Associated BD | BD Subnets | Associated L3Out |
+----------+----------------+---------------+----------------+---------------+------------+------------------+
| mgmt/inb | enforced       | ingress       |                |               |            | mgmt/INB_L3out   | 
+----------+----------------+---------------+----------------+---------------+------------+------------------+
```

[[Back]](./Vrf.md)