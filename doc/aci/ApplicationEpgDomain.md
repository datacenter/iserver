# Application Endpoint Group (EPG)

## Filter by domain name

```
# iserver get aci epg --apic apic21 --contract *vepc* --view domain

Apic: apic21 (mode:online, cache:off)

EPG Domain
----------

+-------------------+-----------------------+-------------+------------+---------------+----------------+------------+------+
| EPG               | Domain Name           | Domain Type | Deployment | Resolution    | Switching Mode | Encap Mode | CoS  |
+-------------------+-----------------------+-------------+------------+---------------+----------------+------------+------+
| vEPC/vSFO_ANP/WWW | VMware/EU-SPDC-CDC-22 | VMM         | immediate  | pre-provision | native         | auto       | Cos0 | 
|                   | VMware/EU-SPDC-R7DC   | VMM         | lazy       | pre-provision | native         | auto       | Cos0 | 
+-------------------+-----------------------+-------------+------------+---------------+----------------+------------+------+
```

Developer

```
# iserver get aci epg --apic apic21 --contract *vepc* --view domain

{
    "duration": 2998,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 2048,
        "total_time": 2470
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

True	422	-	connect apic21o.emea-sp.cisco.com:443
True	382	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	281	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	368	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	335	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	343	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	339	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)