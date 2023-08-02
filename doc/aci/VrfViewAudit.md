# VRF

## Audit view

```
# iserver get aci vrf --apic apic21 --name *infra* --when 90d --view audit

Apic: apic21 (mode:online, cache:off)

VRF - Audit Logs last 90d [#19]
-------------------------------

+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| VRF                     | Sev  | Code     | Cause      | Created Time                  | Description                                           | Change Set                             |
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_privIP_VRF | Info | E4215475 | transition | 2023-07-21T10:20:54.041+02:00 | SubnetFilter 0.0.0.0/0 created From:10.58.29.241      | subnetIp:0.0.0.0/0, userdom::all:      | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_privIP_VRF | Info | E4215478 | transition | 2023-07-21T10:20:54.040+02:00 | SubnetFltGrp created From:10.58.29.241                | name:TEST, userdom::all:               | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_privIP_VRF | Info | E4215477 | transition | 2023-07-21T10:12:45.112+02:00 | SubnetFilter 0.0.0.0/0 deleted From:10.58.29.241      |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_privIP_VRF | Info | E4215480 | transition | 2023-07-21T10:12:45.111+02:00 | SubnetFltGrp deleted From:10.58.29.241                |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_privIP_VRF | Info | E4215475 | transition | 2023-07-20T10:36:21.505+02:00 | SubnetFilter 0.0.0.0/0 created From:10.58.29.242      | subnetIp:0.0.0.0/0, userdom::all:      | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_privIP_VRF | Info | E4215478 | transition | 2023-07-20T10:36:21.504+02:00 | SubnetFltGrp created From:10.58.29.242                | name:TEST, userdom::all:               | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215475 | transition | 2023-07-21T10:20:54.020+02:00 | SubnetFilter 10.58.0.0/16 created From:10.58.29.241   | subnetIp:10.58.0.0/16, userdom::all:   | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215475 | transition | 2023-07-21T10:20:54.020+02:00 | SubnetFilter 192.168.0.0/16 created From:10.58.29.241 | subnetIp:192.168.0.0/16, userdom::all: | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215478 | transition | 2023-07-21T10:20:54.019+02:00 | SubnetFltGrp created From:10.58.29.241                | name:common, userdom::all:             | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215477 | transition | 2023-07-21T10:12:45.051+02:00 | SubnetFilter 10.58.0.0/16 deleted From:10.58.29.241   |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215480 | transition | 2023-07-21T10:12:45.050+02:00 | SubnetFltGrp deleted From:10.58.29.241                |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215477 | transition | 2023-07-21T10:12:45.050+02:00 | SubnetFilter 192.168.0.0/16 deleted From:10.58.29.241 |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215475 | transition | 2023-07-20T10:39:53.031+02:00 | SubnetFilter 10.58.0.0/16 created From:10.58.29.242   | subnetIp:10.58.0.0/16, userdom::all:   | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215475 | transition | 2023-07-20T10:39:53.031+02:00 | SubnetFilter 192.168.0.0/16 created From:10.58.29.242 | subnetIp:192.168.0.0/16, userdom::all: | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215477 | transition | 2023-07-20T10:39:53.030+02:00 | SubnetFilter 0.0.0.0/0 deleted From:10.58.29.242      |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215475 | transition | 2023-07-06T10:23:40.105+02:00 | SubnetFilter 0.0.0.0/0 created From:10.58.29.242      | subnetIp:0.0.0.0/0, userdom::all:      | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215478 | transition | 2023-07-06T10:23:40.104+02:00 | SubnetFltGrp created From:10.58.29.242                | name:common, userdom::all:             | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215477 | transition | 2023-06-15T19:13:27.115+02:00 | SubnetFilter 0.0.0.0/0 deleted                        |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
| common/Infra_VRF        | Info | E4215480 | transition | 2023-06-15T19:13:27.114+02:00 | SubnetFltGrp deleted                                  |                                        | 
+-------------------------+------+----------+------------+-------------------------------+-------------------------------------------------------+----------------------------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --name *infra* --when 90d --view audit

{
    "duration": 7190,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 523,
        "disconnect_time": 0,
        "mo_time": 5704,
        "total_time": 6227
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

True	523	-	connect apic21o.emea-sp.cisco.com:443
True	485	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	516	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	409	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	357	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	465	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	518	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	354	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	397	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	2203	598	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./Vrf.md)