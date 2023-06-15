# Bridge Domain

## Get multicast properties of bridge domains

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

+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| Bridge Domain             | PIM | Unknown IPv4 Flooding | IGMP Snooping  | PIMv6 | Unknown IPv6 Flooding | MLD Snooping   |
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| common/default            | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| common/Infra_BD           | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| common/Infra_privIP_BD    | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| common/Test_BD            | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| hefernan_ni-demo/BD1      | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| hefernan_ni-demo/BD2      | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| infra/ave-ctrl            | X   | flood                 | infra/default  | X     | flood                 | infra/default  | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| infra/default             | X   | flood                 | infra/default  | X     | flood                 | infra/default  | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/bmk8s_1_BD            | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/bmk8s_2_BD            | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/bmk8s_prov_BD         | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/bml3outk8s_BD         | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/MGMT_BD               | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/SRIoV_A_BD            | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/SRIoV_B_BD            | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/Test                  | X   | flood                 | k8s/Test       | X     | flood                 | k8s/Test       | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/vk8s_1_BD             | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/vk8s_2_BD             | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/vk8s_3_BD             | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/vk8s_4_BD             | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/vl3outk8s_BD          | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| k8s/VM2VM_BD              | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| mgmt/EU-SPDC-BD1          | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| mgmt/EU-SPDC-ERSPAN_BD    | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| mgmt/inb                  | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| nidemo/appserver          | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| nidemo/database           | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| nidemo/frontend           | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| nidemo/management         | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| SPN_IntraLab/SPN_BD1      | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| vEPC/Leaking_BD           | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| vEPC/vSFO_BD              | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| vEPC_demo/ACC_BD          | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| vEPC_demo/INT_BD          | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| vEPC_demo/MGMT_BD         | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
| vEPC_demo/vEPC-CTRL-SX_BD | X   | flood                 | common/default | X     | flood                 | common/default | 
+---------------------------+-----+-----------------------+----------------+-------+-----------------------+----------------+
```

Developer

```
# iserver get aci bd --apic apic21 --view mcast

{
    "duration": 2452,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 1191,
        "total_time": 1628
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

True	437	-	connect apic21o.emea-sp.cisco.com
True	411	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	368	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	412	92	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)