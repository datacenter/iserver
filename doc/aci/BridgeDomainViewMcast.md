# Bridge Domain

## Multicast view

Use '--view mcast' to get multicast forwarding related properties of selected bridge domains
- PIM
- L3 unknown multicast flooding
- IGMP snooping policy
- PIMv6
- IPv6 L3 unknown multicast flooding
- MLD snooping policy

```
# iserver get aci bd --apic apic21 --view mcast

Apic: apic21 (mode:online, cache:off)

Bridge Domain - Multicast Properties [#35]
------------------------------------------

+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| Bridge Domain             | PIM | Unknown IPv4 Flooding | IGMP Snooping Policy | PIMv6 | Unknown IPv6 Flooding | MLD Snooping Policy |
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| common/default            | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| common/Infra_BD           | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| common/Infra_privIP_BD    | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| common/Test_BD            | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| hefernan_ni-demo/BD1      | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| hefernan_ni-demo/BD2      | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| infra/ave-ctrl            | X   | Flood                 | infra/default        | X     | Flood                 | infra/default       | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| infra/default             | X   | Flood                 | infra/default        | X     | Flood                 | infra/default       | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/bmk8s_1_BD            | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/bmk8s_2_BD            | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/bmk8s_prov_BD         | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/bml3outk8s_BD         | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/MGMT_BD               | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/SRIoV_A_BD            | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/SRIoV_B_BD            | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/Test                  | X   | Optimized Flood       | k8s/Test             | X     | Flood                 | k8s/Test            | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_1_BD             | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_2_BD             | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_3_BD             | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vk8s_4_BD             | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/vl3outk8s_BD          | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| k8s/VM2VM_BD              | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| mgmt/EU-SPDC-ERSPAN_BD    | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| mgmt/inb                  | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| nidemo/appserver          | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| nidemo/database           | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| nidemo/frontend           | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| nidemo/management         | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| SPN_IntraLab/SPN_BD1      | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| vEPC/Leaking_BD           | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| vEPC/vSFO_BD              | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| vEPC_demo/ACC_BD          | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| vEPC_demo/INT_BD          | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| vEPC_demo/MGMT_BD         | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
| vEPC_demo/vEPC-CTRL-SX_BD | X   | Flood                 | common/default       | X     | Flood                 | common/default      | 
+---------------------------+-----+-----------------------+----------------------+-------+-----------------------+---------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --view mcast

{
    "duration": 3301,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 513,
        "disconnect_time": 0,
        "mo_time": 1885,
        "total_time": 2398
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

True	513	-	connect apic21o.emea-sp.cisco.com:443
True	503	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	532	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	381	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	469	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)