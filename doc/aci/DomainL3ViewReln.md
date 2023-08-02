# L3 Domain

## Reln view

```
# iserver get aci domain l3 --apic apic21 --view reln

Apic: apic21 (mode:online, cache:off)

L3 Domain - Policy Relationships [#7]
-------------------------------------

+---------+-----------------------+-------------+---------------------------+
| Faults  | Domain                | Policy Type | Policy Name               |
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | Infra_L3Dom           | AAEP        | TEST-AAP                  | 
|         |                       | AAEP        | Infra_AAEP                | 
|         |                       | L3 Out      | mgmt/INB_L3out            | 
|         |                       | L3 Out      | common/Infra_privIP_L3out | 
|         |                       | L3 Out      | Ericsson_PACO/DUMMY       | 
|         |                       | L3 Out      | k8s/vl3_k8s               | 
|         |                       | L3 Out      | vEPC/vSFO_L3out           | 
|         |                       | L3 Out      | k8s/bml3_k8s              | 
|         |                       | L3 Out      | common/Infra_L3out        | 
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | k8s_phys_L3Dom        | AAEP        | k8s_phys_AAEP             | 
|         |                       | L3 Out      | Ericsson_PACO/RAN         | 
|         |                       | L3 Out      | Ericsson_PACO/PDN         | 
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | L3_Domain_vsfo        |             |                           | 
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | multipodL3out_L3Dom   | AAEP        | multipodL3out_AAEP        | 
|         |                       | L3 Out      | infra/intersite           | 
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | RL-L3Out_RoutedDomain | AAEP        | RL-L3Out_EntityProfile    | 
|         |                       | L3 Out      | infra/RL-L3Out            | 
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | UCSB1_L3Dom           | AAEP        | UCSB1_AAEP                | 
+---------+-----------------------+-------------+---------------------------+
| 0 0 0 0 | vEPC_ESX              | AAEP        | ESX-CDC-22_AAEP           | 
|         |                       | AAEP        | vEPC-ESX21-22_AAEP        | 
|         |                       | L3 Out      | vEPC_demo/ACC_L3out       | 
|         |                       | L3 Out      | vEPC_demo/SX_L3out        | 
|         |                       | L3 Out      | vEPC_demo/INT_L3out       | 
+---------+-----------------------+-------------+---------------------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --view reln

{
    "duration": 1157,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 380,
        "total_time": 802
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

True	422	-	connect apic21o.emea-sp.cisco.com:443
True	380	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
```

[[Back]](./DomainL3.md)