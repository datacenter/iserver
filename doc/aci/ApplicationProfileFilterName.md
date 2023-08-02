# Application Profile (AP)

## Filter by application profile's name

Example: name

```
# iserver get aci ap --apic apic21 --name *k8s*

Apic: apic21 (mode:online, cache:off)

Application Profile [#1]
------------------------

+--------+---------+---------------------+------------------+-------------+
| Health | Faults  | Application Profile | Application EPGs | Priority    |
+--------+---------+---------------------+------------------+-------------+
| 95     | 0 0 2 0 | k8s/k8s_ANP         | k8s/backbone1    | unspecified | 
|        |         |                     | k8s/bmk8s_1      |             | 
|        |         |                     | k8s/bmk8s_2      |             | 
|        |         |                     | k8s/bmk8s_prov   |             | 
|        |         |                     | k8s/csr1_lan     |             | 
|        |         |                     | k8s/csr2_lan     |             | 
|        |         |                     | k8s/csr_b2b      |             | 
|        |         |                     | k8s/MGMT         |             | 
|        |         |                     | k8s/site1_lan    |             | 
|        |         |                     | k8s/site1_pe     |             | 
|        |         |                     | k8s/site2_lan    |             | 
|        |         |                     | k8s/site2_pe     |             | 
|        |         |                     | k8s/SRIoV_A      |             | 
|        |         |                     | k8s/SRIoV_B      |             | 
|        |         |                     | k8s/Test         |             | 
|        |         |                     | k8s/vk8s_1       |             | 
|        |         |                     | k8s/vk8s_2       |             | 
|        |         |                     | k8s/vk8s_3       |             | 
|        |         |                     | k8s/vk8s_4       |             | 
+--------+---------+---------------------+------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s*

{
    "duration": 3037,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 534,
        "disconnect_time": 0,
        "mo_time": 1555,
        "total_time": 2089
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

True	534	-	connect apic21o.emea-sp.cisco.com:443
True	476	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	705	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	374	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

Example: tenant and name

```
# iserver get aci ap --apic apic21 --name k8s/k8s_ANP

Apic: apic21 (mode:online, cache:off)

Application Profile [#1]
------------------------

+--------+---------+---------------------+------------------+-------------+
| Health | Faults  | Application Profile | Application EPGs | Priority    |
+--------+---------+---------------------+------------------+-------------+
| 95     | 0 0 2 0 | k8s/k8s_ANP         | k8s/backbone1    | unspecified | 
|        |         |                     | k8s/bmk8s_1      |             | 
|        |         |                     | k8s/bmk8s_2      |             | 
|        |         |                     | k8s/bmk8s_prov   |             | 
|        |         |                     | k8s/csr1_lan     |             | 
|        |         |                     | k8s/csr2_lan     |             | 
|        |         |                     | k8s/csr_b2b      |             | 
|        |         |                     | k8s/MGMT         |             | 
|        |         |                     | k8s/site1_lan    |             | 
|        |         |                     | k8s/site1_pe     |             | 
|        |         |                     | k8s/site2_lan    |             | 
|        |         |                     | k8s/site2_pe     |             | 
|        |         |                     | k8s/SRIoV_A      |             | 
|        |         |                     | k8s/SRIoV_B      |             | 
|        |         |                     | k8s/Test         |             | 
|        |         |                     | k8s/vk8s_1       |             | 
|        |         |                     | k8s/vk8s_2       |             | 
|        |         |                     | k8s/vk8s_3       |             | 
|        |         |                     | k8s/vk8s_4       |             | 
+--------+---------+---------------------+------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name k8s/k8s_ANP

{
    "duration": 2656,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 435,
        "disconnect_time": 0,
        "mo_time": 1334,
        "total_time": 1769
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

True	435	-	connect apic21o.emea-sp.cisco.com:443
True	394	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	538	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	402	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ApplicationProfile.md)