# Application Endpoint Group (EPG)

## Filter by deployed node name

```
# iserver get aci epg --apic apic21 --node *2207* --view node --pivot

Apic: apic21 (mode:online, cache:off)

EPG - Deployed Nodes (pivot view) [#19]
---------------------------------------

+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| Node Name      | IP Address  | Admin | Fabric | Model            | Serial      | Version        | EPG                          |
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| cl2208-eu-spdc | 10.5.240.35 | on    | active | N9K-C9336C-FX2   | FDO234807ED | n9000-16.0(2h) | k8s/k8s_ANP/backbone1        | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/bmk8s_1          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/bmk8s_2          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/bmk8s_prov       | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/csr1_lan         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/csr2_lan         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/csr_b2b          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/MGMT             | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site1_lan        | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site1_pe         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site2_lan        | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site2_pe         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/SRIoV_A          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/SRIoV_B          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_1           | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_2           | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_3           | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_4           | 
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| cl2207-eu-spdc | 10.5.240.34 | on    | active | N9K-C9336C-FX2   | FDO23490E4G | n9000-16.0(2h) | k8s/k8s_ANP/backbone1        | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/bmk8s_1          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/bmk8s_2          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/bmk8s_prov       | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/csr1_lan         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/csr2_lan         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/csr_b2b          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/MGMT             | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site1_lan        | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site1_pe         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site2_lan        | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/site2_pe         | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/SRIoV_A          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/SRIoV_B          | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_1           | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_2           | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_3           | 
|                |             |       |        |                  |             |                | k8s/k8s_ANP/vk8s_4           | 
|                |             |       |        |                  |             |                | vEPC_demo/vEPG_ANP/vEPG_MGMT | 
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| cl2201-eu-spdc | 10.5.80.96  | on    | active | N9K-C93360YC-FX2 | FDO2441006U | n9000-16.0(2h) | vEPC_demo/vEPG_ANP/vEPG_MGMT | 
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| cl2202-eu-spdc | 10.5.216.67 | on    | active | N9K-C93360YC-FX2 | FDO24350A1T | n9000-16.0(2h) | vEPC_demo/vEPG_ANP/vEPG_MGMT | 
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| bl2205-eu-spdc | 10.5.216.66 | on    | active | N9K-C93600CD-GX  | FDO24280TYP | n9000-16.0(2h) | vEPC_demo/vEPG_ANP/vEPG_MGMT | 
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
| bl2206-eu-spdc | 10.5.216.64 | on    | active | N9K-C93600CD-GX  | FDO243707PU | n9000-16.0(2h) | vEPC_demo/vEPG_ANP/vEPG_MGMT | 
+----------------+-------------+-------+--------+------------------+-------------+----------------+------------------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --node *2207* --view node --pivot

{
    "duration": 2222,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 481,
        "disconnect_time": 0,
        "mo_time": 1264,
        "total_time": 1745
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

True	481	-	connect apic21o.emea-sp.cisco.com:443
True	479	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	377	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	408	154	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./ApplicationEpg.md)