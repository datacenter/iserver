# Application Endpoint Group (EPG)

## Filter by contract name

```
# iserver get aci epg --apic apic21 --contract *all* --view contract

Apic: apic21

+----+------------------------------+-----------------------------+-----------------------------+
| Up | EPG                          | Contract Consumed           | Contract Provided           |
+----+------------------------------+-----------------------------+-----------------------------+
| V  | hefernan_ni-demo/APP/EPG1    | hefernan_ni-demo/PERMIT_ALL |                             | 
+----+------------------------------+-----------------------------+-----------------------------+
| V  | hefernan_ni-demo/APP/EPG2    |                             | hefernan_ni-demo/PERMIT_ALL | 
+----+------------------------------+-----------------------------+-----------------------------+
| V  | vEPC/vSFO_ANP/WWW            | vEPC/vEPC_alltraffic        |                             | 
+----+------------------------------+-----------------------------+-----------------------------+
| V  | vEPC_demo/vEPG_ANP/vEPG_MGMT |                             | common/vEPG-MGMT_alltraffic | 
+----+------------------------------+-----------------------------+-----------------------------+

Standard Contracts
------------------

+-----------------------------+---------+---------+-------------+--------------------------+----------------------+
| Contract                    | Scope   | Intent  | Target DSCP | Subject                  | Filter               |
+-----------------------------+---------+---------+-------------+--------------------------+----------------------+
| common/vEPG-MGMT_alltraffic | global  | install | unspecified | common/IKSHS-alltraffic  | common/alltraffic    | 
+-----------------------------+---------+---------+-------------+--------------------------+----------------------+
| hefernan_ni-demo/PERMIT_ALL | context | install | unspecified | Ericsson_PACO/PERMIT_ALL | common/default       | 
+-----------------------------+---------+---------+-------------+--------------------------+----------------------+
| vEPC/vEPC_alltraffic        | tenant  | install | unspecified | vEPC/vEPC_alltraffic     | vEPC/vEPC_alltraffic | 
+-----------------------------+---------+---------+-------------+--------------------------+----------------------+

Contract Filters
----------------

+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter               | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/alltraffic    | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/default       | default    |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| vEPC/vEPC_alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
```

Developer

```
# iserver get aci epg --apic apic21 --contract *all* --view contract

{
    "duration": 5108,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 4354,
        "total_time": 4797
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

True	443	-	connect apic21o.emea-sp.cisco.com
True	818	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	412	53	apic21o.emea-sp.cisco.com class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	317	13	apic21o.emea-sp.cisco.com class fabricNode
True	1385	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	382	72	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	334	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	322	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	384	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)