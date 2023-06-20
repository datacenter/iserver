# Application Endpoint Group (EPG)

## Get EPGs' contract properties

Use '--view contract' to get contract properties of selected epgs
- epg name, application profile and tenant
- contracts consumed, provided and taboo

```
# iserver get aci epg --apic apic21 --tenant k8s --view contract

Apic: apic21 (mode:online, cache:off)

EPG Contracts
-------------

+----+------------------------+----------+-------------------+-------------------+---------------------+
| Up | EPG                    | Class ID | Contract Consumed | Contract Provided | Contract Taboo      |
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/backbone1  | 49167    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/bmk8s_1    | 16404    | common/k8s_bm     |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/bmk8s_2    | 49165    | common/k8s_bm     |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/bmk8s_prov | 49163    | common/k8s_prov   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/csr1_lan   | 16387    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/csr2_lan   | 16389    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/csr_b2b    | 16390    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/MGMT       | 32772    | common/ESX_mgmt   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/site1_lan  | 16388    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/site1_pe   | 49168    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/site2_lan  | 32773    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/site2_pe   | 32775    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/SRIoV_A    | 32772    | k8s/BT-Demo       | k8s/BT-Demo       | k8s/MyTabooContract | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/SRIoV_B    | 32771    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/Test       | 32773    |                   |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/vk8s_1     | 49162    | common/k8s_vm     |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/vk8s_2     | 49164    | common/k8s_vm     |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/vk8s_3     | 49166    | common/k8s_vm     |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/vk8s_4     | 16403    | common/k8s_vm     |                   |                     | 
+----+------------------------+----------+-------------------+-------------------+---------------------+
```

Use '--pivot' flag to get contract specific output

```
# iserver get aci epg --apic apic21 --view contract --pivot

Apic: apic21 (mode:online, cache:off)

EPG Contracts (pivot view)
--------------------------

+-----------------------------+----------+-------------------------------------------+
| Contract                    | Type     | EPG                                       |
+-----------------------------+----------+-------------------------------------------+
| common/ESX_mgmt             | Contract | k8s/k8s_ANP/MGMT (Consumed)               | 
+-----------------------------+----------+-------------------------------------------+
| common/default              | Contract | common/privIP_TEST/privIP_TEST (Provided) | 
|                             |          | common/Test_ANP/Test_EPG (Provided)       | 
|                             |          | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT (Consumed)  | 
+-----------------------------+----------+-------------------------------------------+
| common/k8s_bm               | Contract | k8s/k8s_ANP/bmk8s_1 (Consumed)            | 
|                             |          | k8s/k8s_ANP/bmk8s_2 (Consumed)            | 
+-----------------------------+----------+-------------------------------------------+
| common/k8s_prov             | Contract | k8s/k8s_ANP/bmk8s_prov (Consumed)         | 
+-----------------------------+----------+-------------------------------------------+
| common/k8s_vm               | Contract | k8s/k8s_ANP/vk8s_1 (Consumed)             | 
|                             |          | k8s/k8s_ANP/vk8s_2 (Consumed)             | 
|                             |          | k8s/k8s_ANP/vk8s_3 (Consumed)             | 
|                             |          | k8s/k8s_ANP/vk8s_4 (Consumed)             | 
+-----------------------------+----------+-------------------------------------------+
| common/vEPG-MGMT_alltraffic | Contract | vEPC_demo/vEPG_ANP/vEPG_MGMT (Provided)   | 
+-----------------------------+----------+-------------------------------------------+
| hefernan_ni-demo/PERMIT_ALL | Contract | hefernan_ni-demo/APP/EPG1 (Consumed)      | 
|                             |          | hefernan_ni-demo/APP/EPG2 (Provided)      | 
+-----------------------------+----------+-------------------------------------------+
| k8s/BT-Demo                 | Contract | k8s/k8s_ANP/SRIoV_A (Consumed)            | 
|                             |          | k8s/k8s_ANP/SRIoV_A (Provided)            | 
+-----------------------------+----------+-------------------------------------------+
| k8s/MyTabooContract         | Taboo    | k8s/k8s_ANP/SRIoV_A                       | 
+-----------------------------+----------+-------------------------------------------+
| nidemo/app-service          | Contract | nidemo/streamz/appserver (Provided)       | 
|                             |          | nidemo/streamz/frontend (Consumed)        | 
+-----------------------------+----------+-------------------------------------------+
| nidemo/database-service     | Contract | nidemo/streamz/appserver (Consumed)       | 
|                             |          | nidemo/streamz/database (Provided)        | 
+-----------------------------+----------+-------------------------------------------+
| nidemo/frontend-service     | Contract | nidemo/streamz/frontend (Provided)        | 
+-----------------------------+----------+-------------------------------------------+
| nidemo/management-access    | Contract | nidemo/streamz/appserver (Provided)       | 
|                             |          | nidemo/streamz/database (Provided)        | 
|                             |          | nidemo/streamz/frontend (Provided)        | 
|                             |          | nidemo/streamz/management (Consumed)      | 
+-----------------------------+----------+-------------------------------------------+
| vEPC/vEPC_alltraffic        | Contract | vEPC/vSFO_ANP/WWW (Consumed)              | 
+-----------------------------+----------+-------------------------------------------+
| vEPC_demo/vEPG_ACC          | Contract | vEPC_demo/vEPG_ANP/vEPG_ACC (Provided)    | 
+-----------------------------+----------+-------------------------------------------+
| vEPC_demo/vEPG_INT          | Contract | vEPC_demo/vEPG_ANP/vEPG_INT (Provided)    | 
+-----------------------------+----------+-------------------------------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s --view contract

{
    "duration": 3570,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 423,
        "disconnect_time": 0,
        "mo_time": 2514,
        "total_time": 2937
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

True	423	-	connect apic21o.emea-sp.cisco.com:443
True	423	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	329	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	372	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	356	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	356	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	338	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	340	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./ApplicationEpg.md)