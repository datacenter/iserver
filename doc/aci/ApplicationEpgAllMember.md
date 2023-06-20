# Application Endpoint Group (EPG)

## Get EPGs' member properties

```
# iserver get aci epg --apic apic21 --tenant k8s* --view member

Apic: apic21 (mode:online, cache:off)

EPG Members
-----------

+------------------------+-------------+------+------+----+------+
| EPG                    | Member Type | Node | Type | ID | VLAN |
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/backbone1  |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/bmk8s_1    |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/bmk8s_2    |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/bmk8s_prov |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/csr1_lan   |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/csr2_lan   |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/csr_b2b    |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/MGMT       |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/site1_lan  |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/site1_pe   |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/site2_lan  |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/site2_pe   |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/SRIoV_A    |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/SRIoV_B    |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/Test       |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/vk8s_1     |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/vk8s_2     |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/vk8s_3     |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/vk8s_4     |             |      |      |    |      | 
+------------------------+-------------+------+------+----+------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s* --view member

{
    "duration": 2694,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 1876,
        "total_time": 2293
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

True	417	-	connect apic21o.emea-sp.cisco.com:443
True	1174	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	337	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	365	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
```

[[Back]](./ApplicationEpg.md)