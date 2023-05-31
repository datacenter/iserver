# Application Endpoint Group (EPG)

## Get EPGs' contract properties

Use '--view contract' to get contract properties of selected epgs
- epg name, application profile and tenant
- contracts consumed and provided

Following with contract and filter details of all related objects.

```
# iserver get aci epg --apic apic21 --view contract

Apic: apic21

+----+------------------------------------+-----------------------------+-----------------------------+
| Up | EPG                                | Contract Consumed           | Contract Provided           |
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | common/privIP_TEST/privIP_TEST     |                             | common/default              | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | common/Test_ANP/Test_EPG           |                             | common/default              | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | hefernan_ni-demo/APP/EPG1          | hefernan_ni-demo/PERMIT_ALL |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | hefernan_ni-demo/APP/EPG2          |                             | hefernan_ni-demo/PERMIT_ALL | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | infra/access/default               |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | infra/ave-ctrl/ave-ctrl            |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/backbone1              |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/bmk8s_1                | common/k8s_bm               |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/bmk8s_2                | common/k8s_bm               |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/bmk8s_prov             | common/k8s_prov             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/csr1_lan               |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/csr2_lan               |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/csr_b2b                |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/MGMT                   | common/ESX_mgmt             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/site1_lan              |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/site1_pe               |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/site2_lan              |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/site2_pe               |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/SRIoV_A                | k8s/BT-Demo                 | k8s/BT-Demo                 | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/SRIoV_B                |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/Test                   |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/vk8s_1                 | common/k8s_vm               |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/vk8s_2                 | common/k8s_vm               |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/vk8s_3                 | common/k8s_vm               |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | k8s/k8s_ANP/vk8s_4                 | common/k8s_vm               |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      | common/default              |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | nidemo/streamz/appserver           | nidemo/database-service     | nidemo/app-service          | 
|    |                                    |                             | nidemo/management-access    | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | nidemo/streamz/database            |                             | nidemo/management-access    | 
|    |                                    |                             | nidemo/database-service     | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | nidemo/streamz/frontend            | nidemo/app-service          | nidemo/frontend-service     | 
|    |                                    |                             | nidemo/management-access    | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | nidemo/streamz/management          | nidemo/management-access    |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | SPN_IntraLab/SPN_Connect_ANP/TEST2 |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | vEPC/vSFO_ANP/WWW                  | vEPC/vEPC_alltraffic        |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_ACC        |                             | vEPC_demo/vEPG_ACC          | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_CTRL       |                             |                             | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_INT        |                             | vEPC_demo/vEPG_INT          | 
+----+------------------------------------+-----------------------------+-----------------------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_MGMT       |                             | common/vEPG-MGMT_alltraffic | 
+----+------------------------------------+-----------------------------+-----------------------------+

Standard Contracts
------------------

+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| Contract                    | Scope   | Intent  | Target DSCP | Subject                       | Filter               |
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| common/default              | context | install | unspecified | Ericsson_PACO/PERMIT_ALL      | common/default       | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| common/ESX_mgmt             | global  | install | unspecified | k8s/k8s_tn_bm                 | common/any           | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| common/k8s_bm               | global  | install | unspecified | k8s/k8s_tn_bm                 | common/any           | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| common/k8s_prov             | global  | install | unspecified | k8s/k8s_tn_bm                 | common/any           | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| common/k8s_vm               | global  | install | unspecified | k8s/k8s_tn_bm                 | common/any           | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| common/vEPG-MGMT_alltraffic | global  | install | unspecified | common/IKSHS-alltraffic       | common/alltraffic    | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| hefernan_ni-demo/PERMIT_ALL | context | install | unspecified | Ericsson_PACO/PERMIT_ALL      | common/default       | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| k8s/BT-Demo                 | context | install | unspecified | k8s/Any                       | k8s/alltraffic       | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| nidemo/app-service          | tenant  | install | unspecified | nidemo/frontend-service       | nidemo/https         | 
|                             |         |         |             | nidemo/database-service       | nidemo/icmp          | 
|                             |         |         |             | nidemo/frontend-service       | nidemo/http          | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| nidemo/database-service     | tenant  | install | unspecified | nidemo/database-service       | nidemo/icmp          | 
|                             |         |         |             | nidemo/database-service       | nidemo/sql           | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| nidemo/frontend-service     | tenant  | install | unspecified | nidemo/frontend-service       | nidemo/https         | 
|                             |         |         |             | nidemo/database-service       | nidemo/icmp          | 
|                             |         |         |             | nidemo/frontend-service       | nidemo/http          | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| nidemo/management-access    | tenant  | install | unspecified | nidemo/management-access      | nidemo/any           | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| vEPC/vEPC_alltraffic        | tenant  | install | unspecified | vEPC/vEPC_alltraffic          | vEPC/vEPC_alltraffic | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| vEPC_demo/vEPG_ACC          | context | install | unspecified | vEPC_demo/vEPC_INT_alltraffic | vEPC_demo/alltraffic | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+
| vEPC_demo/vEPG_INT          | context | install | unspecified | vEPC_demo/vEPC_INT_alltraffic | vEPC_demo/alltraffic | 
+-----------------------------+---------+---------+-------------+-------------------------------+----------------------+

Contract Filters
----------------

+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| Filter               | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination   | Rules |
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| common/default       | default    |       |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| common/any           | any        | ipv4  |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| common/alltraffic    | alltraffic |       |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/alltraffic       | alltraffic |       |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| nidemo/https         | https      | ipv4  |          | tcp   | no        | no       |        | https - https |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| nidemo/icmp          | icmp       | ipv4  |          | icmp  | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| nidemo/http          | http       | ipv4  |          | tcp   | no        | no       |        | http - http   |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| nidemo/sql           | sql        | ipv4  |          | tcp   | no        | no       |        | 3306 - 3306   |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| nidemo/any           | any        | ipv4  |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| vEPC/vEPC_alltraffic | alltraffic |       |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| vEPC_demo/alltraffic | alltraffic |       |          |       | no        | no       |        |               |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
```

Developer

```
# iserver get aci epg --apic apic21 --view contract

{
    "duration": 4095,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 3105,
        "total_time": 3515
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

True	410	-	connect apic21o.emea-sp.cisco.com
True	365	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	568	53	apic21o.emea-sp.cisco.com class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	375	13	apic21o.emea-sp.cisco.com class fabricNode
True	379	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	378	73	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	353	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	345	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	342	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)