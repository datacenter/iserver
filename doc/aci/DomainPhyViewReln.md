# Physical Domain

## Reln view

```
# iserver get aci domain phy --apic apic21 --view reln

Apic: apic21 (mode:online, cache:off)

Physical Domain - Policy Relationships [#12]
--------------------------------------------

+---------+-----------------------+-----------------+------------------------------------+
| Faults  | Domain                | Policy Type     | Policy Name                        |
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | ESX-CDC-22_PhysDom    | Application EPG | common/Test_ANP/Test_EPG           | 
|         |                       | AAEP            | ESX-CDC-22_AAEP                    | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | ESX-R7DC_PhysDom      | AAEP            | ESX-R7DC_AAEP                      | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | HX1_PhysDom           | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
|         |                       | AAEP            | HX1_AAEP                           | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | Infra_PhysDom         | AAEP            | Infra_AAEP                         | 
|         |                       | AAEP            | vEPC-ESX21-22_AAEP                 | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | k8s_esx_PhysDom       | Application EPG | k8s/k8s_ANP/MGMT                   | 
|         |                       | Application EPG | k8s/k8s_ANP/SRIoV_A                | 
|         |                       | Application EPG | k8s/k8s_ANP/SRIoV_B                | 
|         |                       | Application EPG | k8s/k8s_ANP/backbone1              | 
|         |                       | Application EPG | k8s/k8s_ANP/bmk8s_prov             | 
|         |                       | Application EPG | k8s/k8s_ANP/csr1_lan               | 
|         |                       | Application EPG | k8s/k8s_ANP/csr2_lan               | 
|         |                       | Application EPG | k8s/k8s_ANP/csr_b2b                | 
|         |                       | Application EPG | k8s/k8s_ANP/site1_lan              | 
|         |                       | Application EPG | k8s/k8s_ANP/site1_pe               | 
|         |                       | Application EPG | k8s/k8s_ANP/site2_lan              | 
|         |                       | Application EPG | k8s/k8s_ANP/site2_pe               | 
|         |                       | Application EPG | k8s/k8s_ANP/vk8s_1                 | 
|         |                       | Application EPG | k8s/k8s_ANP/vk8s_2                 | 
|         |                       | Application EPG | k8s/k8s_ANP/vk8s_3                 | 
|         |                       | Application EPG | k8s/k8s_ANP/vk8s_4                 | 
|         |                       | AAEP            | k8s_esx_AAEP                       | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | k8s_phys_PhysDom      | Application EPG | k8s/k8s_ANP/SRIoV_A                | 
|         |                       | Application EPG | k8s/k8s_ANP/SRIoV_B                | 
|         |                       | Application EPG | k8s/k8s_ANP/bmk8s_1                | 
|         |                       | Application EPG | k8s/k8s_ANP/bmk8s_2                | 
|         |                       | Application EPG | k8s/k8s_ANP/bmk8s_prov             | 
|         |                       | AAEP            | k8s_phys_AAEP                      | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | nidemo                | Application EPG | nidemo/streamz/database            | 
|         |                       | AAEP            | nidemo                             | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | SPN_PhysDom           | Application EPG | SPN_IntraLab/SPN_Connect_ANP/TEST2 | 
|         |                       | AAEP            | SPN_AAEP                           | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom    | AAEP            | UCSB1-R7DC_AAEP                    | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | UCSB1_PhysDom         | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
|         |                       | AAEP            | UCSB1_AAEP                         | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | vEPC-ESX20_PhysDom    | AAEP            | vEPC-ESX21-22_AAEP                 | 
+---------+-----------------------+-----------------+------------------------------------+
| 0 0 0 0 | vEPC-ESX21-22_PhysDom | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
|         |                       | AAEP            | vEPC-ESX21-22_AAEP                 | 
+---------+-----------------------+-----------------+------------------------------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --view reln

{
    "duration": 1189,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 449,
        "disconnect_time": 0,
        "mo_time": 377,
        "total_time": 826
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

True	449	-	connect apic21o.emea-sp.cisco.com:443
True	377	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
```

[[Back]](./DomainPhy.md)