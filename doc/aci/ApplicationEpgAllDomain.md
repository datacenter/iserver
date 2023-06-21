# Application Endpoint Group (EPG)

## Get EPGs' domain properties

```
# iserver get aci epg --apic apic21 --tenant k8s --view domain

Apic: apic21 (mode:online, cache:off)

EPG Domain
----------

+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| EPG                    | Domain Name          | Domain Type | Deployment | Resolution    | Switching Mode | Encap Mode | CoS  |
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/backbone1  | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/bmk8s_1    | k8s_phys_PhysDom     | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/bmk8s_2    | k8s_phys_PhysDom     | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/bmk8s_prov | VMware/EU-SPDC-POD2B | VMM         | immediate  | pre-provision | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
|                        | k8s_phys_PhysDom     | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/csr1_lan   | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/csr2_lan   | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/csr_b2b    | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/MGMT       | VMware/EU-SPDC-POD2B | VMM         | immediate  | pre-provision | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/site1_lan  | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/site1_pe   | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/site2_lan  | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/site2_pe   | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/SRIoV_A    | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
|                        | k8s_phys_PhysDom     | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/SRIoV_B    | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
|                        | k8s_phys_PhysDom     | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/Test       |                      |             |            |               |                |            |      | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/vk8s_1     | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/vk8s_2     | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/vk8s_3     | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
| k8s/k8s_ANP/vk8s_4     | VMware/EU-SPDC-POD2B | VMM         | immediate  | immediate     | native         | auto       | Cos0 | 
|                        | k8s_esx_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | 
+------------------------+----------------------+-------------+------------+---------------+----------------+------------+------+
```

Use '--pivot' option to get the domain specific output

```
# iserver get aci epg --apic apic21 --view domain --pivot

Apic: apic21 (mode:online, cache:off)

EPG Domain (pivot view)
-----------------------

+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| Domain Name           | Domain Type | Deployment | Resolution    | Switching Mode | Encap Mode | CoS  | EPG                                |
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| VMware/EU-SPDC-CDC-22 | VMM         | immediate  | immediate     | native         | auto       | Cos0 | common/privIP_TEST/privIP_TEST     | 
|                       |             |            |               |                |            |      | hefernan_ni-demo/APP/EPG1          | 
|                       |             |            |               |                |            |      | hefernan_ni-demo/APP/EPG2          | 
|                       |             |            |               |                |            |      | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | 
|                       |             |            |               |                |            |      | nidemo/streamz/appserver           | 
|                       |             |            |               |                |            |      | nidemo/streamz/database            | 
|                       |             |            |               |                |            |      | nidemo/streamz/frontend            | 
|                       |             |            |               |                |            |      | nidemo/streamz/management          | 
|                       |             |            |               |                |            |      | SPN_IntraLab/SPN_Connect_ANP/TEST2 | 
|                       |             |            |               |                |            |      | vEPC/vSFO_ANP/WWW                  | 
|                       |             |            |               |                |            |      | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| ESX-CDC-22_PhysDom    | Physical    | lazy       | immediate     | native         | auto       | Cos0 | common/Test_ANP/Test_EPG           | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| VMware/EU-SPDC-POD2B  | VMM         | immediate  | immediate     | native         | auto       | Cos0 | k8s/k8s_ANP/backbone1              | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/bmk8s_prov             | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/csr1_lan               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/csr2_lan               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/csr_b2b                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/MGMT                   | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site1_lan              | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site1_pe               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site2_lan              | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site2_pe               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_1                 | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_2                 | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_3                 | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_4                 | 
|                       |             |            |               |                |            |      | nidemo/streamz/management          | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| k8s_esx_PhysDom       | Physical    | lazy       | lazy          | native         | auto       | Cos0 | k8s/k8s_ANP/backbone1              | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/bmk8s_prov             | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/csr1_lan               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/csr2_lan               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/csr_b2b                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/MGMT                   | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site1_lan              | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site1_pe               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site2_lan              | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/site2_pe               | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/SRIoV_A                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/SRIoV_B                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_1                 | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_2                 | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_3                 | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/vk8s_4                 | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| k8s_phys_PhysDom      | Physical    | lazy       | lazy          | native         | auto       | Cos0 | k8s/k8s_ANP/bmk8s_1                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/bmk8s_2                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/bmk8s_prov             | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/SRIoV_A                | 
|                       |             |            |               |                |            |      | k8s/k8s_ANP/SRIoV_B                | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| Infra_PhysDom         | Physical    | lazy       | immediate     | native         | auto       | Cos0 | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| nidemo                | Physical    | lazy       | immediate     | native         | auto       | Cos0 | nidemo/streamz/database            | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| VMware/EU-SPDC-R7DC   | VMM         | lazy       | pre-provision | native         | auto       | Cos0 | nidemo/streamz/management          | 
|                       |             |            |               |                |            |      | vEPC/vSFO_ANP/WWW                  | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| SPN_PhysDom           | Physical    | lazy       | immediate     | native         | auto       | Cos0 | SPN_IntraLab/SPN_Connect_ANP/TEST2 | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| VMware/vEPC-Dataplane | VMM         | immediate  | immediate     | native         | auto       | Cos0 | vEPC_demo/vEPG_ANP/vEPG_ACC        | 
|                       |             |            |               |                |            |      | vEPC_demo/vEPG_ANP/vEPG_CTRL       | 
|                       |             |            |               |                |            |      | vEPC_demo/vEPG_ANP/vEPG_INT        | 
|                       |             |            |               |                |            |      | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| HX1_PhysDom           | Physical    | lazy       | immediate     | native         | auto       | Cos0 | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| UCSB1_PhysDom         | Physical    | lazy       | immediate     | native         | auto       | Cos0 | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
| vEPC-ESX21-22_PhysDom | Physical    | lazy       | immediate     | native         | auto       | Cos0 | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
+-----------------------+-------------+------------+---------------+----------------+------------+------+------------------------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s --view domain

{
    "duration": 2111,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1066,
        "total_time": 1467
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

True	401	-	connect apic21o.emea-sp.cisco.com:443
True	379	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	320	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	367	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
```

[[Back]](./ApplicationEpg.md)