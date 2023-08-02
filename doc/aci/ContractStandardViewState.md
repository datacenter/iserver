# Standard Contract

## State view

```
# iserver get aci contract standard --apic apic21

Apic: apic21 (mode:online, cache:off)

Standard Contract [#22]
-----------------------

+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| Faults  | Contract                     | Scope   | Intent  | Target DSCP | Subject                       | Filter                |
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/default               | context | install | unspecified | common/default                | common/default        | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/ESX_mgmt              | global  | install | unspecified | k8s/k8s_tn_vm                 | common/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/IKSHS-alltraffic      | global  | install | unspecified | common/vEPG-MGMT_alltraffic   | common/alltraffic     | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/k8s_bm                | global  | install | unspecified | k8s/k8s_tn_vm                 | common/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/k8s_prov              | global  | install | unspecified | k8s/k8s_tn_vm                 | common/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/k8s_vm                | global  | install | unspecified | k8s/k8s_tn_vm                 | common/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | common/vEPG-MGMT_alltraffic  | global  | install | unspecified | common/vEPG-MGMT_alltraffic   | common/alltraffic     | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | Ericsson_PACO/PERMIT_ALL     | context | install | unspecified | common/default                | common/default        | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | hefernan_ni-demo/PERMIT_ALL  | context | install | unspecified | common/default                | common/default        | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | hefernan_ni-demo/PERMIT_HTTP | context | install | unspecified | hefernan_ni-demo/PERMIT_HTTP  | hefernan_ni-demo/HTTP | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | k8s/BT-Demo                  | context | install | unspecified | k8s/Any                       | k8s/alltraffic        | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | k8s/k8s_tn_bm                | global  | install | unspecified | k8s/k8s_tn_vm                 | common/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | k8s/k8s_tn_vm                | global  | install | unspecified | k8s/k8s_tn_vm                 | common/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | mgmt/inband-default-contract | context | install | unspecified | mgmt/default                  | mgmt/inband-default   | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | nidemo/app-service           | tenant  | install | unspecified | nidemo/app-service            | nidemo/http           | 
|         |                              |         |         |             | nidemo/database-service       | nidemo/icmp           | 
|         |                              |         |         |             | nidemo/app-service            | nidemo/https          | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | nidemo/database-service      | tenant  | install | unspecified | nidemo/database-service       | nidemo/icmp           | 
|         |                              |         |         |             | nidemo/database-service       | nidemo/sql            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | nidemo/frontend-service      | tenant  | install | unspecified | nidemo/app-service            | nidemo/https          | 
|         |                              |         |         |             | nidemo/database-service       | nidemo/icmp           | 
|         |                              |         |         |             | nidemo/app-service            | nidemo/http           | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | nidemo/management-access     | tenant  | install | unspecified | nidemo/management-access      | nidemo/any            | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | vEPC/vEPC_alltraffic         | tenant  | install | unspecified | vEPC/vEPC_alltraffic          | vEPC/vEPC_alltraffic  | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | vEPC_demo/vEPG_ACC           | context | install | unspecified | vEPC_demo/vEPC_INT_alltraffic | vEPC_demo/alltraffic  | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | vEPC_demo/vEPG_INT           | context | install | unspecified | vEPC_demo/vEPC_INT_alltraffic | vEPC_demo/alltraffic  | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+
| 0 0 0 0 | vEPC_demo/vEPG_SX            | context | install | unspecified | vEPC_demo/vEPC_INT_alltraffic | vEPC_demo/alltraffic  | 
+---------+------------------------------+---------+---------+-------------+-------------------------------+-----------------------+

Contract Filter [#13]
---------------------

+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| Faults  | Filter                | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination   | Rules |
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | common/default        | default    |       |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | common/any            | any        | ipv4  |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | common/alltraffic     | alltraffic |       |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | hefernan_ni-demo/HTTP | HTTP       | ip    |          | tcp   | no        | no       |        | http - http   |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | k8s/alltraffic        | alltraffic |       |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | mgmt/inband-default   | default    |       |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | nidemo/http           | http       | ipv4  |          | tcp   | no        | no       |        | http - http   |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | nidemo/icmp           | icmp       | ipv4  |          | icmp  | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | nidemo/https          | https      | ipv4  |          | tcp   | no        | no       |        | https - https |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | nidemo/sql            | sql        | ipv4  |          | tcp   | no        | no       |        | 3306 - 3306   |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | nidemo/any            | any        | ipv4  |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | vEPC/vEPC_alltraffic  | alltraffic |       |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | vEPC_demo/alltraffic  | alltraffic |       |          |       | no        | no       |        |               |       | 
+---------+-----------------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
```

Developer

```
# iserver get aci contract standard --apic apic21

{
    "duration": 2450,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 509,
        "disconnect_time": 0,
        "mo_time": 1306,
        "total_time": 1815
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

True	509	-	connect apic21o.emea-sp.cisco.com:443
True	444	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	444	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	418	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractStandard.md)