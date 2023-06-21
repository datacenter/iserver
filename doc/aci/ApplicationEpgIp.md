# Application Endpoint Group (EPG)

## Filter by associated bridge domain IP address

EPGs associated with bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci epg --apic apic21 --address 10.58.24.209

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+--------------------+----------+---------------+-----------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| Up | EPG                | Class ID | BD            | BD Subnet       | Endpoint | Node                 | Domain               | Contract | StPort | StMember | DynMember |
+----+--------------------+----------+---------------+-----------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_4 | 16403    | k8s/vk8s_4_BD | 10.58.24.222/28 | 8        | pod-1/cl2207-eu-spdc | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 4         | 
|    |                    |          |               |                 |          | pod-1/cl2208-eu-spdc | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+----------+---------------+-----------------+----------+----------------------+----------------------+----------+--------+----------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --address 10.58.24.209

{
    "duration": 4508,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 3092,
        "total_time": 3482
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

True	390	-	connect apic21o.emea-sp.cisco.com:443
True	359	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	278	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	342	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	306	152	apic21o.emea-sp.cisco.com:443 class fvLocale
True	394	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	379	95	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	359	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	328	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	347	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)