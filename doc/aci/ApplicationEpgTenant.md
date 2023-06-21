# Application Endpoint Group (EPG)

## Filter by tenant name

```
# iserver get aci epg --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| Up | EPG                    | Class ID | BD                | BD Subnet          | Endpoint | Node                 | Domain               | Contract | StPort | StMember | DynMember |
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/backbone1  | 49167    | k8s/VM2VM_BD      |                    | 2        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/bmk8s_1    | 16404    | k8s/bmk8s_1_BD    | 10.58.24.78/28     | 0        | pod-1/cl2207-eu-spdc | k8s_phys_PhysDom     | 1        | 1      | 2        | 0         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc |                      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/bmk8s_2    | 49165    | k8s/bmk8s_2_BD    | 10.58.24.94/28     | 0        | pod-1/cl2208-eu-spdc | k8s_phys_PhysDom     | 1        | 1      | 2        | 0         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc |                      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/bmk8s_prov | 49163    | k8s/bmk8s_prov_BD | 10.58.29.94/28     | 4        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 5      | 10       | 0         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
|    |                        |          |                   |                    |          |                      | k8s_phys_PhysDom     |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/csr1_lan   | 16387    | k8s/VM2VM_BD      |                    | 1        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/csr2_lan   | 16389    | k8s/VM2VM_BD      |                    | 1        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/csr_b2b    | 16390    | k8s/VM2VM_BD      |                    | 0        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/MGMT       | 32772    | k8s/MGMT_BD       | 10.58.25.174/28    | 0        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 1      | 2        | 0         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site1_lan  | 16388    | k8s/VM2VM_BD      |                    | 1        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site1_pe   | 49168    | k8s/VM2VM_BD      |                    | 2        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site2_lan  | 32773    | k8s/VM2VM_BD      |                    | 1        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/site2_pe   | 32775    | k8s/VM2VM_BD      |                    | 2        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 0        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_A    | 32772    | k8s/SRIoV_A_BD    | 15.20.16.254/24    | 1        | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      | 3        | 14     | 14       | 0         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_phys_PhysDom     |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_B    | 32771    | k8s/SRIoV_B_BD    | 15.20.17.254/24    | 2        | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      | 0        | 14     | 14       | 0         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_phys_PhysDom     |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/Test       | 32773    | k8s/Test          | 169.169.169.254/24 | 0        |                      |                      | 0        | 0      | 0        | 0         | 
|    |                        |          |                   | 169.169.170.254/24 |          |                      |                      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_1     | 49162    | k8s/vk8s_1_BD     | 10.58.24.174/28    | 8        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_2     | 49164    | k8s/vk8s_2_BD     | 10.58.24.190/28    | 8        | pod-1/cl2208-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2207-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_3     | 49166    | k8s/vk8s_3_BD     | 10.58.24.206/28    | 8        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_4     | 16403    | k8s/vk8s_4_BD     | 10.58.24.222/28    | 8        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 4         | 
|    |                        |          |                   |                    |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+------------------------+----------+-------------------+--------------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s

{
    "duration": 7875,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 6178,
        "total_time": 6593
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

True	415	-	connect apic21o.emea-sp.cisco.com:443
True	2480	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	324	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	335	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	331	152	apic21o.emea-sp.cisco.com:443 class fvLocale
True	406	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	545	96	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	383	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	363	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	356	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	334	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	321	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./ApplicationEpg.md)