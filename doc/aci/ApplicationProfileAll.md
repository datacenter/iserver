# Application Profile (AP)

## Get application profile properties

```
# iserver get aci ap --apic apic21

Apic: apic21

+------------------------------+-----------------------+-------------+
| Application Profile          | Application EPGs      | Priority    |
+------------------------------+-----------------------+-------------+
| common/default               |                       | unspecified | 
+------------------------------+-----------------------+-------------+
| common/privIP_TEST           | common/privIP_TEST    | unspecified | 
+------------------------------+-----------------------+-------------+
| common/Test_ANP              | common/Test_EPG       | unspecified | 
+------------------------------+-----------------------+-------------+
| hefernan_ni-demo/APP         | hefernan_ni-demo/EPG1 | unspecified | 
|                              | hefernan_ni-demo/EPG2 |             | 
+------------------------------+-----------------------+-------------+
| infra/access                 | infra/default         | unspecified | 
+------------------------------+-----------------------+-------------+
| infra/ave-ctrl               | infra/ave-ctrl        | unspecified | 
+------------------------------+-----------------------+-------------+
| k8s/k8s_ANP                  | k8s/backbone1         | unspecified | 
|                              | k8s/bmk8s_1           |             | 
|                              | k8s/bmk8s_2           |             | 
|                              | k8s/bmk8s_prov        |             | 
|                              | k8s/csr1_lan          |             | 
|                              | k8s/csr2_lan          |             | 
|                              | k8s/csr_b2b           |             | 
|                              | k8s/MGMT              |             | 
|                              | k8s/site1_lan         |             | 
|                              | k8s/site1_pe          |             | 
|                              | k8s/site2_lan         |             | 
|                              | k8s/site2_pe          |             | 
|                              | k8s/SRIoV_A           |             | 
|                              | k8s/SRIoV_B           |             | 
|                              | k8s/Test              |             | 
|                              | k8s/vk8s_1            |             | 
|                              | k8s/vk8s_2            |             | 
|                              | k8s/vk8s_3            |             | 
|                              | k8s/vk8s_4            |             | 
+------------------------------+-----------------------+-------------+
| mgmt/EU-SPDC_ANP             | mgmt/EU-SPDC-ERSPAN   | unspecified | 
|                              | mgmt/EU-SPDC-MGMT     |             | 
+------------------------------+-----------------------+-------------+
| nidemo/streamz               | nidemo/appserver      | unspecified | 
|                              | nidemo/database       |             | 
|                              | nidemo/frontend       |             | 
|                              | nidemo/management     |             | 
+------------------------------+-----------------------+-------------+
| SPN_IntraLab/SPN_Connect_ANP | SPN_IntraLab/TEST2    | unspecified | 
+------------------------------+-----------------------+-------------+
| TESTING_BRUNO/sdfgd          | TESTING_BRUNO/site2   | unspecified | 
+------------------------------+-----------------------+-------------+
| TESTING_BRUNO/UntitledAP1    | TESTING_BRUNO/SITE1   | unspecified | 
+------------------------------+-----------------------+-------------+
| vEPC/vSFO_ANP                | vEPC/WWW              | unspecified | 
+------------------------------+-----------------------+-------------+
| vEPC_demo/vEPG_ANP           | vEPC_demo/vEPG_ACC    | unspecified | 
|                              | vEPC_demo/vEPG_CTRL   |             | 
|                              | vEPC_demo/vEPG_INT    |             | 
|                              | vEPC_demo/vEPG_MGMT   |             | 
+------------------------------+-----------------------+-------------+
```

[[Back]](./ApplicationProfile.md)