# Bridge Domain

## Get L2 properties of bridge domains

Use '--view l2' to get L2 forwarding related properties of selected bridge domains
- L2 unknown unicast
- ARP flooding
- multi destination flooding
- clear remote MAC entries
- scaled L2 only (legacy) mode

```
# iserver get aci bd --apic apic21 --view l2

Apic: apic21 (mode:online, cache:off)

Bridge Domain L2 Properties
---------------------------

+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| Bridge Domain             | L2 Unknown Ucast | ARP Flooding | Multi Dest Flooding | Clear Remote MAC | Scaled L2 Only |
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| common/default            | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| common/Infra_BD           | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| common/Infra_privIP_BD    | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| common/Test_BD            | proxy            | yes          | bd-flood            | no               | yes            | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| hefernan_ni-demo/BD1      | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| hefernan_ni-demo/BD2      | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| infra/ave-ctrl            | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| infra/default             | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/bmk8s_1_BD            | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/bmk8s_2_BD            | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/bmk8s_prov_BD         | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/bml3outk8s_BD         | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/MGMT_BD               | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/SRIoV_A_BD            | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/SRIoV_B_BD            | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/Test                  | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/vk8s_1_BD             | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/vk8s_2_BD             | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/vk8s_3_BD             | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/vk8s_4_BD             | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/vl3outk8s_BD          | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| k8s/VM2VM_BD              | flood            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| mgmt/EU-SPDC-BD1          | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| mgmt/EU-SPDC-ERSPAN_BD    | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| mgmt/inb                  | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| nidemo/appserver          | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| nidemo/database           | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| nidemo/frontend           | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| nidemo/management         | proxy            | no           | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| SPN_IntraLab/SPN_BD1      | flood            | yes          | encap-flood         | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| vEPC/Leaking_BD           | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| vEPC/vSFO_BD              | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| vEPC_demo/ACC_BD          | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| vEPC_demo/INT_BD          | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| vEPC_demo/MGMT_BD         | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
| vEPC_demo/vEPC-CTRL-SX_BD | proxy            | yes          | bd-flood            | no               | no             | 
+---------------------------+------------------+--------------+---------------------+------------------+----------------+
```

Developer

```
# iserver get aci bd --apic apic21 --view l2

{
    "duration": 2985,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 1513,
        "total_time": 1947
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

True	434	-	connect apic21o.emea-sp.cisco.com:443
True	388	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	392	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	311	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	422	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)