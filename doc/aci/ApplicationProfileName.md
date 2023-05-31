# Application Profile (AP)

## Filter by application profile's name

Example: name

```
# iserver get aci ap --apic apic21 --name *k8s*

Apic: apic21

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
    "duration": 1210,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 643,
        "total_time": 1029
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
    }
}

Log: apic
----------

True	386	-	connect apic21o.emea-sp.cisco.com
True	297	12	apic21o.emea-sp.cisco.com class fvAp
True	346	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

Example: tenant and name

```
# iserver get aci ap --apic apic21 --name k8s/k8s_ANP

Apic: apic21

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
    "duration": 1174,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 653,
        "total_time": 1047
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
    }
}

Log: apic
----------

True	394	-	connect apic21o.emea-sp.cisco.com
True	294	12	apic21o.emea-sp.cisco.com class fvAp
True	359	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
```

[[Back]](./ApplicationProfile.md)