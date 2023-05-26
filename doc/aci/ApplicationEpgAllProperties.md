# Application Endpoint Group (EPG)

## Get EPGs properties

Use '-o props' to get properties of selected epgs
- epg name, application profile and tenant
- preferred member
- flood
- class id
- QoS class
- isolation
- label match

```
# iserver get aci epg --apic apic21 -o prop

Apic: apic21

+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| Up | EPG                                | Preferred Member | Flood    | Class ID | QoS Class   | Isolation  | Label Match |
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | common/privIP_TEST/privIP_TEST     | exclude          | disabled | 16388    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | common/Test_ANP/Test_EPG           | exclude          | disabled | 16387    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | hefernan_ni-demo/APP/EPG1          | exclude          | disabled | 49153    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | hefernan_ni-demo/APP/EPG2          | exclude          | disabled | 49154    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | infra/access/default               | exclude          | disabled | 49153    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | infra/ave-ctrl/ave-ctrl            | exclude          | disabled | 16386    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/backbone1              | exclude          | disabled | 49167    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/bmk8s_1                | exclude          | disabled | 16404    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/bmk8s_2                | exclude          | disabled | 49165    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/bmk8s_prov             | exclude          | disabled | 49163    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/csr1_lan               | exclude          | disabled | 16387    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/csr2_lan               | exclude          | disabled | 16389    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/csr_b2b                | exclude          | disabled | 16390    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/MGMT                   | exclude          | disabled | 32772    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/site1_lan              | exclude          | disabled | 16388    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/site1_pe               | exclude          | disabled | 49168    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/site2_lan              | exclude          | disabled | 32773    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/site2_pe               | exclude          | disabled | 32775    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/SRIoV_A                | exclude          | disabled | 32772    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/SRIoV_B                | exclude          | disabled | 32771    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/Test                   | exclude          | disabled | 32773    | level2      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_1                 | exclude          | disabled | 49162    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_2                 | exclude          | disabled | 49164    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_3                 | exclude          | disabled | 49166    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_4                 | exclude          | disabled | 16403    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | exclude          | disabled | 32771    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      | exclude          | disabled | 16387    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | nidemo/streamz/appserver           | exclude          | disabled | 49155    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | nidemo/streamz/database            | exclude          | disabled | 16390    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | nidemo/streamz/frontend            | exclude          | disabled | 49156    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | nidemo/streamz/management          | exclude          | disabled | 16389    | unspecified | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPN_IntraLab/SPN_Connect_ANP/TEST2 | exclude          | disabled | 32770    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | TESTING_BRUNO/sdfgd/site2          | exclude          | disabled | 49154    | unspecified | unenforced | None        | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | TESTING_BRUNO/UntitledAP1/SITE1    | exclude          | disabled | 49155    | unspecified | unenforced | None        | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | vEPC/vSFO_ANP/WWW                  | exclude          | disabled | 32771    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_ACC        | exclude          | disabled | 16386    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_CTRL       | exclude          | disabled | 32772    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_INT        | exclude          | disabled | 32771    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_MGMT       | exclude          | disabled | 49158    | level3      | unenforced | AtleastOne  | 
+----+------------------------------------+------------------+----------+----------+-------------+------------+-------------+
```

[[Back]](./ApplicationEpg.md)