# Application Profile (AP)

## Default output

```
# iserver get aci ap --apic apic21

Apic: apic21 (mode:online, cache:off)

Application Profile [#12]
-------------------------

+--------+---------+------------------------------+-----------------------+-------------+
| Health | Faults  | Application Profile          | Application EPGs      | Priority    |
+--------+---------+------------------------------+-----------------------+-------------+
| 100    | 0 0 0 0 | common/default               |                       | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 100    | 0 0 0 0 | common/privIP_TEST           | common/privIP_TEST    | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 100    | 0 0 0 0 | common/Test_ANP              | common/Test_EPG       | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 61     | 0 0 0 0 | hefernan_ni-demo/APP         | hefernan_ni-demo/EPG1 | unspecified | 
|        |         |                              | hefernan_ni-demo/EPG2 |             | 
+--------+---------+------------------------------+-----------------------+-------------+
| 100    | 0 0 0 0 | infra/access                 | infra/default         | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 100    | 0 0 0 0 | infra/ave-ctrl               | infra/ave-ctrl        | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 95     | 0 0 2 0 | k8s/k8s_ANP                  | k8s/backbone1         | unspecified | 
|        |         |                              | k8s/bmk8s_1           |             | 
|        |         |                              | k8s/bmk8s_2           |             | 
|        |         |                              | k8s/bmk8s_prov        |             | 
|        |         |                              | k8s/csr1_lan          |             | 
|        |         |                              | k8s/csr2_lan          |             | 
|        |         |                              | k8s/csr_b2b           |             | 
|        |         |                              | k8s/MGMT              |             | 
|        |         |                              | k8s/site1_lan         |             | 
|        |         |                              | k8s/site1_pe          |             | 
|        |         |                              | k8s/site2_lan         |             | 
|        |         |                              | k8s/site2_pe          |             | 
|        |         |                              | k8s/SRIoV_A           |             | 
|        |         |                              | k8s/SRIoV_B           |             | 
|        |         |                              | k8s/Test              |             | 
|        |         |                              | k8s/vk8s_1            |             | 
|        |         |                              | k8s/vk8s_2            |             | 
|        |         |                              | k8s/vk8s_3            |             | 
|        |         |                              | k8s/vk8s_4            |             | 
+--------+---------+------------------------------+-----------------------+-------------+
| 61     | 0 0 0 0 | mgmt/EU-SPDC_ANP             | mgmt/EU-SPDC-ERSPAN   | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 93     | 0 0 0 0 | nidemo/streamz               | nidemo/appserver      | unspecified | 
|        |         |                              | nidemo/database       |             | 
|        |         |                              | nidemo/frontend       |             | 
|        |         |                              | nidemo/management     |             | 
+--------+---------+------------------------------+-----------------------+-------------+
| 79     | 0 0 2 0 | SPN_IntraLab/SPN_Connect_ANP | SPN_IntraLab/TEST2    | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 59     | 0 0 0 0 | vEPC/vSFO_ANP                | vEPC/WWW              | unspecified | 
+--------+---------+------------------------------+-----------------------+-------------+
| 87     | 0 0 8 0 | vEPC_demo/vEPG_ANP           | vEPC_demo/vEPG_ACC    | unspecified | 
|        |         |                              | vEPC_demo/vEPG_CTRL   |             | 
|        |         |                              | vEPC_demo/vEPG_INT    |             | 
|        |         |                              | vEPC_demo/vEPG_MGMT   |             | 
+--------+---------+------------------------------+-----------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21

{
    "duration": 2471,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 508,
        "disconnect_time": 0,
        "mo_time": 1280,
        "total_time": 1788
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

True	508	-	connect apic21o.emea-sp.cisco.com:443
True	450	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	483	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	347	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationProfile.md)