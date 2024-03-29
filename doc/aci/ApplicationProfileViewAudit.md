# Application Profile

## Audit view

```
# iserver get aci ap --apic apic21 --name *k8s* --when 90d --view audit

Apic: apic21 (mode:online, cache:off)

Application Profile - Audit Logs last 90d [#21]
-----------------------------------------------

+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Application Profile | Sev  | Code     | Cause      | Created Time                  | Description                                                         | Change Set                                                                       |
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214170 | transition | 2023-06-19T08:21:23.394+02:00 | RsCustQosPol deleted From:10.61.98.234                              |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211986 | transition | 2023-06-19T08:21:23.393+02:00 | RsBd deleted From:10.61.98.234                                      |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211938 | transition | 2023-06-19T08:21:23.392+02:00 | AEPg KaliTest1 deleted From:10.61.98.234                            |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4212010 | transition | 2023-06-19T08:21:00.560+02:00 | RsDomAtt uni/vmmp-VMware/dom-EU-SPDC-R7DC deleted From:10.61.98.234 |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214170 | transition | 2023-06-19T08:21:00.559+02:00 | RsCustQosPol deleted From:10.61.98.234                              |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211986 | transition | 2023-06-19T08:21:00.559+02:00 | RsBd deleted From:10.61.98.234                                      |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211938 | transition | 2023-06-19T08:21:00.558+02:00 | AEPg KaliTest2 deleted From:10.61.98.234                            |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4212008 | transition | 2023-06-19T08:19:16.795+02:00 | RsDomAtt uni/vmmp-VMware/dom-EU-SPDC-R7DC created From:10.61.98.234 | bindingType:none, classPref:encap, encap:unknown, encapMode:auto, epgCos:Cos0,   | 
|                     |      |          |            |                               |                                                                     | epgCosPref:disabled, instrImedcy:lazy, netflowDir:both, netflowPref:disabled,    | 
|                     |      |          |            |                               |                                                                     | numPorts:0, portAllocation:none, primaryEncap:unknown,                           | 
|                     |      |          |            |                               |                                                                     | primaryEncapInner:unknown, resImedcy:pre-provision,                              | 
|                     |      |          |            |                               |                                                                     | secondaryEncapInner:unknown, switchingMode:native,                               | 
|                     |      |          |            |                               |                                                                     | tDn:uni/vmmp-VMware/dom-EU-SPDC-R7DC, untagged:no, userdom::all:common:,         | 
|                     |      |          |            |                               |                                                                     | vnetOnly:no                                                                      | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214168 | transition | 2023-06-19T08:19:16.794+02:00 | RsCustQosPol created From:10.61.98.234                              | userdom:all                                                                      | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211984 | transition | 2023-06-19T08:19:16.794+02:00 | RsBd created From:10.61.98.234                                      | tnFvBDName:vk8s_1_BD, userdom:all                                                | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211936 | transition | 2023-06-19T08:19:16.793+02:00 | AEPg KaliTest2 created From:10.61.98.234                            | floodOnEncap:disabled, hasMcastSource:no, isAttrBasedEPg:no, matchT:AtleastOne,  | 
|                     |      |          |            |                               |                                                                     | name:KaliTest2, pcEnfPref:unenforced, prefGrMemb:exclude, prio:level3,           | 
|                     |      |          |            |                               |                                                                     | shutdown:no, userdom::all:common:                                                | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211984 | transition | 2023-06-19T08:18:14.953+02:00 | RsBd created From:10.61.98.234                                      | tnFvBDName:vk8s_1_BD, userdom:all                                                | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214168 | transition | 2023-06-19T08:18:14.953+02:00 | RsCustQosPol created From:10.61.98.234                              | userdom:all                                                                      | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211936 | transition | 2023-06-19T08:18:14.952+02:00 | AEPg KaliTest1 created From:10.61.98.234                            | floodOnEncap:disabled, hasMcastSource:no, isAttrBasedEPg:no, matchT:AtleastOne,  | 
|                     |      |          |            |                               |                                                                     | name:KaliTest1, pcEnfPref:unenforced, prefGrMemb:exclude, prio:level3,           | 
|                     |      |          |            |                               |                                                                     | shutdown:no, userdom::all:common:                                                | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4215518 | transition | 2023-05-05T16:41:31.540+02:00 | Annotation a created                                                | key:a, userdom::all:common:, value:b                                             | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4215520 | transition | 2023-05-05T16:41:05.541+02:00 | Annotation a deleted                                                |                                                                                  | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211937 | transition | 2023-05-05T16:40:32.567+02:00 | AEPg Test modified                                                  | nameAlias (Old: , New: alias)                                                    | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4211937 | transition | 2023-05-05T16:40:17.220+02:00 | AEPg Test modified                                                  | nameAlias (Old: alias, New: )                                                    | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214180 | transition | 2023-05-03T12:40:47.924+02:00 | RsProtBy MyTabooContract created                                    | tnVzTabooName:MyTabooContract, userdom::all:common:                              | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214159 | transition | 2023-05-02T20:34:08.770+02:00 | RsCons BT-Demo created                                              | intent:install, prio:unspecified, tnVzBrCPName:BT-Demo, userdom::all:common:     | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4214183 | transition | 2023-05-02T20:34:00.630+02:00 | RsProv BT-Demo created                                              | intent:install, matchT:AtleastOne, prio:unspecified, tnVzBrCPName:BT-Demo,       | 
|                     |      |          |            |                               |                                                                     | userdom::all:common:                                                             | 
+---------------------+------+----------+------------+-------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s* --when 90d --view audit

{
    "duration": 4999,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 510,
        "disconnect_time": 0,
        "mo_time": 2654,
        "total_time": 3164
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

True	510	-	connect apic21o.emea-sp.cisco.com:443
True	423	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	520	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	366	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1345	1943	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ApplicationProfile.md)