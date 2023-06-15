# Application Endpoint Group (EPG)

## Filter by pcTag

Supported pcTag filtering options by example:
- --pctag global
- --pctag 32770
- --pctag lt100
- --pctag 32000-32100

```
# iserver get aci epg --apic apic11 --pctag global --view prop

Apic: apic11 (mode:online, cache:off)

+----+---------------------------------+------------------+----------+----------------+-------------+------------+-------------+
| Up | EPG                             | Preferred Member | Flood    | Class ID       | QoS Class   | Isolation  | Label Match |
+----+---------------------------------+------------------+----------+----------------+-------------+------------+-------------+
| V  | common/Infra_ANP/PrivateIP-MGMT | exclude          | disabled | 18 (global)    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------+------------------+----------+----------------+-------------+------------+-------------+
| V  | ECMP-demo/ECMP_ANP/Web          | exclude          | disabled | 10940 (global) | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------+------------------+----------+----------------+-------------+------------+-------------+
| V  | P5G/P5G_App/P5G-F1C-NGC-N2      | exclude          | disabled | 17 (global)    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------+------------------+----------+----------------+-------------+------------+-------------+
| V  | P5G/P5G_App/P5G-F1U-NGU-N3      | exclude          | disabled | 10937 (global) | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------+------------------+----------+----------------+-------------+------------+-------------+
```

Developer

```
# iserver get aci epg --apic apic11 --pctag global --view prop

{
    "duration": 3837,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 407,
        "disconnect_time": 0,
        "mo_time": 2903,
        "total_time": 3310
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

True	407	-	connect apic11o.emea-sp.cisco.com:443
True	616	245	apic11o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	596	314	apic11o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	321	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	817	264	apic11o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	553	193	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./ApplicationEpg.md)