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
| vEPC/vSFO_ANP                | vEPC/WWW              | unspecified | 
+------------------------------+-----------------------+-------------+
| vEPC_demo/vEPG_ANP           | vEPC_demo/vEPG_ACC    | unspecified | 
|                              | vEPC_demo/vEPG_CTRL   |             | 
|                              | vEPC_demo/vEPG_INT    |             | 
|                              | vEPC_demo/vEPG_MGMT   |             | 
+------------------------------+-----------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21

{
    "duration": 1206,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 663,
        "total_time": 1048
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

True	385	-	connect apic21o.emea-sp.cisco.com
True	317	12	apic21o.emea-sp.cisco.com class fvAp
True	346	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

[[Back]](./ApplicationProfile.md)