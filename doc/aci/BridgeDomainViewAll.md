# Bridge Domain

## All view

```
# iserver get aci bd --apic apic21 --name *vk8s* --when 60d --view all

Apic: apic21 (mode:online, cache:off)

Bridge Domain [#4]
------------------

+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| Health | Faults  | Bridge Domain | Class ID | VNID     | Subnet          | Usage | EPG        | VRF              | L3Out              |
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| 100    | 0 0 0 0 | k8s/vk8s_1_BD | 16399    | 15007706 | 10.58.24.174/28 | 10/14 | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| 100    | 0 0 0 0 | k8s/vk8s_2_BD | 32777    | 14745597 | 10.58.24.190/28 | 1/14  | k8s/vk8s_2 | common/Infra_VRF | common/Infra_L3out | 
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| 100    | 0 0 0 0 | k8s/vk8s_3_BD | 16400    | 15335346 | 10.58.24.206/28 | 2/14  | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| 100    | 0 0 0 0 | k8s/vk8s_4_BD | 32776    | 14843889 | 10.58.24.222/28 | 2/14  | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+

Bridge Domain - L2 Forwarding Properties [#4]
---------------------------------------------

+---------------+------------------+--------------+--------------+---------------------+------------------+
| Bridge Domain | L2 Unknown Ucast | Mcast (GIPo) | ARP Flooding | Multi Dest Flooding | Clear Remote MAC |
+---------------+------------------+--------------+--------------+---------------------+------------------+
| k8s/vk8s_1_BD | Flood            | 225.1.58.128 | V            | Flood in BD         | X                | 
+---------------+------------------+--------------+--------------+---------------------+------------------+
| k8s/vk8s_2_BD | Flood            | 225.0.87.208 | V            | Flood in BD         | X                | 
+---------------+------------------+--------------+--------------+---------------------+------------------+
| k8s/vk8s_3_BD | Flood            | 225.0.28.112 | V            | Flood in BD         | X                | 
+---------------+------------------+--------------+--------------+---------------------+------------------+
| k8s/vk8s_4_BD | Flood            | 225.1.182.64 | V            | Flood in BD         | X                | 
+---------------+------------------+--------------+--------------+---------------------+------------------+

Bridge Domain - L3 Forwarding Properties [#4]
---------------------------------------------

+---------------+---------------+-------------------+-------------+-------------+-------------------------+-----------------+------------------------+
| Bridge Domain | Ucast Routing | BD MAC            | Virtual MAC | IP Learning | Limit Local IP Learning | Adv Host Routes | EP Move Detection Mode |
+---------------+---------------+-------------------+-------------+-------------+-------------------------+-----------------+------------------------+
| k8s/vk8s_1_BD | V             | 00:22:BD:C8:11:FF | --          | V           | V                       | X               | --                     | 
+---------------+---------------+-------------------+-------------+-------------+-------------------------+-----------------+------------------------+
| k8s/vk8s_2_BD | V             | 00:22:BD:C8:22:FF | --          | V           | V                       | X               | --                     | 
+---------------+---------------+-------------------+-------------+-------------+-------------------------+-----------------+------------------------+
| k8s/vk8s_3_BD | V             | 00:22:BD:C8:33:FF | --          | V           | V                       | X               | --                     | 
+---------------+---------------+-------------------+-------------+-------------+-------------------------+-----------------+------------------------+
| k8s/vk8s_4_BD | V             | 00:22:BD:C8:44:FF | --          | V           | V                       | X               | --                     | 
+---------------+---------------+-------------------+-------------+-------------+-------------------------+-----------------+------------------------+

Bridge Domain - Multicast Properties [#4]
-----------------------------------------

+---------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| Bridge Domain | PIM | Unknown IPv4 Flooding | IGMP Snooping Policy | PIMv6 | Unknown IPv6 Flooding | MLD Snooping Policy |
+---------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_1_BD | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_2_BD | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_3_BD | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_4_BD | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+

Bridge Domain - VRF Properties [#4]
-----------------------------------

+---------------+------------------+----------+---------------+----------------+----------------+
| Bridge Domain | VRF              | Learning | PCE Direction | PCE Preference | BD Enforcement |
+---------------+------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_1_BD | common/Infra_VRF | V        | ingress       | unenforced     | X              | 
+---------------+------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_2_BD | common/Infra_VRF | V        | ingress       | unenforced     | X              | 
+---------------+------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_3_BD | common/Infra_VRF | V        | ingress       | unenforced     | X              | 
+---------------+------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_4_BD | common/Infra_VRF | V        | ingress       | unenforced     | X              | 
+---------------+------------------+----------+---------------+----------------+----------------+

Bridge Domain - Nodes [#4]
--------------------------

+---------+---------------+----------------+------------+
| Faults  | Bridge Domain | Node           | Interfaces |
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_1_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_2_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_3_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+
| 0 0 0 0 | k8s/vk8s_4_BD | cl2207-eu-spdc | 4          | 
|         |               | cl2208-eu-spdc | 4          | 
+---------+---------------+----------------+------------+

Bridge Domain - Interfaces [#4]
-------------------------------

+---------+---------------+----------------+-----------+
| Faults  | Bridge Domain | Node           | Interface |
+---------+---------------+----------------+-----------+
| 0 0 0 0 | k8s/vk8s_1_BD | cl2207-eu-spdc | eth1/1/1  | 
|         |               | cl2207-eu-spdc | eth1/1/2  | 
|         |               | cl2207-eu-spdc | po5       | 
|         |               | cl2207-eu-spdc | po6       | 
|         |               | cl2208-eu-spdc | eth1/1/1  | 
|         |               | cl2208-eu-spdc | eth1/1/2  | 
|         |               | cl2208-eu-spdc | po2       | 
|         |               | cl2208-eu-spdc | po3       | 
+---------+---------------+----------------+-----------+
| 0 0 0 0 | k8s/vk8s_2_BD | cl2207-eu-spdc | eth1/1/1  | 
|         |               | cl2207-eu-spdc | eth1/1/2  | 
|         |               | cl2207-eu-spdc | po5       | 
|         |               | cl2207-eu-spdc | po6       | 
|         |               | cl2208-eu-spdc | eth1/1/1  | 
|         |               | cl2208-eu-spdc | eth1/1/2  | 
|         |               | cl2208-eu-spdc | po2       | 
|         |               | cl2208-eu-spdc | po3       | 
+---------+---------------+----------------+-----------+
| 0 0 0 0 | k8s/vk8s_3_BD | cl2207-eu-spdc | eth1/1/1  | 
|         |               | cl2207-eu-spdc | eth1/1/2  | 
|         |               | cl2207-eu-spdc | po5       | 
|         |               | cl2207-eu-spdc | po6       | 
|         |               | cl2208-eu-spdc | eth1/1/1  | 
|         |               | cl2208-eu-spdc | eth1/1/2  | 
|         |               | cl2208-eu-spdc | po2       | 
|         |               | cl2208-eu-spdc | po3       | 
+---------+---------------+----------------+-----------+
| 0 0 0 0 | k8s/vk8s_4_BD | cl2207-eu-spdc | eth1/1/1  | 
|         |               | cl2207-eu-spdc | eth1/1/2  | 
|         |               | cl2207-eu-spdc | po5       | 
|         |               | cl2207-eu-spdc | po6       | 
|         |               | cl2208-eu-spdc | eth1/1/1  | 
|         |               | cl2208-eu-spdc | eth1/1/2  | 
|         |               | cl2208-eu-spdc | po2       | 
|         |               | cl2208-eu-spdc | po3       | 
+---------+---------------+----------------+-----------+

Bridge Domain - Faults [#0]
---------------------------
None

Bridge Domain - Fault Records last 60d [#0]
-------------------------------------------
None

Bridge Domain - Event Logs last 60d [#0]
----------------------------------------
None

Bridge Domain - Audit Logs last 60d [#0]
----------------------------------------
None
```

Developer

```
# iserver get aci bd --apic apic21 --name *vk8s* --when 60d --view all

{
    "duration": 10778,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 542,
        "disconnect_time": 0,
        "mo_time": 8542,
        "total_time": 9084
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

True	542	-	connect apic21o.emea-sp.cisco.com:443
True	499	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	476	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	484	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	368	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	479	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	368	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_1_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
True	386	0	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=faults,no-scoped,subtree
True	1301	18	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1347	70	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1744	1711	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
True	340	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_3_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
True	351	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_4_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
True	399	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/BD-vk8s_2_BD query rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf
```

[[Back]](./BridgeDomain.md)