# Application Endpoint Group (EPG)

## Filter by contract name

```
# iserver get aci epg --apic apic21 --contract *all* --view contract

Apic: apic21 (mode:online, cache:off)

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

+-----------------------------+---------+---------+-------------+-------------------------+----------------------+
| Contract                    | Scope   | Intent  | Target DSCP | Subject                 | Filter               |
+-----------------------------+---------+---------+-------------+-------------------------+----------------------+
| common/vEPG-MGMT_alltraffic | global  | install | unspecified | common/IKSHS-alltraffic | common/alltraffic    | 
+-----------------------------+---------+---------+-------------+-------------------------+----------------------+
| hefernan_ni-demo/PERMIT_ALL | context | install | unspecified | common/default          | common/default       | 
+-----------------------------+---------+---------+-------------+-------------------------+----------------------+
| vEPC/vEPC_alltraffic        | tenant  | install | unspecified | vEPC/vEPC_alltraffic    | vEPC/vEPC_alltraffic | 
+-----------------------------+---------+---------+-------------+-------------------------+----------------------+

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
    "duration": 3932,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 3196,
        "total_time": 3608
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

True	412	-	connect apic21o.emea-sp.cisco.com:443
True	366	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	378	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	341	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	412	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	420	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	495	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	379	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	405	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)