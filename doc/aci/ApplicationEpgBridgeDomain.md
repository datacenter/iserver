# Application Endpoint Group (EPG)

## Filter by bridge domain name

```
# iserver get aci epg --apic apic21 --bd sriov*

Apic: apic21 (mode:online, cache:off)

EPG [#2]
--------

+--------+---------+----+---------------------+----------+----------------+-----------------+----------+----------------------+------------------+----------+--------+----------+-----------+
| Health | Faults  | Up | EPG                 | Class ID | BD             | BD Subnet       | Endpoint | Node                 | Domain           | Contract | StPort | StMember | DynMember |
+--------+---------+----+---------------------+----------+----------------+-----------------+----------+----------------------+------------------+----------+--------+----------+-----------+
| 100    | 0 0 0 0 | V  | k8s/k8s_ANP/SRIoV_A | 32772    | k8s/SRIoV_A_BD | 15.20.16.254/24 | 1        | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom  | 3        | 14     | 14       | 0         | 
|        |         |    |                     |          |                |                 |          | pod-1/cl2207-eu-spdc | k8s_phys_PhysDom |          |        |          |           | 
+--------+---------+----+---------------------+----------+----------------+-----------------+----------+----------------------+------------------+----------+--------+----------+-----------+
| 82     | 0 0 0 0 | V  | k8s/k8s_ANP/SRIoV_B | 32771    | k8s/SRIoV_B_BD | 15.20.17.254/24 | 1        | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom  | 0        | 14     | 14       | 0         | 
|        |         |    |                     |          |                |                 |          | pod-1/cl2207-eu-spdc | k8s_phys_PhysDom |          |        |          |           | 
+--------+---------+----+---------------------+----------+----------------+-----------------+----------+----------------------+------------------+----------+--------+----------+-----------+
```

## Filter by bridge domain tenant and name

```
# iserver get aci epg --apic apic21 --bd nidemo/*

Apic: apic21 (mode:online, cache:off)

EPG [#4]
--------

+--------+---------+----+---------------------------+----------+-------------------+-------------+----------+----------------------+-----------------------+----------+--------+----------+-----------+
| Health | Faults  | Up | EPG                       | Class ID | BD                | BD Subnet   | Endpoint | Node                 | Domain                | Contract | StPort | StMember | DynMember |
+--------+---------+----+---------------------------+----------+-------------------+-------------+----------+----------------------+-----------------------+----------+--------+----------+-----------+
| 100    | 0 0 0 0 | V  | nidemo/streamz/appserver  | 49155    | nidemo/appserver  | 10.0.2.1/24 | 1        | pod-1/cl2202-eu-spdc | VMware/EU-SPDC-CDC-22 | 3        | 0      | 0        | 2         | 
|        |         |    |                           |          |                   |             |          | pod-1/cl2201-eu-spdc |                       |          |        |          |           | 
+--------+---------+----+---------------------------+----------+-------------------+-------------+----------+----------------------+-----------------------+----------+--------+----------+-----------+
| 80     | 0 0 0 0 | V  | nidemo/streamz/database   | 16390    | nidemo/database   | 10.0.3.1/24 | 1        | pod-1/cl2201-eu-spdc | VMware/EU-SPDC-CDC-22 | 2        | 1      | 1        | 2         | 
|        |         |    |                           |          |                   |             |          | pod-1/rl2702-eu-spdc | nidemo                |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/cl2202-eu-spdc |                       |          |        |          |           | 
+--------+---------+----+---------------------------+----------+-------------------+-------------+----------+----------------------+-----------------------+----------+--------+----------+-----------+
| 100    | 0 0 0 0 | V  | nidemo/streamz/frontend   | 49156    | nidemo/frontend   | 10.0.1.1/24 | 4        | pod-1/bl2205-eu-spdc | VMware/EU-SPDC-CDC-22 | 3        | 0      | 0        | 6         | 
|        |         |    |                           |          |                   |             |          | pod-1/rl2701-eu-spdc |                       |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/bl2206-eu-spdc |                       |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/rl2702-eu-spdc |                       |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/cl2202-eu-spdc |                       |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/cl2201-eu-spdc |                       |          |        |          |           | 
+--------+---------+----+---------------------------+----------+-------------------+-------------+----------+----------------------+-----------------------+----------+--------+----------+-----------+
| 85     | 0 0 0 0 | V  | nidemo/streamz/management | 16389    | nidemo/management | 10.0.4.1/24 | 1        | pod-1/cl2201-eu-spdc | VMware/EU-SPDC-CDC-22 | 1        | 0      | 0        | 2         | 
|        |         |    |                           |          |                   |             |          | pod-1/rl2701-eu-spdc | VMware/EU-SPDC-POD2B  |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/rl2702-eu-spdc | VMware/EU-SPDC-R7DC   |          |        |          |           | 
|        |         |    |                           |          |                   |             |          | pod-1/cl2202-eu-spdc |                       |          |        |          |           | 
+--------+---------+----+---------------------------+----------+-------------------+-------------+----------+----------------------+-----------------------+----------+--------+----------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --bd sriov*

{
    "duration": 6962,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 487,
        "disconnect_time": 0,
        "mo_time": 5506,
        "total_time": 5993
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

True	487	-	connect apic21o.emea-sp.cisco.com:443
True	493	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	357	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	420	282	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	1401	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	453	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	454	99	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	448	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	361	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	379	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	370	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	370	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./ApplicationEpg.md)