# Bridge Domain

## Filter by bridge domain's name

Example: domain name value

```
# iserver get aci bd --apic apic21 --name *vk8s*

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
```

Example: tenant and domain name value

```
# iserver get aci bd --apic apic21 --name k8s/vk8s*

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
```

Developer

```
# iserver get aci bd --apic apic21 --name *vk8s*

{
    "duration": 3125,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 476,
        "disconnect_time": 0,
        "mo_time": 1887,
        "total_time": 2363
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

True	476	-	connect apic21o.emea-sp.cisco.com:443
True	520	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	531	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	367	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	469	87	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)