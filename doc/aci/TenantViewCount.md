# Tenant

## Count view

```
# iserver get aci tenant --apic apic21 --view count

Apic: apic21 (mode:online, cache:off)

Tenant - Object Counts [#12]
----------------------------

+--------+------------------+-------------+-----+----+-----+-------+-------+---------------+----------------+-------------+--------+----------+
| Health | Name             | App Profile | EPG | BD | VRF | L2Out | L3Out | MPLS-SR L3Out | Standard Contr | Taboo Contr | Filter | Endpoint |
+--------+------------------+-------------+-----+----+-----+-------+-------+---------------+----------------+-------------+--------+----------+
| 100    | common           | 3           | 2   | 4  | 5   | 1     | 0     | 0             | 7              | 1           | 9      | 2        | 
| 100    | Ericsson_PACO    | 0           | 0   | 0  | 2   | 0     | 0     | 0             | 1              | 0           | 0      | 28       | 
| 61     | hefernan_ni-demo | 1           | 2   | 2  | 1   | 0     | 0     | 0             | 2              | 0           | 1      | 0        | 
| 100    | infra            | 2           | 2   | 2  | 2   | 0     | 0     | 0             | 0              | 0           | 0      | 0        | 
| 95     | k8s              | 1           | 19  | 14 | 2   | 1     | 0     | 0             | 3              | 1           | 5      | 49       | 
| 61     | mgmt             | 1           | 1   | 2  | 4   | 0     | 0     | 0             | 1              | 0           | 7      | 2        | 
| 93     | nidemo           | 1           | 4   | 4  | 1   | 0     | 0     | 0             | 4              | 0           | 6      | 7        | 
| 79     | SPN_IntraLab     | 1           | 1   | 1  | 1   | 0     | 0     | 0             | 0              | 0           | 0      | 0        | 
| 100    | Testing_MSO      | 0           | 0   | 0  | 0   | 0     | 0     | 0             | 0              | 0           | 0      | 0        | 
| 100    | ttrabatt-test    | 0           | 0   | 0  | 0   | 0     | 0     | 0             | 0              | 0           | 0      | 0        | 
| 59     | vEPC             | 1           | 1   | 2  | 2   | 0     | 0     | 0             | 1              | 0           | 1      | 2        | 
| 87     | vEPC_demo        | 1           | 4   | 4  | 3   | 0     | 0     | 0             | 3              | 0           | 1      | 8        | 
+--------+------------------+-------------+-----+----+-----+-------+-------+---------------+----------------+-------------+--------+----------+
```

Developer

```
# iserver get aci tenant --apic apic21 --view count

{
    "duration": 8187,
    "apic": {
        "read": true,
        "success": 16,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 15,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 6778,
        "total_time": 7205
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

True	427	-	connect apic21o.emea-sp.cisco.com:443
True	536	12	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	442	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	431	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	334	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	464	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	331	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	333	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	365	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	328	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	356	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	391	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	1371	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	338	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	322	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	436	98	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Tenant.md)