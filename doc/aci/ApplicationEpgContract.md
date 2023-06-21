# Application Endpoint Group (EPG)

## Filter by contract name

```
# iserver get aci epg --apic apic21 --contract comm*/k8s* --view contract

Apic: apic21 (mode:online, cache:off)

EPG Contracts
-------------

+----+------------------------+----------+-------------------+-------------------+----------------+
| Up | EPG                    | Class ID | Contract Consumed | Contract Provided | Contract Taboo |
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/bmk8s_1    | 16404    | common/k8s_bm     |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/bmk8s_2    | 49165    | common/k8s_bm     |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/bmk8s_prov | 49163    | common/k8s_prov   |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/vk8s_1     | 49162    | common/k8s_vm     |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/vk8s_2     | 49164    | common/k8s_vm     |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/vk8s_3     | 49166    | common/k8s_vm     |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
| V  | k8s/k8s_ANP/vk8s_4     | 16403    | common/k8s_vm     |                   |                | 
+----+------------------------+----------+-------------------+-------------------+----------------+
```

Developer

```
# iserver get aci epg --apic apic21 --contract comm*/k8s* --view contract

{
    "duration": 2411,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 1630,
        "total_time": 2021
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

True	391	-	connect apic21o.emea-sp.cisco.com:443
True	380	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	286	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	306	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	329	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	329	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)