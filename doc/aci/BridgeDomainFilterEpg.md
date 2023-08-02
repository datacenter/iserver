# Bridge Domain

## Filter by bridge domain's associated EPG name

```
# iserver get aci bd --apic apic21 --epg *vEPG_MGMT*

Apic: apic21 (mode:online, cache:off)

Bridge Domain [#1]
------------------

+--------+---------+-------------------+----------+----------+-----------------+-------+---------------------+------------------+--------------------+
| Health | Faults  | Bridge Domain     | Class ID | VNID     | Subnet          | Usage | EPG                 | VRF              | L3Out              |
+--------+---------+-------------------+----------+----------+-----------------+-------+---------------------+------------------+--------------------+
| 100    | 0 0 0 0 | vEPC_demo/MGMT_BD | 16391    | 16449430 | 10.58.25.158/27 | 1/30  | vEPC_demo/vEPG_MGMT | common/Infra_VRF | common/Infra_L3out | 
+--------+---------+-------------------+----------+----------+-----------------+-------+---------------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --epg *vEPG_MGMT*

{
    "duration": 2760,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 465,
        "disconnect_time": 0,
        "mo_time": 1771,
        "total_time": 2236
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

True	465	-	connect apic21o.emea-sp.cisco.com:443
True	485	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	508	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	343	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	435	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)