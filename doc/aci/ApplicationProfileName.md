# Application Profile (AP)

## Filter by application profile's name

Example: name

```
# iserver get aci ap --apic apic21 --name *k8s*

Apic: apic21 (mode:online, cache:off)

+---------------------+------------------+-------------+
| Application Profile | Application EPGs | Priority    |
+---------------------+------------------+-------------+
| k8s/k8s_ANP         | k8s/backbone1    | unspecified | 
|                     | k8s/bmk8s_1      |             | 
|                     | k8s/bmk8s_2      |             | 
|                     | k8s/bmk8s_prov   |             | 
|                     | k8s/csr1_lan     |             | 
|                     | k8s/csr2_lan     |             | 
|                     | k8s/csr_b2b      |             | 
|                     | k8s/MGMT         |             | 
|                     | k8s/site1_lan    |             | 
|                     | k8s/site1_pe     |             | 
|                     | k8s/site2_lan    |             | 
|                     | k8s/site2_pe     |             | 
|                     | k8s/SRIoV_A      |             | 
|                     | k8s/SRIoV_B      |             | 
|                     | k8s/Test         |             | 
|                     | k8s/vk8s_1       |             | 
|                     | k8s/vk8s_2       |             | 
|                     | k8s/vk8s_3       |             | 
|                     | k8s/vk8s_4       |             | 
+---------------------+------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s*

{
    "duration": 1363,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 423,
        "disconnect_time": 0,
        "mo_time": 729,
        "total_time": 1152
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

True	423	-	connect apic21o.emea-sp.cisco.com
True	322	12	apic21o.emea-sp.cisco.com class fvAp
True	407	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

Example: tenant and name

```
# iserver get aci ap --apic apic21 --name k8s/k8s_ANP

Apic: apic21 (mode:online, cache:off)

+---------------------+------------------+-------------+
| Application Profile | Application EPGs | Priority    |
+---------------------+------------------+-------------+
| k8s/k8s_ANP         | k8s/backbone1    | unspecified | 
|                     | k8s/bmk8s_1      |             | 
|                     | k8s/bmk8s_2      |             | 
|                     | k8s/bmk8s_prov   |             | 
|                     | k8s/csr1_lan     |             | 
|                     | k8s/csr2_lan     |             | 
|                     | k8s/csr_b2b      |             | 
|                     | k8s/MGMT         |             | 
|                     | k8s/site1_lan    |             | 
|                     | k8s/site1_pe     |             | 
|                     | k8s/site2_lan    |             | 
|                     | k8s/site2_pe     |             | 
|                     | k8s/SRIoV_A      |             | 
|                     | k8s/SRIoV_B      |             | 
|                     | k8s/Test         |             | 
|                     | k8s/vk8s_1       |             | 
|                     | k8s/vk8s_2       |             | 
|                     | k8s/vk8s_3       |             | 
|                     | k8s/vk8s_4       |             | 
+---------------------+------------------+-------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name k8s/k8s_ANP

{
    "duration": 1387,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 710,
        "total_time": 1153
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

True	443	-	connect apic21o.emea-sp.cisco.com
True	325	12	apic21o.emea-sp.cisco.com class fvAp
True	385	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

[[Back]](./ApplicationProfile.md)