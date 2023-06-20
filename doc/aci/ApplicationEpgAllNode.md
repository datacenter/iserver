# Application Endpoint Group (EPG)

## Get EPGs' deployed nodes properties

Use '--view node' to get deployed node properties of selected epgs
- epg name, application profile and tenant
- node properties
    - name
    - ip address
    - admin state
    - fabric state
    - model
    - serial
    - version

```
# iserver get aci epg --apic apic21 --name vk8s* --view node

Apic: apic21 (mode:online, cache:off)

EPG Deployed Nodes
------------------

+--------------------+-----------+------------+-------+--------+-------+--------+---------+
| EPG                | Node Name | IP Address | Admin | Fabric | Model | Serial | Version |
+--------------------+-----------+------------+-------+--------+-------+--------+---------+
| k8s/k8s_ANP/vk8s_1 |           |            |       |        |       |        |         | 
+--------------------+-----------+------------+-------+--------+-------+--------+---------+
| k8s/k8s_ANP/vk8s_2 |           |            |       |        |       |        |         | 
+--------------------+-----------+------------+-------+--------+-------+--------+---------+
| k8s/k8s_ANP/vk8s_3 |           |            |       |        |       |        |         | 
+--------------------+-----------+------------+-------+--------+-------+--------+---------+
| k8s/k8s_ANP/vk8s_4 |           |            |       |        |       |        |         | 
+--------------------+-----------+------------+-------+--------+-------+--------+---------+
```

Use '--pivot' option to get the node specific output

```
# iserver get aci epg --apic apic21 --name vk8s* --view node --pivot

Apic: apic21 (mode:online, cache:off)

EPG Deployed Nodes (pivot view)
-------------------------------

+-----------+------------+-------+--------+-------+--------+---------+-----+
| Node Name | IP Address | Admin | Fabric | Model | Serial | Version | EPG |
+-----------+------------+-------+--------+-------+--------+---------+-----+
```

Developer

```
# iserver get aci epg --apic apic21 --name vk8s* --view node

{
    "duration": 1834,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 439,
        "disconnect_time": 0,
        "mo_time": 1039,
        "total_time": 1478
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

True	439	-	connect apic21o.emea-sp.cisco.com:443
True	406	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	314	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	319	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./ApplicationEpg.md)