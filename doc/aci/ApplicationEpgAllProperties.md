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

EPG Policy Properties
---------------------

+----+--------------------+------------------+----------+----------+-------------+------------+-------------+
| Up | EPG                | Preferred Member | Flood    | Class ID | QoS Class   | Isolation  | Label Match |
+----+--------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_1 | exclude          | disabled | 49162    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_2 | exclude          | disabled | 49164    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_3 | exclude          | disabled | 49166    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/vk8s_4 | exclude          | disabled | 16403    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+------------------+----------+----------+-------------+------------+-------------+
```

Developer

```
# iserver get aci epg --apic apic21 --name vk8s* --view prop

{
    "duration": 1533,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 733,
        "total_time": 1177
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

True	444	-	connect apic21o.emea-sp.cisco.com:443
True	400	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	333	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationEpg.md)