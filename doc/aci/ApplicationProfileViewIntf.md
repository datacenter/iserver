# Application Profile

## Intf view

```
# iserver get aci ap --apic apic21 --name *k8s* --view intf

Apic: apic21 (mode:online, cache:off)

Application Profile - Interfaces [#1]
-------------------------------------

+---------+---------------------+----------------+-----------+
| Faults  | Application Profile | Node           | Interface |
+---------+---------------------+----------------+-----------+
| 0 0 2 0 | k8s/k8s_ANP         | cl2207-eu-spdc | eth1/1/1  | 
|         |                     | cl2207-eu-spdc | eth1/1/2  | 
|         |                     | cl2207-eu-spdc | eth1/1/3  | 
|         |                     | cl2207-eu-spdc | eth1/1/4  | 
|         |                     | cl2207-eu-spdc | eth1/2/1  | 
|         |                     | cl2207-eu-spdc | eth1/2/2  | 
|         |                     | cl2207-eu-spdc | eth1/2/3  | 
|         |                     | cl2207-eu-spdc | eth1/3/1  | 
|         |                     | cl2207-eu-spdc | eth1/3/2  | 
|         |                     | cl2207-eu-spdc | eth1/3/3  | 
|         |                     | cl2207-eu-spdc | eth1/3/4  | 
|         |                     | cl2207-eu-spdc | eth1/4/1  | 
|         |                     | cl2207-eu-spdc | eth1/4/2  | 
|         |                     | cl2207-eu-spdc | eth1/4/3  | 
|         |                     | cl2207-eu-spdc | eth1/5/1  | 
|         |                     | cl2207-eu-spdc | eth1/5/2  | 
|         |                     | cl2207-eu-spdc | eth1/5/3  | 
|         |                     | cl2207-eu-spdc | eth1/5/4  | 
|         |                     | cl2207-eu-spdc | eth1/6/1  | 
|         |                     | cl2207-eu-spdc | eth1/6/2  | 
|         |                     | cl2207-eu-spdc | eth1/6/3  | 
|         |                     | cl2207-eu-spdc | po2       | 
|         |                     | cl2207-eu-spdc | po3       | 
|         |                     | cl2207-eu-spdc | po4       | 
|         |                     | cl2207-eu-spdc | po7       | 
|         |                     | cl2207-eu-spdc | po8       | 
|         |                     | cl2208-eu-spdc | eth1/1/1  | 
|         |                     | cl2208-eu-spdc | eth1/1/2  | 
|         |                     | cl2208-eu-spdc | eth1/1/3  | 
|         |                     | cl2208-eu-spdc | eth1/1/4  | 
|         |                     | cl2208-eu-spdc | eth1/2/1  | 
|         |                     | cl2208-eu-spdc | eth1/2/2  | 
|         |                     | cl2208-eu-spdc | eth1/2/3  | 
|         |                     | cl2208-eu-spdc | eth1/3/1  | 
|         |                     | cl2208-eu-spdc | eth1/3/2  | 
|         |                     | cl2208-eu-spdc | eth1/3/3  | 
|         |                     | cl2208-eu-spdc | eth1/3/4  | 
|         |                     | cl2208-eu-spdc | eth1/4/1  | 
|         |                     | cl2208-eu-spdc | eth1/4/2  | 
|         |                     | cl2208-eu-spdc | eth1/4/3  | 
|         |                     | cl2208-eu-spdc | eth1/5/1  | 
|         |                     | cl2208-eu-spdc | eth1/5/2  | 
|         |                     | cl2208-eu-spdc | eth1/5/3  | 
|         |                     | cl2208-eu-spdc | eth1/5/4  | 
|         |                     | cl2208-eu-spdc | eth1/6/1  | 
|         |                     | cl2208-eu-spdc | eth1/6/2  | 
|         |                     | cl2208-eu-spdc | eth1/6/3  | 
|         |                     | cl2208-eu-spdc | po4       | 
|         |                     | cl2208-eu-spdc | po5       | 
|         |                     | cl2208-eu-spdc | po6       | 
|         |                     | cl2208-eu-spdc | po7       | 
|         |                     | cl2208-eu-spdc | po8       | 
+---------+---------------------+----------------+-----------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s* --view intf

{
    "duration": 3530,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 486,
        "disconnect_time": 0,
        "mo_time": 1849,
        "total_time": 2335
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

True	486	-	connect apic21o.emea-sp.cisco.com:443
True	470	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	537	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	381	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	461	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/ap-k8s_ANP query rsp-subtree-include=full-deployment&target-node=all&target-path=ApToNwIf
```

[[Back]](./ApplicationProfile.md)