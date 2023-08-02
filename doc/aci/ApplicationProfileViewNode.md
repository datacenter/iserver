# Application Profile

## Node view

```
# iserver get aci ap --apic apic21 --name *k8s* --view node

Apic: apic21 (mode:online, cache:off)

Application Profile - Nodes [#1]
--------------------------------

+---------+---------------------+----------------+------------+
| Faults  | Application Profile | Node           | Interfaces |
+---------+---------------------+----------------+------------+
| 0 0 2 0 | k8s/k8s_ANP         | cl2207-eu-spdc | 26         | 
|         |                     | cl2208-eu-spdc | 26         | 
+---------+---------------------+----------------+------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s* --view node

{
    "duration": 3019,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 2185,
        "total_time": 2628
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

True	443	-	connect apic21o.emea-sp.cisco.com:443
True	694	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	543	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	408	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	540	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/ap-k8s_ANP query rsp-subtree-include=full-deployment&target-node=all&target-path=ApToNwIf
```

[[Back]](./ApplicationProfile.md)