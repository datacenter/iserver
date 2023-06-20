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

+--------------------+----------------+-------------+-------+--------+----------------+-------------+----------------+
| EPG                | Node Name      | IP Address  | Admin | Fabric | Model          | Serial      | Version        |
+--------------------+----------------+-------------+-------+--------+----------------+-------------+----------------+
| k8s/k8s_ANP/vk8s_1 | cl2208-eu-spdc | 10.5.240.35 | on    | active | N9K-C9336C-FX2 | FDO234807ED | n9000-16.0(2h) | 
|                    | cl2207-eu-spdc | 10.5.240.34 | on    | active | N9K-C9336C-FX2 | FDO23490E4G | n9000-16.0(2h) | 
+--------------------+----------------+-------------+-------+--------+----------------+-------------+----------------+
| k8s/k8s_ANP/vk8s_2 | cl2208-eu-spdc | 10.5.240.35 | on    | active | N9K-C9336C-FX2 | FDO234807ED | n9000-16.0(2h) | 
|                    | cl2207-eu-spdc | 10.5.240.34 | on    | active | N9K-C9336C-FX2 | FDO23490E4G | n9000-16.0(2h) | 
+--------------------+----------------+-------------+-------+--------+----------------+-------------+----------------+
| k8s/k8s_ANP/vk8s_3 | cl2207-eu-spdc | 10.5.240.34 | on    | active | N9K-C9336C-FX2 | FDO23490E4G | n9000-16.0(2h) | 
|                    | cl2208-eu-spdc | 10.5.240.35 | on    | active | N9K-C9336C-FX2 | FDO234807ED | n9000-16.0(2h) | 
+--------------------+----------------+-------------+-------+--------+----------------+-------------+----------------+
| k8s/k8s_ANP/vk8s_4 | cl2207-eu-spdc | 10.5.240.34 | on    | active | N9K-C9336C-FX2 | FDO23490E4G | n9000-16.0(2h) | 
|                    | cl2208-eu-spdc | 10.5.240.35 | on    | active | N9K-C9336C-FX2 | FDO234807ED | n9000-16.0(2h) | 
+--------------------+----------------+-------------+-------+--------+----------------+-------------+----------------+
```

Use '--pivot' option to get the node specific output

```
# iserver get aci epg --apic apic21 --name vk8s* --view node --pivot

Apic: apic21 (mode:online, cache:off)

EPG Deployed Nodes (pivot view)
-------------------------------

+----------------+-------------+-------+--------+----------------+-------------+----------------+--------------------+
| Node Name      | IP Address  | Admin | Fabric | Model          | Serial      | Version        | EPG                |
+----------------+-------------+-------+--------+----------------+-------------+----------------+--------------------+
| cl2208-eu-spdc | 10.5.240.35 | on    | active | N9K-C9336C-FX2 | FDO234807ED | n9000-16.0(2h) | k8s/k8s_ANP/vk8s_1 | 
|                |             |       |        |                |             |                | k8s/k8s_ANP/vk8s_2 | 
|                |             |       |        |                |             |                | k8s/k8s_ANP/vk8s_3 | 
|                |             |       |        |                |             |                | k8s/k8s_ANP/vk8s_4 | 
+----------------+-------------+-------+--------+----------------+-------------+----------------+--------------------+
| cl2207-eu-spdc | 10.5.240.34 | on    | active | N9K-C9336C-FX2 | FDO23490E4G | n9000-16.0(2h) | k8s/k8s_ANP/vk8s_1 | 
|                |             |       |        |                |             |                | k8s/k8s_ANP/vk8s_2 | 
|                |             |       |        |                |             |                | k8s/k8s_ANP/vk8s_3 | 
|                |             |       |        |                |             |                | k8s/k8s_ANP/vk8s_4 | 
+----------------+-------------+-------+--------+----------------+-------------+----------------+--------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --name vk8s* --view node

{
    "duration": 1868,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 429,
        "disconnect_time": 0,
        "mo_time": 1032,
        "total_time": 1461
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

True	429	-	connect apic21o.emea-sp.cisco.com:443
True	380	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	311	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	341	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./ApplicationEpg.md)