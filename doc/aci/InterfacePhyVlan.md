# Node Interface - Physical

## Filter by internal vlan

Example: single vlan

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --vlan 27 -o vlan

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
+---------------------+-----------+------+---------+---------+--------------------------+---------------+------------+--------------+-----------------+
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 27,42-45 -o vlan

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         | P5G/P5G_App/P5G-mgmt     | 44            | vlan-2173  | vxlan-12064  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         | P5G/P5G_App/P5G-mgmt     | 44            | vlan-2173  | vxlan-12064  | up              | 
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-45 | vlan-1  | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-45 | vlan-1  | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-45 | vlan-1  | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
+---------------------+-----------+------+---------+---------+--------------------------+---------------+------------+--------------+-----------------+
```

[[Back]](./InterfacePhy.md)