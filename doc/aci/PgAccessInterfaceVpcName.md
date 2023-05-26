# Policy Group - Access Interface VPC

## Filter by name

```
# iserver get aci pg access intf vpc --apic apic11 --name HX*

Apic: apic11

+-----------------+-------------------------+------------+-----------+------------+---------+-------------+-------------+---------+--------------+---------------+---------------+
| Name            | Attached Entity Profile | Link Level | Link Flap | CDP        | MCP     | LACP        | LLDP        | STP     | L2           | Storm Control | Port Security |
+-----------------+-------------------------+------------+-----------+------------+---------+-------------+-------------+---------+--------------+---------------+---------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | Inherit    | default   | CDP_enable | default | LACP-active | LLDP_enable | default | L2-local_Pol | default       | default       | 
| HX1-FI-B_PolGrp | HX1_AAEP                | Inherit    | default   | CDP_enable | default | LACP-active | LLDP_enable | default | L2-local_Pol | default       | default       | 
+-----------------+-------------------------+------------+-----------+------------+---------+-------------+-------------+---------+--------------+---------------+---------------+
```

[[Back]](./PgAccessInterfaceVpc.md)