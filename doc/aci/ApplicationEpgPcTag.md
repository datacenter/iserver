# Application Endpoint Group (EPG)

## Filter by pcTag

Supported pcTag filtering options by example:
- --pctag system
- --pctag global
- --pctag 32770
- --pctag lt100
- --pctag 32000-32100

```
# iserver get aci epg --apic apic11 --pctag global --view prop

Apic: apic11 (mode:online, cache:off)

EPG Policy Properties
---------------------

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
    "duration": 3179,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 1798,
        "total_time": 2190
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

True	392	-	connect apic11o.emea-sp.cisco.com:443
True	1427	245	apic11o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	371	13	apic11o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationEpg.md)