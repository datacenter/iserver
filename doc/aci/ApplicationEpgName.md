# Application Endpoint Group (EPG)

## Filter by EPG name

Example: name

```
# iserver get aci epg --apic apic21 --name *vk8s*

Apic: apic21 (mode:online, cache:off)

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | BD Subnets      | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
```

Example: profile and name

```
# iserver get aci epg --apic apic21 --name k8s*/vk8s*

Apic: apic21 (mode:online, cache:off)

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | BD Subnets      | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
```

Example: tenant, profile and name

```
# iserver get aci epg --apic apic21 --name k8s/k8s_ANP/vk8s*

Apic: apic21 (mode:online, cache:off)

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | BD Subnets      | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
```

Developer

```
# iserver get aci epg --apic apic21 --name *vk8s*

{
    "duration": 2916,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 783,
        "disconnect_time": 0,
        "mo_time": 1937,
        "total_time": 2720
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

True	783	-	connect apic21o.emea-sp.cisco.com:443
True	374	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	374	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	355	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	411	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	423	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./ApplicationEpg.md)