# Application Endpoint Group (EPG)

## Filter by bridge domain name

```
# iserver get aci epg --apic apic21 --bd sriov*

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
| Up | EPG                 | BD             | BD Subnet       | Endpoint | Node | Domain           | Contract | StPort | StMember | DynMember |
+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_A | k8s/SRIoV_A_BD | 15.20.16.254/24 | 1        |      | k8s_esx_PhysDom  | 3        | 14     | 0        | 0         | 
|    |                     |                |                 |          |      | k8s_phys_PhysDom |          |        |          |           | 
+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_B | k8s/SRIoV_B_BD | 15.20.17.254/24 | 1        |      | k8s_esx_PhysDom  | 0        | 14     | 0        | 0         | 
|    |                     |                |                 |          |      | k8s_phys_PhysDom |          |        |          |           | 
+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
```

## Filter by bridge domain tenant and name

```
# iserver get aci epg --apic apic21 --bd nidemo/*

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+---------------------------+-------------------+-------------+----------+------+-----------------------+----------+--------+----------+-----------+
| Up | EPG                       | BD                | BD Subnet   | Endpoint | Node | Domain                | Contract | StPort | StMember | DynMember |
+----+---------------------------+-------------------+-------------+----------+------+-----------------------+----------+--------+----------+-----------+
| V  | nidemo/streamz/appserver  | nidemo/appserver  | 10.0.2.1/24 | 1        |      | VMware/EU-SPDC-CDC-22 | 3        | 0      | 0        | 0         | 
+----+---------------------------+-------------------+-------------+----------+------+-----------------------+----------+--------+----------+-----------+
| V  | nidemo/streamz/database   | nidemo/database   | 10.0.3.1/24 | 1        |      | VMware/EU-SPDC-CDC-22 | 2        | 1      | 0        | 0         | 
|    |                           |                   |             |          |      | nidemo                |          |        |          |           | 
+----+---------------------------+-------------------+-------------+----------+------+-----------------------+----------+--------+----------+-----------+
| V  | nidemo/streamz/frontend   | nidemo/frontend   | 10.0.1.1/24 | 4        |      | VMware/EU-SPDC-CDC-22 | 3        | 0      | 0        | 0         | 
+----+---------------------------+-------------------+-------------+----------+------+-----------------------+----------+--------+----------+-----------+
| V  | nidemo/streamz/management | nidemo/management | 10.0.4.1/24 | 1        |      | VMware/EU-SPDC-CDC-22 | 1        | 0      | 0        | 0         | 
|    |                           |                   |             |          |      | VMware/EU-SPDC-POD2B  |          |        |          |           | 
|    |                           |                   |             |          |      | VMware/EU-SPDC-R7DC   |          |        |          |           | 
+----+---------------------------+-------------------+-------------+----------+------+-----------------------+----------+--------+----------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --bd sriov*

{
    "duration": 5148,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 3935,
        "total_time": 4340
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

True	405	-	connect apic21o.emea-sp.cisco.com:443
True	386	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	322	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	347	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	351	152	apic21o.emea-sp.cisco.com:443 class fvLocale
True	408	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	404	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	352	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	344	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	355	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	321	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	345	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./ApplicationEpg.md)