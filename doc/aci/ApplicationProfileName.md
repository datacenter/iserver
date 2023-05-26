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

[[Back]](./ApplicationProfile.md)