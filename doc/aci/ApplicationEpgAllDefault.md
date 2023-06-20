# Application Endpoint Group (EPG)

## Get EPGs

Get all epgs from selected APIC. Default view shows main properties of epgs as well as associated objects.
- epg name, application profile and tenant
- bridge domain name and subnets
- endpoints count
- contract

```
# iserver get aci epg --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| Up | EPG                    | BD                | BD Subnet          | Endpoint | Node | Domain               | Contract | StPort | StMember | DynMember |
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/backbone1  | k8s/VM2VM_BD      |                    | 2        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/bmk8s_1    | k8s/bmk8s_1_BD    | 10.58.24.78/28     | 0        |      | k8s_phys_PhysDom     | 1        | 1      | 0        | 0         | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/bmk8s_2    | k8s/bmk8s_2_BD    | 10.58.24.94/28     | 0        |      | k8s_phys_PhysDom     | 1        | 1      | 0        | 0         | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/bmk8s_prov | k8s/bmk8s_prov_BD | 10.58.29.94/28     | 4        |      | VMware/EU-SPDC-POD2B | 1        | 5      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
|    |                        |                   |                    |          |      | k8s_phys_PhysDom     |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/csr1_lan   | k8s/VM2VM_BD      |                    | 1        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/csr2_lan   | k8s/VM2VM_BD      |                    | 1        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/csr_b2b    | k8s/VM2VM_BD      |                    | 0        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/MGMT       | k8s/MGMT_BD       | 10.58.25.174/28    | 0        |      | VMware/EU-SPDC-POD2B | 1        | 1      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site1_lan  | k8s/VM2VM_BD      |                    | 1        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site1_pe   | k8s/VM2VM_BD      |                    | 2        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site2_lan  | k8s/VM2VM_BD      |                    | 1        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site2_pe   | k8s/VM2VM_BD      |                    | 2        |      | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_A    | k8s/SRIoV_A_BD    | 15.20.16.254/24    | 1        |      | k8s_esx_PhysDom      | 3        | 14     | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_phys_PhysDom     |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_B    | k8s/SRIoV_B_BD    | 15.20.17.254/24    | 1        |      | k8s_esx_PhysDom      | 0        | 14     | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_phys_PhysDom     |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/Test       | k8s/Test          | 169.169.169.254/24 | 0        |      |                      | 0        | 0      | 0        | 0         | 
|    |                        |                   | 169.169.170.254/24 |          |      |                      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_1     | k8s/vk8s_1_BD     | 10.58.24.174/28    | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_2     | k8s/vk8s_2_BD     | 10.58.24.190/28    | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_3     | k8s/vk8s_3_BD     | 10.58.24.206/28    | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_4     | k8s/vk8s_4_BD     | 10.58.24.222/28    | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                        |                   |                    |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+-------------------+--------------------+----------+------+----------------------+----------+--------+----------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s

{
    "duration": 5734,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 492,
        "disconnect_time": 0,
        "mo_time": 4061,
        "total_time": 4553
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

True	492	-	connect apic21o.emea-sp.cisco.com:443
True	402	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	339	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	374	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	350	152	apic21o.emea-sp.cisco.com:443 class fvLocale
True	429	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	386	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	443	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	336	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	334	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	329	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	339	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./ApplicationEpg.md)