# VMM Domain

## Prop view

```
# iserver get aci domain vmm --apic apic21 --view prop

Apic: apic21 (mode:online, cache:off)

VMM Domain - Properties [#4]
----------------------------

+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| Domain Name    | Encap | Access Mode | Cfg Infra PGs | Tag Collection | VM Folder Data | Ep Inventory | Ep Retention Time | Uplinks |
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| EU-SPDC-CDC-22 | vlan  | RW          | no            | no             | no             | on-link      | 0                 | None    | 
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| EU-SPDC-POD2B  | vlan  | RW          | no            | no             | no             | on-link      | 0                 | 2       | 
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| EU-SPDC-R7DC   | vlan  | RW          | no            | no             | no             | on-link      | 0                 | None    | 
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| vEPC-Dataplane | vlan  | RW          | no            | no             | no             | on-link      | 0                 | 2       | 
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view prop

{
    "duration": 2591,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 533,
        "disconnect_time": 0,
        "mo_time": 1613,
        "total_time": 2146
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
    },
    "cache_hits": 0
}

Log: apic
----------

True	533	-	connect apic21o.emea-sp.cisco.com:443
True	714	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	899	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
```

[[Back]](./DomainVmm.md)