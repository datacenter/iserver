# Application Endpoint Group (EPG)

## Filter by leaf policy group

```
# iserver get aci epg --apic apic21 --pg k8s_esx71_PolGrp --view member

Apic: apic21 (mode:online, cache:off)

EPG - Member [#12]
------------------

+-----------------------+-------------+----------------+--------------+------------------+-----------+
| EPG                   | Member Type | Node           | Type         | ID               | VLAN      |
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/backbone1 | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1301 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1301 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/csr1_lan  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1303 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1303 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/csr2_lan  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1435 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1435 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/csr_b2b   | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1305 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1305 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/site1_lan | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1306 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1306 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/site1_pe  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1304 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1304 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/site2_lan | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1437 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1437 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/site2_pe  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1302 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1302 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/vk8s_1    | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1367 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1367 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/vk8s_2    | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1300 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1300 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/vk8s_3    | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1369 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1369 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
| k8s/k8s_ANP/vk8s_4    | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1368 | 
|                       | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp | vlan-1368 | 
+-----------------------+-------------+----------------+--------------+------------------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --pg k8s_esx71_PolGrp --view member

{
    "duration": 2469,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 488,
        "disconnect_time": 0,
        "mo_time": 1309,
        "total_time": 1797
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

True	488	-	connect apic21o.emea-sp.cisco.com:443
True	498	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	391	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	420	282	apic21o.emea-sp.cisco.com:443 class fvIfConn
```

[[Back]](./ApplicationEpg.md)