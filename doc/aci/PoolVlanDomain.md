# VLAN Pool

## Filter by domain

```
# iserver get aci pool vlan --apic apic21 --domain *vmw*

Apic: apic21

+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| VLAN Pool Name         | Allocation Mode | Encapsulation Block   | Role     | Domain                | EPG Usage |
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-CDC-22_VlanPool    | dynamic         | [2501-2502] (static)  | external | ESX-CDC-22_PhysDom    | 12/309    | 
|                        |                 | [2503-2509] (static)  | external | vEPC_ESX              |           | 
|                        |                 | [2700-2999] (dynamic) | external | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-R7DC_VlanPool      | dynamic         | [3701-3800] (dynamic) | external | ESX-R7DC_PhysDom      | 2/100     | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| k8s_esx_VlanPool       | dynamic         | [800-809] (static)    | external | k8s_esx_PhysDom       | 15/210    | 
|                        |                 | [1300-1499] (inherit) | external | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| vEPC-ESX21-22_VlanPool | dynamic         | [2501-2509] (static)  | external | vEPC-ESX20_PhysDom    | 4/309     | 
|                        |                 | [2700-2999] (dynamic) | external | vEPC-ESX21-22_PhysDom |           | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
```

[[Back]](./PoolVlan.md)