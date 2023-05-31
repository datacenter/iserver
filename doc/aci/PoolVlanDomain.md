# VLAN Pool

## Filter by domain

```
# iserver get aci pool vlan --apic apic21 --domain *vmw*

Apic: apic21

+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| VLAN Pool Name         | Allocation Mode | Encapsulation Block   | Role     | Domain                | EPG Usage |
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-CDC-22_VlanPool    | dynamic         | [2501-2502] (static)  | external | ESX-CDC-22_PhysDom    | 11/309    | 
|                        |                 | [2503-2509] (static)  | external | vEPC_ESX              |           | 
|                        |                 | [2700-2999] (dynamic) | external | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-R7DC_VlanPool      | dynamic         | [3701-3800] (dynamic) | external | ESX-R7DC_PhysDom      | 2/100     | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| k8s_esx_VlanPool       | dynamic         | [1300-1499] (inherit) | external | k8s_esx_PhysDom       | 15/200    | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| vEPC-ESX21-22_VlanPool | dynamic         | [2501-2509] (static)  | external | vEPC-ESX20_PhysDom    | 4/309     | 
|                        |                 | [2700-2999] (dynamic) | external | vEPC-ESX21-22_PhysDom |           | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --domain *vmw*

{
    "duration": 1310,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 654,
        "total_time": 1076
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    }
}

Log: apic
----------

True	422	-	connect apic21o.emea-sp.cisco.com
True	333	13	apic21o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	321	32	apic21o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./PoolVlan.md)