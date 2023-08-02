# Application Endpoint Group (EPG)

## Get EPGs properties

Use '--view props' to get properties of selected epgs
- epg name, application profile and tenant
- preferred member
- flood
- class id
- QoS class
- isolation
- label match

```
# iserver get aci epg --apic apic21 --name vk8s* --view prop

Apic: apic21 (mode:online, cache:off)

EPG - Properties [#4]
---------------------

+--------+---------+--------------------+------------------+----------+----------+-------------+------------+-------------+
| Health | Faults  | EPG                | Preferred Member | Flood    | Class ID | QoS Class   | Isolation  | Label Match |
+--------+---------+--------------------+------------------+----------+----------+-------------+------------+-------------+
| 100    | 0 0 0 0 | k8s/k8s_ANP/vk8s_1 | exclude          | disabled | 49162    | unspecified | unenforced | AtleastOne  | 
+--------+---------+--------------------+------------------+----------+----------+-------------+------------+-------------+
| 100    | 0 0 0 0 | k8s/k8s_ANP/vk8s_2 | exclude          | disabled | 49164    | unspecified | unenforced | AtleastOne  | 
+--------+---------+--------------------+------------------+----------+----------+-------------+------------+-------------+
| 100    | 0 0 0 0 | k8s/k8s_ANP/vk8s_3 | exclude          | disabled | 49166    | unspecified | unenforced | AtleastOne  | 
+--------+---------+--------------------+------------------+----------+----------+-------------+------------+-------------+
| 100    | 0 0 0 0 | k8s/k8s_ANP/vk8s_4 | exclude          | disabled | 16403    | unspecified | unenforced | AtleastOne  | 
+--------+---------+--------------------+------------------+----------+----------+-------------+------------+-------------+
```

Developer

```
# iserver get aci epg --apic apic21 --name vk8s* --view prop

{
    "duration": 1489,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 451,
        "disconnect_time": 0,
        "mo_time": 827,
        "total_time": 1278
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

True	451	-	connect apic21o.emea-sp.cisco.com:443
True	500	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	327	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationEpg.md)