# Node Interface - Physical

## Filter by fabric vxlan

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --fvxlan 10297 -o vlan

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+----------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | EPG                        | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+----------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-45 | vlan-1  | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-45 | vlan-1  | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-45 | vlan-1  | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
+---------------------+-----------+------+---------+---------+----------------------------+---------------+------------+--------------+-----------------+
```

[[Back]](./InterfacePhy.md)