# Application Endpoint Group (EPG)

## Get EPGs' Bridge Domain properties

Use '--view bd' to get bridge domain properties of selected epgs
- epg name, application profile and tenant
- bridge domain name
- bridge domain subnets with usage
- associated L3 Out

```
# iserver get aci epg --apic apic21 --name vk8s* --view bd

Apic: apic21 (mode:online, cache:off)

EPG - Bridge Domain [#4]
------------------------

+----+--------------------+---------------+-----------------+-------+------------------+--------------------+
| Up | EPG                | Bridge Domain | BD Subnets      | Usage | VRF              | L3Out              |
+----+--------------------+---------------+-----------------+-------+------------------+--------------------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 10/14 | common/Infra_VRF | common/Infra_L3out | 
+----+--------------------+---------------+-----------------+-------+------------------+--------------------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+----+--------------------+---------------+-----------------+-------+------------------+--------------------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 2/14  | common/Infra_VRF | common/Infra_L3out | 
+----+--------------------+---------------+-----------------+-------+------------------+--------------------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 2/14  | common/Infra_VRF | common/Infra_L3out | 
+----+--------------------+---------------+-----------------+-------+------------------+--------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --name vk8s* --view bd

{
    "duration": 3468,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 501,
        "disconnect_time": 0,
        "mo_time": 2383,
        "total_time": 2884
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

True	501	-	connect apic21o.emea-sp.cisco.com:443
True	524	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	370	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	501	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	480	96	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	508	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
```

[[Back]](./ApplicationEpg.md)