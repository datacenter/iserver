# L2Out

## Audit view

```
# iserver get aci l2out --apic apic21 --when any --view audit

Apic: apic21 (mode:online, cache:off)

L2Out - Audit Logs last 10y [#9]
--------------------------------

+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| L2Out    | Sev  | Code     | Cause      | Created Time                  | Description                                                                     | Change Set                                                               |
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212443 | transition | 2023-05-05T14:08:52.099+02:00 | RsPathL2OutAtt topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp]  | tDn:topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp],     | 
|          |      |          |            |                               | created                                                                         | targetDscp:unspecified, userdom::all:common:                             | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212440 | transition | 2023-05-05T13:07:47.171+02:00 | RsL2DomAtt created                                                              | tDn:uni/l2dom-Infra_L2dom, userdom::all:common:                          | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212443 | transition | 2023-05-05T13:07:47.171+02:00 | RsPathL2OutAtt topology/pod-1/paths-2207/pathep-[eth1/30] created               | tDn:topology/pod-1/paths-2207/pathep-[eth1/30], targetDscp:unspecified,  | 
|          |      |          |            |                               |                                                                                 | userdom::all:common:                                                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212428 | transition | 2023-05-05T13:07:47.170+02:00 | LIfP default created                                                            | name:default, tag:yellow-green, userdom::all:common:                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4214168 | transition | 2023-05-05T13:07:47.170+02:00 | RsCustQosPol created                                                            | userdom:all                                                              | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212431 | transition | 2023-05-05T13:07:47.170+02:00 | LNodeP default created                                                          | name:default, tag:yellow-green, userdom::all:common:                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212425 | transition | 2023-05-05T13:07:47.169+02:00 | InstP L2Out-ext-epg created                                                     | floodOnEncap:disabled, matchT:AtleastOne, name:L2Out-ext-epg,            | 
|          |      |          |            |                               |                                                                                 | prefGrMemb:exclude, prio:unspecified, targetDscp:unspecified,            | 
|          |      |          |            |                               |                                                                                 | userdom::all:common:                                                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212437 | transition | 2023-05-05T13:07:47.169+02:00 | RsEBd created                                                                   | encap:vlan-666, tnFvBDName:Test, userdom:all                             | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212434 | transition | 2023-05-05T13:07:47.168+02:00 | Out Test created                                                                | name:Test, targetDscp:unspecified, userdom::all:common:                  | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --when any --view audit

{
    "duration": 2015,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 492,
        "disconnect_time": 0,
        "mo_time": 1228,
        "total_time": 1720
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

True	492	-	connect apic21o.emea-sp.cisco.com:443
True	401	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	403	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	424	9	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./L2Out.md)